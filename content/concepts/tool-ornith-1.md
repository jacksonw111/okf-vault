---
type: Tool
title: "Ornith-1"
description: "DeepReinforce 推出的开源编程智能体模型系列，基于 Gemma 4 与 Qwen 3.5 后训练，9B Dense / 35B MoE / 397B MoE 三规格；用强化学习同时优化模型输出的解决方案与驱动方案的 scaffold，多项编码 benchmark 同等规模开源最佳（397B SWE-Bench Verified 82.4%）。"
resource: "https://github.com/deepreinforce-ai/Ornith-1"
tags: "[llm, coding-agent, reinforcement-learning, gemma, qwen, open-source]"
timestamp: "2026-07-02T03:00:00Z"
---

# Ornith-1

## 它是什么
DeepReinforce 推出的**开源编程智能体模型系列**。基于 Gemma 4 与 Qwen 3.5 后训练，分 9B Dense / 35B MoE / 397B MoE 三个规格。训练方式特别：用强化学习**同时优化模型输出的解决方案与驱动方案的 scaffold**，让模型能找到更好的搜索路径。

## 为什么用它 / 适合什么场景
- 想在本地或私有部署跑一个强力的开源编码 Agent 模型。
- 不想付闭源模型 API 费，又想要接近 SOTA 的 SWE-Bench 表现。
- 想用大模型自带的 scaffold（搜索路径 + 工具调用策略），而不是自己拼。
- 研究 RL-trained coding agent 的训练范式。

## 关键能力
| 能力 | 说明 |
|------|------|
| 基础模型 | Gemma 4 + Qwen 3.5（后训练） |
| 规格 | 9B Dense / 35B MoE / 397B MoE |
| 训练方式 | RL 同时优化「解决方案」与「驱动方案的 scaffold」 |
| Benchmark | Terminal-Bench 2.1 / SWE-Bench / NL2Repo 等多项 |
| 性能 | 同等规模下开源最佳；397B SWE-Bench Verified 82.4% |
| 形态 | 开源模型系列 |

## 相关概念
- [DeepSpec](tool-deepspec.md) — DeepSeek 的投机解码框架；Ornith-1 是模型层，DeepSpec 是推理加速层
- [12-Factor Agents](tool-12-factor-agents.md) — Agent 工程原则；Ornith-1 是「scaffold 优化」原则的模型层实现
- [OpenSeek](tool-openseek-moonbit.md) — 编程助手基础库；Ornith-1 是模型本身
- [Qwen-AgentWorld](tool-qwen-agentworld.md) — 通义千问的 Agent 训练；Ornith-1 是另一条 RL 训练路径

## 项目链接
- 项目主页：<https://github.com/deepreinforce-ai/Ornith-1>

## 媒体
![](https://pbs.twimg.com/media/HMG1qyWbMAAFRfk.jpg)