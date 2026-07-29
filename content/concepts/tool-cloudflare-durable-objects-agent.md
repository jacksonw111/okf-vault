---
type: Tool
title: "Cloudflare Durable Objects Agent 运行时（Code Mode 范式）"
description: "Cloudflare 上的 Agent 运行时范式：用 Durable Objects 承载 agent 与文件系统，R2 存大文件，Artifacts 管 git 历史，pi 做 harness，Code Mode + 动态 Workers 跑执行。Agent 不再写 bash，而是写 JavaScript。"
resource: "https://x.com/akazwz_/status/2082317377027653758"
tags: [cloudflare, agent, durable-objects, code-mode, runtime, serverless]
timestamp: "2026-07-29T14:56:39.000Z"
---

# Cloudflare Durable Objects Agent 运行时

## 它是什么

一种把 agent 跑在 **Cloudflare 全家桶**上的范式（原始推文描述）：用 Durable Objects 同时承载 agent 状态与文件系统，用 R2 存大文件，用 Artifacts 管 git 历史，用 pi 作为 harness，用 Code Mode + 动态生成的 Workers 做执行。Agent 不再写 bash，而是写 JavaScript，直接在 Cloudflare 边缘运行。

部署形态与任何 Cloudflare 应用一致（`wrangler deploy`），无需外部容器服务、无需运维 K8s。

## 关键组件

| 组件 | 角色 |
|------|------|
| Durable Objects | 跑 agent 实例 + 充当文件系统 |
| R2 | 存放大文件（数据集、产物） |
| Artifacts | 管理 git 历史（版本化、可追溯） |
| pi | agent harness（驱动循环、工具路由） |
| Code Mode + 动态 Workers | agent 写 JS，由平台生成 Worker 执行 |

## 为什么值得收藏

- **冷启动 vs 容器**：传统 agent sandbox 起 VM 起容器，秒级开销；Durable Objects 复用单例，几乎 0 冷启动
- **无服务器运维**：不需管 K8s、不需管容器服务，Cloudflare 全家桶自带全球分布
- **agent 写代码而非 bash**：Code Mode 范式让 agent 操作更像「写一个临时 Worker」，可控、可审计、可复现
- **git 化产物**：Artifacts 把每次 agent 执行落 git 历史，回放与对比天然支持

## 与「本地 agent runtime」的差异

本地 agent runtime（如 Pi Coding Agent）把 harness + 工具注册 + 沙箱都装在用户电脑上；这个范式把它们都搬到 Cloudflare 边缘。用户客户端只需发请求，结果回写 R2 / 落 git。

## 原始链接

- [项目原始推文](https://x.com/akazwz_/status/2082317377027653758)
- [推文剪藏](https://x.com/Wen_Zw/status/2082480427647078553)

## 相关概念

- [Forkd（microVM fork 化沙箱）](./tool-forkd.md) — 另一种"按需冷沙箱"思路，但跑在本地
- [Dormice（本地冷冻沙箱）](./tool-dormice.md) — 把沙箱跑在用户机器上，空闲冷冻
- [Pi Coding Agent 沙箱环境（pi-env）](./tool-pi-env.md) — 本地可复现隔离的沙箱运行时
- [Cloudflare Kumo](./tool-kumo.md) — Cloudflare 官方 UI 组件库与文档框架