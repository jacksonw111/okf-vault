---
type: Tool
title: "Swiftlet"
description: "在普通 Apple 设备上流式运行 35B / 80B 规模 Qwen MoE 混合模型的推理运行时：仅驻留小规模稠密核心，路由专家按需从 SSD 流式取回，峰值内存压到 2.6GB / 4.3GB。"
resource: "https://github.com/leonickson1/Swiftlet"
tags: [llm-inference, moe, apple-silicon, ssd-offload, qwen, local-llm]
timestamp: 2026-08-06T01:30:00Z
---

# Swiftlet

## 它是什么

leonickson1 开源的本地 LLM 推理运行时，专为消费级 Apple 设备运行 MoE（Mixture of Experts）大模型设计：模型权重按专家粒度切片，活跃稠密核心常驻内存，不活跃专家按路由需要从 SSD 流式取回。

## 为什么用它 / 适合什么场景

- 想在 16GB / 32GB 内存的 MacBook 上跑 35B / 80B 量级的 Qwen MoE。
- 不想每次都把整模型加载进内存（普通 mmap 方案会一次性占满 RAM）。
- 接受 SSD 流式取回的延迟换取峰值内存大幅下降。

## 关键能力

| 能力 | 说明 |
|------|------|
| SSD 流式专家取回 | 路由触发的专家按需从 SSD 加载到内存，不用的专家可丢弃 |
| 极低峰值内存 | 35B 规模峰值约 2.6GB、80B 规模峰值约 4.3GB |
| 兼容 Qwen MoE 混合模型 | 现成的 Qwen MoE 系列权重即可跑 |

## 相关概念
- [PicoLM](./tool-picolm.md) — 约 2500 行 C11 写的极简 LLM 推理引擎，零依赖单文件可跑 TinyLlama
- [Local Hermes Portable](./tool-local-hermes-portable.md) — llama.cpp + Nous Hermes Agent 跨平台便携包