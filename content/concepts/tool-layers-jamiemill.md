---
type: "Tool"
title: "Layers（Jamie Mill 的设计层次 Skill）"
description: "Jamie Mill 出品的设计 Skill：聚焦「视觉层次 / 信息层级」设计主题，给 Claude / Cursor 等编码 Agent 加载后在 UI 排版时主动拉开层级、避免一锅平铺。"
resource: "http://layers.jamiemill.com"
tags: "[agent-skills, design, ui, typography, hierarchy]"
timestamp: "2026-10-03T00:00:00Z"
---

# Layers

## 它是什么

[Layers](http://layers.jamiemill.com) 是 **Jamie Mill** 出品的设计 Skill——专门训练编码 Agent 在做 UI 时建立**视觉层次 / 信息层级**，避免把字号 / 间距 / 颜色用成「一锅平铺」。

## 为什么用它 / 适合什么场景

- **AI 默认容易「平铺」**：不引导的话，AI 会把每个标题、段落都设成接近的字号，结果页面没有主次。
- **给 Agent 一条「层次优先」的设计守则**：让 Layer 显式拉开主标题 / 副标题 / 正文 / 注释之间的视觉等级。
- **配合其它设计 Skill**：与 hallmark / taste / 0xdesign-plugin 一起装，Agent 既有品味又有层次感。

## 关键能力

| 能力 | 说明 |
|------|------|
| 主题 | 视觉层次（hierarchy） |
| 触发方式 | 编码 Agent 加载 Skill 后自动遵守 |
| 适用 | UI 排版 / Landing / Dashboard / 文档站 |
| 作者 | Jamie Mill |

## 参考链接

- 项目链接：<http://layers.jamiemill.com>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 装载机制本身
- [Hallmark Skill](./tool-hallmark-skill.md) — 同类设计 Skill
- [taste Skill](./tool-taste-skill-redesign.md) — 同类设计品味 Skill
