---
type: "Tool"
title: "llama.cpp"
description: "Georgi Gerganov 主导的 C++ 本地大模型推理引擎：把 GGUF 量化模型跑在 CPU / GPU / Apple Silicon / NPU 上，是本地 LLM 推理的事实标准底层之一。"
resource: "https://github.com/ggerganov/llama.cpp"
tags: [llm-inference, local-llm, gguf, quantization, cpp]
timestamp: "2026-08-08T20:00:00Z"
---

# llama.cpp

## 它是什么

llama.cpp 是 Georgi Gerganov 主导的开源 C++ 项目，把 GGUF 量化模型跑在各种硬件上：CPU、Apple Silicon、NVIDIA / AMD GPU 甚至部分 NPU。它以极低门槛让「在自己机器上跑大模型」成为现实，是本地 LLM 推理生态事实标准的底层引擎之一。

## 为什么用它 / 适合什么场景

- 想在普通笔记本 / 树莓派 / 游戏机上跑 7B ~ 70B 模型。
- 需要本地推理，不希望依赖云端 API。
- 想在不同硬件间灵活切换（Apple Silicon ↔ NVIDIA ↔ CPU）。
- 作为上层应用的推理后端（Ollama / LM Studio / GPT4All 都依赖它）。

## 关键能力

| 能力 | 说明 |
|------|------|
| GGUF 模型支持 | 加载官方 / 社区量化后的 GGUF 模型 |
| 多硬件后端 | CPU / CUDA / Metal / Vulkan / SYCL |
| RPC 分布式 | 通过 RPC 后端拼多节点异构集群 |
| OpenAI 兼容 server | 内置 HTTP server，对外暴露 OpenAI 兼容接口 |
| 量化工具链 | 自带模型量化脚本，把 fp16 转 Q4/Q5/Q8 等 |

## 相关概念

- [Ghostlink](./tool-ghostlink.md) — 基于 llama.cpp RPC 后端做异构集群的分布式推理
- [Ollama](./tool-ollama.md) — 封装 llama.cpp 的本地推理一键启动器
- [本地 LLM 硬件搭建实操指南](./note-local-llm-hardware-guide.md) — 选硬件与布署本地推理集群的入门参考