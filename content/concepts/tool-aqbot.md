---
type: "Tool"
title: "AQBot（AI 对话 / Agent / 网关桌面客户端）"
description: "AQBot-Desktop/AQBot —— Tauri 2 打造的 AI 桌面工具，三件套：多服务商对话 + AI Agent + API 网关。OpenAI / Claude / Gemini / DeepSeek / 任何 OpenAI 兼容接口统一收口。"
tags: "[ai-client, desktop, tauri, multi-provider, agent, api-gateway]"
timestamp: "2026-06-22T16:08:00Z"
---

# AQBot（AI 对话 / Agent / 网关桌面客户端）

## 它是什么

[`AQBot-Desktop/AQBot`](https://github.com/AQBot-Desktop/AQBot) 是一套 **Tauri 2 打造的 AI 桌面工具**，主打三个核心功能：

1. **多服务商对话**：把 OpenAI、Claude、Gemini、DeepSeek 和任何兼容 OpenAI 的接口都收到一个窗口里聊
2. **AI Agent**：内置 Agent 能力
3. **API 网关**：作为本地 API 网关代理 / 转发 / 路由请求

> 截图：![](https://pbs.twimg.com/media/HLWQHlyaMAEE9OT.jpg)

## 为什么用它 / 适合什么场景

- **统一对话窗口**：不想再开 5 个不同 AI 的网页标签，AQBot 把它们都聚合到桌面客户端。
- **本地 API 网关**：可以当本地 LLM API 路由（按模型 / 成本 / 速度自动选上游）。
- **AI Agent + 知识库**：内置 Agent 与知识库能力，不开浏览器也能跑自动化任务。
- **Tauri 2**：资源占用低，跨平台。

适合：

- 同时订阅多个 AI 服务（OpenAI + Claude + Gemini + 自建 LLM）的**重度用户**
- 想把不同 AI 收口到桌面、**不开浏览器**的隐私 / 效率控
- 想用本地 API 网关按规则路由 LLM 请求的开发者

## 关键能力

| 能力 | 说明 |
|---|---|
| 多服务商 | OpenAI / Claude / Gemini / DeepSeek / OpenAI 兼容 |
| AI Agent | 内置 Agent 执行能力 |
| API 网关 | 本地路由 / 代理 / 转请求 |
| Tauri 2 | 跨平台、轻量 |
| 知识库 | 内置知识库能力 |
| 一窗多模型 | 不开浏览器就能切模型对比 |

## 与同类工具对比

| 维度 | ChatBox / Cherry Studio 等 | AQBot |
|---|---|---|
| 形态 | Electron / Web | **Tauri 2**（资源占用更低） |
| 对话 | 多服务商 | 多服务商 |
| Agent | 通常无 | 内置 AI Agent |
| API 网关 | 通常无 | 内置本地 API 网关 |

## 参考链接

- [项目链接](https://github.com/AQBot-Desktop/AQBot)

## 相关概念

- [本地 AI 桌面工作台](tool-local-ai-workbench.md) — Electron + 模型/Agent/路由三件套（同属「桌面 AI 客户端」方向）
- [Claude Code](tool-claude-code.md) — 终端 AI 编码 agent
- [Vaultty](tool-vaultty.md) — macOS 块式终端 + 钥匙串自动注入 .env