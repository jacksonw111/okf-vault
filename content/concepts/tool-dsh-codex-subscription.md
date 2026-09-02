---
type: Tool
title: "dsh-codex-subscription"
description: "把 ChatGPT / Codex 订阅直接接入 DeepSeek Harness：用户已在 ChatGPT 账号里附带的 Codex 能力，DSH 拿来当模型用，不需要 OpenAI API Key，也不需要装 Codex CLI。"
resource: "https://github.com/WSL043/dsh-codex-subscription"
tags: [deepseek-harness, codex, chatgpt, subscription, dsh-plugin]
timestamp: 2026-09-02T12:00:00Z
---

# dsh-codex-subscription

## 它是什么

DeepSeek Harness（DSH）通常通过各家 LLM 的 API Key 来接入模型，但 OpenAI 的 Codex 模型被绑定在 ChatGPT 订阅里，订阅附带的 Codex 额度不走 API Key。`dsh-codex-subscription` 是一个 DSH 插件，把 ChatGPT / Codex 订阅作为模型来源接入 DSH：直接复用用户已经付费的 ChatGPT 账号凭证，DSH 调用 Codex 模型时自动消费订阅内额度，免去 OpenAI API Key、也免去装 Codex CLI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 订阅即模型来源 | 不需要 OpenAI API Key，复用 ChatGPT / Codex 订阅 |
| 免 Codex CLI | DSH 直接调用 Codex 模型，不依赖 Codex 命令行 |
| 沿用 DSH 生态 | 作为 DSH 插件存在，复用 DSH 的会话 / 工具 / 上下文管理 |

## 项目链接

- [项目主页](https://github.com/WSL043/dsh-codex-subscription)

## 相关概念

- [DeepSeek Harness 核心机制](./tool-deepseek-harness-core.md) — DSH 作为可插拔智能体框架的基座
