---
type: Tool
title: "mcp-gsc"
description: "面向 AI 助手的 Google Search Console MCP 工具集——不是 API 的 thin wrapper，而是真正覆盖 overview / 周期对比 / 单页 query 批量 inspect / indexing issues 等 SEO 场景的工具集。"
resource: "https://github.com/AminForou/mcp-gsc"
tags: "[mcp, seo, google-search-console, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# mcp-gsc

## 它是什么
一个**针对 Google Search Console（GSC）数据的 MCP 服务器**，让 Claude / Cursor / Codex 等 AI 助手能直接调用 GSC 工具获取 SEO 数据：

> 不仅仅是 API 的薄封装，而是把 SEO 真实场景做了进去：overview、周期对比、单页 query 批量 inspect、indexing issues 等。

## 为什么用它 / 适合什么场景
- 让 AI 助手直接帮你查 GSC：覆盖度、点击、印象、平均位、CTR、周期对比。
- 批量 inspect 一批页面的 query / 索引状态，而不是一页一页手工看。
- 比 Chrome CDP 抓 GSC 页面方便，避开登录态 / 反爬。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | MCP server |
| 范围 | Google Search Console |
| 工具数 | overview / 周期对比 / 单页 query / indexing issues / 批量 inspect 等 |
| 授权 | OAuth / 服务账号（按 GSC 常规配置） |
| 优势 | 比 Chrome CDP 抓页面更稳 |

## 相关概念
- [MCP（Model Context Protocol）](term-mcp.md) — 该工具遵循的协议
- [seo-monster](tool-seo-monster.md) — 把 GSC / GA4 / PageSpeed / Cloudflare 全部塞进 AI 助手的更大封装

## 项目链接
- 项目主页：<https://github.com/AminForou/mcp-gsc>
