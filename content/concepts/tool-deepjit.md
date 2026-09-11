---
type: "Tool"
title: "DeepJIT（DeepSeek 开源的 C++20 JIT 运行时）"
description: "DeepSeek 开源的轻量头文件式 C++20 JIT 运行时，同时支持 NVIDIA CUDA GPU 与华为昇腾 NPU，给扩展作者提供统一的内核编译、缓存、加载与启动接口。"
resource: "https://github.com/deepseek-ai/DeepJIT"
tags: "[cpp, jit, cuda, npu, deepseek, runtime]"
timestamp: "2026-09-11T22:05:00Z"
---

# DeepJIT

## 它是什么

[deepseek-ai/DeepJIT](https://github.com/deepseek-ai/DeepJIT) 是 **DeepSeek** 开源的**轻量头文件式 C++20 JIT 运行时**，给扩展作者提供**统一的内核编译、缓存、加载与启动接口**，同一份代码可在 **NVIDIA CUDA GPU** 与**华为昇腾 NPU** 上跑。

## 三大能力

| 能力 | 说明 |
|------|------|
| **统一编译** | 内核代码按 C++20 写一次 |
| **统一缓存** | 编译产物自动缓存，避免重复编译 |
| **统一加载与启动** | 同一 API 在 CUDA 与昇腾上启动 |

## 为什么用它 / 适合什么场景

- 想给自家推理 / 训练框架做扩展，希望**一份内核代码跨 NVIDIA / 华为**。
- 想避免每个厂商 SDK 单独接入（CUDA 一套、昇腾一套）的胶水代码。
- 研究国产 NPU 与 CUDA 的统一抽象层。

## 关键能力

| 能力 | 说明 |
|------|------|
| 头文件式 | 包含即用，零构建依赖 |
| C++20 | 用现代 C++ 写 |
| 双硬件 | NVIDIA CUDA + 华为昇腾 NPU |
| 统一接口 | 编译 / 缓存 / 加载 / 启动一套 API |
| 轻量 | 不引入大型运行时 |

## 参考链接

- 项目仓库：<https://github.com/deepseek-ai/DeepJIT>

## 相关概念

- [deepseek-recipe](./tool-deepseek-recipe.md) — DeepSeek 官方的 Rust + Python 模型调用 SDK
- [dsh-trading](./tool-dsh-trading.md) — 基于 DeepSeek Harness 的 Agent 原生交易终端
- [dsh-plugin-shop](./tool-dsh-plugin-shop.md) — DeepSeek Harness 插件目录
</content>
</invoke>