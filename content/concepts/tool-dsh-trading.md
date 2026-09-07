---
type: Tool
title: "dsh-trading"
description: "基于 DeepSeek Harness 的 Agent 原生交易终端，一个界面管理加密货币 / 美股 / A 股 / 港股四个市场，19+ 数据源/券商可热切换，默认模拟下单，实盘需逐笔人工审批。"
resource: "https://github.com/zhu1090093659/dsh-trading"
tags: "[trading, agent, deepseek, multi-market, crypto, stocks]"
timestamp: "2026-09-07T13:01:00Z"
---

# dsh-trading

## 它是什么
一个基于 DeepSeek Harness 思想构建的"Agent 原生"跨市场交易终端，单界面统一管理加密货币、美股、A股、港股四类市场。下单默认仅模拟，进入实盘需要手动开启开关，并且每笔订单都需要人工审批——headless 环境会被直接拦截。

## 核心思路
- **多市场聚合**：一个 UI 同时呈现四类资产（加密货币、美股、A 股、港股）的行情与账户
- **数据源/券商热切换**：内置 19+ 数据源与券商适配器，运行时可切换而不需重启
- **Agent 执行层**：决策可由本地 Agent 给出，调用统一交易适配器下单
- **多层人工把关**：模拟 → 实盘的开关 + 每笔实盘单审批 + 无头环境强制拦截

## 关键能力
| 能力 | 说明 |
|------|------|
| 多市场 | 加密货币 / 美股 / A 股 / 港股 统一视图 |
| 数据源热切换 | 19+ 数据源/券商，运行时切换 |
| 默认模拟 | 不开开关就只是模拟盘 |
| 实盘逐笔审批 | 每笔实盘单都需要人确认 |
| Headless 拦截 | CI/无人值守场景无法下单 |
| Agent 原生 | 与 DeepSeek Harness 类 Agent 框架对接 |

## 适用场景
- 个人多市场投资统一管理
- Agent / 半自动交易研究
- 防止 Agent 在无人监督下直接下单

## 参考
- 项目链接：<https://github.com/zhu1090093659/dsh-trading>

## 相关概念
- [DeepSeek Harness](note-deepseek-harness-handbook.md) — 同名框架思想，dsh-trading 借鉴其 Agent 执行层
- [tickflow-stock-panel](tool-tickflow-stock-panel.md) — 另一个自托管 A 股量化工作台
- [Vibe-Trading](tool-vibe-trading.md) — 多 AI Agent 一句话跑量化研究流水线