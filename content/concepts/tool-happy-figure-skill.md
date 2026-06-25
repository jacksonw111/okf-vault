---
type: Tool
title: "happy-figure-skill"
description: "面向 Claude Code / Codex 的科研绘图提示词生成技能：先读懂科研内容，再按研究领域 × 图类型 × 模型特性路由生成可复制、可校对、可控制的 AI 绘图 prompt。"
resource: "https://github.com/BAIKEMARK/happy-figure-skill"
tags: [agent-skills, claude-code, codex, scientific-plotting, prompt-engineering]
timestamp: "2026-06-25T02:21:00Z"
---

# happy-figure-skill

## 它是什么

一个给 Claude Code / Codex 用的 Skill，专门处理「把科研内容编译成 AI 绘图提示词」这件事。它**自己不画图**，而是先读懂科研内容（论文、图注、开题材料），再根据研究领域、图类型和目标模型的特性，生成能复制、能校对、能控制的 AI 绘图提示词。

## 为什么用它

- 避免「让模型自己画科研图」时的反复试错——把控图的责任**前置到 prompt**。
- 路由而非一刀切：同一段内容，在 Nano Banana、Qwen Image、GPT Image 上可能各有最合适的 prompt。
- 适合科研写作里「流程图、机制图、图形摘要」这类**讲清楚比好看更重要**的图。

## 覆盖范围

| 维度 | 范围 |
|------|------|
| 研究领域 | CS/ML、材料化学、生物医学、地球科学 等 |
| 图类型 | 流程图、机制图、图形摘要 等 7 类 |
| 目标模型 | Nano Banana、Qwen Image、GPT Image 等 |

## 它不是什么

- 不是直接出图的工具（出图仍交给 Nano Banana / Qwen Image / GPT Image 本身）。
- 不是通用 prompt 模板库——专注于「科研语义 → 图语义 → 模型语义」的转译。

## 媒体

![](https://pbs.twimg.com/media/HLjGBR0bQAEgvvQ.jpg)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — 这就是一个 SKILL.md 形态的科研绘图技能
- [GPT Image Skills](./tool-gpt-image-skills.md) — 同类「把配图需求编译为模型 prompt」的合集，可对照看路由粒度差异
- [Light-skills](./tool-light-skills.md) — 科研全流程 Skill，happy-figure-skill 可作为其中「配图」环节的子技能