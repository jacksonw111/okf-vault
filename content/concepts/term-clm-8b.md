---
type: "Term"
title: "CLM-8B（CLM 的 8B 参数版本：System One 专用决策模型）"
description: "CLM（Contrastive Language Model）的 8B 参数实现——三阶段训练（6000 万通用问答 + 3000 万合成难负样本 + 100 万条 Agent 轨迹），把 state 和 candidate action 映射到同一向量空间，用双向 InfoNCE 学习对应关系，给 Agent 当 System One 路由层用。"
resource: "https://github.com/Contrastive-LM/CLM"
tags: "[clm, contrastive-learning, infonce, system-one, agent, decision-model, 8b, open-source]"
timestamp: "2026-09-26T21:50:00Z"
---

# CLM-8B（CLM 的 8B 参数版本：System One 专用决策模型）

## 定义

[CLM-8B](https://github.com/Contrastive-LM/CLM) 是 [CLM（Contrastive Language Model）](./term-clm.md) 的 **8B 参数实现**——专做 Agent System One 快速决策：把「当前状态」与「候选动作」映射到**同一向量空间**，用**双向 InfoNCE** 学对应关系。

## 三阶段训练

| 阶段 | 数据 | 规模 | 作用 |
|------|------|------|------|
| 1 | 通用问答对 | 6000 万组 | 建立基础语义对比能力 |
| 2 | 合成的难负样本 | 3000 万组 | 训练区分细粒度差异 |
| 3 | Agent 轨迹（state–action） | 100 万条 | 把模型从「语言对比」拉到「Agent 决策对比」 |

## 要点

- **对比学习 + 双向 InfoNCE**：state → correct action 与 action → correct state 同时训练，迫使嵌入空间对称。
- **免微调**：下游任务只要给候选动作列表，CLM-8B 就能直接打分 / 排序，无需 SFT。
- **System One 定位**：不替代 LLM 慢思考，给 Agent 当路由层。
- **典型用途**：工具调用选择、动作路由、状态评估、风险分级、排序建议。

## 相关概念

- [CLM](./term-clm.md) — CLM 模型家族的总体定义与训练范式
- [Jev](./term-jev.md) — 同属「非生成式决策模型」家族，但偏 TypeSafe schema 输出
- [Laya](./term-laya.md) — 另一款 System One 判定引擎
- [decider-2b](./term-decider-2b.md) — 更小的端侧决策模型（2B）