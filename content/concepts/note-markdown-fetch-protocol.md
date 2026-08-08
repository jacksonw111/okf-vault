---
type: "Note"
title: "Markdown Fetch Protocol"
description: "「把任意网页抽成 Markdown」作为 LLM / RAG 友好的中间表示的思路：让 AI 面对结构化文本而非原始 HTML。"
tags: [markdown, web-scraping, llm, rag, protocol]
timestamp: "2026-08-08T20:00:00Z"
---

# Markdown Fetch Protocol

## 什么是 Markdown Fetch Protocol

「Markdown Fetch Protocol」不是单一规范，而是一类把「URL → Markdown」作为 AI 友好的中间表示的思路与工具集合。它假设：与其让 LLM 直接读 HTML，不如先把网页抽成结构化文本（Markdown / JSON），再喂给下游。

## 为什么是 Markdown

- **可读**：人审阅 LLM 抓的内容时，Markdown 比 HTML 直观得多。
- **结构化**：标题 / 列表 / 链接天然保留语义。
- **省 token**：相比 HTML，Markdown 通常显著更短。
- **RAG 友好**：Markdown 文本切片（chunking）效果比 HTML 干净。

## 主流实现

| 工具 | 形态 |
|------|------|
| [Sparkfetch](./tool-sparkfetch.md) | 轻量开源 URL → Markdown/JSON |
| [Jina Reader](./tool-jina-reader.md) | 在线 SaaS，r.jina.ai 直链 |
| [Firecrawl](./tool-firecrawl.md) | SaaS + 自托管，附 schema 抽取 |

## 适用场景

- RAG 知识库：从网页持续构建索引。
- AI agent：把网页作为上下文喂给 LLM。
- 内容聚合：把多个源统一成 Markdown 后再加工。

## 相关概念

- [Sparkfetch](./tool-sparkfetch.md) — Markdown Fetch Protocol 的轻量离线实现
- [Jina Reader](./tool-jina-reader.md) — 在线 SaaS 版代表
- [Firecrawl](./tool-firecrawl.md) — 商业 / SaaS 路线代表