---
type: Tool
title: "HttpSMS"
description: "自托管的短信网关：把闲置 Android 手机改造成 HTTP 短信发送/接收 API，云函数 / CI / AI agent 都能调用。"
resource: "https://github.com/NdoleStudio/httpsms"
tags: [httpsms, sms, android, self-hosted, api]
timestamp: "2026-07-04T15:00:00Z"
---

# HttpSMS

## 它是什么

HttpSMS 是由 NdoleStudio 开源的自托管短信网关。它让你把家里一台闲置的 Android 手机（Android 11+）变成一个可通过 HTTP API 调用的短信入口，绕开 Twilio 这类商用短信网关的月费与配额限制。

官网：<https://httpsms.com>
文档：<https://docs.httpsms.com>

## 为什么用它 / 适合什么场景

- **给云函数 / CI / AI agent 一个能发短信的接口**：自动化通知、双因素验证码、客服回复，全部走自己的手机号。
- **不想给 Twilio / Vonage 付费**：买一台便宜安卓机 + 一个 SIM，配 HttpSMS 就是你自己的「企业短信网关」。
- **数据归自己**：短信不流经第三方短信服务商；项目主打「coversations are between me and the receiver」。

## 关键能力

| 能力 | 说明 |
|------|------|
| Send SMS | HTTP POST 发送单条短信，支持从手机发或指定 SIM 槽 |
| Receive SMS | Webhook 实时回推收到的短信（按手机号 / 关键词过滤） |
| Scheduled SMS | 计划发送，未来某时刻自动触发 |
| Auto-reply | 收到匹配关键词的短信自动回模板 |
| Phone polling | 通过 FCM 唤醒 Android 端，避免长轮询 |
| Multi-user | 多用户登录，每用户绑定自己的 Android 客户端 |

## 工作原理简述

Android 客户端常驻后台监听 HttpSMS 服务的轮询 / FCM 推送请求 → 收到 API 调用后调系统短信 API 发送 / 接收 → 把状态回写到服务端 → 服务端通过 Webhook 异步通知上游。Android 端用 Kotlin 写，服端 .NET / C#（ASP.NET Core）。

## 相关概念

- [agent-sphere](tool-agent-sphere.md) — AI Agent 编排平台，可让 Agent 通过工具调 HttpSMS 这类自托管 API
- [HttpSMS 仓库](https://github.com/NdoleStudio/httpsms) — 项目链接
- [HttpSMS 官网](https://httpsms.com) — 原始链接
