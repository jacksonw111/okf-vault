---
type: "Tool"
title: "hermes-jev-skills"
description: "把 agent 每轮要做的模型选择、技能挑选、记忆筛选、上下文压缩等小决策交给 TypeSafe 的决策模型 Jev，省掉前沿模型在这些非写作环节上的 token 开销。"
resource: "https://github.com/kerpopule/hermes-jev-skills"
tags: "[agent, jev, decision-model, routing, token-saving, open-source]"
timestamp: "2026-09-23T22:35:00Z"
---

# hermes-jev-skills

## 它是什么

[hermes-jev-skills](https://github.com/kerpopule/hermes-jev-skills) 把 **Jev 决策模型**接入到 Agent 的**每轮小决策环节**：

> 把 agent 每轮要做的模型选择、技能挑选、记忆筛选、上下文压缩等小决策交给 TypeSafe 的决策模型 Jev，省掉前沿模型在这些非写作环节上的 token 开销。

## 为什么用它 / 适合什么场景

- 想**降低 agent 单次任务的 token 开销**——把「**不是写作环节**」的判断交给小模型。
- 想用决策模型做「**模型路由**」——根据当前状态选最合适的模型 / 技能。
- 想做上下文压缩 / 记忆筛选的**概率化判断**而非硬规则。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型选择 | 按状态决定用哪个 LLM |
| 技能挑选 | 从 skills 池里选该调哪个 |
| 记忆筛选 | 决定把哪条记忆喂给当前 prompt |
| 上下文压缩 | 概率化判断保留哪些上下文 |
| 形态 | Jev 驱动的 Skills 集合 |

## 项目链接
- 项目主页：<https://github.com/kerpopule/hermes-jev-skills>

## 媒体
![hermes-jev-skills 截图](https://pbs.twimg.com/media/HSyg3i1a0AAtF2s.png)
