---
type: Tool
title: "agent-manager (tmux TUI)"
description: "YoanWai/agent-manager，Go 写的 TUI 管理器，架在 tmux 上统一管理 Claude Code / Codex / OpenCode / Grok Build 等 AI 编码 agent；每路 agent 跑在独立 tmux session，manager 退出不影响运行。"
resource: "https://github.com/YoanWai/agent-manager"
tags: "[go, tui, tmux, ai-coding, multi-agent, claude-code, codex, opencode, grok-build]"
timestamp: "2026-08-01T20:30:00Z"
---

# agent-manager (tmux TUI)

## 它是什么

[`YoanWai/agent-manager`](https://github.com/YoanWai/agent-manager) 是一个 Go 写的 TUI 管理器，**架在 tmux 上**统一管理多路 AI 编码 agent（Claude Code / Codex / OpenCode / Grok Build 等）。每路 agent 都跑在**独立的 tmux session** 里，manager 退出不影响 agent 持续运行。

## 解决什么痛点

- 同时跑 5 个 AI 编码 agent 来对比效果，终端里来回翻 tab / pane 烦
- 想看到「谁还在跑 / 谁卡住等输入 / 谁跑完了」
- 直接用 tmux 自己起 session 又嫌管理麻烦（attach / detach / 命名）

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 AI agent 兼容 | Claude Code / Codex / OpenCode / Grok Build 等 |
| TUI 面板 | 一个屏幕看到所有 agent 的运行状态（运行中 / 等待 / 完成） |
| 独立 tmux session | 每路 agent 跑在独立 session，manager 退出不杀进程 |
| Go 实现 | 启动快，单二进制 |

## 适合什么场景

- 多 AI 编码 agent 并行（同一个任务跑多家模型对比效果）
- 长时间 agent 任务需要「托管」（关闭 manager 也不影响后台跑）
- 想要比「5 个 tab + 命名规范」更结构化的多 agent 管理面板

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [ccmux](./tool-ccmux.md) | tmux 状态栏 | 单 helper，指示 + 跳转 |
| [ccsessions](./tool-ccsessions.md) | TUI | 历史会话浏览，不做运行监控 |
| [tmux-workbench](./tool-tmux-workbench.md) | TUI + CLI | 通用 tmux 会话记忆管理 |
| agent-manager | TUI | 多 AI agent + 独立 session 托管 |

## 媒体

![agent-manager 截图](https://pbs.twimg.com/media/HOhbYVTaEAAQC4m.jpg)

## 原始链接

- [项目仓库](https://github.com/YoanWai/agent-manager)
- [原始推文](https://x.com/QingQ77/status/2083558871180967970)

## 相关概念

- [ccmux](./tool-ccmux.md) — 同为 tmux 上的 AI 编码助手辅助，定位更轻（状态栏指示器）
- [ccsessions](./tool-ccsessions.md) — 偏历史会话浏览，agent-manager 偏运行监控
- [tmux-workbench](./tool-tmux-workbench.md) — 不限 AI agent 的通用 tmux 会话记忆管理