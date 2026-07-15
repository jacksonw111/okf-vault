---
type: "Tool"
title: "Bonsai 27B（PrismML 三值化小模型 + iPhone 端运行）"
description: "PrismML 发布的 27B 三值化(tri-nary)模型,在 iPhone 上本地运行,提供 WebGPU Demo + Together API + Hugging Face 模型集合,号称「史上最大能在 iPhone 跑的开源模型」。"
resource: "https://prismml.com/news/bonsai-27b"
tags: "[llm, on-device, ternary, iphone, webgpu, quantized, prismml]"
timestamp: "2026-07-15T11:36:48Z"
---

# Bonsai 27B

[Bonsai 27B](https://prismml.com/news/bonsai-27b) 是 Khosla 投资的 PrismML 发布的**27B 三值化(tri-nary)大模型**——参数精度被压到三值,但仍保持 27B 规模,**主打在 iPhone 上本地运行**。白皮书 / 模型权重 / WebGPU Demo / Together API / 官方 demo 仓库一整套公开。

## 它解决了什么

设备端 LLM 通常要在「能跑的大小」(1B–7B) 和「质量」之间妥协。Bonsai 27B 用激进的三值量化方案,把 27B 塞进 iPhone 内存同时保留足够能力,给端侧 agent / 隐私场景提供强基座。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三值化 27B | 比特级压缩仍保持较大规模 |
| iPhone 端运行 | 通过 WebGPU / Metal 后端 |
| WebGPU Demo | Hugging Face Space 直接浏览器试 |
| Together API | 也提供云端推理 + 蒸馏模型 |
| 完整白皮书 | 量化方案 / 评测 / 部署细节公开 |
| 重点场景 | 端侧 agent、隐私对话、低延迟 |

## 关键链接

- 官方博客: <https://prismml.com/news/bonsai-27b>
- 白皮书: <https://github.com/PrismML-Eng/Bonsai-demo/blob/main/bonsai-27b-whitepaper.pdf>
- 模型集合: <https://huggingface.co/collections/prism-ml/bonsai-27b>
- WebGPU Demo: <https://huggingface.co/spaces/webml-community/bonsai-webgpu-kernels>
- Together API: <http://www.together.ai/models/prism-ml-ternary-bonsai-27b>
- 项目仓库: <https://github.com/PrismML-Eng/Bonsai-demo/>
- 官方文档: <http://docs.prismml.com>

## 适合什么场景

- 调研**三值/低比特量化**技术现状的工程师。
- 调研**iPhone / 端侧 LLM** 边界的从业者。
- 想做「不依赖云」的本地 agent,需要大底座模型的人。

## 相关概念

- [本地 LLM 硬件指南](./note-local-llm-hardware-guide.md) — 端侧推理硬件侧的对应笔记,可对比参考
- [Fable 5](./term-fable5.md) — 同一时代(2026)的端侧 / 轻量化模型路线样本,可对比策略
