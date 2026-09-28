---
type: "Tool"
title: "jev-dsh-decision（Jev 决策插件挂到 DSH）"
description: "Devin-AXIS 出品：动手前先过一遍该用哪个工具、哪个 Skill、这活该交给谁。插件把 TypeSafe 的 Jev 决策模型挂到 Harness 上，顺便按给定标准给产出打分。"
resource: "https://github.com/Devin-AXIS/jev-dsh-decision"
tags: "[jev, dsh, deepseek-harness, type-safe-decision, plugin, scoring]"
timestamp: "2026-09-28T23:50:00Z"
---

# jev-dsh-decision（Jev 决策插件挂到 DSH）

## 它是什么

[jev-dsh-decision](https://github.com/Devin-AXIS/jev-dsh-decision) 是 Devin-AXIS 出品的 **DSH 插件**：把 **TypeSafe 的 Jev 决策模型**挂到 **DeepSeek Harness** 上。

核心动作：动手前**先过一遍**「该用哪个工具、哪个 Skill、这活该交给谁」；同时**按给定标准给产出打分**。

## 为什么用它 / 适合什么场景

- 想让 DSH 在动手前先**判定任务归属**——工具 / Skill / 谁。
- 想用 **TypeSafe Jev** 作为系统一的快速判定层，减少 LLM 浪费。
- 想给 DSH 的产出**加一道评分闸门**——按事先定义的标准做质量把关。
- 已在用 Jev / Laya 决策模型家族（参考 [term-jev](./term-jev.md)）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | DSH 插件 |
| 决策模型 | TypeSafe Jev |
| 触发时机 | 任务动手前 |
| 输出 | 决策（用哪个工具 / Skill / 谁）+ 评分 |
| 出品 | Devin-AXIS |

## 媒体

- ![](https://pbs.twimg.com/media/HTSEACibIAAmruX.jpg)

## 相关概念

- [JEV（TypeSafe 判定模型家族）](./term-jev.md) — 决策引擎的核心家族
- [DeepSeek Harness](./term-deepseek-harness.md) — 挂载目标
- [jevrev](./tool-jevrev.md) — 另一个「LLM + Jev 决策回路」项目（每轮生成后用 Jev 审计证据）