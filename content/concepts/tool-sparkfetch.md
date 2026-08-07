---
type: "Tool"
title: "Sparkfetch"
description: "把任意 URL 的杂乱 HTML 转成干净、带元数据的 Markdown / JSON / 纯文本，省去 AI 应用与 RAG 管线自己清洗网页内容的步骤。"
resource: "https://github.com/Sparkfetch/sparkfetch"
tags: [web-scraping, html-to-markdown, rag, ai-pipeline, content-extraction]
timestamp: "2026-08-07T05:52:00Z"
---

# Sparkfetch

## 它是什么

Sparkfetch 是一个网页内容清洗工具，把任意 URL 的 HTML 转成干净、带元数据的 Markdown、JSON 或纯文本。它替 AI 应用和 RAG 管线承担「网页净化」这一步，让下游只需要面对结构化文本，不再被广告、导航栏、脚本注入等噪声污染。

## 为什么用它 / 适合什么场景

- 给 RAG / LLM 应用喂网页数据时，被 HTML 噪声（导航 / 广告 / cookie 弹窗 / 模板填充）反复坑。
- 需要把同一网页同时输出给「人看」（Markdown）与「机器读」（JSON）。
- 想拿一份带元数据（标题 / 作者 / 发布时间 / 站点来源）的结构化文本，而不是裸正文。
- 想省掉自己维护「哪个 extractor 对哪个站点更靠谱」的脏活。

## 关键能力

| 能力 | 说明 |
|------|------|
| URL → Markdown | 输出可读、可渲染的 Markdown，适合人审阅 |
| URL → JSON | 输出结构化 JSON，含元数据（title / author / published / source） |
| URL → Plain Text | 输出纯文本，最省 token |
| 元数据保留 | 抓取的同时把标题、作者、发布时间、来源站等一并带出 |
| 噪声清洗 | 自动剥离广告、导航、cookie 提示等模板噪声 |
| 适配 AI 管线 | 输出可直接喂给 LLM 上下文或作为 RAG 文档入库 |

## 媒体

- ![Sparkfetch 截图](https://pbs.twimg.com/media/HPAbxDkaIAALE9j.jpg)

## 相关概念

- [Jina Reader](./tool-jina-reader.md) — 同为 URL → Markdown 服务，是商业 / 在线版路线的代表
- [Firecrawl](./tool-firecrawl.md) — 同类网页清洗 + 抓取工具，与本工具可直接对比选型
- [Markdown 抓取协议](./note-markdown-fetch-protocol.md) — 把网页抽成 Markdown 当作 AI 友好的中间表示的思路