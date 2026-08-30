---
type: "Tool"
title: "Moduix（框架无关的 Ark UI + Tailwind 组件库）"
description: "构建在 Ark UI 之上的组件库：同一套 API 自动适配 React / Vue / Solid / Svelte 等主流框架；样式默认 Tailwind，可被任意主题层替换；专攻「可访问性 + 跨框架一致」。"
resource: "https://moduix.dev/"
tags: [component-library, ark-ui, tailwind, framework-agnostic, accessibility, react, vue, solid, svelte]
timestamp: "2026-08-30T21:50:00Z"
---

# Moduix

## 它是什么
[Moduix](https://moduix.dev/) 是构建在 **[Ark UI](https://ark-ui.com/)** 之上的**框架无关组件库**——同一套组件 API 自动适配 React、Vue、Solid、Svelte 等主流前端框架，样式层默认走 Tailwind，但可以整体替换成自家主题。

设计要点：

- **底层 Ark UI**：负责无障碍、键盘交互、状态机，是 Zag.js 的官方组件层；
- **样式层 Tailwind**：默认主题，但 `class:` 全开放；
- **跨框架同源**：写一次组件，多框架可用——团队不会因为选型差异再 fork 一份。

## 为什么用它 / 适合什么场景
- **设计系统跨框架分发**：同一个公司 / 产品要在 React + Vue / Solid 项目里共用同一套组件；
- **想要 Zag 的可访问性**：Ark UI 已把 ARIA + 焦点管理 + 状态机做透，Moduix 直接拿来用；
- **拒绝「每个框架写一份」**：组件层只写一次，框架只是适配器；
- **想换主题**：默认 Tailwind 漂亮但可整体替换，不绑定设计语言。

## 关键能力

| 能力 | 说明 |
|------|------|
| 框架无关 | 同一 API 适配 React / Vue / Solid / Svelte |
| Ark UI 内核 | 默认拿到 Zag 的可访问性 + 状态机 |
| Tailwind 默认样式 | 但样式层完全可替换 |
| 单一仓库 | 一处开发，多端分发 |

## 相关概念
- [Ark UI](tool-ark-ui.md) — Moduix 直接构建在其上的无障碍组件内核；同一作者生态
- [Tailwind CSS](tool-tailwind-css.md) — Moduix 默认样式栈
- [Componentry](tool-componentry.md) — 另一类「按类别聚合高质量组件」的目录站；Moduix 是「可直接装」的库

## 参考链接
- 项目链接：<https://moduix.dev/>
