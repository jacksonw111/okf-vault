---
type: "Tool"
title: "Ghostlink"
description: "用 Rust 编写的分布式 LLM 推理平台，面向异构局域网集群：自动发现游戏 GPU、旧笔记本、带 NPU 的超极本、Mac 等设备，通过 llama.cpp RPC 后端拼出跨机器的零配置分布式推理，对外暴露 OpenAI 兼容 API + GUI。"
resource: "https://github.com/rwilliamspbg-ops/Ghostlink"
tags: [llm-inference, distributed, rust, llama-cpp, rpc, heterogeneous-cluster, local-llm]
timestamp: "2026-08-07T03:21:00Z"
---

# Ghostlink

## 它是什么

Ghostlink 是一款用 Rust 编写的分布式 LLM 推理运行时，目标是把局域网里各种「不挑食」的硬件——游戏 GPU、旧笔记本、带 NPU 的超极本、Apple Silicon Mac——组成一个零配置的分布式推理集群。它基于 llama.cpp 的 RPC 后端，让异构 CPU/GPU/NPU 设备协同跑同一份大模型，对外暴露 OpenAI 兼容 API 与完整 GUI 控制台。

## 为什么用它 / 适合什么场景

- 手里有多台「吃灰」机器（旧的 N 卡、老款 Mac mini、带 NPU 的轻薄本）想攒成一个本地推理集群。
- 不希望为推理专门采购一台高配服务器。
- 想用本地推理替代部分云端调用，同时保留 OpenAI 兼容接口。
- 想让不同设备的算力（CPU/GPU/NPU）协同，而非各自跑小模型。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动设备发现 | 局域网内的节点自动被发现，无需手工登记 IP |
| 异构硬件聚合 | 同时消费 NVIDIA GPU、Apple Silicon、NPU 等不同算力类型 |
| llama.cpp RPC 后端 | 走 llama.cpp 的远程过程调用后端跑模型分片推理 |
| OpenAI 兼容 API | 上游调用者无需改动代码，按现有 OpenAI 客户端对接 |
| 内置 GUI 控制台 | 集群状态、节点负载、请求路由直观可见 |
| Rust 实现 | 资源占用低、部署体积小、运行稳定 |
| 零配置启动 | 装好即跑，省掉手写 YAML / 配置中心节点 |

## 媒体

- 演示视频：<https://video.twimg.com/tweet_video/HO9h9mIa4AAnBl5.mp4>

## 相关概念

- [llama.cpp](./tool-llama-cpp.md) — 提供本地推理和 RPC 后端能力的底层引擎
- [Swiftlet](./tool-swiftlet.md) — Apple 设备上单节点 MoE 流式推理，与本工具侧重不同（节点内 vs 节点间）
- [Local LLM Hardware Guide](./note-local-llm-hardware-guide.md) — 选硬件与布署本地推理集群的入门参考