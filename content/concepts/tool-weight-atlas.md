---
type: Tool
title: "Weight Atlas"
description: "对每个权重张量跑一遍真实量化的可视化工具：把 INT8 / INT4 / FP8 三套方案的误差、频谱、离群通道测出来，铺到一张可缩放画布上，让模型压缩时看清哪里能压、哪里一压就坏。"
resource: "https://github.com/alesha-pro/atlas"
tags: [quantization, llm, model-compression, visualization, safetensors]
timestamp: 2026-09-02T12:00:00Z
---

# Weight Atlas

## 它是什么

下载下来一目录 `.safetensors` 分片，权重张量内部到底长什么样、哪些通道对量化敏感、哪些安全，传统做法只能盲压盲跑。`Weight Atlas` 对每个权重张量实际跑 INT8 / INT4 / FP8 三套量化方案，把误差分布、频谱特征、离群通道位置等指标测出来，铺到一张可缩放的画布上。压缩模型时直接看图就知道哪些层能安全压、哪些层一压就崩。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实测三种量化 | INT8 / INT4 / FP8 都跑一遍，不是只看理论误差 |
| 多维度指标 | 误差 / 频谱 / 离群通道同时呈现 |
| 可缩放画布 | 整张权重地图可缩放，便于定位敏感区域 |

## 项目链接

- [项目主页](https://github.com/alesha-pro/atlas)

## 相关概念

- [llama.cpp](./tool-llama-cpp.md) — 主流本地 LLM 推理引擎（量化是其核心场景）
