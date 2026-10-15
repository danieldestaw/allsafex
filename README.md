<div align="center">

# AllSafeX Jumphost
### An Open-Source Jumphost Platform

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Version](https://img.shields.io/badge/version-1.0.0-orange.svg)](https://github.com/danieldestaw/allsafex/releases)
[![Docker](https://img.shields.io/badge/docker-ready-blue.svg)](https://www.docker.com/)
[![Documentation](https://img.shields.io/badge/docs-allsafex--pam-green.svg)](https://jump.allsafex.com/)

[Documentation](https://jump.allsafex.com/) · [Releases](https://github.com/danieldestaw/allsafex/releases) · [Support](https://jump.allsafex.com/support)

</div>

---

##  What is AllSafeX?

**AllSafeX** is an open-source **Jumphost** solution engineered for modern DevOps, SecOps, and IT engineering teams. It enforces Zero Trust principles by mediating, securing, authenticating, and auditing all administrative sessions across critical infrastructure:

- **SSH & Telnet** infrastructure (Linux, Unix, network appliances)
- **RDP & VNC** remote desktops (Windows, macOS)
- **Database Gateways** (MySQL, PostgreSQL, Oracle, SQL Server, Redis, MongoDB)
- **Cloud & Kubernetes** clusters
- **Web Applications & Internal Admin Consoles**

All connections occur securely through web browsers or native desktop terminals without requiring direct network exposure of backend targets or distributing raw server credentials to operators.

---

## Key Features

- **Centralized Credential Vault**: Eliminate hardcoded passwords and SSH keys. AllSafeX automatically injects credentials at session launch.
- **Protocol Gateway**: High-performance browser-based terminal emulator, web-based RDP desktop client, and database workspace.
- **Granular Access Control (RBAC/ABAC)**: Define precise permissions based on user groups, asset tags, time windows, and client IP addresses.
- **Command Filtering & Security Policies**: Block dangerous commands (e.g. `rm -rf`, `DROP DATABASE`) in real time with custom approval triggers.
- **Real-Time Monitoring & Video Auditing**: Record, monitor, and terminate active privileged sessions in real time with high-fidelity keystroke playback.
- **Multi-Language Support**: Fully localized in English, Amharic (አማርኛ), and multiple global languages.
- **Modern Security Architecture**: Safety Orange visual theme, rate-limit defense, MFA authentication, and containerized deployment.

---

##  Architecture

```
+-------------------------------------------------------------+
|                      Clients / Users                        |
|        Web Browser (HTTPS) / Native SSH (Port 2222)         |
+-------------------------------------------------------------+
                              |
                              v
+-------------------------------------------------------------+
|                     AllSafeX Web (Nginx)                    |
|             Port 80 / 443 - Reverse Proxy & Static UI       |
+-------------------------------------------------------------+
         |                                           |
         v                                           v
+-------------------------+             +-------------------------+
|      AllSafeX Core      |             |   AllSafeX SSH Gateway  |
|  (Django / Python API)  | <=========> |     (Koko Terminal)     |
+-------------------------+             +-------------------------+
         |               |
         v               v
+------------------+  +------------------+
|  PostgreSQL 16   |  |     Redis 7      |
| (Database Store) |  |  (Cache & Task)  |
+------------------+  +------------------+
```

---

## 🚀 Quick Start

### Prerequisites
- Docker Engine 20.10+
- Docker Compose v2+
- Linux x86_64 or aarch64 server (>= 4 CPU cores, >= 8 GB RAM recommended)

### 1. Clone Repository
```bash
git clone https://github.com/danieldestaw/allsafex.git
cd allsafex
```

### 2. Launch Services
```bash
docker compose up -d
```

### 3. Access AllSafeX Web Console
Open your web browser and navigate to:
```
http://<your-server-ip>/
```

- **Default Username**: `admin`
- **Default Password**: `admin`

*(We recommend updating the default password and configuring MFA after your initial login.)*

---

## Container Services

| Container Name | Service | Function |
| :--- | :--- | :--- |
| `allsafex_web` | Nginx | Reverse proxy, static asset distributor, and TLS termination |
| `allsafex_core` | Core API | Django backend, authentication engine, authorization rules, and REST API |
| `allsafex_ssh_gateway` | Koko | Terminal gateway proxy for SSH/Telnet sessions |
| `allsafex_db` | PostgreSQL 16 | Primary relational database storage |
| `allsafex_redis` | Redis 7 | Distributed cache, task queue, and session store |

---

##  Internationalization

AllSafeX supports internationalization out-of-the-box:
- **English** (Default)
- **Amharic (አማርኛ)**

Switch languages dynamically from the top-right user menu.

---

##  Resources & Links

- **Official Website & Docs**: [https://jump.allsafex.com/](https://jump.allsafex.com/)
- **Technical Support**: [https://jump.allsafex.com/support](https://jump.allsafex.com/support)
- **Release Downloads**: [https://github.com/danieldestaw/allsafex/releases](https://github.com/danieldestaw/allsafex/releases)

---

## License

AllSafeX is open source software released under the **GNU General Public License v3.0 (GPLv3)**. See the `LICENSE` file for details.
