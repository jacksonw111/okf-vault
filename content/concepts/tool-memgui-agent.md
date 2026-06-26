---
type: Tool
title: "MemGUI-Agent（移动端 GUI Agent 上下文管理）"
description: "快手开源的移动端 GUI Agent 框架，把上下文管理（ConAct 机制）直接塞进模型输出里，靠折叠历史 / 记住 UI / 保留最近几步缓解长任务上下文膨胀。"
resource: "https://github.com/kwai/MemGUI-Agent"
tags: [ai, agent, gui-agent, mobile, context-management, kwai]
timestamp: 2026-06-26T16:50:00Z
---

# MemGUI-Agent

## 它是什么

MemGUI-Agent 是快手（Kuaishou / kwai）开源的**移动端 GUI Agent** 研究框架。它针对一个非常具体的痛点：手机上的 GUI Agent 一旦做长任务，对话历史和 UI 状态截图会迅速塞满上下文，导致 token 成本飙升、推理质量下降。

它的核心创新叫 **ConAct（Context in Action）**——把上下文管理逻辑**直接编码进模型的输出**里：让模型在每一步动作时同步决定要"折叠哪些历史"、"记住哪些 UI 信息"、"保留最近几步动作"，而**不再依赖外部模块去后处理**砍上下文长度。

## 关键能力

| 能力 | 说明 |
|------|------|
| ConAct 机制 | 上下文管理写进模型动作输出，折叠 / 记忆 / 截断三件套在一次 step 内完成 |
| UI 状态记忆 | 自动保留对当前任务有关键作用的 UI 元素，去掉已结束步骤的冗余视觉信息 |
| 折叠历史 | 把已完成子目标的历史动作压成短摘要而非完整轨迹 |
| 移动场景优化 | 专为手机端长任务设计（不限于手机，也适用于 Web/桌面长链） |
| 框架定位 | 研究型框架，给后续"长任务 Agent"工程化提供可复现基线 |

## 与典型方案的差异

| 维度 | 传统做法 | ConAct（MemGUI-Agent）|
|------|---------|----------------------|
| 上下文管理 | 外部模块后处理 | 模型自己决定 |
| 决策时机 | 推理之后 | 推理之中 |
| 冗余信号 | 全部由工程师调阈值 | 模型学会取舍 |

## 原始链接

- [项目仓库](https://github.com/kwai/MemGUI-Agent)
- [原始推文剪藏](https://x.com/QingQ77/status/2070276349428982141)

## 相关概念

- [Aura-IDE](./tool-aura-ide.md) — 同样在"长编码任务的人类审阅"上做工程取舍，但走 Planner/Worker 拆解而非上下文压缩
- [Lumina（端侧 Agent 运行时）](./tool-lumina-agent-runtime.md) — 通过"上下文预算 + 会话快照"控制长任务显存，与 ConAct 是正交思路
- [EchoesVault（OpenCode 持久记忆插件）](./tool-echoes-vault-opencode.md) — 解决"跨会话记忆连续性"，与 ConAct 解决"单会话内上下文膨胀"互补
