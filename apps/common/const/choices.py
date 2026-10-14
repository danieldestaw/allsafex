import phonenumbers
import pycountry
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from phonenumbers import PhoneMetadata

ADMIN = 'Admin'
USER = 'User'
AUDITOR = 'Auditor'


def get_country_phone_codes():
    phone_codes = []
    for region_code in phonenumbers.SUPPORTED_REGIONS:
        phone_metadata = PhoneMetadata.metadata_for_region(region_code)
        if phone_metadata:
            phone_codes.append((region_code, phone_metadata.country_code))
    return phone_codes


def get_country(region_code):
    country = pycountry.countries.get(alpha_2=region_code)
    if country:
        return country
    else:
        return None


def get_country_phone_choices():
    codes = get_country_phone_codes()
    choices = []
    for code, phone in codes:
        country = get_country(code)
        if not country:
            continue
        country_name = country.name
        flag = country.flag

        if country.name == 'China':
            country_name = _('China')

        if code == 'TW':
            country_name = 'Taiwan'
            flag = get_country('CN').flag
        choices.append({
            'name': country_name,
            'phone_code': f'+{phone}',
            'flag': flag,
            'code': code,
        })

    choices.sort(key=lambda x: (0 if x['code'] == 'ET' else 1, x['name']))
    return choices


class Trigger(models.TextChoices):
    manual = 'manual', _('Manual')
    timing = 'timing', _('Timing')


class Status(models.TextChoices):
    ready = 'ready', _('Ready')
    pending = 'pending', _("Pending")
    running = 'running', _("Running")
    success = 'success', _("Success")
    failed = 'failed', _("Failed")
    error = 'error', _("Error")
    canceled = 'canceled', _("Canceled")


class Language(models.TextChoices):
    en = 'en', 'English'
    am = 'am', 'አማርኛ (Amharic)'

    @classmethod
    def choices_supported(cls):
        _choices = []
        code_mapper = cls.get_code_mapper()
        supported = [ code_mapper.get(code, code) for code in settings.LANGUAGES_SUPPORTED ]
        for code, label in cls.choices:
            if code in supported:
                _choices.append((code, label))
        if not _choices:
            return cls.choices
        return _choices

    @classmethod
    def get_code_mapper(cls):
        code_mapper = {code: code for code, name in cls.choices}
        code_mapper.update({
            'amharic': cls.am.value,
            'amh': cls.am.value,
            'am-et': cls.am.value,
            'en-us': cls.en.value,
            'en': cls.en.value,
            'zh': cls.en.value,
            'zh-cn': cls.en.value,
            'zh-hans': cls.en.value,
            'zh-hant': cls.en.value,
            'zh-tw': cls.en.value,
            'zh-hk': cls.en.value,
            'ja': cls.en.value,
            'ko': cls.en.value,
            'es': cls.en.value,
            'ru': cls.en.value,
            'pt-br': cls.en.value,
            'vi': cls.en.value,
        })
        return code_mapper

    @classmethod
    def to_internal_code(cls, code: str, default='en', with_filename=False):
        code_mapper = cls.get_code_mapper()
        code = code.lower()
        code = code_mapper.get(code) or code_mapper.get(default) or 'en'
        code = code.replace('-', '_')
        return code

    @classmethod
    def get_other_codes(cls, code):
        data = {
            cls.en.value: ['en', 'en-us'],
            cls.am.value: ['am', 'am-et', 'amh'],
        }
        return data.get(code, [code])


class ConfirmOrIgnore(models.TextChoices):
    pending = '0', _('Pending')
    confirmed = '1', _('Confirmed')
    ignored = '2', _('Ignored')


COUNTRY_CALLING_CODES = get_country_phone_choices()


class LicenseEditionChoices(models.TextChoices):
    COMMUNITY = 'community', _('Community edition')
    BASIC = 'basic', _('Basic edition')
    STANDARD = 'standard', _('Standard edition')
    PROFESSIONAL = 'professional', _('Professional edition')
    ULTIMATE = 'ultimate', _('Ultimate edition')

    @staticmethod
    def from_key(key: str):
        for choice in LicenseEditionChoices:
            if choice == key:
                return choice
        return LicenseEditionChoices.COMMUNITY

    @staticmethod
    def parse_license_edition(info):
        count = info.get('license', {}).get('count', 0)

        if 0 < count <= 50:
            return LicenseEditionChoices.BASIC
        elif count <= 500:
            return LicenseEditionChoices.STANDARD
        elif count <= 5000:
            return LicenseEditionChoices.PROFESSIONAL
        elif count > 5000:
            return LicenseEditionChoices.ULTIMATE
        else:
            return LicenseEditionChoices.COMMUNITY
