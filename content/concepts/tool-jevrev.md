---
type: "Tool"
title: "JevRev（LLM 之外加一层决策与证据审计的回路）"
description: "在 LLM 外面套一层 Jev 决策与证据审计：先用 Jev 把重复、跑偏、低回报的候选方案筛掉，再让 Jev 在每一轮生成后审计证据，避免 agent 持续在错方向上消耗时间和 token。"
resource: "https://github.com/Alex314618-create/JevRev"
tags: "[llm, jev, agent, decision-layer, evidence-audit, token-saving, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# JevRev（LLM 之外加一层决策与证据审计的回路）

## 它是什么

[JevRev](https://github.com/Alex314618-create/JevRev) 是给 LLM 调用栈**外加一层决策 / 审计回路**的开源项目——把 [Jev](./term-jev.md) 类型的 TypeSafe 判定模型当成「**外脑**」放在 LLM 主循环之外：

1. **方案筛选**：在让 LLM 展开之前，先用 Jev 把候选方案里的「重复 / 跑偏 / 低回报」剔除。
2. **证据审计**：每一轮 LLM 生成结果之后，Jev 再基于已有证据做一次「结论是否站得住」的判定，把无依据的自信拦下来。

这样能避免 agent 在错误方向上反复烧 token 与时间。

## 为什么用它 / 适合什么场景

- 跑长链路 agent 时发现它会**重复试同一类错误路径**或**一直朝收益低的方向走**——典型的「LLM 没人喊停」症状。
- 想在不改主 LLM 的前提下**加一道机器化的判断闸**，降低无效生成。
- 想用「判定模型」而非「又一个大 LLM」做决策——Jev 这类 TypeSafe 模型便宜、低延迟、可解释（直接给概率 / 选项 / 打分）。
- 工程上需要可审计的「为什么这一步被否决」——每一轮的筛选 / 审计依据都能回放。

## 关键能力

| 能力 | 说明 |
|------|------|
| 决策层 | Jev 在 LLM 之外做判定（不进 LLM 主循环） |
| 预筛选 | 进入 LLM 展开前剔除重复 / 跑偏 / 低回报方案 |
| 证据审计 | 每轮生成后用 Jev 复核结论是否站得住 |
| 可回放 | 筛选 / 审计依据可追溯 |
| 接口形态 | 给现有 LLM 栈接入「外层判断 + 审计」套壳 |

## 媒体

![](https://pbs.twimg.com/media/HTBe64WaUAAkVRr.jpg)

## 相关概念

- [Jev](./term-jev.md) — TypeSafe 判定模型家族，JevRev 用它做「外脑」
- [clearai-dsh](./tool-clearai-dsh.md) — DeepSeek Harness 上的证据链 + 独立评审机制，与 JevRev 同思路（审计 agent 的完工宣称）
- [agent-verification-ladder](./note-agent-verification-ladder.md) — SpaceX / Dune 视角的 5 级 agent 自我验证阶梯
