---
type: "Tool"
title: "SimpleLogin"
description: "开源的邮件别名服务：注册第三方服务时生成中转别名收信再转发，可随时关停单一别名，被 Proton 收购后继续开源。"
resource: "https://simplelogin.io/"
tags: [email-alias, privacy, open-source, self-hosted, saas]
timestamp: "2026-08-08T20:00:00Z"
---

# SimpleLogin

## 它是什么

SimpleLogin 是一款开源的邮件别名服务（email aliasing），让你在注册第三方服务时用临时别名收信再转发到真实邮箱。被 Proton 收购后继续保持开源 / 自托管可选，是「Hide My Email」类需求的事实标准开源替代品。

## 为什么用它 / 适合什么场景

- 想在多个服务间用不同别名，但又只暴露一个真实邮箱。
- 不希望被 Apple / 微软等平台锁定。
- 想要 SaaS + 自托管两种部署方式。
- 想用 API / CLI 批量管理别名。

## 关键能力

| 能力 | 说明 |
|------|------|
| 邮件别名 | 生成无限别名，统一转发到真实邮箱 |
| 域名别名 | 可绑定自有域名，作为域名邮箱别名 |
| 随时关停 | 单个别名一键停用，停服立即生效 |
| 自托管 | 社区版可自行部署 |
| 多平台客户端 | Web / iOS / Android / CLI / 浏览器扩展 |

## 相关概念

- [Apple Hide My Email](./term-apple-hide-my-email.md) — Apple iCloud+ 内置的同类服务
- [iCloud Create Workbench](./tool-icloud-create-workbench.md) — 围绕 Hide My Email 的批量管理控制台