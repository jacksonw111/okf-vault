---
type: Tool
title: "jev-dreaming（Jev 分块判定 + Gemini 记忆 vs 全 Gemini 对照实验台）"
description: "AdnanQuazi 开源的本地测试台：把「Jev 分块判定 + Gemini 写记忆」与「全程 Gemini」两条 Agent 记忆管线摆在一起跑，速度、花费、记忆质量各出各的数，不用从零搭对照实验。"
resource: "https://github.com/AdnanQuazi/jev-dreaming"
tags: [jev, gemini, agent-memory, benchmark, ab-test, decision-engine, typesafe]
timestamp: 2026-10-01T04:49:00Z
---

# jev-dreaming

## 它是什么

**jev-dreaming** 是 [AdnanQuazi](https://github.com/AdnanQuazi) 开源的**本地 Agent 记忆管线对照测试台**——把两条记忆管线摆在一起跑：

1. **Jev 分块判定 + Gemini 写记忆**：用 [Jev](./term-jev.md) 这种类型化决策模型对记忆做「分块 / 归档 / 检索判断」，写入由 Gemini 完成
2. **全程 Gemini**：让 Gemini 独立完成所有记忆相关决策

输出三项关键指标的对照数据：**速度 / 花费 / 记忆质量**。

设计上把整套测试框架搭好，用户不用从零搭对照实验，可以直接复现 / 改参数。

## 为什么用它 / 适合什么场景

- 想验证「**Jev 当外层判定 + 大模型生成**」这条 TypeSafe 路线在 Agent 记忆场景下是否真的比纯 LLM 更划算。
- 需要为自己的 Agent 选记忆管线，但不知道加一层判定模型是否值得。
- 团队在做「模型分层 / 决策分离」研究，希望有一个可复用的对照实验模板。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本地测试台 |
| 对照方案 | A: Jev 分块判定 + Gemini 记忆；B: 全程 Gemini |
| 指标 | 速度 / 花费 / 记忆质量 |
| 价值 | 不用从零搭对照实验 |
| 适用对象 | Agent 记忆管线研究者 |
| 上游依赖 | Jev + Gemini |

## 参考链接

- 仓库：<https://github.com/AdnanQuazi/jev-dreaming>

## 媒体

- ![](https://pbs.twimg.com/media/HTcvCmGawAA5Jne.jpg)

## 相关概念

- [Jev](./term-jev.md) — 对照方案 A 里的决策引擎
- [Gemini](https://deepmind.google/technologies/gemini/) — 对照方案里的生成模型
- [Agent 记忆](./term-okf.md) — 整体研究方向
