---
type: "Tool"
title: "hqbase"
description: "HQBase 开源的部署在 Cloudflare 账户里的共享邮箱工作台：共享收件箱、团队访问控制、多域名、草稿、审计历史，外加 OAuth 保护的远程 MCP 服务器。"
resource: "https://github.com/HQBase/hqbase"
tags: ["email", "shared-inbox", "cloudflare", "mcp", "open-source", "self-hosted"]
timestamp: "2026-08-14T19:50:00Z"
---

# hqbase

## 它是什么
hqbase 是一个跑在你 Cloudflare 账户里的共享邮箱工作台。它把邮箱变成「团队共享收件箱」：支持共享收件箱、团队访问控制、多域名配置、草稿、审计历史等运维能力；并额外附带一个由 OAuth 保护的远程 MCP 服务器，让 AI 助手能在合规前提下读写邮件。

## 为什么用它 / 适合什么场景
- 不想把团队邮件托管在第三方 SaaS（如 Front / Help Scout），但又想要共享收件箱体验。
- 用 Cloudflare 已经构建了 Workers / D1 等基础设施，hqbase 直接复用。
- 团队想让 AI 助手能代起草 / 回复邮件（通过 MCP），但希望有审计与权限边界。

## 关键能力
| 能力 | 说明 |
|------|------|
| 部署 | Cloudflare 账户内自托管 |
| 收件箱 | 共享收件箱 + 多域名 |
| 治理 | 团队访问控制、审计历史 |
| 工作流 | 草稿 |
| AI 接入 | OAuth 保护的远程 MCP 服务器 |

## 媒体

UI 示例：![UI 示例](https://pbs.twimg.com/media/HPlw0Fca0AA-89h.jpg)

## 相关概念
- [Cloud Mail](./tool-cloud-mail.md) — 类似「自托管邮件」思路，hqbase 在 Cloudflare 账户内的形态与 Cloud Mail 在自有服务器上的形态互补
- [MailWorker](./tool-mailworker.md) — 跑在 Cloudflare Workers 上的自托管邮件运行时，与 hqbase 同处 Cloudflare 邮件赛道
- [MailWorker MCP server 部分](./tool-mailworker.md) — MailWorker 也提供 MCP 接口，与 hqbase 的 MCP 服务器能力并列
