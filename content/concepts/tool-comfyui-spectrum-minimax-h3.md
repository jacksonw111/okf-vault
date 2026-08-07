---
type: Tool
title: "ComfyUI-Spectrum-MiniMax-H3"
description: "ComfyUI 原生 MiniMax H3 音频-视频模型的加速采样节点：用切比雪夫岭回归预测 post-transformer 特征，对规划好的未来 solver 步骤跳过 transformer 求值，但每步的输出头 / 视频 / 音频重建 / sigma 映射照常执行。"
resource: "https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3"
tags: [comfyui, sampling, chebyshev, ridge-regression, video-generation, audio-generation, minimax-h3, diffusion]
timestamp: 2026-08-06T04:30:00Z
---

# ComfyUI-Spectrum-MiniMax-H3

## 它是什么

xmarre 为 ComfyUI 写的 MiniMax H3 音频-视频模型专属加速采样节点。用切比雪夫岭回归（Chebyshev ridge regression）预测 post-transformer 特征，让 solver 跳过若干未来步的 transformer 求值，但仍执行输出头 / 视频 / 音频重建 / sigma 映射。

## 为什么用它 / 适合什么场景

- 你在 ComfyUI 工作流里用 MiniMax H3 做音视频生成，想要缩短采样耗时又不愿意换模型。
- 能接受一定的输出质量抖动，换取明显的推理步数减少。
- 喜欢「保留数学正确性」型加速——它跳的是 transformer 求值而非输出重建，可控可分析。

## 关键能力

| 能力 | 说明 |
|------|------|
| Chebyshev 岭回归预测 | 用历史 post-transformer 特征拟合预测未来步 |
| 跳 transformer 不跳输出 | 节省主要算力的同时保留重建、sigma 映射 |
| 规划式跳过 | 提前规划好哪些 solver 步可跳，而非运行时随机 |
| ComfyUI 原生 | 直接接入节点图，与其它 ComfyUI 节点组合 |

## 相关概念
- [Open AI Canvas (影策)](./tool-open-ai-canvas.md) — AI 影视无限画布工作台，文字 / 图片 / 视频 / 音频生成 + 分镜脚本编辑器
- [Stickman Video Director](./tool-stickman-video-director.md) — 文案 → 一分钟火柴人视频的轻量方案