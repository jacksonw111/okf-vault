---
type: Tool
title: "EvoOntology（数据 Agent 业务词典）"
description: "给数据分析 AI 助手打造一本业务词典：自动梳理企业表 / 字段的真实业务含义，AI 一边干活一边自动补充和修正，越用越懂业务。"
resource: "https://github.com/ruc-datalab/EvoOntology"
tags: [data-agent, ontology, business-glossary, llm, text-to-sql, analytics]
timestamp: "2026-09-18T10:43:00Z"
---

# EvoOntology（数据 Agent 业务词典）

## 它是什么

[EvoOntology](https://github.com/ruc-datalab/EvoOntology)（ruc-datalab 出品）是一个**给数据 Agent 用的业务词典 / 本体构建工具**。

许多企业的表 / 字段只记录代号和数字，AI agent 做分析时很难直接看懂背后的真实业务含义，每次都要重新猜、重复摸索。EvoOntology 把这些隐藏的业务规则**梳理成结构化的知识库**（ontology），让数据 Agent 在分析 / Text-to-SQL 时有一份可查的「业务词典」。

更妙的是：它能**一边看 AI 干活，一边自动补充和修正这本词典**——AI 用得越多，词典越准，AI 越准。

## 关键能力

| 能力 | 说明 |
|------|------|
| 业务词典 | 表 / 字段 → 真实业务含义的映射 |
| 结构化本体 | 把散落的业务规则整理为 ontology |
| 自动补充 | AI 干活过程中词典自动扩充 |
| 自动修正 | AI 用错的解释会被识别并修正 |
| 越用越准 | 与 AI Agent 形成反馈闭环 |
| Text-to-SQL 友好 | 给 text-to-sql 类任务提供语义层支撑 |

## 适合什么场景

- 数据团队里数据分析 / Text-to-SQL agent 总在「猜字段含义」上栽跟头的工程师。
- 企业里表 / 字段命名不规范、靠「老员工口口相传」维持语义一致性的组织。
- 想把业务词典与 AI agent 绑成反馈环，让知识库随使用自动演进的团队。

## 与相关概念的关系

- [RAG（检索增强生成）](./term-rag.md) — EvoOntology 在数据语义层做的事，是 RAG 在业务词典 / ontology 上的特化形态。
- [Context Engineering（上下文工程）](./term-context-engineering.md) — 它本质上是一种「**自动维护的上下文源**」，让 AI 不必每次都从头学业务。

## 参考

- 项目链接：<https://github.com/ruc-datalab/EvoOntology>
- 论文：<https://arxiv.org/abs/2609.15779>

![业务词典结构示意](https://pbs.twimg.com/media/HSe0tH3aYAAB1Ph.jpg)
