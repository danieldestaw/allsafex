<div align="center">
  <a name="readme-top"></a>
  <a href="https://allsafex-pam.allsafex.com" target="_blank"><img src="https://download.allsafex-pam.allsafex.com/images/allsafex-logo.svg" alt="AllSafeX" width="300" /></a>
  
## 一個開源的 PAM 平台 (堡壘主機)

</div>
<br/>

## AllSafeX 是什麼？

AllSafeX 是一個開源的特權訪問管理 (PAM) 平台，為 DevOps 和 IT 團隊提供按需和安全的 SSH、RDP、Kubernetes、數據庫和 RemoteApp 端點的訪問，通過網頁瀏覽器實現。

<picture>
  <source media="(prefers-color-scheme: light)" srcset="https://www.allsafex.com/images/allsafex-arch-light.png">
  <source media="(prefers-color-scheme: dark)" srcset="https://www.allsafex.com/images/allsafex-arch-dark.png">
  <img src="https://github.com/user-attachments/assets/dd612f3d-c958-4f84-b164-f31b75454d7f" alt="Theme-based Image">
</picture>

## 快速開始

準備一台乾淨的 Linux 伺服器 (64 位，>= 4c8g)

```sh
curl -sSL https://github.com/danieldestaw/allsafex/releases/latest/download/quick_start.sh | bash
```

在您的瀏覽器中訪問 AllSafeX，地址為 `http://your-allsafex-ip/`
- 用戶名：`admin`
- 密碼：`ChangeMe`

[![AllSafeX 快速開始](https://github.com/user-attachments/assets/0f32f52b-9935-485e-8534-336c63389612)](https://www.youtube.com/watch?v=UlGYRbKrpgY "AllSafeX 快速開始")

## 畫面截圖
<table style="border-collapse: collapse; border: 1px solid black;">
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/99fabe5b-0475-4a53-9116-4c370a1426c4" alt="AllSafeX 控制台"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/7c1f81af-37e8-4f07-8ac9-182895e1062e" alt="AllSafeX PAM"   /></td>    
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/a424d731-1c70-4108-a7d8-5bbf387dda9a" alt="AllSafeX 審計"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/393d2c27-a2d0-4dea-882d-00ed509e00c9" alt="AllSafeX 工作台"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/user-attachments/assets/eaa41f66-8cc8-4f01-a001-0d258501f1c9" alt="AllSafeX RBAC"   /></td>     
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/3a2611cd-8902-49b8-b82b-2a6dac851f3e" alt="AllSafeX 設定"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/1e236093-31f7-4563-8eb1-e36d865f1568" alt="AllSafeX SSH"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/69373a82-f7ab-41e8-b763-bbad2ba52167" alt="AllSafeX RDP"   /></td>
  </tr>
  <tr>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/5bed98c6-cbe8-4073-9597-d53c69dc3957" alt="AllSafeX K8s"   /></td>
    <td style="padding: 5px;background-color:#fff;"><img src= "https://github.com/danieldestaw/allsafex/assets/32935519/b80ad654-548f-42bc-ba3d-c1cfdf1b46d6" alt="AllSafeX 數據庫"   /></td>
  </tr>
</table>

## 組件

AllSafeX 由多個關鍵組件組成，這些組件共同構成了 AllSafeX 的功能框架，為用戶提供全面的操作管理和安全控制能力。

| 專案                                                  | 狀態                                                                                                                                                                 | 描述                                                                                                   |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [Lina](https://github.com/danieldestaw/lina)             | <a href="https://github.com/danieldestaw/lina/releases"><img alt="Lina 版本" src="https://img.shields.io/github/release/allsafex/lina.svg" /></a>                   | AllSafeX 網頁 UI                                                                                     |
| [Luna](https://github.com/danieldestaw/luna)             | <a href="https://github.com/danieldestaw/luna/releases"><img alt="Luna 版本" src="https://img.shields.io/github/release/allsafex/luna.svg" /></a>                   | AllSafeX 網頁終端                                                                                   |
| [KoKo](https://github.com/danieldestaw/koko)             | <a href="https://github.com/danieldestaw/koko/releases"><img alt="Koko 版本" src="https://img.shields.io/github/release/allsafex/koko.svg" /></a>                   | AllSafeX 字符協議連接器                                                                             |
| [Lion](https://github.com/danieldestaw/lion)             | <a href="https://github.com/danieldestaw/lion/releases"><img alt="Lion 版本" src="https://img.shields.io/github/release/allsafex/lion.svg" /></a>                   | AllSafeX 圖形協議連接器                                                                             |
| [Chen](https://github.com/danieldestaw/chen)             | <a href="https://github.com/danieldestaw/chen/releases"><img alt="Chen 版本" src="https://img.shields.io/github/release/allsafex/chen.svg" />                       | AllSafeX 網頁數據庫                                                                                 |  
| [Tinker](https://github.com/danieldestaw/tinker)         | <img alt="Tinker" src="https://img.shields.io/badge/release-private-red" />                                                                                            | AllSafeX 遠程應用連接器 (Windows)                                                                  |
| [Panda](https://github.com/danieldestaw/Panda)           | <img alt="Panda" src="https://img.shields.io/badge/release-private-red" />                                                                                             | AllSafeX EE 遠程應用連接器 (Linux)                                                                  |
| [Razor](https://github.com/danieldestaw/razor)           | <img alt="Chen" src="https://img.shields.io/badge/release-private-red" />                                                                                              | AllSafeX EE RDP 代理連接器                                                                          |
| [Magnus](https://github.com/danieldestaw/magnus)         | <img alt="Magnus" src="https://img.shields.io/badge/release-private-red" />                                                                                            | AllSafeX EE 數據庫代理連接器                                                                        |
| [Nec](https://github.com/danieldestaw/nec)               | <img alt="Nec" src="https://img.shields.io/badge/release-private-red" />                                                                                               | AllSafeX EE VNC 代理連接器                                                                          |
| [Facelive](https://github.com/danieldestaw/facelive)     | <img alt="Facelive" src="https://img.shields.io/badge/release-private-red" />                                                                                          | AllSafeX EE 面部識別                                                                                 |

## 貢獻

歡迎提交 PR 以貢獻。請參考 [CONTRIBUTING.md][contributing-link] 獲取指南。

## License

Copyright (c) 2014-2025 FIT2CLOUD, All rights reserved.

Licensed under The GNU General Public License version 3 (GPLv3) (the "License"); you may not use this file except in compliance with the License. You may obtain a copy of the License at

https://www.gnu.org/licenses/gpl-3.0.html

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an " AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.

<!-- AllSafeX official link -->
[docs-link]: https://allsafex-pam.allsafex.com/docs
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