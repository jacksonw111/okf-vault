---
type: "Tool"
title: "Nimble（bespokelabsai 的 9B 类型化判断本地模型）"
description: "用一个 9B 本地模型对文本做类型化判断，按你给的扁平 schema 直接返回选项和每个选项的概率，不写推理过程、不生成 JSON。"
resource: "https://github.com/bespokelabsai/nimble"
tags: "[local-llm, classification, schema, 9b, agent-tool, structured-output]"
timestamp: "2026-09-21T22:00:00Z"
---

# Nimble（bespokelabsai）

## 它是什么

[bespokelabsai/nimble](https://github.com/bespokelabsai/nimble) 是用一个 **9B 本地模型**对文本做**类型化判断**的工具——按你给的**扁平 schema**直接返回**选项和每个选项的概率**。

## 输出形态

- **不写推理过程**（不像思维链那样展开）。
- **不生成 JSON 字符串**——直接以**类型化结果**返回，每个候选项附**概率**。
- **扁平 schema**——输入只接受简单枚举 / 数值字段。

## 为什么用它 / 适合什么场景

- 想做**实时、批量**的类型化判断——9B 本地推理比 70B 云端便宜得多。
- 想要**带概率**的结果——「是 prompt injection」置信度 0.92，而不是 yes/no。
- 想**避开 JSON 解析**的脆弱性——直接拿到类型化对象。

## 关键能力

| 能力 | 说明 |
|------|------|
| 9B 本地模型 | 单卡可跑，延迟低 |
| 扁平 schema 输入 | 用例聚焦，复杂任务交给别的工具 |
| 输出带概率 | 不只是分类，还有置信度 |
| 类型化输出 | 不解析 JSON，直接拿对象 |

## 项目链接

- 仓库：<https://github.com/bespokelabsai/nimble>

## 媒体

![](https://pbs.twimg.com/media/HStDRLiaMAAghRX.jpg)

## 相关概念

- [Laya（编码器式决策引擎）](./tool-laya-decision-engine.md) — 同样是不生成文本的判断工具
- [SemIf](./tool-semif.md) — 同样用本地小模型做 if 式判断
- [Datalab LIFT（视觉文档 JSON 抽取模型）](./tool-datalab-lift.md) — 同思路的视觉文档抽取器
