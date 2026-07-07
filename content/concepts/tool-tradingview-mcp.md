---
type: Tool
title: "tradingview-mcp"
description: "通过 MCP 协议把 TradingView 市场数据 / 多交易所扫描器 / 回测引擎暴露给 AI 助手和自动化工具。"
resource: "https://github.com/jaipreet15/tradingview-mcp"
tags: [mcp, trading, market-data, backtest]
timestamp: "2026-07-07T12:00:00Z"
---

# tradingview-mcp

## 它是什么
`jaipreet15/tradingview-mcp` —— 把 **TradingView 市场数据 / 多交易所扫描器 / 回测引擎**通过 **MCP 协议**暴露给 AI 助手和自动化工具，让 Claude / Codex / Cherry Studio 等 MCP 客户端能像访问本地工具一样拉取行情、跑回测。

## 为什么用它 / 适合什么场景
- 想让 AI 助手**直接调实时行情数据**而不是写代码 + API key。
- 用 TradingView 但希望"对话里就能跑扫描 / 回测"。
- 适合做：交易策略助理、行情问答机器人、研究类工作流。

## 关键能力
| 能力 | 说明 |
|------|------|
| TradingView 数据 | 接入行情、K 线、技术指标 |
| 多交易所扫描器 | 跨交易所市场扫描 |
| 回测引擎 | 把策略想法在历史数据上跑一遍 |
| MCP 协议暴露 | 与任何 MCP 客户端（Claude / Codex / Cherry Studio）即插即用 |

## 相关概念
- [12306-mcp](tool-12306-mcp.md) — 12306 购票查询 MCP 服务器
- [a-stock-data](tool-a-stock-data.md) — A 股全栈数据 Skill
- [stock-sdk](tool-stock-sdk.md) — 浏览器端股票数据库（零依赖）
- [Vibe-Trading](tool-vibe-trading.md) — 港大 HKUDS AI 交易研究平台
- [codex-control-plane-mcp](tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP
- [devspace-mcp](tool-devspace-mcp.md) — 自托管 MCP 编程工作台
