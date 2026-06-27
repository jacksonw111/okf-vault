---
type: "Tool"
title: "global-stock-data（美港股全栈数据 Skill）"
description: "面向 AI 编程助手的美港股全栈数据 Skill：整合美股期权链、财报三表与 503 个 GAAP 财务指标 / 技术指标计算，封装成可直接调用的数据接口。"
tags: "[ai, finance, us-stock, hk-stock, data, agent-skills]"
timestamp: "2026-06-26T20:27:53.000Z"
resource: "https://github.com/simonlin1212/global-stock-data"
---

# global-stock-data（美港股全栈数据 Skill）

## 它是什么

[`global-stock-data`](https://github.com/simonlin1212/global-stock-data) 是 [`a-stock-data`](tool-a-stock-data.md) 的**美港股姊妹版**——把分散的美股 / 港股数据源整合成 AI 可直接调用的 Skill，覆盖期权链、财报三表、503 个 GAAP 财务指标和技术指标，让 Claude Code、Codex、Cursor 这类编程代理能立刻上手做美港股复盘或自动生成投研报告。

## 关键能力

| 能力 | 说明 |
|------|------|
| 美股期权链 | 完整期权链数据，覆盖常用到期日 |
| 财报三表 | 利润表 / 资产负债表 / 现金流量表 |
| GAAP 指标 | 503 个 GAAP 财务指标计算接口 |
| 技术指标 | 常用技术指标（MA / MACD / RSI / 布林等） |
| Skill 封装 | 适配 Claude Code / Codex / Cursor，agent 即取即用 |

## 适用场景

- 用 AI 代理快速拉取美股 / 港股财报做对比分析
- 量化研究中的财务因子 / 技术因子批量计算
- 自动生成美股 / 港股投研晨报
- 与 A 股版 [`a-stock-data`](tool-a-stock-data.md) 配合，跨市场做组合研究

## 参考链接

- [项目链接](https://github.com/simonlin1212/global-stock-data)
- [A 股姊妹版](tool-a-stock-data.md) — A 股版 Skill，覆盖行情 / 研报 / 龙虎榜等

## 相关概念

- [a-stock-data](tool-a-stock-data.md) — A 股姊妹 Skill，跨市场研究时互补
- [Finnhub 美股 API](tool-finnhub-api.md) — 另一份免费层美股 REST API 数据源
- [Mira（Agent-native 投研）](tool-mira.md) — 把 agent 用到投研流程的代表工具