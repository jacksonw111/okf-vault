---
type: "Term"
title: "Apple Silicon"
description: "Apple 自研的 Mac / iPad 系列 ARM 架构芯片——M1 / M2 / M3 / M4 等系列，统一内存架构让 CPU / GPU / Neural Engine 共享同一块高带宽内存，是当下端侧 LLM 推理 / 本地 Agent 的主流硬件底座之一。"
resource: "https://support.apple.com/en-us/121553"
tags: "[apple-silicon, m-series, apple, hardware, local-llm]"
timestamp: "2026-10-06T22:51:00Z"
---

# Apple Silicon

## 定义

**Apple Silicon** 是 Apple 自 2020 年起在 Mac / iPad 上使用的**自研 ARM 架构 SoC 系列**（M1 / M2 / M3 / M4 / M5 等）的统称。区别于传统 x86 + 独立显卡方案，**统一内存架构（UMA）**让 CPU、GPU 与 Neural Engine 共享同一块高带宽、低延迟的统一内存池，省去数据搬运开销，是端侧 LLM 推理、本地 Agent、多媒体创作的主流硬件底座之一。

## 要点

- **代表型号**：M1 / M1 Pro / M1 Max / M1 Ultra；M2 / M2 Pro / M2 Max / M2 Ultra；M3 / M3 Pro / M3 Max；M4 / M4 Pro / M4 Max
- **统一内存（UMA）**：CPU / GPU / NPU 共用内存池，GPU 直接吃系统内存，无需 VRAM 拷贝
- **Neural Engine（ANE）**：低功耗矩阵加速单元，适合小模型推理 / 端侧 ML
- **本地 LLM 场景**：用 `llama.cpp` / `MLX` / `ollama` 在 M 系列上跑 Qwen3 / Llama 3.x 等量化模型
- **跨设备统一内存**：Mac 与 iPhone 通过 USB-C 桥接可拼成「分布式算力」（如 `tool-backburner` 的 USB-C iPhone 算力扩展方案）

## 相关概念

- [Qwen3](./term-qwen3.md) — 量化后可在 Apple Silicon 本地推理
- [Pi Agent](./term-pi-agent.md) — Apple Silicon 上跑的本地编码 Agent
