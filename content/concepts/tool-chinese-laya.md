---
type: "Tool"
title: "chinese-laya（把 Laya multilingual 决策模型微调出中文能力）"
description: "yanqiangmiffy 开源：把 Laya multilingual 决策模型的中文能力微调出来——翻译公开英文决策数据 + 保留软目标分布，训练后**目标类别一致率从 34% 提到 76%**。"
resource: "https://github.com/yanqiangmiffy/chinese-laya"
tags: "[chinese-laya, laya, decision-model, multilingual, fine-tune, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# chinese-laya（把 Laya multilingual 决策模型微调出中文能力）

## 它是什么

[chinese-laya](https://github.com/yanqiangmiffy/chinese-laya) 是 yanqiangmiffy 开源的 **Laya multilingual 决策模型中文微调项目**——

## 做法

1. **翻译**公开**英文决策数据** → 中文
2. **保留软目标分布**（soft target）——而不是硬标签
3. 微调后**目标类别一致率从 34% 提到 76%**

## 为什么用它 / 适合什么场景

- 想在**中文任务**上用 [Laya System One](./term-laya.md) 决策模型，但默认是英文。
- 想参考「**翻译 + 软目标保留**」的微调套路——比硬标签翻译损失更少信息。
- 研究多语言决策模型的中文化策略。

## 关键能力

| 能力 | 说明 |
|------|------|
| 数据准备 | 翻译英文决策数据为中文 |
| 训练技巧 | 保留软目标分布 |
| 改进 | 目标类别一致率 **34% → 76%** |
| 底座 | Laya multilingual |

## 媒体

- ![](https://pbs.twimg.com/media/HTHx9HHaQAA1Z04.jpg)

## 相关概念

- [Laya System One（1Panel）](./term-laya.md) — 本项目微调的底座模型
- [Laya 决策引擎（编码器式）](./tool-laya-decision-engine.md) — 同名不同项目：NandhaKishorM/laya 编码器式决策引擎