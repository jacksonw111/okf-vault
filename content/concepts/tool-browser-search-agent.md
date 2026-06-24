---
type: "Tool"
title: "browser-search（Johell1NS/browser-search）"
description: "面向 AI 代理的自托管搜索与浏览工具链，把 SearXNG、Camofox、CloakBrowser 串成全自动流水线，Docker + npm 一键启动。"
resource: "https://github.com/Johell1NS/browser-search"
tags: [agent, search, searxng, self-host, anti-bot, docker]
timestamp: "2026-06-23T15:30:00Z"
---

# browser-search（Johell1NS/browser-search）

## 它是什么

一个把三款开源工具粘合起来的「AI 代理搜索 + 浏览」端到端方案：先用 SearXNG 元搜索拉结果 → Camofox 浏览器打开落地页 → 遇到 Cloudflare 反爬自动切换到 CloakBrowser 隐身模式。整套链路用 Docker Compose 和 npm 就能跑，没有 API 配额，树莓派也能扛。

## 为什么用它 / 适合什么场景

- **自托管搜索栈**：不愿给 OpenAI / Anthropic 每月付搜索 API 账单的团队；
- **反爬场景**：常规 headless 浏览器被 CF 拦截时，无感切到隐身浏览器；
- **本地 AI 助理**：给本地大模型一个能「真上网」的子代理，避免它胡编 URL。

## 关键能力

| 阶段 | 工具 | 职责 |
|------|------|------|
| 搜索 | SearXNG | 聚合多搜索引擎元结果 |
| 浏览 | Camofox | 常规 headless 抓取 |
| 隐身 | CloakBrowser | Cloudflare / 反爬挑战绕过 |
| 部署 | Docker + npm | 一键起栈，可跑在树莓派 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/Johell1NS/browser-search>

## 相关概念

- [Obscura](tool-obscura-headless-browser.md) — 同属「自托管反检测浏览器」赛道（Rust / CDP 兼容）
- [DeepSeek MCP WebSearch](tool-deepseek-mcp-websearch.md) — 把联网搜索装进 MCP server 的另一条路径
- [pi-web-agent](tool-pi-web-agent.md) — 把同类能力封装为 Pi 代理可调用的单工具