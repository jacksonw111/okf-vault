---
type: "Tool"
title: "AWR（Agent Work Runtime）"
description: "为 AI 结对编程场景而设计的工作运行时：把目标、进度与卡点持久化，按任务切片定量喂给智能体，断线重连可继续。"
resource: "https://github.com/originoneai/agent-work-runtime"
tags: "[agent, runtime, coding, pair-programming, stateful]"
timestamp: "2026-09-13T08:12:00Z"
---

# AWR（Agent Work Runtime）

## 它是什么

[originoneai/agent-work-runtime](https://github.com/originoneai/agent-work-runtime) 是一个面向「AI 结对写代码」场景的工作运行时（work runtime）。它解决**每次新开会话都要重翻一遍历史**的痛点：把目标、进度与卡点持久化存储，并按任务切片定量喂给下游智能体，让会话之间不断档。

## 为什么用它 / 适合什么场景

- 多人/多 agent 协作编码时，**上下文跨会话持久化**：无需在新窗口复述背景。
- **任务切片**：把一个工程任务切成可被 LLM 定量消费的小段，避免一次性灌入整个仓库历史。
- **断线续作**：网络掉线、模型超时后回来还能接着干。
- 把「agent 状态 / 计划 / 笔记」从纯 prompt 提升到 runtime 一等公民。

## 关键能力

| 能力 | 说明 |
|------|------|
| 目标持久化 | 把会话目标、约束、进度写进 runtime |
| 任务切片 | 把一个大任务切成 LLM 可消费的定量片段 |
| 卡点记录 | 记录模型卡在何处，避免下次重复踩坑 |
| 续作机制 | 中断后回到原状态继续执行 |
| 上下文定量注入 | 按任务片段定量喂给智能体，减少 token 浪费 |

## 媒体

- ![](https://pbs.twimg.com/media/HR_DNBMbwAAuxuG.jpg)

## 项目链接

- 仓库：<https://github.com/originoneai/agent-work-runtime>