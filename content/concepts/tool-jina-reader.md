---
type: "Tool"
title: "Jina Reader"
description: "Jina AI 推出的 URL → Markdown 在线服务（r.jina.ai）：把任意网页转成 LLM 友好的干净 Markdown，可直链或调 API。"
resource: "https://jina.ai/reader/"
tags: [web-scraping, html-to-markdown, llm-friendly, saas]
timestamp: "2026-08-08T20:00:00Z"
---

# Jina Reader

## 它是什么

Jina Reader 是 Jina AI 推出的 URL → Markdown 在线服务（域名前缀 `r.jina.ai`）。它把任意 URL 转成 LLM 友好的干净 Markdown，并提供可直接拼接到 prompt 里的直链形式，是「让 LLM 看懂网页」最简方案之一。

## 为什么用它 / 适合什么场景

- 临时给 LLM 喂网页内容，不想自建抓取管线。
- 想用一行 URL 把网页塞给 OpenAI / Anthropic 等模型。
- 需要把网页转 Markdown 做语料或搜索索引。

## 关键能力

| 能力 | 说明 |
|------|------|
| 直链形式 | `https://r.jina.ai/<URL>` 一行链接返回 Markdown |
| API 调用 | 支持自定义请求头、批量抓取 |
| 干净输出 | 剥离广告 / 导航 / cookie 弹窗 |
| 多格式 | Markdown / HTML / JSON / Text |
| 高级模式 | 读取模式、JSON 模式、对话模式 |

## 相关概念

- [Sparkfetch](./tool-sparkfetch.md) — 同为 URL → Markdown 工具，偏轻量离线
- [Firecrawl](./tool-firecrawl.md) — 同类网页清洗 + 抓取工具，支持按 schema 抽取