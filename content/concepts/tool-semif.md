---
type: "Tool"
title: "SemIf（本地 4B 模型做 if 式决策，不生成答案文本）"
description: "TheoLeeCJ/SemIf：让本地 4B 模型一次前向直接读出选项概率，把 agent 里「路由 / 重试 / 证据够不够」这类机械判断从「生成整句文本再解析」改成「直接读 logits」，不生成答案文本。"
resource: "https://github.com/TheoLeeCJ/SemIf"
tags: "[local-llm, decision-engine, classification, agent, small-model]"
timestamp: "2026-09-20T18:00:00Z"
---

# SemIf

## 它是什么

[TheoLeeCJ/SemIf](https://github.com/TheoLeeCJ/SemIf) 把 agent 里那些「**这条路由到哪个队列 / 要不要重试 / 证据够不够**」的小判断从「**让聊天模型生成整句文本再解析回 if**」改成「**让本地 4B 模型一次前向直接读出选项概率**」。

最大差别：**不生成答案文本**——直接读 logits，对应 token 的概率就是答案。

## 为什么用它 / 适合什么场景

- 大量「**机械判断**」没必要上大模型；4B 本地模型在边端设备就能跑。
- 想要**确定性输出**——读 logits 而不是生成再解析，省掉解析失败 / hallucination 风险。
- 关心**延迟与成本**——单次前向 + 小模型，比「大模型生成整段再正则解析」快一截。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地小模型 | 4B 参数，本机即可跑 |
| 直接读 logits | 不生成文本，输出即选项概率 |
| 适合机械判断 | 路由 / 重试 / 证据够不够 等 if 类决策 |
| 与大模型互补 | 大模型负责生成，本地 4B 负责「if」 |

## 项目链接

- 仓库：<https://github.com/TheoLeeCJ/SemIf>

## 媒体

![](https://pbs.twimg.com/media/HSn0qb1aEAAhCEH.jpg)

## 相关概念

- [Laya](./tool-laya-decision-engine.md) — 同为编码器式决策引擎，用 choice / score / noul 三种原语
- [Jevbridge](./tool-jevbridge.md) — 同类「类型化决策层」思路
- [kev（Qwen 底座决策模型）](./tool-kev-decision-model.md) — 同为本地决策模型的另一实现
