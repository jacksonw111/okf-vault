---
type: "Tool"
title: "AgentAcct（mikehasa/agentacct）"
description: "读 Claude Code 和 Codex 留在本地的会话日志，把 token 用量、预估费用和任务记录展成一个仪表盘。"
resource: "https://github.com/mikehasa/agentacct"
tags: [claude-code, codex, token-usage, cost, dashboard, observability]
timestamp: "2026-07-26T15:18:00Z"
---

# AgentAcct（mikehasa/agentacct）

## 它是什么

`mikehasa/agentacct` **读取 Claude Code 和 Codex 留在本地的会话日志**，把 **token 用量、预估费用和任务记录**展成一个**仪表盘**。

## 为什么用它 / 适合什么场景

- 同时重度使用 Claude Code + Codex，想**统一看花了多少**；
- 想按会话 / 按天 / 按项目**算 token 成本**而不是只盯着 LLM 平台账单；
- 需要在**本地**看这些数据，不希望再上传到云。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地日志读取 | 直接读 Claude Code / Codex 落盘的会话日志 |
| Token 用量 | 按会话 / 时间维度统计 |
| 费用预估 | 把 token 折算成钱 |
| 任务记录 | 每个任务的开销可追溯 |
| 仪表盘 | 一屏总览 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOHqZJfbUAA0XJw.jpg)

- 项目链接：<https://github.com/mikehasa/agentacct>

## 相关概念

- [Claude Code](tool-claude-code.md) — 本工具读取的本地日志来源之一
- [Inferock Bench](tool-inferock-bench.md) — 同样做代理成本/调用可观测（偏 API 流量拦截）
- [ai_usage_dashboard](tool-ai-usage-dashboard.md) — 同样做 AI 用量可视化（偏多厂商配额血条）
