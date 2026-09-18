---
type: Tool
title: "Monid"
description: "统一的 Agent 工具网关：一套 base URL + 一个 key 接入 2000+ 工具和 72+ 提供商，按调用计费、按需选端点，告别每家服务商单独配置。"
resource: "https://github.com/monid-ai/monid"
tags: [agent, gateway, llm, api, tools, unification]
timestamp: "2026-09-18T14:36:00Z"
---

# Monid

## 它是什么

[monid-ai/monid](https://github.com/monid-ai/monid) 是一种**统一的 Agent 工具网关 / 代理**。它把多家服务商（72+ 提供商）和它们背后的 2000+ 工具 / 端点，封装成「**一个 base URL + 一个 key**」的同质化调用接口。

传统做法：每接一个工具，都要去该服务商的 dashboard 申请 key、抄它的 base URL、记住它的 endpoint path，且常写死在 agent 代码里。Monid 把这一层收敛为一个统一入口。

## 关键能力

| 能力 | 说明 |
|------|------|
| 统一鉴权 | 一把 key 替代 N 把 key |
| 统一端点 | 一组 base URL 替代分散的 endpoint |
| 工具池规模 | 2000+ 工具、72+ 提供商 |
| 按调用计费 | 调用层粒度的成本可见 |
| 按需选端点 | 同一类需求可在多家提供商之间切换 |
| 抗硬编码 | 端点不再写死在 agent 代码里 |

## 适合什么场景

- 正在搭建一个调用多种外部工具的 agent 系统，被「每家服务商一份配置」拖慢。
- 想集中观察「某个工具本月调用了多少、花了多少钱」的团队 / 个人。
- 想做多家服务商的 failover / 切换，又不想为每一家都写一遍接入代码的开发者。

## 与相关概念的关系

- [MCP（Model Context Protocol）](./term-mcp.md) — Monid 与 MCP 是互补层：MCP 解决「agent ↔ 工具」的协议，Monid 解决「多服务商 ↔ 工具」的接入聚合。

## 参考

- 项目链接：<https://github.com/monid-ai/monid>

![架构图](https://pbs.twimg.com/media/HSdm153boAA2MdB.jpg)
