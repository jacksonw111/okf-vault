---
type: Tool
title: "ccmux"
description: "epilande/ccmux，tmux 里跟踪多个 AI 编程 agent（Claude Code / Codex / Cursor 等）会话状态的小工具，一键跳到需要你处理的那个会话。"
resource: "https://github.com/epilande/ccmux"
tags: "[tmux, ai-coding, multi-agent, claude-code, codex, cursor, session-manager]"
timestamp: "2026-07-22T08:53:00Z"
---

# ccmux

## 它是什么

[`ccmux`](https://github.com/epilande/ccmux) 是一个 tmux 工具，专为「同时跑多个 AI 编程 agent」的开发者设计。它在 tmux 状态栏里展示每个会话的状态，按一键就能跳到需要处理的那个会话。

## 解决什么痛点

- tmux 里同时挂着 8 个 agent 会话，记不清哪个卡了、哪个等你；
- 切换会话靠 `tmux choose-tree` 或记忆快捷键，效率低；
- 想统一看到所有 agent 的运行 / 等待状态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 agent 支持 | Claude Code / Codex / Cursor 等常见编码 CLI |
| 一键跳转 | 直接跳到目标会话窗口 |
| 状态可读 | 在 tmux 状态栏或弹窗里看到「哪个在等」 |
| 轻量集成 | 作为 tmux 插件存在，不开额外进程 |

## 与同类工具的差异

| 工具 | 范围 | 差异 |
|------|------|------|
| [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) | Claude Code only | 单 agent |
| [ccmux](tool-ccmux.md) | Claude Code / Codex / Cursor | 多 agent 通用 |
| [tmux-spotlight](tool-tmux-spotlight.md) | 通用 tmux 会话 | 不区分 agent |
| [caw](tool-caw-multi-agent-terminal.md) | 浏览器终端 | 跨设备 |

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2079399307648864256/vid/avc1/1716x1080/pP8GTjVS5lCgyCk8.mp4?tag=29>

## 原始链接

- [项目仓库](https://github.com/epilande/ccmux)

## 相关概念

- [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — 同思路但只服务 Claude Code，ccmux 是 Claude Code 之外的扩展
- [tmux-spotlight](tool-tmux-spotlight.md) — 通用 tmux Spotlight 风格切换器，本工具聚焦在 AI agent 会话
- [coding-control-tower](tool-coding-control-tower.md) — 偏会话生命周期观测，本工具偏会话切换操作