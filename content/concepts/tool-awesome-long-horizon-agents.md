---
type: "Tool"
title: "Awesome Long-Horizon Agents（RUC-NLPIR/Awesome-Long-Horizon-Agents）"
description: "中国人民大学 NLPIR 实验室维护的论文清单，对应综述《Towards Long-Horizon Agents: A Survey》：把「长程代理」能力分两条线——harness 层（循环、记忆、工具、编排、钩子、验证）与模型层（架构、预训练、微调、RL、蒸馏、自我进化）；任务按时间跨度分 H1 / H2 / H3 三层；收录几百篇论文，从 CoT/ReAct 到最新代理 RL 全部带链接与代码。"
resource: "https://github.com/RUC-NLPIR/Awesome-Long-Horizon-Agents"
tags: [awesome-list, long-horizon, agents, survey, harnesses, rl, nlpir, papers]
timestamp: "2026-07-27T20:30:00Z"
---

# Awesome Long-Horizon Agents（RUC-NLPIR/Awesome-Long-Horizon-Agents）

## 它是什么

`RUC-NLPIR/Awesome-Long-Horizon-Agents` 是**中国人民大学 NLPIR 实验室**维护的论文清单，对应综述 **《Towards Long-Horizon Agents: A Survey》**。

仓库把「长程代理」能力分成两条线：

- **harness 层**：循环、记忆、工具、编排、钩子、验证；
- **模型层**：架构、预训练、微调、RL、蒸馏、自我进化。

任务按**时间跨度**分三层：

- **H1**：同一上下文窗口内；
- **H2**：跨窗口 / 跨会话；
- **H3**：开放任务流（无明确终止条件的长程任务）。

收录**几百篇论文**，从 CoT / ReAct 一路到最新代理 RL，每篇附链接和代码。

## 为什么用它 / 适合什么场景

- 想系统读「代理如何变长程」的论文，但**不想从零检索**；
- 做代理研究 / 工程，区分**该改 harness 还是改模型**；
- 调研 **H1 / H2 / H3** 各时间跨度下的代表方法；
- 需要一份带**分类 + 注解 + 代码**的 reference list 给团队 / 论文写作。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双线分类 | Harness 层 vs 模型层，便于定位改造点 |
| 三级时间跨度 | H1 窗口内 / H2 跨窗口 / H3 开放任务流 |
| 几百篇论文 | 从 CoT、ReAct 到最新代理 RL 完整覆盖 |
| 链接 + 代码 | 每篇附 paper / code 链接 |
| 综述配套 | 对应《Towards Long-Horizon Agents》综述 |
| 学界维护 | NLPIR @ RUC 实验室持续更新 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOHq7dhbQAAhbDJ.jpg)

- 项目链接：<https://github.com/RUC-NLPIR/Awesome-Long-Horizon-Agents>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Harness 层的「技能」是长程代理记忆 / 编排的关键拼图
