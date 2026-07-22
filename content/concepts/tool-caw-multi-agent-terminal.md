---
type: Tool
title: "caw（04mg/caw）"
description: "04mg/caw，让你可以在浏览器里同时开多个 AI 编程智能体的终端，并盯住它们各自的状态。"
resource: "https://github.com/04mg/caw"
tags: "[ai-coding, multi-agent, terminal, browser, web-ui]"
timestamp: "2026-07-22T02:12:00Z"
---

# caw（04mg/caw）

## 它是什么

[`caw`](https://github.com/04mg/caw) 把多个 AI 编程智能体的终端**搬到浏览器里**，统一呈现它们的运行状态。你不再需要在多个本地终端窗口之间来回切换，也不用挨个等一个跑完再启动下一个。

## 解决什么痛点

- 本地开了 6 个终端跑 Claude Code / Codex / Cursor agent，分不清谁是谁；
- 状态都靠肉眼判断（光标闪不闪、最后一行输出是什么）；
- 想从一个统一的 web 入口看所有 agent 当前在干什么。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多终端聚合 | 浏览器里同时看多个 agent 的输出 |
| 状态可视化 | 各自状态（运行 / 等待 / 卡住）独立显示 |
| 浏览器即开 | 不依赖特定 OS 终端，本地启动一个 web 服务即可访问 |
| AI 编程 agent 优先 | 默认适配 Claude Code / Codex / Cursor 等常见 CLI |

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [mux](tool-mux-claude-tmux.md) | tmux 浮动面板 | 必须在 tmux 里用 |
| [coding-control-tower](tool-coding-control-tower.md) | 本地 dashboard | 偏观测 + token / PR 视角 |
| caw | 浏览器内多终端 | 形态最接近原始终端，但 web 化跨设备 |

## 媒体

![](https://pbs.twimg.com/media/HNt5MsBbAAAelWY.jpg)

## 原始链接

- [项目仓库](https://github.com/04mg/caw)

## 相关概念

- [Mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — 终端侧的多会话管理方案，caw 是它的浏览器侧平替
- [coding-control-tower](tool-coding-control-tower.md) — 偏会话生命周期 + token + PR 的观测面板，本工具偏实时终端流