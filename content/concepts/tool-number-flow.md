---
type: Tool
title: "NumberFlow（数字滚动动画组件）"
description: "Barvian 开发的丝滑数字动画 React 组件，专为价格 / 计数器 / 数值变化场景设计，通过逐字符滚动 + 弹簧曲线让数字变化感觉自然流畅。"
resource: "https://number-flow.barvian.me/"
tags: "[animation, react, number, ui, library]"
timestamp: "2026-07-11T20:00:00Z"
---

# NumberFlow（数字滚动动画组件）

## 它是什么

`barvian/number-flow` 是一个面向 React 的**数字滚动动画组件**。当页面里的数字（价格、计数器、库存、积分、温度等）从旧值变到新值时，NumberFlow 会以**逐字符滚动** + 弹簧曲线的方式过渡，而不是瞬切，看起来既自然又克制。

## 为什么用它 / 适合什么场景

- 数字频繁跳动的页面（行情报价、库存计数器、计时器、得分板）。
- 想要「价格变化有手感」但不想自己写插值动画。
- 不想引一整套动效库——只想解决「数字变化」这一个点。

## 关键能力

| 能力 | 说明 |
|------|------|
| 逐字符滚动 | 多位数同时变化，每位各自滚动而非整体淡入淡出 |
| 弹簧曲线 | 数值不是线性变到终点，而是带轻微回弹，触感真实 |
| 轻量 | 只解决「数字变化」这一件事，包体很小 |
| React 友好 | 标准 React 组件，TS 类型齐全 |
| 无障碍 | `aria-live` 处理好屏幕阅读器可读性 |

## 相关概念

- [Kinetics](tool-kinetics.md) — 99 个开源运动效果动画库（含 CSS + React + Prompt 三版本）
- [Sonner](tool-sonner-toast.md) — 同作者生态里同样走「小而精」路线的 toast 组件

## 项目链接

- 项目主页：<https://number-flow.barvian.me/>