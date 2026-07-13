---
type: "Term"
title: "x402"
description: "基于 HTTP 402 状态码的小额付费协议，让 API/内容按请求原生计费。"
tags: ["protocol", "payment", "web"]
timestamp: "2026-07-13T00:00:00Z"
---

# x402

**x402** 是围绕 HTTP `402 Payment Required` 状态码构建的小额付费协议：客户端请求资源时，服务端返回 402 + 支付凭证，客户端完成微支付后获取内容。常用于 AI API、内容按量计费等场景。

## 相关概念
- [auth-md](tool-auth-md.md) — 与 x402 搭配的鉴权 / 付费方案
