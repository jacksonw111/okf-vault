---
type: "Note"
title: "《深入理解 AI Infra》（开源版）"
description: "bojie_li 写的开源电子书：从硬件约束与模型架构出发，量化推导系统设计；约 500 页 / 12 章，覆盖模型架构 / 推理与训练负载 / 加速器架构 / 算子运行时 / 超节点 / 数据中心网络 / 推理优化 / 分布式推理 / 训练系统 / 资源调度 / 端边云协同。"
resource: "https://github.com/bojieli/ai-infra-book"
tags: "[ai-infra, book, hardware, distributed, training, inference, accelerator]"
timestamp: "2026-09-14T22:30:00Z"
---

# 《深入理解 AI Infra》（开源版）

## 它是什么

[bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book) 是 **bojie_li** 在《深入理解 AI Agent》之后写的**第二本开源书** —— 这次讲 **AI Infra**（模型赖以运行的基础设施）。

> 写完《深入理解 AI Agent》后，在与读者交流的过程中，越来越感到：要开发好基于模型的应用，还需要理解它赖以运行的基础设施。

## 核心论点

- **模型成了 LLM 时代的操作系统，AI Infra 成了 LLM 时代的计算机体系结构**
- 编程抽象从操作系统上移到模型上下文——传统 OS / 编译器 / 硬件要为事先未知的程序提供通用能力，但 LLM 时代可以**针对特定模型 + 加速器架构做优化**
- 模型设计也开始反过来适应硬件（DeepSeek V4/V4.1 重新设计长上下文表示方式）
- AI Infra 领域缺少一本「从硬件约束和模型架构出发、量化推导系统设计」的书——这正是写作动机

## 12 章结构

| 章 | 主题 |
|----|------|
| 1 | 初识 AI Infra |
| 2 | 模型架构 |
| 3 | 推理与训练负载 |
| 4 | 加速器架构 |
| 5 | 算子与运行时 |
| 6 | 超节点 |
| 7 | 数据中心网络 |
| 8 | 推理优化 |
| 9 | 分布式推理 |
| 10 | 训练系统 |
| 11 | 资源调度与运行环境 |
| 12 | 端边云协同 |

## 适合谁

- 想从硬件 / 模型联合视角理解 AI 系统的工程师
- 想搞清楚 vLLM / SGLang / TensorRT-LLM 等推理引擎到底在做什么
- 在做大规模训练 / 推理系统设计

## 项目链接

- 仓库：<https://github.com/bojieli/ai-infra-book>
