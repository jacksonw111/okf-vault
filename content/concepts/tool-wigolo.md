---
type: "Tool"
title: "wigolo（KnockOutEZ/wigolo）"
description: "免费、本地、私有的 MCP 服务,让 AI Agent 能搜索、抓取、研究网页——效果对标付费服务,但永远不花钱,且数据完全在本地。"
resource: "https://github.com/KnockOutEZ/wigolo"
tags: "[mcp, web-search, web-scraper, agent-toll, local-first, free]"
timestamp: "2026-07-16T15:19:00Z"
---

# wigolo

[wigolo](https://github.com/KnockOutEZ/wigolo) 是一个**免费、本地、私有的 MCP 服务**,目标是为 AI Agent 提供「网页搜索 + 抓取 + 研究」能力——不依赖任何商业搜索 API,完全跑在用户自己机器上,效果对标付费服务,但不花钱。

## 它解决了问题

让 AI Agent 能联网时,通常要接 Tavily / SerpAPI / Exa 之类付费搜索服务——免费 tier 配额抠门,大项目里直接烧钱。wigolo 反其道:全本地实现网页搜索/抓取/总结,在 MCP 标准下把同样的能力暴露给 Agent。

## 关键能力

| 能力 | 说明 |
|------|------|
| 搜索/抓取/研究三合一 | 一次 MCP 调用覆盖检索 → 抓内容 → 总结研究 |
| 免费 | 完全开源,无任何 API 配额/订阅费 |
| 本地 | 跑在用户自己机器,数据不出本机 |
| MCP 协议 | 任何兼容 MCP 的 Client(Claude Desktop / Codex / Cline)直接连 |
| 隐私优先 | 不向任何第三方上传查询/抓取内容 |

## 媒体

![](https://pbs.twimg.com/media/HNWOfz6aEAAbn_a.jpg)

## 参考链接

- [项目仓库](https://github.com/KnockOutEZ/wigolo)

## 相关概念

- [agent-reach](./tool-agent-reach.md) — 同样给编码 Agent 提供联网能力的多协议工具集,与本工具并列参考
- [ax CLI Scraper](./tool-ax-cli-scraper.md) — 同样是面向 Agent 的命令行抓取工具,与本工具并列参考
- [Bot Signal](./tool-bot-signal.md) — 同作者 KnockOutEZ 风格社区的另一类 MCP 服务(机器人检测),与本工具并列参考
