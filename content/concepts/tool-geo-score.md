---
type: "Tool"
title: "geo-score（答案引擎友好度 GEO 评分工具）"
description: "geo-score 用公开量表检查网站是否具备被 ChatGPT / Perplexity / Google AI 等答案引擎读取和引用的条件，并指出最值得先补的缺口。"
resource: "https://github.com/jianruntech/geo-score"
tags: "[geo, answer-engine, chatgpt, perplexity, google-ai, llm-seo, audit, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# geo-score（答案引擎友好度 GEO 评分工具）

## 它是什么

[geo-score](https://github.com/jianruntech/geo-score) 是一个**GEO（Generative Engine Optimization）评分工具**——用**公开量表**给一个网站打分，回答：

> 我的网站**是否具备被 ChatGPT / Perplexity / Google AI 等答案引擎读取和引用**的条件？

并给出**最值得先补的缺口**清单。

## 为什么用它 / 适合什么场景

- 做内容站 / SaaS / 文档站，希望**被 LLM 答案引擎引用**，但不知道现在到底缺什么。
- 「**LLM SEO**」和传统 SEO（Google 关键词）不一样——需要专门针对「**答案引擎怎么读 / 怎么引**」做体检。
- 想用**公开标准量表**做评估，避免被某个 SaaS 的「独家指标」绑定。
- 拿到一份缺口清单后，可以**直接交给 Agent Skill**（如 [jev-seo](./tool-jev-seo.md) / [awesome-design-md](./tool-awesome-design-md.md) 思路）逐条修复。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本地工具 |
| 量表 | 公开量表（非闭源指标） |
| 评估对象 | 网站对 ChatGPT / Perplexity / Google AI 等答案引擎的可读性 / 可引用性 |
| 输出 | GEO 评分 + 缺口清单（按优先级） |
| 适用 | 内容站 / SaaS / 文档站 |

## 媒体

![](https://pbs.twimg.com/media/HTByIavboAAMWaP.jpg)

## 相关概念

- [jev-seo](./tool-jev-seo.md) — 同为「网站体检 + 改进清单」思路的 SEO 工具，geo-score 聚焦答案引擎侧
- [RAG（检索增强生成）](./term-rag.md) — 答案引擎「读取 / 引用」网站内容的底层机制
