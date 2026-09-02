---
type: Tool
title: "Clawdeck"
description: "零依赖的 Claude Code 本地仪表盘：在浏览器里实时看到 Claude Code 在项目里到底干了什么——会话、事件、成本、工树、评审一屏掌握，无需构建步骤。"
resource: "https://github.com/m-sanchez/clawdeck"
tags: [claude-code, dashboard, monitoring, observability, local-first]
timestamp: 2026-09-02T12:00:00Z
---

# Clawdeck

## 它是什么

Claude Code 默认在终端里跑，会话历史、事件流、token 成本、改了哪些文件、review 节点等状态都得靠 `Ctrl+R` 回看。`Clawdeck` 提供一个零依赖的本地仪表盘：浏览器打开就能看到 Claude Code 当前的会话、事件流、成本、工树、评审一屏掌握。不需要构建步骤（打开即用），也不依赖外部服务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零依赖 | 不需要 npm install / 构建，浏览器即开 |
| 会话 + 事件流 | 实时看到 Claude Code 在做什么、改了什么 |
| 成本追踪 | token 用量 / 花费统计 |
| 工树 + 评审 | 文件改动树与评审节点在同一面板 |

## 项目链接

- [项目主页](https://github.com/m-sanchez/clawdeck)

## 相关概念

- [AgentTrail](./tool-agenttrail.md) — 另一种把 Agent 实时工作画成可视化地图的工具
- [Claude Code](./tool-claude-code.md) — Clawdeck 观测的对象
