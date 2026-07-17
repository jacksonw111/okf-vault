---
type: "Tool"
title: "FreeBuddy"
description: "桌面工作台, 让多个本地编码 Agent（Codex / Claude Code / OpenCode / Cursor / Kimi / Qoder / CodeBuddy）各自占一个工作区并行干活, 所有任务统一追踪。"
resource: "https://github.com/maojindao55/freebuddy"
tags: "[agent-orchestration, coding-agents, desktop, multi-agent, workspace]"
timestamp: "2026-07-17T01:38:00Z"
---

# FreeBuddy

[FreeBuddy](https://github.com/maojindao55/freebuddy) 是一个**桌面工作台**, 把 Codex、Claude Code、OpenCode、Cursor、Kimi、Qoder、CodeBuddy 等本地编码 Agent 收进同一个 GUI, 让它们**各自占一个独立工作区并行干活**, 同时所有任务在统一面板里追踪。

## 它解决了什么

今天一个重度 AI 编码用户可能同时开着 Codex 改 React、Claude Code 写 ETL、Cursor 调 UI……它们彼此独立、目录隔离、上下文不共享, 体验上却要把 7 个终端叠着切。FreeBuddy 把这套「多 Agent 协同」统一搬到 GUI, 用户只看一个工作台：

- 每个 Agent 一个独立的 Workspace (目录 + 配置)
- 任务统一收口在面板中央
- 进度 / 失败 / 完成统一在底部状态栏

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 Agent 共存 | Codex / Claude Code / OpenCode / Cursor / Kimi / Qoder / CodeBuddy 同框并行 |
| 工作区隔离 | 每个 Agent 在自己的目录、配置下执行, 不互相污染 |
| 任务统一追踪 | 全部任务流水化展示, 可筛选可跳转 |
| 桌面 GUI | 不依赖终端, 一键启动即可 |

## 媒体

![](https://pbs.twimg.com/media/HNRO7bEbAAAu_MI.jpg)

## 参考链接

- [项目仓库](https://github.com/maojindao55/freebuddy)

## 相关概念

- [AgentCrew](./tool-agent-crew.md) — 多智能体协作聊天应用, FreeBuddy 偏桌面 GUI + 编码工作区
- [MCO（多 AI 编程代理编排层）](./tool-mco.md) — 中立编排层, 调度 Claude Code / Codex CLI / Gemini CLI, FreeBuddy 在 GUI 层与之相邻
- [PeakCode](./tool-peakcode.md) — AI 编码代理的图形界面, 思路相近, FreeBuddy 更专注于「多 Agent 并行工作区」场景
