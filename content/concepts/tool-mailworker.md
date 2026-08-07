---
type: "Tool"
title: "Mailworker"
description: "跑在 Cloudflare Workers 上的自托管邮件运行时：产品侧用类 Resend 的 REST API 发事务邮件（含附件 / 批量 / webhook），Agent 侧用 CLI 收件、等邮件、提取 OTP、起草回复，关键发送由人在 dashboard 批准，一次部署服务多个产品和域名。"
resource: "https://github.com/guangzhengli/mailworker"
tags: [email, self-hosted, cloudflare-workers, rest-api, agent-tooling, transactional-email]
timestamp: "2026-08-07T04:14:00Z"
---

# Mailworker

## 它是什么

Mailworker 是一个开源、跑在 Cloudflare Workers 上的自托管邮件运行时，目标让「产品」和「AI Agent」共用同一份邮件基础设施。它把发件、收件、OTP 提取、回复起草都收敛到一套系统里，关键的发送动作由人在 dashboard 上批准，避免 AI Agent 失控发邮件。

## 为什么用它 / 适合什么场景

- 自托管一套事务邮件后端，不想把交付流量交给第三方 ESP（如 Resend、SendGrid）。
- 同时有多个域名 / 多个产品都依赖邮件能力，希望一份部署服务所有。
- AI Agent 需要邮箱做交互（注册、等验证码、回信），但希望「发件」被人把关。
- 想用 Cloudflare Workers 的边缘部署降低运维负担。

## 关键能力

| 能力 | 说明 |
|------|------|
| 类 Resend 的 REST API | 产品侧以 HTTP 接口发送事务邮件，含附件、批量发送、webhook 回调 |
| Agent 侧 CLI | 提供建收件箱、等邮件、提取 OTP、起草回复的命令行工具 |
| OTP 自动提取 | 自动从收到的邮件里解析一次性验证码，省去人工读邮件 |
| 人工批准 dashboard | 关键发送动作必须在 dashboard 审批才真发出，防止 Agent 失控 |
| 一次部署多产品 / 多域名 | 单实例同时服务多个业务和邮箱后缀 |
| Cloudflare Workers 部署 | 部署到自己账户，免运维、边缘加速、按请求计费 |
| 完全自托管 | 代码开源，数据、凭据、流量都留在自己的 Cloudflare 账户内 |

## 媒体

- ![Mailworker 架构示意](https://pbs.twimg.com/media/HPAFXwGbcAEtTC4.jpg)

## 相关概念

- [Resend](./tool-resend.md) — 商业事务邮件服务，本工具模仿其 REST API 形态
- [gmail-mcp](./tool-gmail-mcp.md) — 把 Gmail 接到 MCP 客户端，与本工具同样把邮件能力暴露给 Agent，定位互为替代
- [Cloudflare Workers](./tool-cloudflare-workers.md) — 本工具的部署载体