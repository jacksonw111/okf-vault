---
type: "Tool"
title: "DeepSeek-V4.1-Flash-EXL3（双 DGX Spark 量化方案）"
description: "MiaAI-Lab 把 DeepSeek V4.1 Flash 量化到 EXL3 mul1 平均 2.9bpw、39 分片 196 GiB，TP=2 跑 vLLM 在 8888 端口挂 OpenAI 接口，给 2 台 GB10 DGX Spark 提供可开箱跑的推理方案。"
resource: "https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-EXL3-2x-DGX-Sparks"
tags: "[llm, quantization, exl3, vllm, dgx-spark, deepseek]"
timestamp: "2026-09-15T05:45:00Z"
---

# DeepSeek-V4.1-Flash-EXL3（双 DGX Spark 量化方案）

## 它是什么

[MiaAI-Lab/DeepSeek-v4.1-Flash-EXL3-2x-DGX-Sparks](https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-EXL3-2x-DGX-Sparks) 是为 **2 台 NVIDIA GB10 DGX Spark** 量身准备的 DeepSeek V4.1 Flash 量化包：把整模型压到 **EXL3（ExLlamaV3）mul1 平均 2.9 bpw、39 个分片、合计约 196 GiB**，通过 **TP=2（Tensor Parallel 两卡分摊）** 跑 vLLM，并在 8888 端口挂出兼容 OpenAI 的 API。

## 关键参数

| 项 | 值 |
|----|----|
| 目标模型 | DeepSeek V4.1 Flash |
| 量化方案 | EXL3，mul1，平均 **2.9 bpw** |
| 分片数 | 39 |
| 总体积 | ~196 GiB |
| 推理引擎 | vLLM |
| 并行策略 | TP = 2 |
| 部署形态 | 2 × GB10 DGX Spark |
| API 兼容 | OpenAI 协议（默认 8888 端口） |
| 模型名 | `DeepSeek-v4.1-Flash-EXL3` |

## 为什么用它

- **不需要再自己跑一遍量化**——bpw / 分片 / TP 都已经配好，直接拉权重开 vLLM 即可。
- 已经按 **OpenAI 协议** 暴露端口，下游任何 OpenAI SDK、Agent、IDE 插件都能直连。
- 是少数**面向双 DGX Spark 的现成 profile**，省去新机器到手第一次调通的折腾。

## 适合谁

- 拥有或即将入手 2 台 DGX Spark 的团队
- 想本地自托管 DeepSeek Flash 类模型，又不想自己选 bpw / 分片 / TP 的人
- 需要把模型挂到现有 OpenAI 协议 Agent 平台的人

## 项目链接

- 仓库：<https://github.com/MiaAI-Lab/DeepSeek-v4.1-Flash-EXL3-2x-DGX-Sparks>