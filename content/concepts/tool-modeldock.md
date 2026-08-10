---
type: "Tool"
title: "modeldock"
description: "architectds 开源的本地 Responses 协议桥接层：在 Codex CLI 里给 DeepSeek 补上看图 / 语音 / 联网搜索 / 跨会话记忆，同时把原生 GPT 模型透传，不修改客户端调用方式。"
resource: "https://github.com/architectds/modeldock"
tags: [codex, deepseek, responses-api, multimodal, bridge, mcp]
timestamp: "2026-08-10T02:43:00Z"
---

# modeldock

## 它是什么

[modeldock](https://github.com/architectds/modeldock) 是一层**本地跑的 Responses API 兼容桥**：前面对接 Codex CLI（继续按 OpenAI Responses 协议调用），后面同时接 OpenCode Go 的本地服务与 DeepSeek 官方 API。它的核心动机是——**给 DeepSeek 补齐 OpenAI 已具备但 DeepSeek 端缺位的能力**：识图、语音、联网搜索、跨会话记忆；同时把原生 GPT 模型直接透传，避免「在 Codex 里想用 GPT-5 又得换一套客户端」。

## 为什么用它 / 适合什么场景

- 想在 Codex CLI 里把主力模型切到 DeepSeek，又希望继续使用识图 / TTS / 联网 / 记忆这些 Responses 协议层的能力。
- 想用同一个 Codex 客户端同时跑 DeepSeek 与原生 GPT 模型，由 modeldock 负责协议路由。
- 想做「本地协议适配层」实验，modeldock 是少有的把 Responses 拆出去代理的实现范例。

## 关键能力

| 能力 | 说明 |
|------|------|
| Responses API 兼容 | 前端是 OpenAI Responses 调用，开发者无感 |
| DeepSeek 增强 | 给 DeepSeek 补识图 / 语音 / 联网搜索 / 跨会话记忆 |
| GPT 透传 | 把原生 GPT 模型直接转发，不需另开客户端 |
| 本地优先 | 桥接层跑在本地，不依赖外部托管服务 |
| OpenCode Go 后端 | 与本地 OpenCode 服务配套使用 |

## 媒体

![](https://pbs.twimg.com/media/HPPonOCbMAAg7dF.jpg)

## 参考链接

- [项目仓库](https://github.com/architectds/modeldock)
- [原始链接](https://x.com/QingQ77/status/2086644452915835012)

## 相关概念

- [opencode-cc](./tool-opencode-cc.md) — 把 OpenCode Zen 协议桥成 Anthropic / OpenAI 兼容，让 Claude Code / Codex CLI 透明调用国产模型，同属「代理层把模型接进来」一类
- [codex-bridge](./tool-codex-bridge.md) — 把 Codex CLI 里已有的 ChatGPT 登录借给 Claude，用 gpt-image-2 出图、子代理路由到 GPT-5
