---
type: "Tool"
title: "NanoJev（0.6B 小模型并行决策复刻）"
description: "复刻 Jev 的并行决策思路，让 0.6B 小模型一次前向直接输出完整概率分布，不做输出 token 解码。"
resource: "https://github.com/TianyuCodings/NanoJev"
tags: "[small-model, parallel-decoding, jev, llm, probability-distribution]"
timestamp: "2026-09-19T16:00:00Z"
---

# NanoJev（0.6B 小模型并行决策复刻）

## 它是什么

[TianyuCodings/NanoJev](https://github.com/TianyuCodings/NanoJev) 是一个**把 Jev 风格的并行决策思路复刻到 0.6B 参数量级小模型**的实验性项目。核心做法是：让模型在**一次前向传播**内直接输出完整的概率分布，**不做输出 token 的逐位解码**——典型的做法是把候选 token 的 logit 视为打分，对一组候选答案直接打分排序，而不是自回归地生成 JSON / 文本。

## 为什么用它 / 适合什么场景

- 想在**极小模型**（手机端 / 嵌入式 / 浏览器侧）上跑「多选题 / 分类 / 打分」类任务，又不想拉起完整 LLM 自回归生成。
- 做 agent 工具：需要让小模型以「打分器」身份给候选输出排名，比自回归解释器更省时省 token。
- 研究「不靠大规模自回归、靠一次前向分布输出」的小模型推理范式。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一次前向打全分布 | 跳过 token-by-token 解码，直接拿到候选输出上的概率质量 |
| 0.6B 参数量级 | 极小尺寸，CPU / 端侧也能跑 |
| Jev 思路复刻 | 与 browser-use/jev-ultrafast 一脉相承的「打分式」推理范式 |
| 适合机械判断任务 | 验真 / 排序 / 多选 / 是否题等不需自由生成的任务 |

## 与相关概念的关系

- [JEV Ultrafast（browser-use 极速浏览器自动化）](./tool-jev-ultrafast.md) — 同源于 Jev「一次前向直接打分」的并行决策思路，但应用在浏览器自动化而非纯模型推理

## 参考

- 项目链接：<https://github.com/TianyuCodings/NanoJev>
- 原始推文：<https://x.com/QingQ77/status/2101125879766421755>