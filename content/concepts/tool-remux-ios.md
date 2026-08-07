---
type: Tool
title: "Remux"
description: "h3nock 开发的 iOS 原生 tmux 远程管理 App：用 Ghostty 终端内核渲染，SSH 直连远程服务器上的 tmux，不走中继 / 不注册账号，密码和私钥存 iOS Keychain；会话 / 窗口 / 窗格模型完整保留，左右滑切窗口、底部面板实时预览窗格，支持拆分 / 缩放 / 关闭。"
resource: "https://github.com/h3nock/remux"
tags: [ios, tmux, ssh, ghostty, keychain, terminal, remote-work]
timestamp: 2026-08-06T14:30:00Z
---

# Remux

## 它是什么

h3nock 开发的 iOS 原生应用，让 iPhone / iPad 能像本地终端一样管理远程服务器上的 tmux 工作区。

## 为什么用它 / 适合什么场景

- 你日常依赖 tmux 做长任务 / 多窗格工作，又想在 iPhone 上临时远程看 / 操作。
- 不愿意为远程终端装第三方中转服务（Termius / Blink 等），坚持 SSH 直连。
- 需要 iOS Keychain 存密码和私钥而不是云同步。

## 关键能力

| 能力 | 说明 |
|------|------|
| Ghostty 终端内核 | 高质量渲染，颜色 / 字符宽度对齐桌面端 |
| 直连 SSH | 不走中继，无注册账号 |
| 完整 tmux 模型 | 会话 / 窗口 / 窗格 三层保留 |
| 手势优化 | 左右滑切窗口、底部面板实时预览窗格 |
| iOS Keychain | 密码和私钥系统级加密存储 |

## 相关概念
- [Pixshell](./tool-pixshell.md) — 跨平台原生 SSH/SFTP 客户端，macOS Swift + Windows WPF
- [MaidKit](./tool-maidkit.md) — 基于 Flutter 构建的跨平台 SSH 服务器管理器
- [Tmux Workbench](./tool-tmux-workbench.md) — tmux 状态栏增强工作台