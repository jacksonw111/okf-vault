---
type: "Tool"
title: "Aimux（arcships/aimux）"
description: "把上百家 AI 服务商的 HTTP 接口收敛成一个 Rust crate 的统一接口：模型调用方写一套代码就能换任意一家服务商。"
resource: "https://github.com/arcships/aimux"
tags: [rust, llm-sdk, ai-providers, abstraction, multi-provider, crate]
timestamp: "2026-08-05T09:20:00Z"
---

# Aimux（arcships/aimux）

## 它是什么

**Aimux** 把**上百家 AI 服务商**的 HTTP 接口**收敛成一个 Rust crate 的统一接口**——模型调用方写一套代码就能换任意一家服务商。

## 为什么用它 / 适合什么场景

- 想做**模型无关**的应用，今天用 OpenAI、明天想换 Ollama / DeepSeek / Anthropic。
- 不想为每家服务商写一遍客户端（鉴权、流式、错误处理各异）。
- Rust 项目：想要**类型安全 + 编译期校验**的 LLM 调用层。

## 关键能力

| 能力 | 说明 |
|------|------|
| 统一接口 | 一套 API 覆盖上百家 AI 服务商 |
| Rust crate | 类型安全 + 编译期校验 |
| 多 Provider | 任意切换上游 |
| 模型无关 | 调用方不绑死具体服务商 |

## 参考链接

- [GitHub 仓库](https://github.com/arcships/aimux)

## 相关概念

- [Grafana AI SDK](./tool-grafana-ai-sdk.md) — 另一款 Go 后端多 provider LLM SDK，可与 Aimux 对照「Go vs Rust」
- [Animarouter](./tool-animarouter.md) — 聚合多家 LLM 提供商的统一 OpenAI 兼容接口 + 路由策略，对照「统一接口 vs 智能路由」