---
type: Tool
title: "jspace-viz（开源 LLM 实时 Jacobian-lens 可视化）"
description: "给开源语言模型做实时可视化用的工具：用 Jacobian-lens 把论文里说的「可言说工作空间」画成一张能点的「层 × 位置」热力图，让你看见模型每一层、每个位置「正准备吐出哪个词」。"
resource: "https://github.com/Festyve/jspace-viz"
tags: [tool, llm, visualization, interpretability, jspace, heatmap]
timestamp: 2026-07-12T16:30:00Z
---

# jspace-viz（开源 LLM 实时 Jacobian-lens 可视化）

## 它是什么
给开源语言模型（Open-source LLM）做的实时可视化工具。它用「Jacobian-lens」技术把可解释性论文里说的"可言说工作空间"（jspace）渲染成一张"层 × 位置"的热力图——你能直观看到模型每一层（layer）、每个 token 位置（position）此刻"正准备吐出哪个词"的概率分布。

## 为什么用它 / 适合什么场景
- 研究 LLM 内部表示 / 可解释性，需要可视化 jspace / Jacobian-lens 而非只看论文里的静态图。
- 想理解 prompt 中每个 token 在不同层对输出的影响（教学 / 调试 / 论文图表）。
- 想对比不同开源模型在同一 prompt 下的 jspace 差异。

## 关键能力
| 能力 | 说明 |
|------|------|
| 实时可视化 | 模型推理时同步渲染 jspace 热力图 |
| 层 × 位置矩阵 | 直观看到"哪一层哪个位置正在影响哪个 token" |
| 可点交互 | 单元格可点击下钻到具体 token / logit |
| Jacobian-lens | 用论文里的 Jacobian 视角切片模型内部状态 |
| 开源 LLM 友好 | 兼容常见开源 transformer 模型 |

## 参考链接
- [项目链接](https://github.com/Festyve/jspace-viz)
- [原始链接](https://x.com/QingQ77/status/2076191576322191474)

![jspace-viz 截图](https://pbs.twimg.com/media/HM7RtQqbkAAOYce.jpg)

## 相关概念
- [jlens-qwen36（Apple Silicon 本地跑 Qwen3.6 + 层 × 位置 token 读可视化）](tool-jlens-qwen36.md) — 同类"层 × 位置"可视化思路，但聚焦 Apple Silicon + MLX 上的 Qwen3.6-27B 4-bit