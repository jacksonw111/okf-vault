---
type: "Tool"
title: "buzzkit（应用通知编排层）"
description: "为应用开发者提供统一的通知编排层：一次接入后通过事件驱动多渠道消息发送，覆盖订阅者管理、偏好、定时、工作流与送达回执。"
resource: "https://github.com/buzzkit-dev/buzzkit"
tags: "[notification, event-driven, sdk, api, orchestration]"
timestamp: "2026-09-11T22:05:00Z"
---

# buzzkit

## 它是什么

[buzzkit-dev/buzzkit](https://github.com/buzzkit-dev/buzzkit) 是面向**应用开发者**的**统一通知编排层**：一次接入后，开发者用**事件驱动**方式触发多渠道消息发送，无需自己拼邮件 / 短信 / 推送 / Webhook。

## 覆盖能力

| 维度 | 说明 |
|------|------|
| 订阅者管理 | 用户订阅 / 退订 / 分组 |
| 偏好 | 频道 / 时段 / 频率 |
| 定时 | cron / delay / send_at |
| 工作流 | 触发链 + 模板 + 条件分支 |
| 送达回执 | 投递 / 打开 / 点击 全链路追踪 |

## 为什么用它 / 适合什么场景

- 做 SaaS / App 时通知逻辑散落在邮件、推送、短信、Webhook 各处。
- 想给团队一个统一通知 API，业务只关心「发什么」，不管「走哪个渠道」。
- 想沉淀送达数据做后续运营优化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多渠道统一 | 邮件 / 推送 / 短信 / Webhook 一套 API |
| 事件驱动 | 业务事件触发，无需手动调度 |
| 订阅管理 | 用户级偏好与组 |
| 模板系统 | 跨渠道模板复用 |
| 送达回执 | 全链路追踪投递 / 打开 / 点击 |

## 参考链接

- 项目仓库：<https://github.com/buzzkit-dev/buzzkit>

## 媒体

- ![](https://pbs.twimg.com/media/HR0fNcUb0AAVdQ7.jpg)

## 相关概念

- [OpenSend](./tool-opensend.md) — 同样做邮件编排，自托管在 SES 上
- [HttpSMS](./tool-httpsms.md) — 自托管短信网关
- [OpenSend MCP 集成](./tool-opensend.md) — 自托管邮件 + MCP
</content>
</invoke>