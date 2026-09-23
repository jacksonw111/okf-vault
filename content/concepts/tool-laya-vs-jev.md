---
type: "Tool"
title: "laya-vs-jev（T-Rex Runner 对比跑道）"
description: "把本地 MLX 推理的 Laya 模型和托管 API 的 Jev 放在同一个 T-Rex 跑酷赛道上对打，用延迟 / 存活 / 回放数据对比本地推理 vs 云 API 的实际差异。"
resource: "https://github.com/virajbhartiya/laya-vs-jev"
tags: "[benchmark, laya, jev, mlx, decision-model, comparison]"
timestamp: "2026-09-23T22:30:00Z"
---

# laya-vs-jev（T-Rex Runner 对比跑道）

## 它是什么

[laya-vs-jev](https://github.com/virajbhartiya/laya-vs-jev) 是一个**决策模型对比基准**：把 **本地 MLX 推理的 Laya 模型**和**托管 API 的 Jev** 放在同一个 **T-Rex 跑酷游戏赛道**上对打，用「**延迟 / 存活时间 / 关键决策回放**」三个维度对比本地推理与云 API 的实际差异。

## 为什么用它 / 适合什么场景

- 想直观看到**本地推理 vs 云 API** 在低延迟决策场景的差距。
- 用 T-Rex 跑酷这种实时反应游戏作为「高频小决策」的可视化基准——存活时间直接反映模型决策质量。
- 想用回放数据研究「**模型在第几个障碍挂了**」的失败模式。

## 关键能力

| 能力 | 说明 |
|------|------|
| 对比对象 | 本地 Laya（MLX）vs 云端 Jev（HTTP） |
| 跑道 | T-Rex Runner 游戏 |
| 指标 | 延迟 / 存活时间 / 决策回放 |
| 数据 | 失败决策可逐帧回看 |

## 与同类基准的差异

| 基准 | 形式 |
|------|------|
| laya-vs-jev | 游戏化实时反应对比 |
| 学术 benchmark | 静态题库（多选题 / 概率校准等） |
| laya-mlx | 单一模型的本地推理实现 |

## 项目链接
- 项目主页：<https://github.com/virajbhartiya/laya-vs-jev>

## 媒体
![laya-vs-jev 跑道截图](https://pbs.twimg.com/media/HS5omAObcAA8c_Z.png)
