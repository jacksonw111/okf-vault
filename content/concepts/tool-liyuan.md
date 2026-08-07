---
type: "Tool"
title: "Liyuan（梨园）"
description: "用 AI Agent 架构重构角色扮演体验的应用：通过记忆账本、决策卡、自建面板与世界线存档，解决传统角色扮演中上下文冗余、剧情不可控、结局单一的问题，每轮省 53%–63% 上下文。"
resource: "https://github.com/weidu12123/Liyuan"
tags: [roleplay, agent-architecture, story-engine, context-optimization, ai-agent]
timestamp: "2026-08-07T14:56:00Z"
---

# Liyuan（梨园）

## 它是什么

Liyuan（梨园）是一款把「角色扮演体验」交给 AI Agent 架构重构的应用。它用记忆账本、决策卡、自建面板与世界线存档四件套，解决传统 LLM 角色扮演里上下文冗余、剧情不可控、结局单一的老毛病，每轮对话能省 53%–63% 上下文，同样的窗口能装下翻倍的剧情。

## 为什么用它 / 适合什么场景

- 用 LLM 跑长程角色扮演，但受困于「聊到一半忘记前情」「剧情全凭模型心情」「结局同质化」。
- 想在关键剧情节点停下来，让用户「拍板」决定走向，而不是被模型自动收尾。
- 想要「装备库 / 地图 / 角色状态」这类可视化面板，且面板随剧情自动更新。
- 希望同一段故事能开多条「世界线」存档，便于复盘与对比。

## 关键能力

| 能力 | 说明 |
|------|------|
| 记忆账本 | 把剧情关键事实记入账本，避免每轮重复喂入上下文 |
| 决策卡 | 关键剧情节点停下，弹决策卡由用户拍板，避免模型擅自收尾 |
| 自建面板 | Agent 自动生成装备库 / SVG 地图等可视化面板，随剧情更新 |
| 世界线存档 | 每条剧情线可独立存档，便于复盘、对比、二次启动 |
| 上下文裁剪 | Harness 层直接裁剪过程性内容，省 53%–63% 上下文 |
| Agent 架构 | 不再是「单 LLM 念旁白」，而是多 Agent 协作推进剧情 |
| 结局多样化 | 多世界线并存，单一结局的同质化被打破 |

## 媒体

- ![Liyuan 决策卡 / 面板示意](https://pbs.twimg.com/media/HPAcqvrbgAAEV9B.jpg)

## 相关概念

- [LongHorizon-Harness](./tool-longhorizon-harness.md) — 长程代理脚手架，把记忆 / 工具 / 技能 / 评测做成一整套，本工具借用其长程优化思想
- [Story Engine](./term-story-engine.md) — 「以世界线 / 决策卡驱动故事」的总称
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程化原则，可指导本工具的架构取舍