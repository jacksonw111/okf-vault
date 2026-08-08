---
type: "Tool"
title: "LSPanel"
description: "Tauri 搭的 PHP 本地开发环境桌面面板：把 Docker 容器、本地数据库、HTTPS 证书、邮件捕获、备份都收到同一处管理，免跳浏览器。"
resource: "https://github.com/bewdes/LSPanel"
tags: [php, tauri, docker, local-dev, devops, desktop]
timestamp: "2026-08-08T20:30:00Z"
---

# LSPanel

## 它是什么

LSPanel 是一款 Tauri 搭的桌面应用，为 PHP 开发者把「本地开发环境」的工具都集中起来：Docker 容器、本地数据库（MySQL / Postgres / SQLite）、HTTPS 证书（mkcert / 自签）、邮件捕获（Mailpit / MailHog）、备份 / 还原。它让你不用跳浏览器去逐个打开 Portainer / phpMyAdmin / MailHog。

## 为什么用它 / 适合什么场景

- PHP / Laravel / WordPress 开发者，希望统一管理本地依赖。
- 想在桌面上一键启动 / 停止整套开发栈。
- 不想切到浏览器看每个工具的状态（容器 / DB / 邮件 / 证书）。
- 想要 Tauri 原生体验（轻量、启动快、跨平台）。

## 关键能力

| 能力 | 说明 |
|------|------|
| Docker 容器管理 | 启停 / 重启 / 查看日志 |
| 本地数据库 | MySQL / Postgres / SQLite 入口 |
| HTTPS 证书 | 自签 / mkcert 一键管理 |
| 邮件捕获 | Mailpit / MailHog 集成 |
| 备份与还原 | 一键打包 / 还原 |
| Tauri 桌面 | 跨平台原生体验 |

## 相关概念

- [Dory](./tool-dory.md) — macOS 上 Docker Desktop 的开源替代品
- [Docksurf](./tool-docksurf.md) — 终端里用键盘操作 Docker 的 TUI
- [Kpanel](./tool-kpanel.md) — 科技狮出品的 Linux 服务器管理面板