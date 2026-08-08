---
type: "Tool"
title: "Resend"
description: "面向开发者的现代事务邮件 API：基于 React Email 模板语法，提供 REST API 发送事务邮件、Webhook、批量发送、附件与域名验证。"
resource: "https://resend.com/"
tags: [email, transactional-email, saas, api, developer-tools]
timestamp: "2026-08-08T20:00:00Z"
---

# Resend

## 它是什么

Resend 是一款面向开发者的现代事务邮件（transactional email）API，由 React Email 团队打造。它以干净的 REST API + React Email 模板语法为卖点，挑战 SendGrid / Postmark / Mailgun 等老牌 ESP 地位。

## 为什么用它 / 适合什么场景

- 想用现代 SDK / React Email 组件写邮件模板。
- 需要干净的 REST API、Webhook 回调、批量发送、附件支持。
- 对老牌 ESP 的开发体验不满（SDK 重、文档绕）。
- 自带域名验证、SPF/DKIM 配置工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| REST API | 简洁的发送接口 |
| React Email | 用 React 组件写邮件模板 |
| Webhook | 投递 / 退信 / 打开等事件 |
| 批量发送 | 单调用发送至多个收件人 |
| 域名验证 | 自动生成 SPF/DKIM |
| 多 SDK | Node / Python / Ruby / Go / PHP 等 |

## 相关概念

- [Mailworker](./tool-mailworker.md) — 自托管事务邮件运行时，模仿 Resend 的 REST API 形态
- [Cloudflare Workers](./tool-cloudflare-workers.md) — Mailworker 的部署载体