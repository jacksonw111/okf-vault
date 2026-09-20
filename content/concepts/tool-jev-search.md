---
type: "Tool"
title: "Jev Search（前端纯网页搜索入口：Jev 解析 + Search1API 并发抓取）"
description: "superagents-lab/jev-search：纯前端网页搜索应用，把一句自然语言提问变成「带来源选择 / 时间范围 / 相关性排序」的网页搜索；TypeSafe Jev 模型先定查询词、来源、时间范围，Search1API 再并发去 Google / DuckDuckGo / Yandex / Hacker News / Reddit / GitHub / X / arXiv / YouTube / Wikipedia / IMDb / 微信等垂直引擎抓取。"
resource: "https://github.com/superagents-lab/jev-search"
tags: "[search, jev, search1api, cloudflare-workers, tanstack, react]"
timestamp: "2026-09-20T18:00:00Z"
---

# Jev Search

## 它是什么

[superagents-lab/jev-search](https://github.com/superagents-lab/jev-search) 把 **Jev Search** 做成了一个**纯前端的网页搜索入口**：

- **前端**：TanStack Start + React
- **部署**：Cloudflare Workers
- **许可**：MIT

## 工作流

1. **请求进来** → TypeSafe 的 **Jev 模型**先读懂问题，**定下查询词 / 来源 / 时间范围**。
2. 再把结构化决策交给 **Search1API**，**并发**去抓：
   - 通用：**Google / DuckDuckGo / Yandex**
   - 垂直：**Hacker News / Reddit / GitHub / X / arXiv / YouTube / Wikipedia / IMDb / 微信**
3. 返回**链接 + 摘要**，**不生成模型答案**。

## 为什么用它 / 适合什么场景

- 想要「**不带模型味儿**」的网页搜索结果——只要摘录 + 链接，不要总结稿。
- 想让搜索**从一开始就被结构化决策框定**（哪几个源 / 哪个时间窗），而不是返回一堆模型润色过的二手答案。
- 想在 **Cloudflare Workers** 上跑一个轻量搜索入口。

## 关键能力

| 能力 | 说明 |
|------|------|
| Jev 解析 | 先用结构化决策框定查询词 / 来源 / 时间范围 |
| 多源并发 | Search1API 并发拉通用 + 垂直搜索 |
| 不生成答案 | 只返回链接与摘要 |
| 纯前端 | TanStack Start + React |
| 部署 | Cloudflare Workers |
| 许可 | MIT |

## 项目链接

- 仓库：<https://github.com/superagents-lab/jev-search>

## 媒体

![](https://pbs.twimg.com/media/HSnzYDJbYAAYlBP.jpg)

## 相关概念

- [DeepSeek MCP WebSearch](./tool-deepseek-mcp-websearch.md) — 同为「给 Agent 联网搜索」的工具
- [browser-search](./tool-browser-search-agent.md) — 自托管搜索栈
