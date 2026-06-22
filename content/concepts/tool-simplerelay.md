---
type: "Tool"
title: "SimpleRelay（自托管 SMTP 中继服务）"
description: "toinbox/simplerelay —— 自托管的多租户 SMTP 中继服务，家庭网络 / 小团队一台服务器搞定统一邮件发送网关，每用户挂自己的上游 SMTP，绑 IP 白名单 + SPF/DKIM/DMARC 校验。"
tags: "[smtp, relay, self-hosted, email, multi-tenant, postfix, fastapi]"
timestamp: "2026-06-22T16:02:00Z"
---

# SimpleRelay（自托管 SMTP 中继服务）

## 它是什么

[`toinbox/simplerelay`](https://github.com/toinbox/simplerelay) 是**自托管的多租户 SMTP 中继服务**。为家庭网络或小团队提供统一的邮件发送网关，避免每台设备（NAS / 智能家居 / 服务脚本）单独配邮箱账号。

技术栈：

- **FastAPI** —— Web UI 与 REST API
- **Postfix** —— 实际 SMTP 投递引擎
- **PostgreSQL** —— 多租户元数据存储
- **Docker** —— 一键部署

核心能力：

- **多租户**：每个用户能加自己的上游 SMTP 提供商（Gmail / Outlook / 自建）
- **自动检测设置**：自动探测 SMTP 端口 / TLS / 认证方式
- **SPF / DKIM / DMARC 校验**：发出的邮件附带正确的反伪造签名
- **IP 白名单**：每个发件人必须绑 IP 白名单才能用，否则拒绝连接
- **可选 SMTP AUTH 二次认证**：在白名单之上再加一层认证

> 截图：![](https://pbs.twimg.com/media/HLThg6CawAAXkeH.jpg)

## 为什么用它 / 适合什么场景

- **多设备邮件发送**：家里 NAS、监控、Home Assistant、自动化脚本全走这一个网关，避免每台机器都暴露一整套 SMTP 凭据。
- **多账号管理**：家庭成员 / 团队成员各自挂自己的 Gmail / Outlook 上游。
- **统一审计**：所有出站邮件都在 SimpleRelay 这一层留痕。
- **安全合规**：IP 白名单 + SPF/DKIM/DMARC 避免被上游当成 spam 源。

适合：

- 家庭网络（NAS / 智能家居监控 / Home Assistant）
- 小团队（不想让所有人都暴露公司主邮箱凭据）
- 重视**邮件外发可审计**的隐私用户

## 关键能力

| 能力 | 说明 |
|---|---|
| 多租户 | 每用户独立上游 SMTP 配置 |
| 自动检测 | 上游 SMTP 端口 / TLS / 认证方式自动探测 |
| 反伪造 | SPF / DKIM / DMARC 校验 |
| IP 白名单 | 未授权 IP 直接拒绝连接 |
| SMTP AUTH（可选） | 在白名单之上叠加认证 |
| 一键部署 | Docker Compose 编排全套 |

## 工作流

```
设备 A (NAS)   ─┐
设备 B (HA)     ─┤──→  SimpleRelay  ──→  用户上游 SMTP (Gmail/Outlook)
设备 C (脚本)   ─┘        │                       │
                        PostgreSQL               Internet
                        (多租户元数据)
```

## 参考链接

- [项目链接](https://github.com/toinbox/simplerelay)

## 相关概念

- [Cloud Mail](tool-cloud-mail.md) — 单域名无限收发的邮件服务
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Kamal 一键部署
- [Lucky](tool-lucky.md) — DDNS + ACME + 反代瑞士军刀（与邮件场景常配合做端口转发）