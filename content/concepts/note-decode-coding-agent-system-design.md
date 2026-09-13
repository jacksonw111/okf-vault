---
type: "Note"
title: "Decode（pauliusztin 的 Coding Agent 系统设计）"
description: "pauliusztin 自建 coding agent 的第一手经验总结：core agent loop 只用 20 行 Pydantic AI，真正难的是 harness——上下文压缩 / 工具边界 / 沙箱 / 子代理 / 可观测 / 评估全套。"
resource: "https://www.decodingai.com/p/building-a-coding-agent-from-scratch-system-design"
tags: "[coding-agent, harness, decode, system-design, pydantic-ai]"
timestamp: "2026-09-12T22:55:00Z"
---

# Decode（pauliusztin 的 Coding Agent 系统设计）

## 它是什么

一篇来自 pauliusztin 的**自建 coding agent 系统设计**长文：他从零搭建 **Decode** coding agent，在 Pydantic AI 之上只用 ~20 行就实现核心 loop，**真正的工作量全在 harness 上**。文章把这整套系统设计公开拆解。

## 核心论点

> **LLM 是好 AI agent 里最小的那块。真正的工程在它周围。**

- **核心 agent loop 非常小**：Reason → Act → Observe → Repeat。
- 但 loop 单独跑不出 production-ready agent。还需要控制 6 件事：
  1. 上下文如何到达模型 + 如何压缩
  2. 工具的边界 + 使用方式
  3. 哪些动作能跑、哪些需要审批
  4. 工具在哪里跑 / 记忆怎么持久 / 沙箱与子代理怎么运作
  5. 如何 trace / debug / test / 验证失败与结果
  6. 最终结果如何回传给用户
- 这一切统称 **the harness**。
- LangChain 在 Terminal-Bench 上做过一个实验：**模型固定，只换 harness**，他们的 coding agent 名次从约 30 上升到前 5。

## Decode 的具体架构

| 部件 | 选型 |
|------|------|
| Tool-calling agent | ~20 行 Pydantic AI |
| Observability / tracing | Cometml Opik |
| Open model hosting | Modal |
| Remote sandboxing | Modal |
| Eval harness | zenml Kitaru |

## 为什么读它 / 适合谁

- 想理解「为什么 agent 工程的真正难点在 harness」。
- 想照抄一份 production 编码 agent 的系统设计骨架。
- 想知道模型替换 vs harness 改造哪个 ROI 高。

## 媒体

- ![](https://pbs.twimg.com/media/HR2rqvjaUAAPO5e.jpg)

## 项目链接

- 文章：<https://www.decodingai.com/p/building-a-coding-agent-from-scratch-system-design>

## 相关概念

- [What is an Agent Harness（earendil 入门科普长文）](./note-earendil-agent-harness.md) — harness 概念的科普版
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程化 12 条原则
- [Harness Engineering Guide（生产级实战）](./note-harness-engineering-guide.md) — 同主题的生产级实战指南