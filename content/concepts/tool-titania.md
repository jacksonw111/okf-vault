---
type: "Tool"
title: "Titania（从 Transformer 到 GPU 全自研的最小 ML 栈）"
description: "penberg/titania：把 transformer、编译器、自研 ISA、ISA 模拟器乃至规划中的 GPU 硬件全部自研，每层保持单人可读，首版已能在 CPU 与 ISA 模拟器上跑 Qwen3-0.6B 聊天。"
resource: "https://github.com/penberg/titania"
tags: "[ml, transformer, compiler, isa, simulator, gpu, learning]"
timestamp: "2026-09-15T11:00:00Z"
---

# Titania（从 Transformer 到 GPU 全自研的最小 ML 栈）

## 它是什么

[Titania](https://github.com/penberg/titania) 是一个**端到端自研**的最小机器学习栈：覆盖 transformer、编译器、自研 ISA、ISA 模拟器，并规划扩展到 GPU 硬件。每一层都刻意保持「单人可读」的代码量与复杂度——它不是生产框架，而是一份「**从头造一台 ML 计算机**」的学习工程。

## 关键里程碑

- 已实现 transformer 模型 + 自研编译器链路
- 已实现自研 ISA + ISA 模拟器
- 首版已能在 **CPU** 与 **ISA 模拟器**上跑起 Qwen3-0.6B 聊天推理
- 规划目标：把整套栈推到自定义 GPU 硬件

## 为什么用它 / 适合谁

- 想**逐层搞懂**「矩阵乘 → 图编译 → ISA → 硬件」全链路，而不只是调包调用框架
- 想找一份**教学用 / 论文用**的可拆解 ML 系统实现，对照论文读源码
- 喜欢 Rust + 自研硬件栈这种「全栈最小化」项目
- 适合作为系统课、编译原理课、ML 系统课的扩展读物

## 关键能力

| 能力 | 说明 |
|------|------|
| Transformer 实现 | 自写而非调用 PyTorch，结构透明 |
| 自研编译器 | 从模型图到目标指令的编译流水线 |
| 自研 ISA | 指令集自己定，可读性优先 |
| ISA 模拟器 | 软件跑 ISA，可在普通 CPU 上验证完整栈 |
| 跑通 Qwen3-0.6B | 已能在 CPU 与 ISA 模拟器上做聊天推理 |
| GPU 硬件规划 | 路线图里包含 GPU 自研 |

## 媒体

![](https://pbs.twimg.com/media/HSOp6NHa0AAB9ao.jpg)

## 项目链接

- 仓库：<https://github.com/penberg/titania>