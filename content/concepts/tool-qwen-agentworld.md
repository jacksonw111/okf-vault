---
type: Tool
title: "Qwen-AgentWorld（原生语言世界模型）"
description: "通义千问团队提出的原生语言世界模型（LWM）：覆盖 MCP / 搜索 / 终端 / SWE / Android / Web / OS 七个智能体交互域，CPT → SFT → RL 三阶段训练，基于 1000 万+真实交互轨迹。"
resource: "https://github.com/QwenLM/Qwen-AgentWorld"
tags: [world-model, agent, qwen, lwm, rl, mcp]
timestamp: "2026-06-25T11:45:00Z"
---

# Qwen-AgentWorld（原生语言世界模型）

## 它是什么

通义千问团队提出的**原生语言世界模型（Language World Model, LWM）**。它不依赖传统环境引擎，而是让模型通过**长链推理**直接在七个统一域中模拟智能体环境——包括：

1. **MCP**（工具调用）
2. **搜索**
3. **终端**
4. **SWE**（软件工程）
5. **Android**
6. **Web**
7. **OS**（操作系统）

## 为什么用它 / 适合什么场景

- **训练 agent 的「环境」**：与其搭一个真实沙箱来生成训练数据，不如让模型在脑内模拟。
- **评估 agent**：离线、低成本地跑大量「如果我点 A 会怎样」式的探索。
- **合成数据**：从 1000 万条真实交互轨迹里学「下一状态预测」，可作为后续 agent 训练的高质量数据源。

## 三阶段训练

| 阶段 | 目标 |
|------|------|
| CPT（Continual Pre-Training） | 注入环境知识——让模型「懂」这些域的语义 |
| SFT（Supervised Fine-Tuning） | 激活下一状态预测推理——让模型能脑内推演 |
| RL（Reinforcement Learning） | 提升仿真保真度——推演结果要尽量贴近真实环境响应 |

## 数据规模

基于 **1000 万+条真实交互轨迹**训练——这一规模是该方案能work的关键前提。

## 媒体

![](https://pbs.twimg.com/media/HLn5y2TbQAA1fqE.png)

## 相关概念

- [Fable 5 World Demo](./tool-fable5-world-demo.md) — 同样「在程序化世界里演示 AI 生成」，但 Fable 5 是真实 GPU 世界，Qwen-AgentWorld 是语言内部世界
- [eot-bench](./tool-eot-bench.md) — 用真实人机对话评估 agent；Qwen-AgentWorld 反过来给 agent 合成训练环境
- [Awesome World Action Models](./tool-awesome-world-action-models.md) — 同属世界模型 / 具身智能领域，可对照看「物理世界模型」与「语言世界模型」两条路
- [pi-fusion](./tool-pi-fusion.md) — 多模型并行思路，Qwen-AgentWorld 也可作为其中一个 worker