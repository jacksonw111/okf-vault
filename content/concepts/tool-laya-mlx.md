---
type: "Tool"
title: "laya-mlx（Apple Silicon 上 Laya 决策引擎的本地推理）"
description: "把 Laya 类型化决策模型搬进 Apple Silicon 本地推理：一次短决策 7–14 毫秒出结果，不生成任何 token，也不依赖 PyTorch、Transformers runtime 或云端 API。"
resource: "https://github.com/mizorewww/laya-mlx"
tags: "[apple-silicon, mlx, laya, local-llm, decision-engine]"
timestamp: "2026-09-21T22:00:00Z"
---

# laya-mlx

## 它是什么

[mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx) 把 [Laya](./tool-laya-decision-engine.md) 类型化决策模型**搬进 Apple Silicon 本地推理**——用 Apple 的 **MLX** 框架跑。

## 关键指标

| 指标 | 数值 |
|------|------|
| 单次短决策延迟 | **7–14 毫秒** |
| 是否生成 token | 不生成 |
| 是否依赖 PyTorch | 不依赖 |
| 是否依赖 Transformers runtime | 不依赖 |
| 是否调用云端 API | 不调用 |

## 为什么用它 / 适合什么场景

- 在 Mac 上做**本地、低延迟、低能耗**的决策判断。
- 不希望被 **PyTorch / Transformers runtime / 云端 API** 绑住。
- 想把 Laya 的 choice / score / noul 原语**直接嵌入 macOS App**。

## 关键能力

| 能力 | 说明 |
|------|------|
| Apple Silicon 优化 | MLX 后端吃满 M 系列芯片 |
| 7–14 ms 短决策 | 适合实时路由 / 拦截 |
| 零云端依赖 | 完全本地运行 |
| 不依赖 PyTorch | 用 MLX 替代 |

## 项目链接

- 仓库：<https://github.com/mizorewww/laya-mlx>

## 媒体

![](https://pbs.twimg.com/media/HSs-UVeagAAePk-.jpg)

## 相关概念

- [Laya（编码器式决策引擎）](./tool-laya-decision-engine.md) — 上游项目，提供架构与原语
- [kev（Qwen 底座本地决策模型）](./tool-kev-decision-model.md) — 同样复刻 Jev 类的另一实现
