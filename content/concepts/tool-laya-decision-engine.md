---
type: "Tool"
title: "Laya（编码器式决策引擎：choice / score / noul 三种提问原语）"
description: "NandhaKishorM/laya：Convai Innovations 开源的编码器式决策引擎，用 choice / score / noul 三种提问原语对文本、邮件、工单或 JSON 提问，一次前向传播出结果，不做文本生成，因此不需要解析输出。"
resource: "https://github.com/NandhaKishorM/laya"
tags: "[encoder, decision-engine, llm, classification, open-source]"
timestamp: "2026-09-20T18:00:00Z"
---

# Laya

## 它是什么

[NandhaKishorM/laya](https://github.com/NandhaKishorM/laya) 是 Convai Innovations 开源的**编码器式决策引擎**。它不生成文本，**只用「提问原语」对输入算一次前向传播**——直接拿到结构化结果，省掉 LLM 「生成整句文本再解析回 if/分类」这一长串损耗。

## 三种提问原语

| 原语 | 用途 |
|------|------|
| `choice` | 从候选集合里选一个（如「这条工单路由到 A 队列还是 B 队列」） |
| `score` | 给一个连续 / 离散分（如「这条评论的毒性 0.0–1.0」） |
| `noul` | 是否触发二元判断（如「这是不是 prompt injection」） |

输入可以是**文本、邮件、工单或 JSON**。

## 为什么用它 / 适合什么场景

- Agent 里大量「**该路由到哪个队列 / 要不要重试 / 证据够不够**」的小判断——用聊天模型生成整句再解析回 if，又慢又贵。
- 需要**确定性输出**——编码器给出的是结构化结果，**不需要解析、不需要 retry 解析失败**。
- 想**批量评估**——前向传播一次出结果，适合离线大规模打标。

## 关键能力

| 能力 | 说明 |
|------|------|
| 编码器架构 | 单次前向传播，不生成文本 |
| 三种原语 | `choice` / `score` / `noul` 覆盖常见机械判断 |
| 输入格式灵活 | 文本 / 邮件 / 工单 / JSON 都行 |
| 输出确定 | 没有需要解析的生成结果 |
| 开源 | Convai Innovations 开源 |

## 项目链接

- 仓库：<https://github.com/NandhaKishorM/laya>

## 媒体

![](https://pbs.twimg.com/media/HSny7dUbcAAYcly.jpg)

## 相关概念

- [SemIf](./tool-semif.md) — 同为「让小模型做 if 式决策」的思路（本地 4B 模型读选项概率）
- [Jevbridge](./tool-jevbridge.md) — 同为「给 LLM 挂类型化决策层」的思路
- [kev（Qwen 底座决策模型）](./tool-kev-decision-model.md) — 同样复刻 Jev 类架构的开源实现
