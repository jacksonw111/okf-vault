---
type: "Tool"
title: "better-harness（QoderAI/better-harness）"
description: "审查 AI 编码工作流五个维度——目标清楚吗 / 执行路径可复现吗 / 变更验证有证据吗 / 质量把关被跳过了吗 / 经验教训沉淀下来了吗；每项发现都绑证据，不空谈打分。"
resource: "https://github.com/QoderAI/better-harness"
tags: "[ai-coding, review, evidence-based, workflow-audit, harness, code-quality]"
timestamp: "2026-07-31T20:30:00Z"
---

# better-harness（QoderAI/better-harness）

[better-harness](https://github.com/QoderAI/better-harness) **审计 AI 编码工作流的五个维度**：目标清晰度 / 执行可复现 / 验证有证据 / 质量把关 / 经验沉淀。每项发现都**绑证据**，不空谈打分。

## 它是什么

不是代码静态分析，而是**对 agent 工作流本身**做反思性审核：

| 维度 | 审核问题 |
|------|----------|
| 目标 | 这一轮的目的说清楚了吗？ |
| 执行路径 | 你走过的步骤能不能复现？ |
| 验证 | 变更是否有可证伪的证据（测试 / 输出 / 截图）？ |
| 质量把关 | lint / type / test / review 是否被跳过？ |
| 经验沉淀 | 这一轮学到的能不能进入记忆 / 文档？ |

## 为什么用它 / 适合什么场景

| 痛点 | better-harness 的回应 |
|------|-----------------------|
| AI 给的「完成」没有证据 | 强制每条结论附证据链接 |
| 工作流漂移：今天用 RAG、明天改 fine-tune，没记录 | 模板化记决策路径 |
| 同一类问题反复出现 | 沉淀到记忆/复盘清单 |
| 团队多 agent 协作风格不统一 | 共享五维评分 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 五维审查 | 目标 / 执行 / 验证 / 质量 / 沉淀 |
| 证据绑定 | 每项发现必须附证据，不准空谈 |
| 工作流自审 | 对 agent 自身过程做反思 |
| 团队模板 | 团队可用同一份评分模板 |
| 经验沉淀模板 | 把教训写回项目知识库 |

## 与其它工具的差异

- **比普通 review 工具更上溯一层**：审查 AI 的工作流，而不是只审查代码
- **比 vibe-coding-rules 更系统**：六步管线是「合规流」，better-harness 是「审计」互补
- **强调证据而非打分**：避免印象流评审

## 相关概念

- [vibe-coding-rules](./tool-vibe-coding-rules.md) — 给 AI agent 装的「编程纪律」六步流水线，与 better-harness 互补（事前规约 vs 事后审计）
- [harness-remote](./tool-harness-remote.md) — 远程 harness，与 better-harness 概念同源
- [fable-harness](./tool-fable-harness.md) — Fable 团队 harness 实践
- [penguin-harness](./tool-penguin-harness.md) — Penguin harness 视角，与 better-harness 五维可互补
- [playbook-orca-ticket-orchestration](./playbook-orca-ticket-orchestration.md) — 票务编排，把「验证」做成一等公民
