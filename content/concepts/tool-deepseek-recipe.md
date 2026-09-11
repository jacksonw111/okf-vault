---
type: "Tool"
title: "deepseek-recipe（DeepSeek 官方 Rust + Python SDK）"
description: "DeepSeek 官方出的 Rust 轮子，另打包了一层 Python 绑定 deepseek_recipe：管请求转 Conversation、拼 prompt、解析模型输出三段；统一处理 Messages / Chat Completions / Responses 三种格式 API 请求到 DeepSeek V4 / V4.1 模型。"
resource: "https://github.com/deepseek-ai/deepseek-recipe"
tags: "[deepseek, rust, python, sdk, llm-api, prompt-engineering]"
timestamp: "2026-09-11T22:05:00Z"
---

# deepseek-recipe

## 它是什么

[deepseek-ai/deepseek-recipe](https://github.com/deepseek-ai/deepseek-recipe) 是 **DeepSeek 官方**出的 **Rust 核心 + Python 绑定**的 SDK，包名 `deepseek_recipe`，专门管三段工作流：

1. **请求转 Conversation**：把 Messages / Chat Completions / Responses 三种格式 API 请求统一转成 Conversation 中间表示
2. **拼 prompt**：编码为 DeepSeek V4 / V4.1 模型的 prompt
3. **解析输出**：把模型输出解析回对应格式的完整或流式响应

## 为什么用它 / 适合什么场景

- 用 DeepSeek V4 / V4.1 想用 OpenAI / Anthropic 风格的 API 协议。
- 想做 DeepSeek 模型的本地代理 / 网关。
- 想在 Rust 项目里直连 DeepSeek。

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust 核心 | 高性能、可嵌入 |
| Python 绑定 | `deepseek_recipe` |
| 协议统一 | Messages / Chat Completions / Responses 三合一 |
| Conversation IR | 中间表示统一 |
| 流式支持 | 完整 / 流式响应都解析 |
| DeepSeek V4 / V4.1 | 官方模型兼容 |

## 参考链接

- 项目仓库：<https://github.com/deepseek-ai/deepseek-recipe>

## 相关概念

- [DeepJIT](./tool-deepjit.md) — DeepSeek 开源的 C++20 JIT 运行时
- [dsh-trading](./tool-dsh-trading.md) — 基于 DeepSeek Harness 的 Agent 原生交易终端
- [fanzha-ai-proxy](./tool-fanzha-ai-proxy.md) — 同为 OpenAI 协议反向代理思路
</content>
</invoke>