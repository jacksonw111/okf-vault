---
type: Tool
title: "Open Agent View（15+ 本地编码工具的终端仪表盘：哪些在跑、哪些需要你介入）"
description: "把 Claude Code、Codex、Cursor、Pi 等 15+ 种本地编码 Agent 工具的会话统一收进一个终端仪表盘，一眼看出哪些任务在跑、哪些需要你介入、哪些已经挂死，免开一堆终端标签页。"
resource: "https://github.com/xhluca/open-agent-view"
tags: [agent, terminal, dashboard, monitoring, claude-code, codex, cursor, pi, tui]
timestamp: "2026-08-28T00:00:00Z"
---

# Open Agent View

## 它是什么
[xhluca/open-agent-view](https://github.com/xhluca/open-agent-view) 是**给 15+ 种本地编码 Agent 工具统一接进同一个终端仪表盘**的轻量 TUI。

痛点：随着本地编码 Agent 工具越来越多（Claude Code、Codex、Cursor、Pi、Aider、Cody、Continue、Phind 等），开发者常常**同时开 5–10 个终端标签页**盯不同 Agent 的运行——状态散落、上下文不一致、哪些任务需要人介入只能靠记忆。

Open Agent View 收拢这些会话到**一个 TUI 仪表盘**：

- **所有任务的当前状态**（运行中 / 等待中 / 已完成 / 失败）；
- **每个 Agent 的最近输出**摘要；
- **需要你介入**的会话单独高亮；
- 不需要切换终端标签页即可逐个跟进。

## 为什么用它 / 适合什么场景
- 同时跑 3+ 个本地编码 Agent，想**一眼看到全局状态**而不是逐个切窗口；
- 团队 / 个人需要**审计**一段时间内所有 Agent 的工作历史；
- 在远程 SSH 终端里也想管本地 Agent（不依赖图形化 IDE）；
- 想给多 Agent 并行任务一个**共享监控面板**。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多工具接入 | Claude Code / Codex / Cursor / Pi 等 15+ 本地编码工具 |
| 终端仪表盘 | TUI 形态，一个屏幕看全部 |
| 状态分层 | 运行中 / 等待 / 完成 / 失败 四类颜色高亮 |
| 介入提示 | 需要人决策的会话单独提示 |
| 历史回溯 | 每个 Agent 最近输出摘要 |
| 零切换 | 不需切终端标签页 |
| SSH 友好 | 纯终端，远程也能用 |

## 相关概念
- [Strado](tool-strado.md) — 多 AI 编码代理工作台（独立 worktree + IDE 验证）；Open Agent View 是更**轻**的**只读监控层**
- [Lody](tool-lody.md) — 跨机器多 Agent 协作；Open Agent View 是**单机多工具**的统一仪表盘
- [Calyx](tool-calyx.md) — 同样面向「多 Agent 终端监控」的并行任务面板

## 参考链接
- 项目链接：<https://github.com/xhluca/open-agent-view>
- 原始推文：<https://x.com/QingQ77/status/2093244693601825148>
- 媒体：<https://video.twimg.com/amplify_video/2093199554443448320/vid/avc1/1292x784/iJyp7dpn3DPzRl_1.mp4?tag=29>
