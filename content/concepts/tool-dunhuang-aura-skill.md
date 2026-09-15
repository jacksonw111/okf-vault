---
type: "Tool"
title: "dunhuang-aura-skill（敦煌矿物美学生成技能）"
description: "govin-ai/dunhuang-aura-skill：给 Codex、Claude Code 等 Agent 提供一套可调用的敦煌矿物美学生成规范，按交付物、比例、文字状态和构图模式约束色板材质光线并做质检，直接产出商业主视觉。"
resource: "https://github.com/govin-ai/dunhuang-aura-skill"
tags: "[agent-skills, design, image-generation, brand, visual]"
timestamp: "2026-09-15T06:45:00Z"
---

# dunhuang-aura-skill（敦煌矿物美学生成技能）

## 它是什么

[dunhuang-aura-skill](https://github.com/govin-ai/dunhuang-aura-skill) 是给 AI 编码 / 设计 Agent 用的「**敦煌矿物美学**」生成规范。它把敦煌壁画里**色板、材质、光线**的经验编码成可调用的 Skill，Agent 在生成商业主视觉时可以按规则约束比例、文字状态与构图模式，并自带质检环节。

## 核心约束维度

| 维度 | 作用 |
|------|------|
| 交付物 | 不同载体（海报 / KV / 详情页）使用不同模板 |
| 比例 | 主体 / 留白 / 文字区的几何关系 |
| 文字状态 | 文字密度 / 字号阶梯 / 排版位置 |
| 构图模式 | 主体、辅助元素、留白的结构化模板 |
| 色板 | 矿物色谱限定，避免随手配色 |
| 材质 | 矿物颗粒 / 砂岩质感的笔触规则 |
| 光线 | 光源方向 / 阴影强度的可量化参数 |
| 质检 | 输出前对照规则自检，不达标重做 |

## 为什么用它

- 「**风格化品牌设计**」对生成式 AI 是难点——模型只会画「像敦煌」的画面，但不会守住**配色 / 比例 / 文字**的工程级一致性。
- 把美学规范**编码成 Skill 而非 Prompt**，等于让 Agent 拥有「**风格手册**」——可重复、可校验、可继承。
- 适合做电商大促、文化 IP、节令主视觉这类「**风格即卖点**」的场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 美学规范 Skill | 敦煌矿物美学的结构化表达 |
| 比例约束 | 主体 / 留白 / 文字几何关系 |
| 色板材质规则 | 矿物色谱 + 砂岩质感限定 |
| 光线参数化 | 光源方向 / 阴影强度可量化 |
| 自带质检 | 输出前对照规则自检 |

## 媒体

![](https://pbs.twimg.com/media/HSOLc9eaAAAeGuf.jpg)

## 项目链接

- 仓库：<https://github.com/govin-ai/dunhuang-aura-skill>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 把领域知识注入 Agent 的标准范式
- [LottieFiles Motion Design Skill](tool-lottiefiles-motion-design-skill.md) — 同类「风格 → Skill」思路，专注动效