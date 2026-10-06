---
type: "Tool"
title: "Termux"
description: "Android 上的开源终端模拟器 + Linux 用户态环境——无需 root 即可在手机上跑 apt / git / python / node / ssh / tmux / nvim / claude-code 等大多数 CLI 工具；是 Android 端 SSH 服务器 / 本地编程环境的代表方案。"
resource: "https://termux.dev"
tags: "[termux, android, terminal, linux, ssh, cli]"
timestamp: "2026-10-06T22:51:00Z"
---

# Termux

## 定义

**Termux** 是 Android 平台上的开源**终端模拟器 + Linux 用户态环境**——通过自带 proot + busybox 实现「无需 root 即可运行完整 apt 包管理」，让用户在 Android 设备上跑 git / python / node / ssh / tmux / nvim / claude-code 等绝大多数 Linux CLI 工具。是 Android 端跑 SSH 服务器、本地编程环境、自托管控制端的事实标准。

## 要点

- **官网**：[termux.dev](https://termux.dev)
- **形态**：APK 安装的 Android App，启动后是一个终端
- **能力**：`apt install <pkg>` 直接装 Debian/Ubuntu 用户态软件
- **典型场景**：
  - 把旧手机变成 SSH / Web 服务器（[`tool-serverbox`](tool-serverbox.md) 的替代）
  - 手机跑 Claude Code / Codex CLI
  - 远程连接 VPS / 自托管服务器
  - 学习 Linux / 编程
- **扩展**：Termux:API（访问 Android 硬件接口）/ Termux:Widget / Termux:Boot

## 相关概念

- [ServerBox](./tool-serverbox.md) — 同为 Android 自托管方向
- [Self-Hosted](./term-self-hosted.md) — 部署形态
