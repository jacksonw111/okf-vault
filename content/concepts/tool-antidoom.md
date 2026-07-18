---
type: "Tool"
title: "antidoom（Liquid4All/antidoom）"
description: "针对 LLM 推理时陷入重复循环（doom loop）的开源项目：合成反偏好数据、训练一个轻量 LoRA 来压制这种循环。"
tags: "[llm, alignment, lora, doom-loop, preference-data, agent]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/Liquid4All/antidoom"
---

# antidoom（Liquid4All/antidoom）

## 它是什么

[`antidoom`](https://github.com/Liquid4All/antidoom) 是 Liquid4All 开源的「反 doom-loop」项目，**专门针对 LLM 在推理时陷入「无限自我重复 / 死循环」**这一现象：

- 合成一批「出现 doom-loop 模式 → 应当被压下去」的偏好数据；
- 用这批数据训练一个轻量 LoRA 适配器；
- 把 LoRA 挂回基座模型，在不重训主模型的前提下压制循环倾向。

## 解决的问题

| 问题 | 说明 |
|------|------|
| Doom loop | 模型在 token 层面不断重复相同短语 / 思路，长时间无收敛 |
| 重训代价大 | 直接改主模型权重成本高、风险大 |
| 工程化补丁缺 | 多数做法（截断、温度、惩罚）都是「症状压制」，而非「行为矫正」 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 反偏好数据合成 | 自动构造 doom-loop 触发 → 偏好的样本对 |
| LoRA 训练 | 廉价、可插拔的小适配器，不动基座权重 |
| 适配多基座 | LoRA 形式通用，可叠加到主流开源 LLM 上 |
| 行为层矫正 | 比截断/温度更彻底——直接改「重复倾向」的概率分布 |

## 适合什么场景

- 开源 LLM / 小模型在 agent / 长上下文任务中**频繁陷入循环**；
- 想避免重训全模型、又需要从「行为根源」压制循环的团队；
- 配合推理框架（vLLM、TGI、SGLang）作为运行时补丁。

## 参考链接

- [原始链接](https://github.com/Liquid4All/antidoom)

## 相关概念

- [forkd](tool-forkd.md) — 同样以「轻量、可插拔的小补丁」思路解决 agent 工程的痛点（microVM 启动慢），方法论可对照