---
type: "Tool"
title: "jev-visual（Apple Silicon MLX 多题视觉推理）"
description: "在 Apple Silicon 本机用 MLX 跑通类 Jev 视觉推理，一张图一次回答几十个问题，直接给候选输出打分而不自回归生成。"
resource: "https://github.com/hr98w/jev-visual"
tags: "[mlx, apple-silicon, jev, visual-reasoning, batched-qa, qwen]"
timestamp: "2026-09-19T16:00:00Z"
---

# jev-visual（Apple Silicon MLX 多题视觉推理）

## 它是什么

[hr98w/jev-visual](https://github.com/hr98w/jev-visual) 是一个**给 Apple Silicon 写的视觉模型推理练手项目**，用 MLX 在本机跑 Qwen3.5-0.8B：**一张图能连答 1 到 64 道题**，支持选项选择、是非、分级打分，每题最多 26 个候选。

不走「自回归写 JSON」的老路，而是把多模态上下文**只 prefill 一次**，后面各题拼后缀**批量读分**——典型的 Jev 风格「打分式」推理范式落到视觉问答上。

## 为什么用它 / 适合什么场景

- 在 Apple Silicon Mac 上做**轻量级 VQA 评测**（一张图几十道题），又不想拉云端大模型。
- 想批量比对候选答案的质量（视觉 A/B test / 数据标注校验）。
- 研究「一次 prefill、多次打分」的多模态推理范式。

## 关键能力

| 能力 | 说明 |
|------|------|
| MLX 本机推理 | Apple Silicon 原生后端，无 CUDA 依赖 |
| Qwen3.5-0.8B | 轻量多模态模型，单卡可跑 |
| 一图多题 | 单张图连答 1~64 题 |
| 多题型 | 选项 / 是非 / 分级打分，最多 26 候选 |
| 一次 prefill | 多模态上下文只编码一次，各题拼后缀读分 |

## 与相关概念的关系

- [JEV Ultrafast（browser-use 极速浏览器自动化）](./tool-jev-ultrafast.md) — 同一个「Jev 打分式」家族，jev-visual 把思路落到视觉问答而不是浏览器自动化

## 参考

- 项目链接：<https://github.com/hr98w/jev-visual>
- 原始推文：<https://x.com/QingQ77/status/2101190048242921651>