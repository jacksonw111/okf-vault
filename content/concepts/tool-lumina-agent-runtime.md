---
type: "Tool"
title: "Lumina（端侧 AI Agent 轻量运行时）"
description: "让 App 能在端侧跑可控、可跟踪、能恢复的 AI Agent 的轻量运行时。ReAct 循环 + 工具注册表 + schema 按需加载 + 上下文预算 + 会话快照/恢复 + 钩子护栏 + 可观测性；底层模型 MiniCPM-V 4.6 经 SFT + DPO 微调后 Agent pass@1 从 3/200 涨到 101/200，tool Recall 从 5% 升到 82%。"
resource: "https://github.com/GongShichen/Lumina"
tags: [agent, runtime, on-device, react, sandbox, snapshot]
timestamp: "2026-06-24T15:30:00Z"
---

# Lumina（端侧 AI Agent 轻量运行时）

## 它是什么

[`GongShichen/Lumina`](https://github.com/GongShichen/Lumina) 是一个**端侧 AI Agent 轻量运行时**，让 App 能在用户设备上跑出**可控、可跟踪、能恢复**的 AI Agent。

核心能力：

- **ReAct 循环**调用模型 → 校验执行步骤 → 调度工具
- **工具注册表** + **schema 按需加载**
- **上下文预算管理**（防上下文爆掉）
- **会话快照 / 恢复**（断电 / 崩溃不丢状态）
- **钩子护栏**（每步可拦截 / 限流 / 改写）
- **可观测性**（日志 / 指标 / trace）

底层基模是 [MiniCPM-V 4.6](https://github.com/OpenBMB/MiniCPM-V)，经过 SFT + DPO 微调后，Agent 任务 **pass@1 从 3/200 涨到 101/200**，**tool Recall 从 5% 升到 82%**。

## 为什么用它 / 适合什么场景

- 想做「端侧 AI Agent App」但不想从 0 拼运行时；
- 需要**可恢复**（用户切走 App 再回来 agent 还在原状态）；
- 需要**可观测**（出问题时能溯源到具体哪步 tool call）；
- 对**上下文预算**敏感（不能让 agent 在端侧把内存吃完）；
- 模型推理 + 工具调度都跑在端侧，**零云端依赖**。

## 关键能力

| 能力 | 说明 |
|---|---|
| ReAct 循环 | 模型 → 行动 → 观察 → 反思 |
| 工具注册表 | 动态注册 / 注销 / schema 按需加载 |
| 上下文预算 | 防上下文溢出 / 自动摘要 |
| 会话快照 | 状态序列化 + 恢复 |
| 钩子护栏 | 每步可拦截 / 限流 / 改写 |
| 可观测性 | 日志 / 指标 / trace |
| 端侧推理 | 不依赖云端 LLM |

## 媒体 / 参考链接

![架构示意](https://pbs.twimg.com/media/HLZn73ZbQAAE5Q6.jpg)

- [项目链接](https://github.com/GongShichen/Lumina)

## 相关概念

- [Evano Studio](tool-evano-studio.md) — 基于 Ollama 的本地 AI 桌面工作台，可与本运行时组合
- [本地 AI 桌面工作台](tool-local-ai-workbench.md) — Electron + 模型/Agent/路由三件套的同类工作台
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 概念元定义
- [forkd](tool-forkd.md) — microVM fork 化沙箱，agent 沙箱执行的另一思路
