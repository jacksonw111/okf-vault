---
type: "Tool"
title: "agent-quantspace（quantskills/agent-quantspace）"
description: "为 AI 编码工具(Claude Code / Codex / Cursor)重做的量化投研框架:数据接入 / 因子 / 回测 / 报告收在固定 skill 边界内,项目里写清楚想法,AI 顺着边界生成代码。"
resource: "https://github.com/quantskills/agent-quantspace"
tags: "[quant, ai-trading, agent-framework, finance, backtest, factor]"
timestamp: "2026-07-14T08:07:00Z"
---

# agent-quantspace（QuantSpace）

[agent-quantspace](https://github.com/quantskills/agent-quantspace) 是为 **AI 编码工具**(Claude Code / Codex / Cursor)重做的**量化投研框架**:把数据接入、因子、回测、报告都收在一套**固定 skill 边界**里,你只管在项目目录里把想法说清楚。

## 关键设计

| 维度 | 设计 |
|------|------|
| 边界 | 量化研究的固定动作(取数据 / 写因子 / 跑回测)封装为 skill |
| 角色 | AI 编码 agent 是执行者,你只写**意图说明** |
| 可审计 | AI 生成的代码仍在固定 skill 边界内,容易 review |
| 可复现 | 项目目录结构化,实验可重现 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 数据接入 | 统一 stock-sdk 等数据源,无需自己写爬虫 |
| 因子开发 | 在固定目录下加因子定义,AI 转化为代码 |
| 回测 | 跑标准回测流水线并出报告 |
| 报告 | 自动出量化报告(Markdown) |
| 工程边界 | 限制 AI 写出「散装」代码,强制走 skill 边界 |

## 适合什么场景

- 想用 **AI 写量化策略**但怕代码散装、难复盘的团队 / 个人。
- 量化研究的新人:**让 AI 帮你写样板**,聚焦在**思路表达**。
- 教学 / 培训:把整套 skill 边界当成「量化工程规范」示范。

## 与同类资源的差别

| 资源 | 特征 | QuantSpace |
|------|------|-----------|
| tickflow-stock-panel | 自托管 A 股量化工作台 | 偏运营 / 监控;QuantSpace 偏研究框架 |
| Vibe-Trading | 29 个 AI Agent 跑量化流水线 | 多 agent 平台;QuantSpace 强调「skill 边界」 |
| a-stock-data / global-stock-data | 数据源 | QuantSpace 是上层框架,数据可接它们 |

## 参考链接

- [项目仓库](https://github.com/quantskills/agent-quantspace)

## 相关概念

- [tickflow-stock-panel](./tool-tickflow-stock-panel.md) — 同样面向 A 股量化的自托管工作台,QuantSpace 偏研究框架
- [Vibe-Trading](./tool-vibe-trading.md) — AI Agent 驱动的量化研究平台
- [stock-sdk](./tool-stock-sdk.md) — 浏览器端股票数据库,QuantSpace 可作为其上层框架
