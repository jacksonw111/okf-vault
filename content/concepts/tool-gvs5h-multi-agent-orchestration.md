---
type: "Tool"
title: "GVS5H（账本式零样本多 agent 自编排）"
description: "GVS5H 提出账本式零样本自编排方法：同一模型的多个新实例通过共享文件系统中的计划、笔记和当前解法分解问题、协同求解，无需任何训练。"
resource: "https://github.com/slee-persis/GVS5H"
tags: "[multi-agent, orchestration, self-ensemble, zero-shot, coding-eval]"
timestamp: "2026-09-13T07:11:00Z"
---

# GVS5H（账本式零样本多 agent 自编排）

## 它是什么

[slee-persis/GVS5H](https://github.com/slee-persis/GVS5H) 是一个**账本式（ledger-style）零样本自编排**多 agent 方法：**不训练**，只把同一个模型的多个新实例放在一起，让它们通过**共享文件系统**里的「计划 / 笔记 / 当前解法」协作解题。

核心思路：在固定模型下，用**结构化的共享账本**（而不是 prompt 拼接）让多个 agent 实例拆分 / 协同任务。

## 为什么看它 / 适合什么场景

- 想在固定后端模型上**白嫖最多 23.2 个百分点的提升**。
- 关心**自托管开源模型能不能逼近闭源**：本地 Qwen3.8-27B 经过编排后 pass@1 从 69.2% 升到 92.4%，略超 Claude Fable 5。
- 关注**成本**：编排后的 GPT-5.6-Terra 88.0% pass@1 成本仅为 Fable 5 的 19%。
- 想做多 agent 协同但**不愿做训练 / RL**。

## 实测结果（仓库公开数据）

| 场景 | pass@1 |
|------|--------|
| 原始 GPT-5.6-Terra | ~64.8% |
| GVS5H 编排后 | 88.0% |
| Claude Fable 5（参考） | 90.4% |
| Qwen3.8-27B 原始 | 69.2% |
| Qwen3.8-27B 编排后 | 92.4% |
| 最高提升 | 23.2 个百分点 |

基准：最新 100 道 LiveCodeBench Hard，覆盖 9 个开闭源模型。

## 媒体

- ![](https://pbs.twimg.com/media/HR_CuByakAAFtxK.png)

## 项目链接

- 仓库：<https://github.com/slee-persis/GVS5H>

## 相关概念

- [LiveCodeBench](https://livecodebench.github.io) — 评测基准（项目未在 concepts 收录，留官方链接）
- [Multi-Agent Collaboration](./term-multi-agent.md) — GVS5H 是同一类思路在 coding 任务上的具体实现（term 暂未独立收录，留概念链接占位）