---
type: "Tool"
title: "AutoJev（thinkany-ai/autojev，本地 AI 网关）"
description: "Tauri + React + Rust 写的桌面应用：本地 AI 网关统一收请求，按规则路由到不同 provider / 模型；兼容 OpenAI Responses / Chat Completions / Anthropic Messages 三种协议，流式和 function tool call 都能过。"
resource: "https://github.com/thinkany-ai/autojev"
tags: "[ai-gateway, model-router, tauri, openai, anthropic, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# AutoJev（thinkany-ai/autojev，本地 AI 网关）

## 它是什么

[AutoJev](https://github.com/thinkany-ai/autojev) 是 thinkany-ai 开源的桌面应用：Tauri + React + Rust 写的本地 AI 网关。本机装了多个 AI agent 时，用一个本地网关统一收请求，按规则把它们路由到合适的模型 / provider。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 provider 配置 | 在一个界面里配 provider / 模型 / 路由规则 |
| 本地网关 | 统一收请求，按规则路由到合适的模型 |
| 多协议兼容 | OpenAI Responses / Chat Completions / Anthropic Messages |
| 流式响应 | 支持 SSE 流式 |
| function tool call | 三种协议下都支持 |
| 桌面形态 | Tauri + React + Rust 跨平台桌面应用 |

## 它解决的问题

本机跑了多个 AI agent，每个 agent 接不同的模型 provider？管理起来：
- 配置散落各处
- 路由规则没有统一管理
- 协议切换麻烦

AutoJev 给一个本地网关界面统一管理。

## 媒体预览

![](https://pbs.twimg.com/media/HTWsmFebQAAsdf5.jpg)

## 原始链接

- 项目主页：<https://github.com/thinkany-ai/autojev>

## 相关概念

- [Ai Gateway Tdn](./tool-ai-gateway-tdn.md) — 类似的 AI 网关
- [Monid](./tool-monid.md) — 统一 base URL + key 接入 2000+ 工具 / 72+ provider
- [Obot](./tool-obot.md) — 企业 AI 治理平台（与 AutoJev 同属 AI 网关 / 治理领域）