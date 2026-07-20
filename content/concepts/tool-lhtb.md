---
type: "Tool"
title: "LHTB（Agent 长任务基准测试）"
description: "测 AI Agent 能不能「长时间干活」的基准：给 46 个要在终端里跑几百步的任务，看它在带状态环境里持续做出有用成果，且用隐藏验证器打分，不让 agent 自己报进度糊弄。"
resource: "https://github.com/zli12321/LHTB"
tags: "[benchmark, agent, long-horizon, evaluation, terminal]"
timestamp: "2026-07-20T20:20:00Z"
---

# LHTB（Agent 长任务基准测试）

## 它是什么

[zli12321/LHTB](https://github.com/zli12321/LHTB)（**L**ong-**H**orizon **T**erminal **B**enchmark）是专门评估 AI Agent「**长时间执行能力**」的基准：传统 SWE-bench / HumanEval 都是几分钟到几十分钟任务，而 LHTB 给出 **46 个在终端里要跑几百步的任务**，专门考察 agent 在「带状态、长链路、有中间依赖」的环境下能不能持续做出有用成果。

## 关键能力

| 能力 | 说明 |
|------|------|
| 46 条任务 | 每条任务在终端跑几百步 |
| 带状态环境 | 模拟真实环境状态依赖 |
| 隐藏验证器 | 隐藏单元测试，对最终状态打分，agent 看不到 |
| 防止糊弄 | 阻止 agent 用「汇报伪进度」糊弄评分 |

![LHTB 截图](https://pbs.twimg.com/media/HNhSa1naEAAZlLn.jpg)

## 相关概念

- [Awesome Scientific LLM Benchmarks](./tool-awesome-scientific-llm-benchmarks.md) — 覆盖数学 / 物理 / 化学 / 生物 / 智能体科学的精选清单
- [ReactBench](./tool-react-bench.md) — 编码 Agent 用的 React 实战评测

## 参考链接

- 项目链接: <https://github.com/zli12321/LHTB>
