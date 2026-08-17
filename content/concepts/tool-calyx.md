---
type: Tool
title: "Calyx"
description: "原生 macOS 终端应用，让用户并行运行并统一监督多个编码 AI agent，不必逐个翻看终端标签页"
resource: "https://github.com/yuuichieguchi/Calyx"
tags: [macos, terminal, coding-agent, multi-agent, parallel, supervisor]
timestamp: 2026-08-17T16:00:00Z
---

# Calyx

## 它是什么

`yuuichieguchi/Calyx` 是一个**原生 macOS 终端应用**（不是 Electron 套壳），专为「**同时跑多个编码 AI agent**」场景设计：在同一个窗口里**并行启动并统一监督**多个 agent 会话，**不用为每个 agent 单开一个终端标签**。

适用对象：并行让多个 Claude Code / Codex / OpenCode 干活，需要统一看进度、发送指令、终止任务。

## 为什么用它 / 适合什么场景

- 同时跑 2+ 个编码 agent 任务，不想开一堆终端标签。
- 想在 macOS 上用**原生应用**而非 Electron / Web 套壳（更省资源、更丝滑）。
- 想统一看每个 agent 的输出、输入、退出码、当前工作目录。
- 想从「面板」角度管理多个 agent，而不是命令行。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原生 macOS | 非 Electron，系统集成 + 性能更优 |
| 多 agent 并行 | 同一窗口跑多个 agent 会话 |
| 统一监督 | 一个面板看所有 agent 状态 |
| 免切标签 | 不用为每个 agent 单开终端 |
| 任务管理 | 启动 / 暂停 / 终止单个 agent |

## 媒体

- ![](https://pbs.twimg.com/media/HPwLvleaEAAQxa1.jpg)

## 原始链接

- [项目仓库](https://github.com/yuuichieguchi/Calyx)

## 相关概念

- [Vesta](./tool-vesta-terminal.md) — 同样是 macOS 原生、为 AI 编码 agent 设计的终端，但 Vesta 偏 session 持久化；Calyx 偏多 agent 并行
- [mux（Claude Code tmux 插件）](./tool-mux-claude-tmux.md) — 同为多会话管理思路，但 mux 走 tmux 浮动面板而非独立 GUI
- [FreeBuddy](./tool-freebuddy.md) — 同样并行承载多个编码 agent，但 FreeBuddy 偏桌面 GUI 而非终端