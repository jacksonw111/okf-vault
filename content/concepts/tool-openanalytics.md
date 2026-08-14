---
type: "Tool"
title: "openanalytics"
description: "OpenLabs-so 开源的隐私优先 Web 分析工具：用无 Cookie、无跨站画像的统计替代传统追踪，支持自托管、收入归因和 MCP 服务。"
resource: "https://github.com/OpenLabs-so/openanalytics"
tags: ["analytics", "privacy", "self-hosted", "mcp", "open-source", "cookie-free"]
timestamp: "2026-08-14T19:50:00Z"
---

# openanalytics

## 它是什么
openanalytics 是一套开源的隐私优先 Web 分析工具，定位是 Google Analytics 的自托管替代。它不做 Cookie 追踪、不做跨站画像，而是用「无 Cookie 的聚合统计」拿到基本的访问 / 来源 / 转化数据；额外支持收入归因和 MCP 服务，让 AI 助手能查询分析数据。

## 为什么用它 / 适合什么场景
- 受 GDPR / CCPA 约束，不想再上 Cookie banner 但仍想看基础访问数据。
- 独立站 / SaaS 想避免把用户行为传给 Google / Adobe。
- 想让 AI Agent 能直接查「昨日注册量 / 转化率」等指标（通过 MCP）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 隐私模型 | 无 Cookie / 无跨站画像 |
| 部署 | 自托管 |
| 数据 | 基础访问统计 |
| 商业能力 | 收入归因 |
| AI 接入 | MCP 服务 |

## 媒体

仪表盘 1：![仪表盘 1](https://pbs.twimg.com/media/HPpeXEDaQAA3eIE.jpg)
仪表盘 2：![仪表盘 2](https://pbs.twimg.com/media/HPpeYl0bgAAwp--.jpg)

## 相关概念
- [Talivia](./tool-talivia.md) — 网站分析 + 支付数据并到一图，与 openanalytics 同样面向「网站行为 / 转化」，但侧重商业转化
- [Akari Agent Skills](./tool-ai-user-roadmap.md) — 不同方向，但同样提供 AI 友好的指标接口（MCP）
