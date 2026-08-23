---
type: Tool
title: "KITE（memoket 的非向量 AI 记忆方案）"
description: "memoket-kite，不用向量检索，靠结构化事实和可读的查询计划找回真正回答问题的记忆，避免「听起来最像」的幻觉"
resource: "https://github.com/memoket/memoket-kite"
tags: [agent-memory, structured-retrieval, non-vector, ai-memory, llm]
timestamp: "2026-08-23T10:22:00Z"
---

# KITE（memoket 的非向量 AI 记忆方案）

## 它是什么

[memoket/memoket-kite](https://github.com/memoket/memoket-kite) 是 memoket 出品的 **AI 记忆**方案：**不用向量检索**，而是把记忆存为**结构化事实 + 可读的查询计划**，检索时按查询计划去找真正能回答问题的那条记忆——而不是返回"听起来最像"的结果。

它针对的是常见向量记忆方案的痛点：检索时即便答案根本不存在也会硬给一个、还解释不了为什么。

## 为什么用它 / 适合什么场景

- 需要 Agent 记忆**可解释**：能说出"我是从哪条事实推出这个答案的"。
- 担心向量检索的"假命中"导致 Agent 幻觉。
- 想用更接近数据库 / 知识图谱的检索方式，而不是纯余弦相似度。

## 关键能力

| 能力 | 说明 |
|------|------|
| 非向量检索 | 走结构化事实查询，不靠余弦相似度 |
| 查询计划可读 | 检索过程以可读的计划呈现，便于调试 |
| 减少幻觉 | 没答案时倾向"找不到"而不是硬编 |
| 与 Agent 集成 | 适合作为 LLM 的外部长期记忆层 |

## 媒体

- ![](https://pbs.twimg.com/media/HQYBn85bkAAWOSN.jpg)

## 相关概念

- [cognee](./tool-cognee.md) — 同样基于知识图谱 + 向量混合检索的 AI 记忆
- [TencentDB-Agent-Memory](./tool-tencentdb-agent-memory.md) — 另一种四层渐进式 Agent 记忆方案
- [EverOS](./tool-everos.md) — 本地长期记忆层，让不同 agent 共享记忆

## 参考链接

- [项目链接](https://github.com/memoket/memoket-kite)
