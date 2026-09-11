---
type: "Tool"
title: "OpenSend（SES 之上的自托管邮件系统）"
description: "构建在 Amazon SES 之上的自托管邮件系统：覆盖事务邮件、newsletter、campaign 群发，后端 Hono/TypeScript API，对外提供 Web 面板、opensend-js SDK 与 MCP 服务器。"
resource: "https://github.com/R44VC0RP/opensend"
tags: "[email, ses, self-host, hono, typescript, mcp]"
timestamp: "2026-09-11T22:05:00Z"
---

# OpenSend

## 它是什么

[R44VC0RP/opensend](https://github.com/R44VC0RP/opensend) 是构建在 **Amazon SES** 之上的**自托管邮件系统**：

| 场景 | 说明 |
|------|------|
| 事务邮件 | 注册验证 / 密码重置 / 订单通知 |
| newsletter | 周期推送 |
| campaign 群发 | 营销活动 |
| API 调用 | 程序化发送 |

**SES 便宜但裸用太糙**，SaaS 又按封收钱，OpenSend 自己架一层：群发、事务信、调 API 全包，**面板和 SDK 调的是同一套接口**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 后端 | Hono / TypeScript API |
| Web 面板 | 完整 GUI 管理 |
| opensend-js SDK | JS / TS 客户端 |
| MCP 服务器 | 直接被 Claude Code / Cursor 调用 |
| 后端 SES | Amazon SES 出信 |
| 统一 API | 面板 / SDK / MCP 共用一套接口 |

## 为什么用它 / 适合什么场景

- 想用 SES 的低价但不愿裸调 AWS API。
- 想把邮件能力通过 MCP 暴露给 AI agent（让 agent 直接发邮件）。
- 想用 SaaS 的便利又不接受「按封收钱」。

## 参考链接

- 项目仓库：<https://github.com/R44VC0RP/opensend>

## 媒体

- ![](https://pbs.twimg.com/media/HR5ee6paEAAIY44.jpg)

## 相关概念

- [buzzkit](./tool-buzzkit.md) — 统一通知编排层（多渠道）
- [FlareMo](./tool-flaremo.md) — Cloudflare Workers + D1 + R2 上的 Flomo 风格时间线
- [Open GENAI](./tool-open-genai.md) — 日本数字厅 GENAI 本地化
</content>
</invoke>