---
type: "Term"
title: "Cloudflare Workers"
description: "Cloudflare 边缘网络上的 V8 隔离 serverless 运行时——支持 JavaScript / TypeScript / Rust / WASM，全球 300+ 边缘节点毫秒级冷启动；Workers KV / D1 / R2 / Durable Objects / Workflows / AI / Agents SDK 组成完整的边缘开发生态。"
resource: "https://workers.cloudflare.com"
tags: "[cloudflare, workers, serverless, edge, wasm]"
timestamp: "2026-10-06T22:51:00Z"
---

# Cloudflare Workers

## 定义

**Cloudflare Workers** 是 Cloudflare 在全球 300+ 边缘节点上提供的**V8 isolate** serverless 运行时——支持 JavaScript / TypeScript / Python（Pyodide）/ Rust（wasm）/ WASM，**毫秒级冷启动**，无服务器运维负担；并以 Workers KV / D1（SQLite）/ R2（S3 兼容对象存储）/ Durable Objects（强一致 actor）/ Queues / Workflows / Vectorize / Workers AI / Agents SDK 等周边产品构成完整的边缘开发生态。

## 要点

- **官网**：[workers.cloudflare.com](https://workers.cloudflare.com)
- **运行时**：V8 isolates（不是 Node.js 完整运行时）；冷启动 ≈ 5 ms
- **配套生态**：
  - **KV**：全球低延迟 KV
  - **D1**：SQLite 接口的边缘数据库
  - **R2**：S3 兼容对象存储，零出口流量费
  - **Durable Objects**：单实例 actor，强一致状态
  - **Workflows / Queues**：长跑任务 / 异步消息
  - **Vectorize**：向量数据库
  - **Workers AI**：托管开源模型推理
  - **Agents SDK**：构建可持久化边缘 Agent
- **典型场景**：边缘 API / 反向代理 / 静态资源 / 边缘 AI 推理 / 边缘 Agent

## 相关概念

- [MapLibre GL](./term-maplibre-gl.md) — Workers 上跑地图服务的渲染引擎
- [Pi Durable on Cloudflare](./tool-pi-durable-cloudflare.md) — 边缘持久化 Agent
