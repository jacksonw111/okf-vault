---
type: Tool
title: "opengrok（让 Grok Bot 内每个智能体都能换成任意 LLM 模型）"
description: "Grok Bot 内的 LLM 模型替换插件：让每个 agent 都能换上任意 LLM 模型，并按各家 API 的真实协议对接。"
resource: "https://github.com/OnlyTerp/opengrok"
tags: [grok, bot, llm, model-replacement, multi-provider, agent]
timestamp: "2026-08-29T21:30:00Z"
---

# opengrok（让 Grok Bot 内每个智能体都能换成任意 LLM 模型）

## 它是什么

[OnlyTerp/opengrok](https://github.com/OnlyTerp/opengrok) 是 Grok Bot 的插件层：**让 Bot 内每一个 agent 都能替换为任意 LLM 模型**（OpenAI / Anthropic / DeepSeek / 国产 / 本地 GGUF），并按各家 API 的**真实协议**对接（不只是把请求体拼好发出去，还要处理流式、工具调用、token 计数差异等）。

解决的问题：Grok Bot 默认绑 Grok 模型，用户想要按场景切换（写作用 Claude / 编程用 DeepSeek / 隐私场景用本地）时只能全局换，不能**每个 agent 单独配**。

## 为什么用它 / 适合什么场景

- 想给一个 Grok Bot 里不同 agent 配不同模型，而不是所有人共用一个；
- 需要把 Grok Bot 接到**国产 / 本地**模型，按真实协议（不只是 OpenAI 兼容接口）打通；
- 想做模型 A/B：用同一个 Bot 同样的 prompt 对比不同模型效果；
- 想给隐私 / 离线场景把某些 agent 切到本地 GGUF。

## 关键能力

| 能力 | 说明 |
|------|------|
| 每 agent 换模型 | 不再是「整 Bot 一个模型」，是「每个智能体独立配」 |
| 多协议对接 | 各家 API 真实协议（流式 / tool use / 计数差异）都覆盖 |
| OpenAI 兼容层 | 走 OpenAI 协议的模型可一键接入 |
| 国产 / 本地支持 | DeepSeek / 智谱 / Ollama / LM Studio 都可挂载 |
| 同一 Bot 多模型 | 不同 agent 不同模型协同工作 |

## 相关概念

- [Protocol Model](./tool-protocol-model.md) — 多协议 LLM 适配层，opengrok 是它在 Grok Bot 上的应用
- [Qwen Audio Agent](./tool-qwen-audio-agent.md) — 同为多模型代理生态的具体项目

## 参考链接

- 项目链接：<https://github.com/OnlyTerp/opengrok>
- 原始推文：<https://x.com/QingQ77/status/2093698433882227178>
- 媒体：<https://pbs.twimg.com/media/HQ4YuU3bIAElE-v.jpg>