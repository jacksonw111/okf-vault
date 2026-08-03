---
type: Tool
title: "Gendangzou (跟党走) Skill"
description: "把 A 股板块的政策、权威媒体、市场资金、公司与 ETF 数据封装成 AI Agent 可直接查询、组合和二次开发的 Skill，每项关键判断保留来源、日期和证据链。"
resource: "https://github.com/MobiusQuant/Gendangzou-skill"
tags: [ai-skill, a-stock, china, policy, etf, finance, quant]
timestamp: "2026-08-03T10:13:00Z"
---

# Gendangzou (跟党走) Skill

## 它是什么
Gendangzou（`MobiusQuant/Gendangzou-skill`）把 A 股板块的**政策、权威媒体、市场资金、公司与 ETF 数据**封装成 AI Agent 可直接查询、组合和二次开发的 Skill。每项关键判断保留来源、日期和证据链——避免 agent 凭空生成伪数据或凭印象下结论。

## 为什么用它 / 适合什么场景
- **政策面 + 资金面 + 基本面 三合一**：覆盖 A 股短线 / 中线决策的主要数据维度。
- **可溯源**：每项判断都带来源 + 日期 + 证据链，agent 不会给「一定涨」之类的虚高结论。
- **可二次开发**：作为 Skill 提供给多家 Agent 平台复用，不绑定单一模型 / workspace。

## 关键能力

| 能力 | 说明 |
|------|------|
| 政策数据 | 部委 / 交易所 / 监管的权威政策落库 |
| 权威媒体 | 财经主流媒体的官方口径与转载 |
| 市场资金 | 主力 / 北向 / 板块资金流数据 |
| 公司 + ETF | 个股基本面 + ETF 持仓 / 申赎数据 |
| 证据链 | 每项结论都保留来源 + 日期 + 证据链 |

## 项目链接
- <https://github.com/MobiusQuant/Gendangzou-skill>

## 相关概念
- [A 股数据 SDK](./tool-a-stock-data.md) — A 股数据获取的另一套工具
- [ETF 网格参数生成器](./tool-etf-grid-design.md) — Python Flask + React 的 ETF 网格交易参数生成器
- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的概念元定义
