---
type: Tool
title: "Argo"
description: "给 AI Agent 用的多语言搜索工具：内置 120+ 搜索源、60+ 业务域（中英日韩、学术、代码、金融、新闻、百科），输出「证据候选 + 可信度评分」的精简 JSON 而非链接清单"
resource: "https://github.com/taxueseek/argo"
tags: [search, agent, multilingual, evidence, retrieval, rag]
timestamp: 2026-08-17T16:00:00Z
---

# Argo

## 它是什么

`taxueseek/argo` 是**专门给 AI Agent 用的多语言搜索工具**：
- 内置 **120+ 搜索源**、覆盖 **60+ 业务域**（学术 / 代码 / 金融 / 新闻 / 百科等）
- 支持**多语言**（中 / 英 / 日 / 韩等）
- **不返回链接清单或总结页**，而是返回**「证据候选 + 可信度评分」**的精简 JSON，方便 agent 直接消费

区别于传统搜索引擎：Argo 的输出是「**适合喂给 LLM 的结构化证据**」，而不是「给人看的搜索结果页」。

## 为什么用它 / 适合什么场景

- AI agent 需要联网搜索，但传统搜索 API 的 HTML / 长文本结果对 LLM 不友好。
- 想要「**带可信度评分的证据列表**」，让 agent 自己判断用哪几条。
- 跨语言搜索任务（中英日韩混搜），不想为每个语言接单独 API。
- 想给 RAG / 深度研究流程准备**结构化、可信度可量化**的输入。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多语言搜索 | 中 / 英 / 日 / 韩 + 多语种通用 |
| 多源聚合 | 120+ 搜索源，60+ 业务域 |
| 学术 / 代码 / 金融 / 新闻 / 百科 | 域化搜索路由 |
| 证据候选 | 输出结构化证据而非链接清单 |
| 可信度评分 | 每条证据带分数，方便 agent 加权 |
| JSON 输出 | 直接喂给 LLM / RAG 流程 |

## 媒体

- ![](https://pbs.twimg.com/media/HPvVtembUAA7DqD.jpg)

## 原始链接

- [项目仓库](https://github.com/taxueseek/argo)

## 相关概念

- [anysearch-skill](./tool-anysearch-skill.md) — 同样给 agent 用的统一搜索 Skill，但偏多家引擎聚合；Argo 偏多语言 + 证据评分
- [wigolo](./tool-wigolo.md) — 同样为 agent 提供搜索 / 抓取 / 研究能力；Argo 偏搜索证据化，wigolo 偏本地 + 隐私