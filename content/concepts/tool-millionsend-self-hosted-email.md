---
type: "Tool"
title: "MillionSend（自托管邮件发送平台）"
description: "可自托管的开源邮件发送平台：用自己的 AWS SES 发信，API 兼容 Resend，迁移只需改两个环境变量。"
resource: "https://github.com/MillionSend/millionsend"
tags: "[email, ses, resend, self-hosted, transactional, deliverability]"
timestamp: "2026-09-13T03:04:00Z"
---

# MillionSend（自托管邮件发送平台）

## 它是什么

[MillionSend/millionsend](https://github.com/MillionSend/millionsend) 是一个**可自托管的事务邮件发送平台**：底层走你自己的 AWS SES 发信（也可以走他们家云），**API 兼容 Resend**，迁移只需要改两个环境变量。

## 为什么用它 / 适合什么场景

- 用 Resend 想换自托管 / 想控成本 / 想换 SES。
- 团队需要统一管理退信、投诉、发信量上限、SES 配额红线。
- 要 DKIM、Webhook 签名、联系人分组、定时群发、模板变量等企业功能，又不想付 SaaS 高价。
- 后台需要多语言（中/英/葡）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自托管 + 走自有 SES | 数据、凭据全在自己手里 |
| Resend 兼容 API | 老代码改 env 即迁移 |
| 退信 / 投诉自动拉黑 | 维护发信声誉 |
| 配额监控 | 盯着 SES 投诉率 / 发信量红线 |
| Webhook 签名 | 防伪回调 |
| DKIM / 联系人分组 / 定时群发 / 模板变量 | 邮件运营全流程 |
| SMTP 中继 | 给老系统当 relay 用 |

## 媒体

- ![](https://pbs.twimg.com/media/HR_BcoLbcAEDRWN.jpg)

## 项目链接

- 仓库：<https://github.com/MillionSend/millionsend>