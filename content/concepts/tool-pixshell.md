---
type: Tool
title: "PixShell（跨平台原生 SSH/SFTP 客户端）"
description: "macOS 用 Swift、Windows 用 WPF——原生跨平台 SSH/SFTP 客户端，不是 Electron 套壳。终端渲染走 SwiftTerm / xterm.js，SSH 走 SwiftNIO / SSH.NET，双端功能对齐。"
resource: "https://github.com/lyu0805/pixshell"
tags: [ssh, sftp, macos, windows, swift, wpf, native, terminal]
timestamp: "2026-07-30T03:37:00.000Z"
---

# PixShell

## 它是什么

**真正的原生跨平台 SSH/SFTP 客户端**——不像 Termius / Electerm 之类用 Electron 套壳，PixShell 在每个平台都走原生 UI 框架：

| 平台 | UI 框架 | 终端渲染 | SSH 实现 |
|------|---------|----------|----------|
| macOS | Swift + SwiftUI/AppKit | SwiftTerm | SwiftNIO |
| Windows | WPF | xterm.js 跑在 WebView2 | SSH.NET |

![截图](https://pbs.twimg.com/media/HOcVQcja4AAInBu.jpg)
![截图](https://pbs.twimg.com/media/HOcVRDCbQAAxTds.jpg)

双端功能对齐：

- 多标签终端
- 连接管理（保存 / 分组 / 搜索）
- SFTP 传文件
- 暗色 / 亮色主题
- 代理（HTTP / SOCKS5）
- 密钥管理
- 云备份
- 文本编辑器
- 下载管理

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生 UI | 不依赖 Electron |
| 双端对齐 | macOS / Windows 功能一致 |
| 终端内嵌 | 真 VT 渲染 |
| SFTP | 浏览器风格的文件管理 |
| 主题 / 代理 / 密钥 | 完整工程化 |

## 适合谁

- 同时用 Mac 和 Windows 的工程师（家里 Mac / 公司 Windows）
- 觉得 Termius / Electerm 太重或太贵的人
- 追求原生 UI 性能 / 体验的用户
- 想自托管 SSH 配置（云备份）的团队

## 原始链接

- [项目仓库](https://github.com/lyu0805/pixshell)
- [推文剪藏](https://x.com/QingQ77/status/2082671776081781206)

## 相关概念

- [hop](./tool-hop-ssh-tui.md) — Go 写的终端 SSH 多服务器切换 TUI
- [sshbox](./tool-sshbox.md) — Go 单二进制 SSH 跳板，每会话一个受限 Alpine 容器
- [tmux-workbench](./tool-tmux-workbench.md) — tmux 会话记忆管理器