---
type: Tool
title: "Vercel Portless"
description: "Vercel Labs 出的本地开发代理：把本地开发端口藏到子域名后，本地多服务可同时占用 80 / 443 端口、避免端口冲突与 hosts 文件污染。"
resource: "https://github.com/vercel-labs/portless"
tags: [vercel, local-dev, reverse-proxy, developer-tools]
timestamp: 2026-09-02T12:00:00Z
---

# Vercel Portless

## 它是什么

本地开发多个微服务时，每个服务都要占一个独立端口（3000 / 4000 / 5000...），端口冲突、跨服务 cookie 共享、hosts 文件污染等问题随之而来。`portless` 由 Vercel Labs 开源：把本地服务藏到 `*.localhost` 子域名后，统一走 80 / 443，端口冲突消失、cookie scope 也更接近生产环境。同类工具被作者称为"被严重低估的 Vercel 项目"。

## 关键能力

| 能力 | 说明 |
|------|------|
| 子域名路由 | 本地服务挂到 `*.localhost` 子域名 |
| 端口冲突消失 | 全部走 80 / 443 |
| 接近生产环境 | cookie / 协议 / 子域名行为都更接近线上 |
| 适配本地多服务开发 | 微服务 / monorepo 场景特别受益 |

## 项目链接

- [项目主页](https://github.com/vercel-labs/portless)

## 相关概念

- [Vercel Design System](./tool-vercel-design-system.md) — 同一生态的 UI 资源
