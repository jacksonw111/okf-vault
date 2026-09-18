---
type: Tool
title: "AZERIOID Stack Manager"
description: "单台 Linux 服务器上一体化的 Web 服务 + 数据库 + 站点运行环境面板：用 Caddy + PHP 8.4 FPM + Laravel 13 / Livewire 4 / SQLite 把安装、配置、运维集中起来，省去逐项手工配置。"
resource: "https://github.com/azerioid/azerioid-stack-manager"
tags: [linux, server, panel, caddy, php, laravel, livewire, sqlite, self-hosted]
timestamp: 2026-09-18T00:00:00Z"
---

# AZERIOID Stack Manager

## 它是什么

[azerioid/azerioid-stack-manager](https://github.com/azerioid/azerioid-stack-manager) 是一款**单台 Linux 服务器的 Web 全栈面板**，目标是把「Web 服务 + 数据库 + 站点运行环境」这三层从零散的命令和配置里收回到同一块面板里点几下装好。

它在一台 VPS 或裸金属服务器上按以下顺序铺底：

1. 装 [Caddy](https://caddyserver.com/) 作为反向代理与 HTTPS 入口
2. 起一个**独立的 PHP 8.4 FPM 进程池**
3. 用 [Laravel 13](https://laravel.com/) + [Livewire 4](https://livewire.laravel.com/) + [SQLite](https://www.sqlite.org/) 跑出管理面板本身

## 关键能力

| 能力 | 说明 |
|------|------|
| 一体化面板 | Web 服务 / 数据库 / 运行环境统一入口 |
| 反向代理 | Caddy 自动 HTTPS，证书由 Caddy 申请并续期 |
| 进程隔离 | 独立 PHP 8.4 FPM 池，与系统默认 PHP 解耦 |
| 管理面板本体 | Laravel 13 + Livewire 4 + SQLite，全栈单体应用 |

## 适合什么场景

- 单台 VPS 想从零搭起一个站点 / Web 服务，又不想逐项写 Nginx / PHP / 数据库配置。
- 个人 / 小团队在裸金属服务器上做轻量自托管，需要一块面板代替零散命令。
- 想要 Caddy 的自动化 HTTPS，又希望 PHP 池与系统默认 PHP 互不干扰的开发者。

## 参考

- 项目链接：<https://github.com/azerioid/azerioid-stack-manager>

![管理面板截图](https://pbs.twimg.com/media/HSY6k0RaYAAS9_N.jpg)
