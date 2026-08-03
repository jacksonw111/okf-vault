---
type: Tool
title: "PicoLM"
description: "约 2500 行 C11 写的极简 LLM 推理引擎，零依赖、单文件约 80KB，能在树莓派 Zero 2W / LicheeRV Nano 这类廉价开发板上本地运行 TinyLlama 1.1B 等 GGUF 模型。"
resource: "https://github.com/RightNow-AI/picolm"
tags: [c, llm, inference, embedded, gguf, tinyllama, raspberry-pi, risc-v]
timestamp: "2026-08-02T23:26:00Z"
---

# PicoLM

## 它是什么
PicoLM（`RightNow-AI/picolm`）是约 **2500 行 C11 写的极简 LLM 推理引擎**，零依赖、单文件约 80KB，能在树莓派 Zero 2W、LicheeRV Nano 这类廉价开发板上跑 TinyLlama 1.1B 等 GGUF 模型。

## 为什么用它 / 适合什么场景
- **极小资源占用**：80KB 单文件、零依赖，能塞进 256MB 内存的廉价板子。
- **纯 C11**：跨平台、可移植，编译器之外不需要任何运行时。
- **教学价值**：2500 行 C 看清楚 LLM 推理主流程（量化 / 加载 / KV cache / 采样）。
- **离线 / 边缘推理**：在没有 GPU、没有大内存的设备上跑 1B 级模型。

## 关键能力

| 能力 | 说明 |
|------|------|
| C11 单文件 | 约 2500 行 C11，零依赖 |
| GGUF 加载 | 支持 TinyLlama 等 GGUF 量化模型 |
| 极小 footprint | 编译后 ~80KB，能跑 256MB 内存的板子 |
| 廉价格局 | 树莓派 Zero 2W、LicheeRV Nano 等 RISC-V / ARM 板子 |
| 1B 级本地推理 | TinyLlama 1.1B 等 <2B 模型 |

## 项目链接
- <https://github.com/RightNow-AI/picolm>

## 相关概念
- [Local LLM Hardware Guide](./note-local-llm-hardware-guide.md) — 本地 LLM 硬件选型 + 部署笔记
- [RVLLM](./tool-rvllm.md) — RISC-V 上的 LLM 推理（与 PicoLM 的 RISC-V 路径互补）
- [LLM Wiki](./term-llm-wiki.md) — LLM 概念元定义
