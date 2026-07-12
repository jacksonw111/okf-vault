---
type: Tool
title: "Colibri（纯 C 零依赖 MoE 流式推理引擎）"
description: "一个纯 C、零依赖的推理引擎，靠把 MoE 专家从磁盘流式读出来，让 25GB 内存的普通电脑也能跑 744B 的 GLM-5.2。"
resource: "https://github.com/JustVugg/colibri"
tags: [tool, llm, inference, moe, rust, c, on-device]
timestamp: 2026-07-12T16:30:00Z
---

# Colibri（纯 C 零依赖 MoE 流式推理引擎）

## 它是什么
纯 C、零依赖的 LLM 推理引擎，专为 MoE（Mixture of Experts）大模型设计。它把 21504 个路由专家放在磁盘上（约 370GB）按需流式读取，只把稠密部分（约 17B 参数）用 int4 常驻内存（约 9.9GB），从而让 25GB 内存、无 GPU 的普通消费级电脑也能跑 744B 参数级别的 GLM-5.2。

## 为什么用它 / 适合什么场景
- 想在普通笔记本 / 台式机（25GB 内存、无 GPU）上跑 700B+ 级别的 MoE 模型做本地推理 / 评估。
- 对 Python / PyTorch / CUDA 依赖敏感（无 GPU 环境、嵌入式 / 边缘部署），希望用纯 C 工具直接调用。
- 想研究 MoE 路由专家调度 / 内存-磁盘换入换出策略。

## 关键能力
| 能力 | 说明 |
|------|------|
| 纯 C 零依赖 | 单文件可执行，无需 Python / CUDA |
| MoE 流式 | 21504 个路由专家按需从磁盘读取 |
| int4 量化 | 稠密部分用 int4，常驻内存约 9.9GB |
| 25GB 内存可跑 744B | 让消费级机器跑 GLM-5.2 级别 MoE |
| 无 GPU 友好 | 纯 CPU 推理 |

## 参考链接
- [项目链接](https://github.com/JustVugg/colibri)
- [原始链接](https://x.com/QingQ77/status/2076108277364965737)

![Colibri 架构示意](https://pbs.twimg.com/media/HM6-3I2aUAAooEQ.png)

## 相关概念
- [本地 LLM 硬件指南（2k / 40k 预算跑 Qwen3-27B / GLM-5.2）](note-local-llm-hardware-guide.md) — 同样是"如何在普通硬件上跑大模型"的方案，但走「整机配置 + VRAM 路线」
- [jlens-qwen36（Apple Silicon 本地跑 Qwen3.6 + 层 × 位置可视化）](tool-jlens-qwen36.md) — 同样聚焦"在普通硬件上本地跑模型"，但路线是 Apple Silicon + MLX