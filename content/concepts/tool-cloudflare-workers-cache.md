---
type: Tool
title: "Cloudflare Workers Cache"
description: "Cloudflare 推出的可挂载在 Worker 入口前的区域分层缓存，用标准 HTTP 头配置且无限可组合。"
resource: "https://blog.cloudflare.com/workers-cache"
tags: [cloudflare, workers, cache, cdn]
timestamp: "2026-07-07T12:00:00Z"
---

# Cloudflare Workers Cache

## 它是什么
Cloudflare 为 Workers 推出的 **Workers Cache**：一层"无限可组合"、按 HTTP 头控制的区域（regional tiered）缓存，**直接坐在 Worker 入口前面**。既是 Cloudflare 全球边缘加速的自然延伸，也保留了普通 Cache API 的语义。

## 为什么用它 / 适合什么场景
- 想要 **Cloudflare Cache API 能力**（保活 / stale-while-revalidate / slice）又不想在代码里手动管理 cache key。
- 需要 **区域（regional）感知**：例如只想在欧盟区域、亚太区域共享同一缓存，而不是全球节点。
- 想用 **标准 HTTP header**（`Cache-Control`、`Vary`）控制缓存，**不用学新配置面**。
- 适合给 Cloudflare Workers 上跑的 React / Astro / Hono / SSR 应用前置一层"几乎不要钱的"缓存层。

## 关键能力
| 能力 | 说明 |
|------|------|
| 区域分层 | 缓存按区域（regional）粒度组织，避免全球节点互相同步 |
| 标准 HTTP 头控制 | 沿用 `Cache-Control` / `Vary` 等已有语义 |
| 可无限组合 | 多层缓存可叠加（边缘 / 区域 / 源） |
| Worker 入口前置 | 入口前自动拦截命中 / 未命中逻辑，**Worker 代码无感知** |
| 零代码改动 | 与已有 Worker 完全兼容，不用改业务代码 |

## 相关概念
- [Cloudflare Kumo](tool-kumo.md) — Cloudflare 官方开源的 UI 组件库与文档框架
- [Cloudflare Kumo](tool-kumo.md) — Cloudflare 官方开源的 UI 组件库与文档框架
- [Single Server](tool-single-server.md) — 一台 Linux 服务器串 Cloudflare + Tailscale + Docker 一键部署
- [FlareMo](tool-flaremo.md) — Cloudflare Workers + D1 + R2 上的 Flomo 风格时间线笔记
- [sub-store-cloudflare](tool-sub-store-cloudflare.md) — Cloudflare Workers 部署的订阅聚合与规则配置工具
