---
type: "Tool"
title: "Ollama"
description: "本地大模型一键启动器：把 llama.cpp 推理引擎封装成简单 CLI，一条 `ollama run` 拉起 GGUF 模型，对外暴露 OpenAI 兼容 HTTP API，让「本机跑 LLM」无需编译环境。"
resource: "https://ollama.com/"
tags: [ollama, llama-cpp, local-llm, gguf, openai-compatible]
timestamp: "2026-08-09T19:30:00Z"
---

# Ollama

## 它是什么

Ollama 是「本地跑大模型」的事实标准之一：在 [llama.cpp](./tool-llama-cpp.md) 之上做了一层 Go 写的包装，自带模型仓库（Modelfile / 自定义 prompt / 参数模板），`ollama run llama3` / `ollama run qwen2.5-coder` 即可在 Mac / Linux / Windows 上拉起 GGUF 量化模型。同时内置 **OpenAI 兼容的 HTTP server**（默认 :11434），便于既有 OpenAI SDK 直接接入。

## 为什么用它 / 适合什么场景

- 想在自己的机器上跑 LLM，但不想碰 llama.cpp 的编译参数。
- 给 IDE 插件 / 桌面应用 / AI agent 提供本地 OpenAI 兼容 endpoint。
- 快速体验不同开源模型（Llama / Qwen / DeepSeek / Gemma / Mistral 等），模型市场一键拉取。
- 多模型并行：同时跑一个对话模型 + 一个 embedding 模型。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一键启动 | `ollama run <model>` 拉取并运行，无编译依赖 |
| 模型仓库 | Ollama Library 提供主流开源模型 + 社区量化版本 |
| OpenAI 兼容 API | `/v1/chat/completions` `/v1/embeddings` `/v1/models` |
| 自定义 Modelfile | 在基础模型上叠加 system prompt / 参数 / 适配模板 |
| GPU 自动检测 | Apple Silicon Metal / NVIDIA CUDA / AMD ROCm 自动启用 |
| 多模型并发 | 单实例可加载多模型，KV cache 按需调度 |

## 相关概念

- [llama.cpp](./tool-llama-cpp.md) — Ollama 底层的 C++ 推理引擎
- [Ghostlink](./tool-ghostlink.md) — 基于 llama.cpp RPC 后端的分布式推理，与 Ollama 并非同一方向