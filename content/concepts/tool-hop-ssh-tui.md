---
type: Tool
title: "hop（终端 SSH 多服务器切换 TUI）"
description: "Go 写的终端 TUI，内置 SSH 客户端和 VT 模拟器。在终端里直接连多台远程服务器，敲一下就进 shell，再敲一下就能翻远程文件或在服务器上直接编辑。不用开新窗口也不用反复输密码。"
resource: "https://github.com/p-arndt/hop"
tags: [ssh, tui, terminal, devops, multiplexer, go]
timestamp: "2026-07-30T01:38:00.000Z"
---

# hop

## 它是什么

**终端 SSH 多服务器切换器**——Go 写的 TUI，内置 SSH 客户端和 VT 模拟器。

打开一个终端窗口，敲几下：

- 选择远程服务器 → 直接进 shell
- 切到文件浏览器 → 浏览 / 编辑远程文件
- 再敲一下 → 切回另一个服务器

不用为每台机器开新窗口 / 新 Tab，不用记密码，不用换工具链。

![截图](https://pbs.twimg.com/media/HOXU4rpa4AA2cmr.jpg)
![截图](https://pbs.twimg.com/media/HOXU5ZgbQAAhNQF.jpg)

## 解决的痛点

| 传统痛点 | hop 解法 |
|----------|----------|
| 同时管理多台服务器 | 单 TUI 切换 |
| 来回输密码 / 加载 SSH key | 内置 SSH 客户端 |
| 远端文件操作靠 scp / rsync | 直接在 TUI 内编辑 |
| 服务器状态不可见 | 列表视图 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 内置 SSH 客户端 | 不依赖系统 ssh / ssh-agent 配置 |
| VT 模拟器 | 在 TUI 里跑完整 shell |
| 文件浏览器 | 远端文件翻页 / 编辑 |
| 多会话切换 | 跳服务器类似跳 tab |
| 终端原生 | 跑在任意 TTY，SSH 进去也能用 |

## 适合谁

- 同时管几台到几十台机器的运维 / SRE
- 经常在服务器上直接改配置但不想 vim 进去找文件的开发
- 想把 SSH 工作流集中在一个 TUI 而非散落的 iTerm tab 里的人

## 原始链接

- [项目仓库](https://github.com/p-arndt/hop)
- [推文剪藏](https://x.com/QingQ77/status/2082641828612846008)

## 相关概念

- [tmux-workbench](./tool-tmux-workbench.md) — tmux 会话记忆管理器，本地 + SSH 统一索引
- [PixShell（跨平台 SSH 客户端）](./tool-pixshell.md) — macOS Swift / Windows WPF 原生 SSH 客户端
- [sshbox](./tool-sshbox.md) — Go 单二进制 SSH 跳板工具，每会话一个受限 Alpine 容器