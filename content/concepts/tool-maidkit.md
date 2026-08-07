---
type: Tool
title: "MaidKit"
description: "基于 Flutter 构建的跨平台 SSH 服务器管理器：运维人员无需在服务器上安装任何软件，仅凭 SSH 即可完成日常服务器维护。"
resource: "https://github.com/Solsynth/MaidKit"
tags: [flutter, ssh, server-management, devops, cross-platform, mobile]
timestamp: 2026-08-06T07:30:00Z
---

# MaidKit

## 它是什么

Solsynth 开发的跨平台 SSH 服务器管理工具（Flutter 实现），强调「零服务端安装」——只要能 SSH 就能管。

## 为什么用过它 / 适合什么场景

- 运维 / 个人站长想用手机 / 平板临时管一台服务器，不想装 Web 控制台（宝塔 / 1Panel 等）。
- 已经习惯 SSH 但想要更顺手的多机管理界面（多标签、命令片段、批量执行等）。
- 喜欢 Flutter 跨端一致体验：iOS / Android / macOS / Linux / Windows 同一套 UI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 纯 SSH | 服务端无需安装任何 agent 或面板 |
| 跨平台 | Flutter 单代码库覆盖 iOS / Android / 桌面 |
| 日常运维 | 跑命令、看日志、改配置、批量操作 |
| Flutter UI | 现代化、响应式、跨端一致的运维体验 |

## 相关概念
- [Remux](./tool-remux-ios.md) — iOS 原生 tmux 远程管理 App
- [Pixshell](./tool-pixshell.md) — 跨平台原生 SSH/SFTP 客户端
- [KPanel](./tool-kpanel.md) — 开源免费 Linux 服务器管理面板