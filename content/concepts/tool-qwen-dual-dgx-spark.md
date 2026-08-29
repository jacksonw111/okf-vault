---
type: Tool
title: "Qwen3.8-Flash-Next-Dual-DGX-Sparks（双 DGX Spark 张量并行跑 176B NVFP4 MoE）"
description: "用两台 NVIDIA DGX Spark 通过张量并行跑 176B NVFP4 量化 MoE：一条命令完成下载、镜像构建和集群启动；并补齐了上游 SGLang 在 SM121 上缺的稀疏注意力内核与 NVFP4 KV cache。"
resource: "https://github.com/MiaAI-Lab/Qwen3.8-Flash-Next-Dual-DGX-Sparks"
tags: [qwen, dgx-spark, tensor-parallel, nvfp4, moe, sglang, sm121, inference]
timestamp: "2026-08-29T21:30:00Z"
---

# Qwen3.8-Flash-Next-Dual-DGX-Sparks（双 DGX Spark 张量并行跑 176B NVFP4 MoE）

## 它是什么

[MiaAI-Lab/Qwen3.8-Flash-Next-Dual-DGX-Sparks](https://github.com/MiaAI-Lab/Qwen3.8-Flash-Next-Dual-DGX-Sparks) 是**用两台 NVIDIA DGX Spark 通过张量并行跑 Qwen 176B NVFP4 量化 MoE 模型**的一键化工程：

- 一条命令完成**权重下载、Docker 镜像构建、集群启动**；
- 利用两台 DGX Spark 互联做张量并行（tensor parallel），单机跑不下 176B 模型；
- 给上游 SGLang 补了在 **SM121**（DGX Spark 的 GPU 架构）上缺的**稀疏注意力内核 + NVFP4 KV cache**。

## 为什么用它 / 适合什么场景

- 想在桌面级 / 工作站级硬件上跑 100B+ 模型，单机显存不够时的**最小集群方案**；
- 用 NVFP4 量化大幅压缩显存占用，让 176B 在双机环境里跑得动；
- SGLang 用户遇到「SM121 上跑 Qwen MoE 报错」时直接复用其补好的 kernel；
- 学习 / 实验多机张量并行的入门工程（一条命令跑通，省去环境踩坑）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双机张量并行 | 把 176B 模型拆到两台 DGX Spark |
| NVFP4 量化 | 大幅降低显存占用 |
| 一键启动 | 下载 / 镜像 / 集群一条命令 |
| SM121 适配 | 补齐 SGLang 在 DGX Spark GPU 架构上缺的内核 |
| 稀疏注意力 | 补 SGLang 缺的稀疏注意力 kernel |
| NVFP4 KV cache | 进一步压缩 KV cache 显存 |

## 相关概念

- [go-llama](./tool-go-llama.md) — goccy 把 llama.cpp 推理完整搬进纯 Go，另一种「跨平台 LLM 推理」思路
- [Protocol Model](./tool-protocol-model.md) — 多协议 LLM 适配层，本工程专注于 SGLang 推理链

## 参考链接

- 项目链接：<https://github.com/MiaAI-Lab/Qwen3.8-Flash-Next-Dual-DGX-Sparks>
- 原始推文（QingQ77 主源）：<https://x.com/QingQ77/status/2093569332932710637>
- 原始推文（Wen_Zw RT）：<https://x.com/Wen_Zw/status/2093580926848794756>