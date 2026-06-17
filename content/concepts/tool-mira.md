---
type: "Tool"
title: "Mira（Agent-native 投研工作台）"
description: "byteseek 开源的「面向 AI Agent 的投资研究」系统：不是荐股 bot / 交易助手，而是一套可复核、可持续刷新的投研协议——分析路由 → 研究框架组织证据 → 区分事实/推断/判断 → 沉淀 investment memo、evidence log、thesis ledger + 刷新条件。"
tags: "[ai, agent, finance, investment-research, evidence-tracked]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/byteseek/Mira"
---

# Mira

## 它是什么

[`Mira`](https://github.com/byteseek/Mira) 是 byteseek (@bc1dml) 开源的 **Agent-native 投资研究工作台**。它的定位刻意和市面上 95% 的「AI 投顾」「荐股 bot」「交易助手」划清界限：

> "它不是荐股 bot，也不是交易助手，而是一套可复核、可持续刷新的投研协议。"

## 核心方法论

```
输入（股票 / 产业 / ETF / 财报 / 宏观）
  ↓ 1. 分析路由（先判断属于哪类研究）
  ↓ 2. 研究框架（按对应框架组织证据）
  ↓ 3. 证据分离（事实 vs 推断 vs 判断）
  ↓
沉淀产物：
  - investment memo（投研备忘录）
  - evidence log（证据台账：每条判断的出处）
  - thesis ledger（论点台账：当前主张）
  - 刷新条件（什么信号出现就更新论点）
```

## 关键能力

| 能力 | 说明 |
|------|------|
| 分析路由 | 决定走哪个研究框架（财报 / 行业 / 宏观 / ETF） |
| 证据分离 | 把「事实」「推断」「判断」显式分层，避免幻觉污染 |
| Investment Memo | 结构化备忘录 |
| Evidence Log | 每条判断都有出处可查 |
| Thesis Ledger | 论点状态机：当前主张 + 触发更新条件 |
| 可刷新 | 新数据进来按 ledger 决定要不要更新 memo |
| Agent-native | 设计给 [Claude Code](./tool-claude-code.md)、Codex、Workbuddy、Marvis 等 agent 客户端用 |

## 为什么这个思路重要

普通「AI 投顾」的失败模式：把幻觉当判断、把历史当预测、把单一来源当结论。Mira 的核心贡献是**把「证据—推断—判断」的边界画清楚**，并把整个过程**显式**——任何时候任何 agent / 人都能：

- 审计一个论点的证据链；
- 知道哪些数据进来要重做判断；
- 区分「这是事实」「这是模型推测」「这是策略选择」。

这套方法论不只适用于投资——任何需要「长期跟踪 / 证据驱动 / 可更新判断」的场景（医疗、学术、商业情报）都能套。

## 与本知识库的关系

- Mira 的产物（memo / log / ledger）**形态上**就是 [OKF 概念文件](./term-okf.md)——每个文件 = 一个观点，带 frontmatter 标 `type: Memo` / `Evidence` / `Thesis`。
- 它可作为**长期运行的 agent skill**：把 inbox → 投研概念 → 论点 ledger 的链路跑成常驻流程。

## 相关概念

- [Agent Skills 是什么](./term-agent-skills.md)
- [Claude Code](./tool-claude-code.md)
- [PRODUCER.md 协议](./../PRODUCER.md)
