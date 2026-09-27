---
type: "Tool"
title: "Skill2Env（NVIDIA：Agent Skill → Harbor RL 训练任务转换器）"
description: "NVIDIA（NVlabs）开源工具：把任意 Agent Skill（带 SKILL.md 的技能文件夹）自动转成 Harbor 框架下、可在 Docker 里跑起来的强化学习（RL）终端训练任务。"
resource: "https://github.com/NVlabs/Skill2Env"
tags: "[nvidia, agent-skill, harbor, reinforcement-learning, docker, rl-training]"
timestamp: "2026-09-27T21:55:00Z"
---

# Skill2Env（NVIDIA：Agent Skill → Harbor RL 训练任务转换器）

## 它是什么

[Skill2Env](https://github.com/NVlabs/Skill2Env) 是 **NVIDIA（NVlabs）** 放出的开源工具，作用是把**任意 Agent Skill**（带 `SKILL.md` 的技能文件夹）自动转成 **Harbor 框架**下**可在 Docker 里跑起来的 RL 训练任务**。

输入是 Agent Skill 生态的「技能包」（目录 + SKILL.md + 工作流定义），输出是 Harbor 兼容的**终端任务定义**——可以直接扔进 RL 训练流水线。

## 为什么用它 / 适合什么场景

- 想把**现成的 Agent Skill** 作为**RL 训练环境**——不必从零写环境接口。
- 用 Harbor（或类似 RL 框架）训练 Agent，但苦于环境难写。
- 想做**Skill-to-Task** 的自动化——把生态里几千个 Skill 全部变成训练素材。
- 想要**Docker 化**的训练环境（隔离、可复现）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | Agent Skill（SKILL.md 等） |
| 输出 | Harbor 框架兼容的 RL 终端训练任务 |
| 隔离 | Docker 容器化 |
| 出品 | NVIDIA NVlabs |
| 框架 | Harbor（NVIDIA 的 RL 终端任务训练系统） |

## 媒体

- ![](https://pbs.twimg.com/media/HTH6_enaMAANlrt.jpg)

## 相关概念

- [NVIDIA Skills](./tool-nvidia-skills.md) — NVIDIA 官方 Agent Skills 合集（Skill2Env 是其生态的下游训练工具）
- [Harbor](./tool-harbor.md) — NVIDIA RL 终端任务训练框架（视情况补链）