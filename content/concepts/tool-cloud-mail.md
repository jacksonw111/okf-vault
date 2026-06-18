---
type: "Tool"
title: "Cloud Mail（maillab/cloud-mail）"
description: "一个域名即可「无限收发」的轻量开源邮件服务：自带 Web 邮箱客户端、注册码 / 多账号、批量发件；定位是「自建邮局 / 隐私邮箱 / 教育邮箱后缀」快速落地。"
tags: "[email, self-host, open-source, mail-server]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/maillab/cloud-mail"
---

# Cloud Mail（maillab/cloud-mail）

> 来源：[@CxxVen on X 2026-05-31](https://x.com/CxxVen/status/2060857604385984948)

## 它是什么

[`maillab/cloud-mail`](https://github.com/maillab/cloud-mail) 是一个**轻量、自托管的「无限收发」邮件服务**——单个域名即可同时获得：

- 无限**接收**外部邮件（任意地址 → 你的域）；
- 无限**发送**邮件（批量 / 注册 / 通知）；
- 自带 Web 邮箱客户端，开箱即用；
- 「注册码」机制：分发 N 个可注册名额（如分享 200 个教育邮箱）。

## 为什么值得知道

- **域名即邮局**——传统自建 Postfix / Dovecot 流程重，Cloud Mail 把整条链路压成「部署 + 配 DNS」两步。
- **批量发件场景**——做产品内「验证码 / 通知 / 注册邮件」时不用挂接第三方 SMTP。
- **隐私 / 隔离邮箱**——做爬虫、薅羊毛、白嫖注册时，比起临时邮箱服务，自己掌控更稳。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单域名无限收件 | MX 指向实例即可 |
| 单域名无限发件 | 自带 SMTP，无需外挂 |
| Web 邮箱 UI | 不用另起客户端 |
| 注册码分发 | 内置邀请码系统（如 `aWA1EWWu` 200 用户名额） |
| 多账号隔离 | 每个用户独立收件箱 / 发件身份 |

## 典型用法

| 场景 | 收益 |
|------|------|
| 自建教育邮箱后缀 | 例如 `mail.yelo.edu.kg`（来源推文示例） |
| 团队通知系统 | 摆脱 Mailgun / SendGrid 配额与计费 |
| 隐私批量注册 | 自控发件源、可随时回收 |
| 临时邮箱服务 | 部署一份即可对外提供服务 |

## 注意事项

- 发件量大时**务必**配 SPF / DKIM / DMARC，否则进垃圾箱。
- 注册码 / 邀请制对开放注册有约束，记得先评估是否需要公网开放。
- 域名被墙 / SMTP 25 端口被运营商封是常见坑，挑 VPS 时留意。

## 相关概念

- [Lucky](tool-lucky.md) — DDNS + ACME + 反代瑞士军刀；常配合 Cloud Mail 一起搭自托管栈
