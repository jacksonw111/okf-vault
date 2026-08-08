---
type: "Tool"
title: "Firecrawl"
description: "面向 AI 应用与 RAG 系统的网页抓取 / 清洗服务：把任意 URL 转为干净的 Markdown / 结构化数据，支持渲染 JavaScript、按 schema 抽取字段，并提供大规模抓取 API。"
resource: "https://firecrawl.dev/"
tags: [web-scraping, html-to-markdown, rag, ai-pipeline, saas]
timestamp: "2026-08-08T20:00:00Z"
---

# Firecrawl

## 它是什么

Firecrawl 是一款面向 AI 应用与 RAG 系统的网页抓取 / 清洗 SaaS。它把任意 URL 转为干净的 Markdown 或结构化 JSON，替下游 LLM 承担「网页净化」这一步，并支持 JS 渲染、按 schema 抽取字段、批量抓取与定时任务。

## 为什么用它 / 适合什么场景

- 给 RAG / LLM 应用准备网页语料，被 HTML 噪声反复坑。
- 想要按 JSON Schema 从网页中结构化抽取字段（如价格 / 标题 / 表格）。
- 需要批量抓取数千 URL，并希望托管抓取调度与反爬对抗。

## 关键能力

| 能力 | 说明 |
|------|------|
| URL → Markdown | 输出可读 Markdown，含标题 / 链接 / 图片 |
| JS 渲染 | 走 headless 浏览器处理 SPA 站点 |
| Schema 抽取 | 按 JSON Schema 直接抽取字段 |
| 批量抓取 | 异步批量 API，支持千级 URL |
| 反爬对抗 | 代理轮换、UA 伪装等托管 |
| 自托管选项 | 提供开源版可自行部署 |

## 相关概念

- [Sparkfetch](./tool-sparkfetch.md) — 类似定位的 URL → Markdown 工具，但偏轻量离线
- [Jina Reader](./tool-jina-reader.md) — 同为 URL → Markdown 服务，商业 / 在线路线代表
- [Deepclone Website](./tool-deepclonewebsite.md) — 离线整站克隆，处理登录态更强