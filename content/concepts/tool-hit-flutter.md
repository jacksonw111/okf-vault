---
type: Tool
title: "hit"
description: "Flutter 命中区扩展示例库：把控件「画多大」和「能点到多大」拆成两回事，小微控件不用撑大布局也能给足点击区，遵循 Apple HIG / Material 触摸目标 ≥44pt 规范。"
resource: "https://github.com/definev/hit"
tags: [flutter, ux, accessibility, hit-area, mobile-ui, material-design, apple-hig]
timestamp: 2026-08-06T02:30:00Z
---

# hit

## 它是什么

definev 开源的 Flutter 微件 / 模式库，把「视觉尺寸」与「触摸命中区」解耦：图标可以画得很小，但点击热区覆盖到 44pt 起步。

## 为什么用它 / 适合什么场景

- 写 Flutter 表单 / 工具栏 / 列表行，想让小图标也能被手指轻松点中而不撑大布局。
- 排查「点击不灵敏 / 边缘点不到」类用户反馈时拿来对照看是否命中区被裁。
- 想系统化遵循 Apple HIG（≥44pt）与 Material（≥48dp）触摸目标规范。

## 关键能力

| 能力 | 说明 |
|------|------|
| 命中区扩展 | 给任意 Widget 套一个不可见的 HitArea 包装层 |
| 视觉尺寸独立 | 图标 / 文字视觉大小不变，点击区按需放大 |
| 跨平台一致 | iOS / Android 共用同一套语义 |

## 相关概念
- [Number Stepper UX](./note-number-stepper-ux.md) — 长按 + 滚动数字 + 渐变遮罩的步进器动效原则
- [Penpot](./tool-penpot.md) — 开源自托管 Figma 替代，MCP + 实时协作