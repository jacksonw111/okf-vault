---
type: Tool
title: "grafana-ai-sdk"
description: "grafana/ai-sdk，在 Go 后端里用同一套 API 统一调用多家大语言模型，输出流式响应、工具调用与结构化结果，并与 Vercel AI SDK 的 React 前端协议兼容。"
resource: "https://github.com/grafana/ai-sdk"
tags: "[go, llm, ai-sdk, vercel, streaming, tool-use, structured-output]"
timestamp: "2026-08-01T20:30:00Z"
---

# grafana-ai-sdk

## 它是什么

[`grafana/ai-sdk`](https://github.com/grafana/ai-sdk) 是 Grafana 开源的 Go 后端 AI SDK，目标是在 Go 服务里**一套 API 调多个 LLM 提供商**——OpenAI / Anthropic / Gemini / 自托管 Ollama 等都能接入；输出侧同时支持**流式响应（streaming）**、**工具调用（tool use）** 与 **结构化输出（structured output / JSON Schema）**。

接口形态刻意对齐 Vercel AI SDK 的 React 前端协议，后端用同一份 schema 出流式 SSE，前端可以直接拿现成的 React hooks 消费，不用再改一遍协议。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 provider 统一调用 | 一套 Go 接口覆盖多家模型，无需为每个厂商写一遍适配 |
| 流式响应 | 原生 SSE，聊天场景首 token 延迟低 |
| 工具调用 | provider 差异被抽象掉，业务侧只描述 schema |
| 结构化输出 | 用 JSON Schema 约束模型返回类型，直接拿到强类型结果 |
| 协议对齐 | 与 Vercel AI SDK 的 React 前端协议同源，前后端可共用类型 |
| Go 原生 | 适合放 Go 后端 / 服务端 agent 链路里 |

## 适合什么场景

- 后端是 Go，前端用 Vercel AI SDK 的 React hook，需要跨语言协议对齐
- 想在 agent / RAG 服务里**一次接入多个模型**（主用 OpenAI、兜底 Anthropic、本地用 Ollama）
- 需要给模型返回强类型结构化结果（避免自己写 JSON 解析容错）

## 与同类工具的差异

| 工具 | 语言 | 特点 |
|------|------|------|
| [openclaude-improved](./tool-openclaude-improved.md) | TypeScript | CLI 编程代理，支持十几家 provider |
| [claude-code-router](./tool-claude-code-router.md) | Go | 本地网关，统一 Claude Code / Codex / Grok 的路由与故障切换 |
| grafana-ai-sdk | Go | 后端 SDK 层多 provider 抽象 + Vercel AI SDK 协议对齐 |

## 媒体

视频：

- <https://video.twimg.com/tweet_video/HOhVcOzasAAbEaV.mp4>

## 原始链接

- [项目仓库](https://github.com/grafana/ai-sdk)
- [原始推文](https://x.com/QingQ77/status/2083348484917518488)

## 相关概念

- [claude-code-router](./tool-claude-code-router.md) — 也是 Go 写的 AI 接入层，但偏「本地网关 / 故障切换」而非「后端 SDK」
- [openclaude-improved](./tool-openclaude-improved.md) — TypeScript 版的「一家 CLI 接多家模型」