---
type: "Tool"
title: "dotfiles-manager"
description: "Rust 写的 dotfiles 同步工具：用 profile 机制让 dotfiles 在多台机器之间保持一致，支持备份、恢复、检查三个命令，新机器上克隆仓库 link 即可还原，敏感文件可加密、密码存钥匙串。"
resource: "https://github.com/alexandretrotel/dotfiles-manager"
tags: [dotfiles, rust, sync, backup, profile]
timestamp: "2026-08-08T20:30:00Z"
---

# dotfiles-manager

## 它是什么

dotfiles-manager 是一款用 Rust 写的 dotfiles 同步工具。它用「profile」机制让同一份 dotfiles 在多台机器（笔记本 / 桌面 / 服务器 / WSL）之间按角色分发，并配套 backup / restore / check 三个命令，新机器上克隆仓库 link 即可还原。敏感文件可加密，密码可存系统钥匙串或临时输入。

## 为什么用它 / 适合什么场景

- 多台机器（家用 / 公司 / 服务器）需要保持 dotfiles 一致。
- 不同机器要不同 profile（如笔记本 vs 服务器）。
- 希望敏感配置加密后再提交 Git。
- 想要一个 Rust 写的稳定、跨平台 dotfiles 工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| Profile 机制 | 一份 dotfiles 按角色分发到不同机器 |
| 三命令工具链 | backup / restore / check 配套 |
| 新机一键 link | 克隆 + link 即还原 |
| 敏感文件加密 | 密码存钥匙串或临时输入 |
| Rust 实现 | 单一二进制、跨平台、启动快 |

## 相关概念

- [Homebrew App](./tool-homebrew-app.md) — macOS 原生 GUI 管理 Homebrew formulae / casks
- [Lazycron](./tool-lazycron.md) — Linux cron TUI 管理器
- [TidyFS](./tool-tidyfs.md) — Linux 智能文件整理工具