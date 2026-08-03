---
type: Tool
title: "CloudflareBase"
description: "在 Cloudflare 账户里跑一套开源的 Firebase 替代方案，认证、文档数据库和可视化控制台都能自己部署。"
resource: "https://github.com/cloudflarebase/cloudflarebase"
tags: [cloudflare, firebase-alternative, baas, workers, d1, auth]
timestamp: "2026-08-03T03:55:00Z"
---

# CloudflareBase

## 它是什么
CloudflareBase（`cloudflarebase/cloudflarebase`）是一套**跑在 Cloudflare 账户里的开源 Firebase 替代方案**。认证、文档数据库和可视化控制台都能自己部署，搭配 Workers / D1 / R2 / Durable Objects 一起使用。

## 为什么用它 / 适合什么场景
- **自有 Firebase 替代**：不想被 Firebase 锁仓、不想付 Firebase 定价。
- **Cloudflare 一体化**：与 Workers / D1 / R2 / Durable Objects 协同，部署 / 运维同栈。
- **可视化控制台**：内置 UI 仪表板，不用纯命令行管理数据。

## 关键能力

| 能力 | 说明 |
|------|------|
| 认证 | 自托管 Auth，替代 Firebase Auth |
| 文档数据库 | NoSQL 文档库，替代 Firestore |
| 可视化控制台 | 数据 / 用户 / 规则的可视化管理 |
| Cloudflare 全家桶 | 基于 Workers / D1 / R2 / Durable Objects |
| 可自部署 | 不绑定 Cloudflare 商业版，社区可自管 |

## 项目链接
- <https://github.com/cloudflarebase/cloudflarebase>

## 相关概念
- [Cloudflarebase] — 项目链接
- [Cloudflare Durable Objects Agent](./tool-cloudflare-durable-objects-agent.md) — Cloudflare 全家桶跑 agent runtime 的范式
- [Cloudflare Kumo](./tool-kumo.md) — Cloudflare 开源的 React 组件库
- [StorageUI](./tool-storageui.md) — 自托管 S3 / Cloudflare R2 文件浏览器
