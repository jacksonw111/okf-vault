---
type: Tool
title: "DonSeTch (dondai44423/donsetch)"
description: "Rust 单二进制 Web 抓取 / 搜索 / 爬站工具，自带 HTTP/2、内容提取、PDF 解析、搜索聚合、爬虫；接 MCP 即可让 AI 代理获得 web_fetch / web_search / web_crawl 三件套，不依赖 API key"
resource: "https://github.com/dondai44423/donsetch"
tags: [rust, web-fetch, mcp, search, crawler, single-binary]
timestamp: 2026-08-20T02:23:00Z
---

# DonSeTch (dondai44423/donsetch)

## 它是什么
[`dondai44423/donsetch`](https://github.com/dondai44423/donsetch) 是一个 **Rust 单二进制**的本地 Web 工具集：把 HTTP/2 客户端、内容提取、PDF 解析、搜索聚合、爬虫这几层从零写一遍，**不依赖**任何现成开源网页工具链（不用 Playwright、不用 Selenium、不用 headless Chrome）。它对外暴露 **web_fetch / web_search / web_crawl** 三个工具，通过 **MCP** 即可让 Claude Code / Cursor / Pi 这些 AI 代理获得联网能力——**全程无需 API key 与账号**。

## 为什么用它 / 适合什么场景
- 给 AI 代理装联网工具，不想为每个 SaaS（Serper、Tavily、Firecrawl、Bing）单独配 key。
- 注重**长期稳定**：作者声称"三年不折腾 API key / 账号"的本地兜底。
- 想用一种统一的 MCP 协议，让 Claude Code / Cursor / Pi 共用同一套抓取 / 搜索能力。
- 不希望依赖浏览器内核——单二进制、无 GUI、跑在服务器也行。

## 关键能力
| 能力 | 说明 |
|------|------|
| 单二进制 | Rust 编译产物，一个文件就能跑 |
| 不依赖浏览器内核 | 不跑 Playwright / Selenium |
| 三个工具 | `web_fetch` / `web_search` / `web_crawl` |
| MCP 适配 | 直接喂给 Claude Code / Cursor / Pi |
| 也可当 CLI | 不接 MCP 时也能直接命令行敲 |
| PDF 解析 | 内容提取支持 PDF |
| 搜索聚合 | 聚合多家搜索结果 |
| 无需 API key | 全本地实现，三年不折腾 |

## 媒体
- ![DonSeTch 截图](https://pbs.twimg.com/media/HP-_GGibUAAH71f.jpg)

## 相关概念
- [项目仓库](https://github.com/dondai44423/donsetch) — 仓库主页
- [pi-web-agent](./tool-pi-web-agent.md) — Pi 编码代理的单 `web_explore` 工具；DonSeTch 是把"抓 / 搜 / 爬"更彻底拆开的实现
- [claude-api-skill (无需具体引用)]：MCP 的接入方式可参考 Claude Code / Cursor 文档
