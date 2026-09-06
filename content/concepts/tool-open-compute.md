---
type: Tool
title: "open-compute（Cloudflare Workers 单二进制本地版）"
description: "把 Cloudflare Workers 整套平台能力装进单个二进制文件，让你在自己的机器上原样运行 Workers 应用，无需账号和云厂商。"
resource: "https://github.com/elliothux/open-compute"
tags: [cloudflare-workers, edge-runtime, local, portable, runtime]
timestamp: "2026-09-06T00:00:00Z"
---

# open-compute（Cloudflare Workers 单二进制本地版）

## 它是什么

[elliothux/open-compute](https://github.com/elliothux/open-compute) 把 **Cloudflare Workers 的整套平台能力**装进**单个二进制文件**，让用户在自己的机器上原样运行 Workers 应用——**无需 Cloudflare 账号、不连云厂商**。

定位：

- **本地化 Workers 运行时**：把边缘平台搬回本机，给开发 / 调试 / 离线场景用。
- **可移植**：单二进制分发，跨机器拷贝即可运行。

## 为什么用它 / 适合什么场景

- 开发或调试 Workers 应用时，不想反复 `wrangler dev` 或受限的本地模拟。
- 需要在离线 / 内网 / 边缘节点本地运行 Workers 兼容代码。
- 不想为开发体验给 Cloudflare 账号或受其 API 配额限制。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单二进制 | 不依赖 Node / 服务端运行时 |
| Workers 兼容 | 跑 Cloudflare Workers 兼容的应用 |
| 本地优先 | 无需账号、无云厂商依赖 |
| 可移植 | 二进制分发，跨机器拷贝即用 |
| 离线 / 内网 | 不需联网即可运行 |

## 相关概念

- [3X-UI](./tool-3x-ui.md) — 同样把云端复杂面板装进本地容器的思路（不过 3X-UI 走 Docker）
- [Lucky](./tool-lucky.md) — 同类「本地瑞士军刀」型网络工具

## 项目链接

- 项目主页：<https://github.com/elliothux/open-compute>
