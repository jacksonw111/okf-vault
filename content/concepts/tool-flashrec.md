---
type: Tool
title: "FlashRec"
description: "搜狐多模态团队开源的生成式推荐推理引擎：基于 mini-sglang，把物品检索做成「语义 ID（SID）序列的宽束生成」，用生成式思路替代传统召回排序管线。"
resource: "https://github.com/sohu-mptc/FlashRec"
tags: [recommender, generative-ai, semantic-id, inference, sglang]
timestamp: "2026-09-06T00:00:00Z"
---

# FlashRec

## 它是什么

[sohu-mptc/FlashRec](https://github.com/sohu-mptc/FlashRec) 是**搜狐多模态团队**开源的**生成式推荐推理引擎**，基于 [mini-sglang](https://github.com/sgl-project/mini-sglang)。把物品检索重新表达为**语义 ID（Semantic ID, SID）序列的宽束生成**——用生成模型一次吐出一组候选 SID，对应一批候选物品。

定位：

- **生成式召回**：把传统「嵌入 → ANN → 排序」管线换成「直接生成候选集合」。
- **基于 mini-sglang**：复用 LLM serving 栈的高吞吐能力。

## 为什么用它 / 适合什么场景

- 已经在用 sglang / mini-sglang 栈做推理，希望把推荐召回也跑在同一基础设施上。
- 关注「语义 ID」路线——把物品、用户行为编码到同一个 token 空间。
- 想要单次推理吐出多候选的「宽束」召回，而不是「先粗排再精排」的多阶段管线。

## 关键能力

| 能力 | 说明 |
|------|------|
| 语义 ID（SID） | 把物品 / 行为映射到同一 token 空间 |
| 生成式召回 | 用 LLM 生成式吐出候选 SID 序列 |
| 宽束生成 | 单次推理给出一组候选物品 |
| mini-sglang 后端 | 复用 sglang 的高效 serving 栈 |

## 相关概念

- [ledgeindex（开发者文档抓取 / 分块 / 嵌入 / 索引工具）](./tool-ledgeindex.md) — 同类「嵌入 + 索引 + 检索」基建思路
- [Agent Skills（代理技能包）](./term-agent-skills.md) — FlashRec 不是 Skill，但是类似的「开源模型 + 推理框架」组合可借鉴

## 项目链接

- 项目主页：<https://github.com/sohu-mptc/FlashRec>
