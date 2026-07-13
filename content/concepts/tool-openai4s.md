---
type: Tool
title: "OpenAI4S"
description: "开源的\"代码即动作\"科研智能体：用持久化内核运行真正的 Python/R 代码（不是固定工具表），让研究者用便宜模型（如豆包 ¥9.9/月）就能复现 Claude Science 级别的科研自动化。"
tags: "[research-agent, code-as-action, python, r, open-source, science, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/PKU-YuanGroup/OpenAI4S"
---

# OpenAI4S

开源的**"代码即动作"科研智能体**——为科研场景设计，**用持久化内核运行真正的 Python / R 代码**（不是死板的固定工具表），目标是用**便宜模型**（如豆包 ¥9.9/月档）就能复现 **Claude Science** 级别的科研自动化能力。

## 它是什么

- 一个**科研向 AI agent 框架**；
- 核心理念是 **"code as action"**：agent 不调用预设的 search/calc 工具，而是**真去写并执行 Python/R 代码**——能 import 任何库、做任意计算；
- 用**持久化内核**（Jupyter-style 风格）维持变量、状态、文件句柄，跨步骤共享；
- 模型层不挑食：能跑小模型，配合持久内核 + 真实代码执行也能扛住科研任务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 持久化内核 | 跨步骤保留变量/数据/中间结果，类 Jupyter 体验 |
| 真实代码执行 | 跑真正的 Python / R，而不是模拟工具调用 |
| 科研工具链 | 直接 import numpy / pandas / scipy / scikit-learn / Bioconductor 等 |
| 模型无关 | 兼容便宜模型（豆包 ¥9.9/月），不必依赖昂贵旗舰模型 |
| 开源 | 可自部署、可改造、可科研复用 |

## 为什么用它 / 适合什么场景

- 科研**数据探索 / 复现实验**链路需要真跑代码（不是假装跑了）；
- 不想被"固定工具表"框死——agent 需要自由组合 numpy、sklearn、statsmodels 干脏活；
- 团队 / 实验室**预算敏感**，希望用便宜模型做出昂贵模型水准的科研自动化；
- 想做"**让 AI 自己写代码、改代码、再跑**"这种迭代式科研工作流。

## "代码即动作" vs 固定工具表

| 维度 | 固定工具表（传统） | 代码即动作（OpenAI4S） |
|------|--------------------|------------------------|
| 能力边界 | 框架预设的工具集 | 任何 Python/R 包 |
| 灵活性 | 中 | 极高 |
| 调试 | 看工具调用日志 | 看真实代码 + 输出 + 报错栈 |
| 模型要求 | 通常需要旗舰模型 | 便宜模型即可 |
| 适合 | 简单数据查询 | 真实科研流程 |

## 预览

![](https://pbs.twimg.com/media/HM_EU7XbMAAe5sT.jpg)

## 相关概念

- [Claude Code](tool-claude-code.md) — 同样以"agent 真实执行命令"为核心的工程 agent；可作为"科研 vs 工程"对照
- [12-Factor Agents](tool-12-factor-agents.md) — 同样强调"agent 状态外置、可观测"的工程原则
