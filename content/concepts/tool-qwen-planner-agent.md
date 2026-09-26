---
type: "Tool"
title: "Qwen-Planner-Agent（通义实验室：有状态的手机端 Agent 框架 + 规划模型）"
description: "通义实验室 Tongyi-MAI 开源：训练后的规划模型 + 有状态执行框架，让智能体在真实手机环境中完成需工具 / 记忆 / 技能 / 多智能体协作的任务；27B 版本在 MobilePA-Bench 上拿 77.05% 综合分（比基线高 9.83 点）。"
resource: "https://github.com/Tongyi-MAI/Qwen-Planner-Agent"
tags: "[qwen, agent, planner, mobile-agent, tongyi, harness, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# Qwen-Planner-Agent（通义实验室：有状态的手机端 Agent 框架 + 规划模型）

## 它是什么

[Qwen-Planner-Agent](https://github.com/Tongyi-MAI/Qwen-Planner-Agent) 是通义实验室（Tongyi-MAI）开源的 **Agent 系统**——由**训练后的规划模型**与**有状态执行框架（Harness）**组成，让 Agent 在**真实手机环境**中完成需要 **工具 / 长期记忆 / 技能复用 / 子智能体交接 / 失败恢复** 的复杂任务。

## 核心思路

不只是「让模型生成操作步骤」，而是通过 Harness：
- 保存**执行状态**并**核对每一步结果**
- **执行反馈**反过来用于改进**训练数据 / 规划模型 / 运行框架**

## 性能

| 模型 | MobilePA-Bench 综合分 |
|------|------|
| **Qwen-Planner-Agent 27B** | **77.05%** |
| 基线 | 67.22% |

> **每千次任务的输出 token 成本约 2.41 美元**。

## 为什么用它 / 适合什么场景

- 想在**真实手机环境**里跑 Agent（不是模拟器），并要可观测 / 可回放。
- 需要**长期记忆 + 技能复用 + 子智能体交接**的完整 Agent 体系。
- 偏好国产开源模型（Qwen 系列）+ 框架一起开源。
- 研究「**规划模型 + Harness 状态机**」如何迭代共同进化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 规划模型 | Qwen 系列微调过的专用规划模型 |
| Harness | 有状态执行框架（Harness Engineering） |
| 运行环境 | 真实手机环境 |
| 能力 | 工具调用 / 长期记忆 / 技能复用 / 子智能体交接 / 失败恢复 |
| 反馈循环 | 执行反馈 → 训练数据 / 模型 / 框架 三方共进化 |
| 性能 | 27B 在 MobilePA-Bench 77.05% |

## 媒体

- ![](https://pbs.twimg.com/media/HTGXhfybYAAqmL3.jpg)

## 相关概念

- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — 围绕「怎么把 LLM 包成稳定可观测产品」的工程实践
- [LoopX](./tool-loopx.md) — 另一种给长时 Agent 加状态管理中间件的思路
- [CUA-S1-4B-0.2](./tool-cua-s1-4b.md) — 同样做电脑 / 设备操作 Agent 的开源模型