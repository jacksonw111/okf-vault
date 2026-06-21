---
type: Note
title: "DESIGN.md 最佳实践（101babich 整理）"
description: "把设计系统信息沉淀进单个 DESIGN.md，给 AI 辅助 UI 设计提供上下文。三个核心原则：tokens 是决策、带理由、组件基于 tokens。"
resource: "https://x.com/i/web/status/2067577922890650063"
tags: [design, design-system, ai, methodology, design-resources]
timestamp: 2026-06-19T00:00:00Z
---

# DESIGN.md 最佳实践（101babich 整理）

DESIGN.md 正在成为 AI 辅助 UI 设计时「最有用的文件之一」——它让 AI 真正理解你的设计系统，从而产出「看起来像你自家产品」的 UI。一个好的 DESIGN.md 通常包含 design tokens、品牌风格、颜色规则、字体、间距、组件指引。

![](https://pbs.twimg.com/media/HLGC1GxXIAApmLH.jpg)

## 三个最佳实践

1. **把 tokens 当作「决策」对待**：token 不只是一个变量，它定义的是「这个东西在界面里扮演什么角色」。命名（如 `--color-text-primary` 而非 `--gray-800`）承载语义，AI 才有判断依据。
2. **写理由，不只写样式**：不要只说「这个颜色是什么」，要解释「为什么存在、何时用、何时不用」。这是 AI 能否做出更准设计判断的关键。
3. **组件基于 tokens 构建**：组件应该引用你的 tokens 和设计规则，而不是硬编码色值 / 尺寸。这样 token 一变，所有组件跟着走，AI 重生成时也不会跑偏。

## 适用场景

- 让 Claude / Cursor / Copilot 生成的 UI 直接「长在你的产品上」，不需要来回修正配色字号
- 多人 / 多 agent 协作时统一视觉语言
- 替换底层实现（Tailwind → CSS-in-JS / 原生 CSS）时只改 tokens 不动组件

## 和现有概念的关系

- 与 [Vercel Design System](./tool-vercel-design-system.md) 的实践同源（公开的 design.md 风格页面）
- 与 [transitions.dev](./tool-transitions-dev.md) / [textmotion.dev](./tool-textmotion-dev.md) / [animations.dev/vocabulary](./tool-animations-dev-vocabulary.md) / [index.how/to/articulate](./tool-index-how-articulate.md) 同属「前端 / 设计资源」组，但本条偏方法论而非素材库

## 相关概念

- [Vercel Design System](./tool-vercel-design-system.md) — 公开的 design.md 风格系统页面，是 DESIGN.md 实践的公开样本
- [前端 / 创客 资源合集](./note-front-end-resources.md) — 同一作者群组的设计 / 前端资源合集
- [index.how/to/articulate](./tool-index-how-articulate.md) — 设计与 UI 术语词典，写 DESIGN.md 时可参考术语一致
