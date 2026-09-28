---
type: "Tool"
title: "Harbor（NVIDIA：RL 终端任务训练框架）"
description: "NVIDIA 的强化学习（RL）终端任务训练框架：把 Agent 需要在真实终端里完成的任务标准化为可 Docker 化的训练环境，是 Skill2Env 等工具产物的下游消费方。"
tags: "[nvidia, rl, terminal-agent, docker, reinforcement-learning, training-framework]"
timestamp: "2026-09-28T23:40:00Z"
---

# Harbor（NVIDIA：RL 终端任务训练框架）

## 它是什么

**Harbor** 是 NVIDIA 出品的**强化学习（RL）终端任务训练框架**：把 Agent 需要在真实终端里完成的任务标准化为**可在 Docker 中跑起来的训练环境**。

设计目标是把「Agent 在终端里干活」这件事变成可大规模并行、可复现的 RL 训练流水线。

## 为什么用它 / 适合什么场景

- 想用 RL 训练终端 Agent（Code Agent / Dev Agent），但缺乏标准化环境。
- 想要 **Docker 化** 的训练环境：隔离、可复现、可横向扩展。
- 是 [Skill2Env](./tool-skill2env.md) 等「Agent Skill → RL 训练任务」转换工具的**下游消费方**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 出品 | NVIDIA |
| 用途 | RL 终端任务训练 |
| 隔离 | Docker 容器化 |
| 上游工具 | Skill2Env（把 Agent Skill 自动转成 Harbor 任务） |
| 适合 | 终端 Agent RL 训练 / Code Agent 训练 |

## 相关概念

- [Skill2Env](./tool-skill2env.md) — 把任意 Agent Skill 自动转成 Harbor 兼容 RL 任务的上游工具