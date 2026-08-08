---
type: "Term"
title: "Story Engine"
description: "以世界线 / 决策卡 / 持久化状态驱动故事的总称：在角色扮演与互动叙事里，用结构化记忆 + 玩家拍板 + 多线存档替代「模型自动念旁白」的旧范式。"
tags: [roleplay, narrative, game-design, agent-architecture]
timestamp: "2026-08-08T20:00:00Z"
---

# Story Engine

## 定义

Story Engine（故事引擎）是把「互动叙事 / 角色扮演」从纯 LLM 念旁白，转向结构化状态驱动的一种总称。它用持久化记忆账本记录关键事实、决策卡让用户在关键节点拍板、世界线存档支持多线对比，让长程剧情可控、可复盘、可分叉。

## 要点

- 核心组件：记忆账本 + 决策卡 + 状态面板 + 多线存档。
- 与传统 LLM 角色扮演的区别：不再「每轮把全部上下文塞给模型」，而是「只把关键事实喂进去」。
- 通常以 Agent 架构组织（导演 / 玩家 / NPC / 记录员等角色分工）。
- 解决 LLM 角色扮演三大老毛病：上下文冗余、剧情不可控、结局同质化。

## 相关概念

- [Liyuan](./tool-liyuan.md) — 用 Story Engine 思想重构 LLM 角色扮演的应用
- [LongHorizon-Harness](./tool-longhorizon-harness.md) — 长程代理脚手架，给 Story Engine 提供底层支撑