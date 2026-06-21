---
type: "Tool"
title: "OPG（一人公司多 app 后端控制面）"
description: "OPG = One-Person-God-mode：TypeScript monorepo 形态的多 app 后端控制面，把账号权限、AI 网关、视频生成、支付、短信、邮件、文件存储、用量计费、审计日志收进同一套系统。接入方式灵活：CLI / SDK / MCP / OpenAPI 都行，Codex / Claude Code / Hermes 等 AI 工具可直接调用；Docker 一条命令拉起。"
resource: "https://t.co/jHXSX9cf9u"
tags: "[typescript, monorepo, baaS, ai-gateway, mcp, one-person-saas]"
timestamp: "2026-06-21T16:08:00Z"
---

# OPG（一人公司多 app 后端控制面）

## 它是什么

**One-Person-God-mode**：一个 TypeScript monorepo 形态的多 app 后端控制面，专为「一人公司 / 独立开发者同时维护多个 app」设计。把账号权限、AI 网关、视频生成、支付、短信 / 邮件、文件存储、用量计费、审计日志等「每个 app 都要重造一遍」的轮子收进同一套系统。

## 为什么用它 / 适合什么场景

- 独立开发者 / 一人公司在同时跑 2 个以上 SaaS / 工具型 app。
- 每个 app 都需要：账号系统、AI 调用网关、支付、文件存储、计费 —— 但又不想接 N 个 SaaS 拼起来。
- 希望 Claude Code / Codex / Hermes 这些 AI 工具能直接「读懂」你的后端能力并自动组合（OPG 提供 MCP / OpenAPI）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 账号权限 | 统一账户 + 角色 / 多租户 |
| AI 网关 | 集中转发大模型调用，便于限流 / 计费 / 路由 |
| 视频生成 | 内置视频生成 pipeline 接入 |
| 支付 | 内置支付集成 |
| 短信 / 邮件 | 通用触达通道 |
| 文件存储 | 通用对象存储抽象 |
| 用量计费 | 按调用 / 用量自动计量 |
| 审计日志 | 全链路调用记录 |
| 接入方式 | CLI / SDK / MCP / OpenAPI 多种 |
| AI 工具兼容 | Codex / Claude Code / Hermes 可直接调用 |
| 部署 | Docker 一条命令拉起 |

## 适用边界

- 不是「零代码 BaaS」—— 你仍要写自己的业务逻辑；OPG 提供的是「轮子层 + 控制面」，不是 SaaS 模板。
- 多租户 / 大流量场景需要二次工程化（OPG 定位在「一人公司」级别）。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLOuKAqa0AACrJO.png)

## 相关概念

- [CodexPro](tool-codexpro.md) — 同为「让本地 Agent 接上更强网页模型」的桥接器，但定位在 ChatGPT Web 桥
- [Repo→Agent](tool-repo-agent-generator.md) — 同为「把现有系统暴露给 AI Agent 消费」的思路
- [Single Server](tool-single-server.md) — 用 OPG 写好的 app 可以走 Single Server 一键部署