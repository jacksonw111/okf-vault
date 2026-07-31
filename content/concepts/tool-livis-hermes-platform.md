---
type: "Tool"
title: "livis-hermes-platform（Surfire/livis-hermes-platform）"
description: "社区维护的独立兼容适配器：在不动 Hermes Core 的前提下，让理想同学 App / Livis 眼镜把用户请求送进自己的 Hermes Agent 配置，结果再原路返回——面向国内用户。"
resource: "https://github.com/Surfire/livis-hermes-platform"
tags: "[livis, hermes, ideal-companion, compatibility, adapter, smart-glasses]"
timestamp: "2026-07-31T20:30:00Z"
---

# livis-hermes-platform（Surfire/livis-hermes-platform）

[livis-hermes-platform](https://github.com/Surfire/livis-hermes-platform) 是**社区维护的独立兼容适配器**，面向国内用户：在**不动 Hermes Core** 的前提下，让「理想同学 App」或「Livis 眼镜」把用户请求送进自家 Hermes Agent 配置，结果再原路返回。

## 它是什么

- 一个**中间适配层**：客户端（理想同学 / Livis 眼镜）与 Hermes Core 之间
- **不动核心**：保留官方 Hermes Core 的升级路径
- **国内可达**：避开官方主线路在国内可能的连通性问题
- **结果回传**：让自家 Hermes Agent 配置从用户端看到回复

## 为什么用它 / 适合什么场景

| 场景 | 价值 |
|------|------|
| 已有 Hermes Agent 配置，想接理想同学 / Livis | 直接对接不用重写 |
| 国内网络下用 Hermes 配置 | 适配层的可达性 |
| 想保留 Hermes Core 官方升级路径 | 不改核心，只换适配 |
| 多端（手机 + 眼镜）共用同一 Agent 配置 | 适配层做协议转换 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 不动 Hermes Core | 保留官方升级 |
| 双端兼容 | 理想同学 App / Livis 眼镜 |
| 自托管配置 | 路由到自家 Hermes Agent |
| 国内可达 | 适配连通性 |

## 相关概念

- [local-hermes-portable](./tool-local-hermes-portable.md) — 本地 LLM + Nous Hermes Agent 的跨平台便携包，与本条都是「Hermes Agent 配置落地」一族
- [nyx-local-ai](./tool-nyx-local-ai.md) — Hermes 同源生态内的本地 AI 工具
- [hermes-browser-extension](./tool-hermes-browser-extension.md) — Hermes 浏览器扩展，与 livis-hermes-platform 端到端呼应
