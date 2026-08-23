---
type: Tool
title: "agent-office（AI 编码代理的 Slack 式协作环境）"
description: "baturyilmaz/agent-office，给一群 AI 编码代理一套类似 Slack 的协作环境：收件箱 / 频道 / 任务看板 / 定时任务 + 容器隔离，组成真正能分工的团队"
resource: "https://github.com/baturyilmaz/agent-office"
tags: [multi-agent, collaboration, slack-like, coding-agent, orchestration]
timestamp: "2026-08-23T04:55:00Z"
---

# agent-office（AI 编码代理的 Slack 式协作环境）

## 它是什么

[baturyilmaz/agent-office](https://github.com/baturyilmaz/agent-office) 给一群 **AI 编码代理**一套类似 **Slack** 的协作环境：收件箱、频道、任务看板、定时任务 + **容器隔离**，让一群 Agent 能像人一样**真正分工**。

针对的痛点：多个 AI 编码代理过去各干各的，缺少共享的协作平面。

## 为什么用它 / 适合什么场景

- 同时跑多个编码 Agent（Claude Code / Codex / Gemini CLI / Pi 等），想让它们有共同任务板 / 上下文。
- 想给 Agent 团队一个**可观测**的工作环境（谁在做什么、阻塞在哪里）。
- 需要按频道 / 项目隔离 Agent 工作空间，并加容器隔离避免互相干扰。

## 关键能力

| 能力 | 说明 |
|------|------|
| Slack 式 UI | 收件箱 / 频道 / 任务看板，对人友好 |
| 容器隔离 | 每个 Agent 任务在独立容器里跑 |
| 多 Agent 协作 | Agent 之间可派单 / 接单 / 互通上下文 |
| 定时任务 | 周期性工作可定时触发 |

## 媒体

- ![](https://pbs.twimg.com/media/HQX_hEBaoAAtb68.jpg)

## 相关概念

- [AgentSpace](./tool-agentspace.md) — 人 + AI 代理团队协作平台
- [Brigade](./tool-brigade.md) — 本地 AI 代理团队 + 共享长期记忆
- [Cotal](./tool-cotal.md) — 多智能体开放协议框架
- [coding-control-tower](./tool-coding-control-tower.md) — 同时跑多个 AI 编码 agent 的本地面板

## 参考链接

- [项目链接](https://github.com/baturyilmaz/agent-office)
