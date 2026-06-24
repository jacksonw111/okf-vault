---
type: "Tool"
title: "pi-web-agent（demigodmode/pi-web-agent）"
description: "Pi 编码代理的网页工具包：只暴露单一 web_explore 工具，内部封装搜索、抓取、渲染、来源排序与质量检查，搜不到就如实说搜不到。"
resource: "https://github.com/demigodmode/pi-web-agent"
tags: [agent, pi, web, search, scraper]
timestamp: "2026-06-23T15:30:00Z"
---

# pi-web-agent（demigodmode/pi-web-agent）

## 它是什么

给 Pi 编码代理加的「老实上网」工具集。它只对外暴露一个 `web_explore` 工具，里面包了搜索、抓取、浏览器渲染、来源排序、质量检查一整条链路；遇到反爬页面就如实返回「读不了」，绝不假装读到了。

## 为什么用它 / 适合什么场景

- **降低幻觉**：编码代理需要「看一眼最新文档」时不必再手喂链接；
- **后端可控**：搜索后端可换 DuckDuckGo / Brave API / 自建 SearXNG / Firecrawl；
- **接口收敛**：代理只需学一个工具名，内部编排对模型透明。

## 关键能力

| 环节 | 职责 |
|------|------|
| Search | DuckDuckGo 默认，可换 Brave / SearXNG / Firecrawl |
| Fetch | 抓取原始 HTML |
| Render | 必要时跑无头浏览器渲染 |
| Rank | 来源排序 |
| QC | 质量检查，未达标的如实报错 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/demigodmode/pi-web-agent>

## 相关概念

- [Proxide](tool-proxide.md) — 同属「让 Pi / 任意 Agent 能正经上网」的桥接思路（Proxide 走的是 ChatGPT 网页）
- [browser-search](tool-browser-search-agent.md) — 同样提供 SearXNG + Camofox + CloakBrowser 自托管搜索栈
- [pi-task](tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展（前后台 + TUI 进度条）