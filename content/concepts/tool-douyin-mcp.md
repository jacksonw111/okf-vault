---
type: Tool
title: "douyin-mcp（抖音创作者中心 MCP 数据桥）"
description: "抖音创作者中心的数据靠 AI 自己读不到,douyin-mcp 把页面指标和视频文案转成 AI 能用的结构化数据,用来做内容复盘。"
resource: "https://github.com/Kuhakucai/douyin-mcp"
tags: [douyin, mcp, content-review, ai-agent, creator]
timestamp: "2026-07-24T00:00:00Z"
---

# douyin-mcp

[douyin-mcp](https://github.com/Kuhakucai/douyin-mcp) 是一个 **MCP 服务器**——把抖音创作者中心的页面指标与视频文案，转成 AI 可直接消费的结构化数据，方便做**内容复盘**。

## 它解决的问题

抖音创作者中心有大量数据（播放、点赞、完播、关注、文案），但：
- 这些数据都封在 Web 页面里，AI 代理没法直接读
- 手动截图 → 复制 → 整理 → 让 AI 总结，流程冗长
- 难以系统化地对比多期内容效果

douyin-mcp 通过 MCP 把创作者中心数据暴露成结构化端点，AI 代理可以直接：
- 拉某期视频的核心指标
- 拿到对应文案
- 跨期对比分析

## 关键能力

| 能力 | 说明 |
|------|------|
| MCP 协议 | 主流 AI 客户端可直接接入 |
| 页面指标结构化 | 把创作者中心 UI 数据转 JSON |
| 视频文案抓取 | 把每条视频文案也带上 |
| 内容复盘友好 | 数据形态便于做周期 / 选题对比 |

## 适用场景

- 抖音创作者 / MCN 内部做内容复盘
- AI Agent 给创作者提「下一条选题方向」建议
- 想把抖音数据接到 Notion / Obsidian 知识库

## 参考链接

- 项目仓库: <https://github.com/Kuhakucai/douyin-mcp>

## 媒体

![](https://pbs.twimg.com/media/HN9TF3kaEAAtHtD.jpg)

## 相关概念

- [MediaCrawler](tool-mediacrawler.md) — 七平台自媒体数据采集（小红书 / 抖音 / 快手 / B 站等），Playwright + JS 表达式签名
- [12306-mcp](tool-12306-mcp.md) — 12306 购票查询 MCP 服务器，同为「数据源 → MCP」结构化转换