---
type: "Term"
title: "CLM（Contrastive Language Model，Agent 快速决策的 System One 模型）"
description: "用对比学习把「当前状态」和「候选动作」映射到同一向量空间，用双向 InfoNCE 损失学习状态–正确动作对应关系；不必为每个任务单独微调，也能快速判断 / 排序 / 路由动作——给 Agent 当 System One 用的专用决策模型。"
resource: "https://github.com/Contrastive-LM/CLM"
tags: "[contrastive-learning, infonce, system-one, agent, decision-model, llm, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# CLM（Contrastive Language Model，Agent 快速决策的 System One 模型）

## 定义

[CLM（Contrastive Language Model）](https://github.com/Contrastive-LM/CLM) 是一种**专门做快速决策**的 **System One 模型**——用对比学习把「当前状态」和「候选动作」映射到**同一向量空间**，用**双向 InfoNCE 损失**学习「状态 ↔ 正确动作」的对应关系。

目标不是「让模型生成自然语言」，而是让 Agent **不必为每个任务单独微调，也能快速判断、排序和路由动作**。

## 训练数据（CLM-8B 为例）

按以下顺序三阶段训练：

| 阶段 | 数据 | 规模 |
|------|------|------|
| 1 | 通用问答对 | 6000 万组 |
| 2 | 合成的难负样本 | 3000 万组 |
| 3 | Agent 轨迹（state–action） | 100 万条 |

> 第三阶段把模型从「语言对比」拉到「**Agent 决策**对比」，状态 / 动作的语义空间对齐。

## 要点

- **对比学习范式**：state 与 candidate action 进同一 embedding 空间，用余弦 / 点积打分。
- **双向 InfoNCE**：state → correct action 与 action → correct state 同时训练，迫使嵌入空间对称。
- **System One 定位**：不替代 LLM 做「慢思考 / 长文生成」，而是给 Agent 当「快思考 / 路由」层。
- **免微调**：下游任务只要给候选动作列表，CLM 就能直接打分 / 排序，无需 SFT。
- **典型用途**：工具调用选择、动作路由、状态评估、风险分级、排序建议。

## 为什么重要

传统做法是给每个新任务微调一个分类头；CLM 把这个动作变成「**直接算相似度**」——同一个 8B 模型可在多个 Agent / 多个工具集之间复用，边际训练成本几乎为零。

## 相关概念

- [Jev](./term-jev.md) — 同属「非生成式决策模型」家族，但偏 TypeSafe schema 输出
- [Laya](./term-laya.md) — 另一款 System One 判定引擎
- [CLM-8B](./term-clm-8b.md) — CLM 的 8B 参数版本
