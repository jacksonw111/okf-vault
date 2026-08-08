---
type: "Tool"
title: "Cloudflare Workers"
description: "Cloudflare 推出的边缘无服务器计算平台：在全球 300+ 边缘节点运行 JavaScript / Rust / WASM 代码，按请求计费，免运维。"
resource: "https://workers.cloudflare.com/"
tags: [serverless, edge, cloudflare, javascript, wasm]
timestamp: "2026-08-08T20:00:00Z"
---

# Cloudflare Workers

## 它是什么

Cloudflare Workers 是 Cloudflare 推出的边缘无服务器计算平台。它让用户把 JavaScript / TypeScript / Rust / WASM 代码部署到全球 300+ 边缘节点，按请求与 CPU 时间计费，几乎免运维。

## 为什么用它 / 适合什么场景

- 想要「上传即上线」的边缘 API，无需管服务器。
- 部署面向全球用户的低延迟服务（API、CDN 边缘逻辑、SSR）。
- 想用 Workers AI / D1 / R2 / KV / Durable Objects 拼一套完整边缘栈。
- 跑小型脚本 / 定时任务 / Webhook 接收端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 边缘部署 | 全球 300+ 边缘节点自动分发 |
| 多语言 | JavaScript / TypeScript / Rust / WASM |
| Workers AI | 边缘节点上跑 LLM 推理 |
| 配套生态 | KV / D1 / R2 / Durable Objects / Queues |
| 按请求计费 | 免费额度大，个人项目几乎免费 |
| Cron Triggers | 定时任务触发器 |

## 相关概念

- [Mailworker](./tool-mailworker.md) — 跑在 Cloudflare Workers 上的自托管邮件运行时
- [cfnew-deployer](./tool-cfnew-deployer.md) — Cloudflare Pages 部署器面板