---
type: "Tool"
title: "mailez（一条命令的自托管域名邮箱）"
description: "自己搭一套域名邮箱，一条命令把收发件、日历、联系人、网盘、Webmail 和管理后台全拉起来，不租外部邮箱服务，邮件数据放自己机子上。"
resource: "https://github.com/mailez-hq/mailez"
tags: "[self-hosted, email, mail-server, domain-email, webmail, calendar, contacts, drive]"
timestamp: "2026-09-19T16:00:00Z"
---

# mailez（一条命令的自托管域名邮箱）

## 它是什么

[mailez-hq/mailez](https://github.com/mailez-hq/mailez) 是一个**一条命令把整套域名邮箱拉起来**的自托管工具——涵盖：

- **收发件**（邮件服务）
- **日历**
- **联系人**
- **网盘**
- **Webmail**
- **管理后台**

整套跑在**自己机子上**，不租外部邮箱服务（SaaS mail），邮件数据完全自主。

## 为什么用它 / 适合什么场景

- 想拥有**以自己域名为后缀的邮箱**（hello@yourdomain.com），又不想交年费给 Google Workspace / Microsoft 365。
- 关注**邮件数据自主**（合规 / 隐私 / 长期成本）。
- 想**一套命令**搞定邮箱 + 日历 + 联系人 + 网盘 + Webmail，而不是分别装 5 个组件。
- 个人开发者 / 小团队「想有自己的邮箱、懒得运维」的折衷方案。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一条命令拉起 | 减少自托管邮件服务的部署门槛 |
| 邮件收发 | SMTP / IMAP 完整链路 |
| 日历 | 不只是邮件，顺手把日历也带上 |
| 联系人 | 地址簿同步 |
| 网盘 | 配套的文件存储 |
| Webmail | 浏览器里直接读邮件 |
| 管理后台 | 域名 / 用户 / 配额统一管理 |
| 完全自托管 | 数据不外流给第三方邮件服务商 |

## 与相关概念的关系

- [Self-Hosted（自托管）](./term-self-hosted.md) — mailez 是「把整套办公套件自托管」的典型实现
- [Millionsend Self-Hosted Email](./tool-millionsend-self-hosted-email.md) — 同为自托管邮件方向，millionsend 偏邮件本身 / 投递链路，mailez 偏「办公套件一体化」
- [Apple Hide My Email](./term-apple-hide-my-email.md) — 隐私邮件方向互补：mailez 是「自建」、Hide My Email 是「云端别名」

## 参考

- 项目链接：<https://github.com/mailez-hq/mailez>
- 原始推文：<https://x.com/QingQ77/status/2101335003221164428>