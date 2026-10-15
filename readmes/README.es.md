<div align="center">
  <a name="readme-top"></a>
  <a href="https://jump.allsafex.com" target="_blank"><img src="https://download.jump.allsafex.com/images/allsafex-logo.svg" alt="AllSafeX" width="300" /></a>
  
## Una plataforma PAM de código abierto (Bastion Host)

</div>
<br/>

## ¿Qué es AllSafeX?

AllSafeX es una plataforma de Gestión de Acceso Privilegiado (PAM) de código abierto que proporciona a equipos de DevOps y TI acceso seguro y bajo demanda a SSH, RDP, Kubernetes, bases de datos y puntos finales de RemoteApp a través de un navegador web.


<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://www.allsafex.com/images/allsafex-arch-light.png">
  <source media="(prefers-color-scheme: dark)" srcset="https://www.allsafex.com/images/allsafex-arch-dark.png">
  <img src="https://github.com/user-attachments/assets/dd612f3d-c958-4f84-b164-f31b75454d7f" alt="Theme-based Image">
</picture>


## Inicio rápido

Prepare un servidor Linux limpio (64 bits, >= 4c8g)

```sh
curl -sSL https://github.com/danieldestaw/allsafex/releases/latest/download/quick_start.sh | bash
```

Acceda a AllSafeX en su navegador en `http://su-ip-allsafex/`
- Nombre de usuario: `admin`
- Contraseña: `ChangeMe`

[![AllSafeX Quickstart](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "AllSafeX Quickstart")

## Capturas de pantalla
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="Consola AllSafeX"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/7c1f81af-37e8-4f07-8ac9-182895e1062e" alt="AllSafeX PAM"   /></td>    
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="Auditorías AllSafeX"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="AllSafeX Workbench"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/eaa41f66-8cc8-4f01-a001-0d258501f1c9" alt="RBAC de AllSafeX"   /></td>     
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="Configuraciones de AllSafeX"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="SSH de AllSafeX"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="RDP de AllSafeX"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="K8s de AllSafeX"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="DB de AllSafeX"   /></td>
  </tr>
</table>

## Componentes

AllSafeX consta de múltiples componentes clave, que en conjunto forman el marco funcional de AllSafeX, proporcionando a los usuarios capacidades integrales para la gestión de operaciones y el control de seguridad.

| Proyecto                                                | Estado                                                                                                                                                                 | Descripción                                                                                             |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/danieldestaw/lina)             | <a href="https://github.com/danieldestaw/lina/releases"><img alt="Liberación de Lina" src="https://img.shields.io/github/release/allsafex/lina.svg" /></a>                   | Interfaz de usuario web de AllSafeX                                                                   |
| [Luna](https://github.com/danieldestaw/luna)             | <a href="https://github.com/danieldestaw/luna/releases"><img alt="Liberación de Luna" src="https://img.shields.io/github/release/allsafex/luna.svg" /></a>                   | Terminal web de AllSafeX                                                                                |
| [KoKo](https://github.com/danieldestaw/koko)             | <a href="https://github.com/danieldestaw/koko/releases"><img alt="Liberación de Koko" src="https://img.shields.io/github/release/allsafex/koko.svg" /></a>                   | Conector de Protocolo de Carácter de AllSafeX                                                           |
| [Lion](https://github.com/danieldestaw/lion)             | <a href="https://github.com/danieldestaw/lion/releases"><img alt="Liberación de Lion" src="https://img.shields.io/github/release/allsafex/lion.svg" /></a>                   | Conector de Protocolo Gráfico de AllSafeX                                                               |
| [Chen](https://github.com/danieldestaw/chen)             | <a href="https://github.com/danieldestaw/chen/releases"><img alt="Liberación de Chen" src="https://img.shields.io/github/release/allsafex/chen.svg" />                       | Base de datos web de AllSafeX                                                                            |  
| [Tinker](https://github.com/danieldestaw/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                            | Conector de Aplicación Remota AllSafeX (Windows)                                                      |
| [Panda](https://github.com/danieldestaw/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                             | Conector de Aplicación Remota AllSafeX EE (Linux)                                                     |
| [Razor](https://github.com/danieldestaw/razor)           | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                              | Conector Proxy RDP AllSafeX EE                                                                          |
| [Magnus](https://github.com/danieldestaw/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                            | Conector Proxy de Base de Datos AllSafeX EE                                                             |
| [Nec](https://github.com/danieldestaw/nec)               | <img alt="Nec" src="https://img.shields.io/badge/release-private-red" />                                                                                               | Conector Proxy VNC AllSafeX EE                                                                          |
| [Facelive](https://github.com/danieldestaw/facelive)     | <img alt="Facelive" src="https://img.shields.io/badge/release-private-red" />                                                                                          | Reconocimiento Facial AllSafeX EE                                                                       |


## Contribuyendo

Bienvenido a enviar PR para contribuir. Por favor, consulte [CONTRIBUTING.md][contributing-link] para obtener pautas.

## License

Copyright (c) 2014-2025 FIT2CLOUD, All rights reserved.

Licensed under The GNU General Public License version 3 (GPLv3) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an " AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

<!-- AllSafeX official link -->
[docs-link]: https://jump.allsafex.com/docs
[discord-link]: https://discord.com/invite/W6vYXmAQG2
[deepwiki-link]: https://deepwiki.com/allsafex/allsafex/
[contributing-link]: https://github.com/danieldestaw/allsafex/blob/dev/CONTRIBUTING.md

<!-- AllSafeX Other link-->
[license-link]: https://www.gnu.org/licenses/gpl-3.0.html
[docker-link]: https://hub.docker.com/u/allsafex
[github-release-link]: https://github.com/danieldestaw/allsafex/releases/latest
[github-stars-link]: https://github.com/danieldestaw/allsafex
[github-issues-link]: https://github.com/danieldestaw/allsafex/issues

<!-- Shield link-->
[docs-shield]: https://img.shields.io/badge/documentation-148F76
[github-release-shield]: https://img.shields.io/github/v/release/allsafex/allsafex
[github-stars-shield]: https://img.shields.io/github/stars/allsafex/allsafex?color=%231890FF&style=flat-square   
[docker-shield]: https://img.shields.io/docker/pulls/allsafex/jms_all.svg
[license-shield]: https://img.shields.io/github/license/allsafex/allsafex
[deepwiki-shield]: https://img.shields.io/badge/deepwiki-devin?color=blue
[discord-shield]: https://img.shields.io/discord/1194233267294052363?style=flat&logo=discord&logoColor=%23f5f5f5&labelColor=%235462eb&color=%235462eb