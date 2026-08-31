---
type: "Tool"
title: "Ark UI"
description: "由 Zag.js 团队打造的无障碍组件「行为层」——处理 ARIA、键盘交互、焦点管理与状态机；样式中立，可与任意 CSS 方案（Tailwind / CSS-in-JS / vanilla）组合。"
resource: "https://ark-ui.com/"
tags: [component-library, headless, accessibility, zag-js, react, vue, solid, svelte]
timestamp: "2026-08-31T23:10:00Z"
---

# Ark UI

## 它是什么

[Ark UI](https://ark-ui.com/) 是由 **[Zag.js](https://zagjs.com/)** 团队（同一作者：Segun Adebayo）开发的**无障碍组件「行为层」**——只关心 ARIA、键盘交互、焦点管理、状态机等「无障碍 + 交互逻辑」，样式完全中立，可与 Tailwind / CSS-in-JS / vanilla CSS 任意组合。

可以理解为：**Radix UI（行为层）+ shadcn/ui 的样式灵活度**，且原生支持 React、Vue、Solid 三套框架。

## 为什么用它 / 适合什么场景

- **想要 Radix 级别的可访问性，但不锁定其样式哲学**；
- **跨框架项目**：同一份状态机源码适配 React / Vue / Solid，避免「每个框架 fork 一份」；
- **设计系统骨架**：把样式交给自家主题层，行为交给 Ark UI，分工清晰；
- **不想引入整个 Material UI / Chakra**：Ark UI 只给行为，体积可控。

## 关键能力

| 能力 | 说明 |
|------|------|
| Headless | 不带样式，纯行为层 |
| 跨框架 | React / Vue / Solid 一套状态机适配 |
| Zag.js 内核 | 状态机驱动交互，可被外部触发 |
| ARIA 完整 | 自动处理焦点陷阱、键盘导航、屏幕阅读器语义 |
| 类型友好 | TypeScript 优先 |

## 相关概念

- [Moduix](tool-moduix.md) — 直接构建在 Ark UI 之上的框架无关组件库
- [Tailwind CSS](tool-tailwind-css.md) — 常与 Ark UI 组合作为样式层

## 参考链接

- 项目链接：<https://ark-ui.com/>