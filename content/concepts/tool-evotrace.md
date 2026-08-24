---
type: Tool
title: "EvoTrace"
description: "把 Claude Code / Codex 留在本地的历史会话挖出来，编译成可直接用于后训练的数据：偏好样本、可复现任务、RL 环境与奖励候选，数据不出本机。"
resource: "https://github.com/jinzijian/EvoTrace"
tags: [post-training, dataset, claude-code, codex, rl, alignment, privacy]
timestamp: "2026-08-24T14:18:00Z"
---

# EvoTrace

## 它是什么

[jinzijian/EvoTrace](https://github.com/jinzijian/EvoTrace) 是给 AI 实验室 / 个人研究者用的**本地化后训练数据编译器**：把 Claude Code / Codex 等 AI 编程 agent 在本机留下的历史会话，挖出来 → 标注 → 编译成可直接喂给后训练流程的数据集——偏好样本（DPO）、可复现任务（SFT / 评测）、RL 环境与奖励候选。

## 为什么用它 / 适合什么场景

- 想用自己的 Agent 使用记录做模型微调 / 评测，但数据敏感不愿上传。
- 想用真实工程师的「修 bug / 重构 / 跑测试」轨迹做 DPO 数据。
- 想给 RL 训练构造「带奖励函数候选的可复现任务环境」。
- 想给 Agent 公司 / 团队沉淀出可对外授权的、隐私脱敏过的训练语料。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地会话抽取 | 读 Claude Code / Codex 本地日志，不联网 |
| 偏好样本编译 | 自动产出 DPO 风格 (prompt, chosen, rejected) 三元组 |
| 任务可复现化 | 把会话里的修复任务结构化，附前置状态 / 验证步骤 |
| RL 环境候选 | 自动识别可作为训练环境的子任务 |
| 奖励函数候选 | 从 diff / 测试结果反推可能的 reward signal |
| 隐私优先 | 数据全程在本地处理，可脱敏后再导出 |

## 相关概念

- [Codex Trajectory](./tool-codex-trajectory.md) — 解析 Codex 本地任务日志，EvoTrace 是其下游消费者
- [DSH SessionGraph](./tool-dsh-sessiongraph.md) — 把 DSH 会话压缩成可编辑导图，结构化思路一致
- [Local LLM 硬件指南](./note-local-llm-hardware-guide.md) — 跑本地模型训练的硬件参考

## 参考链接

- [项目链接](https://github.com/jinzijian/EvoTrace)
- ![](https://pbs.twimg.com/media/HQdAqRUaQAAA2n0.jpg)