---
type: Tool
title: "sonaui AnimatedDropdown（带 shared layout 指示器的下拉）"
description: "sona UI 组件库中的 AnimatedDropdown 组件：使用 shared layout 指示器实现下拉动画过渡的 React 组件，开箱即用。"
resource: "https://www.sonaui.com/docs/animated-dropdown"
tags: [react, dropdown, animation, shared-layout, sona-ui, component]
timestamp: "2026-09-06T00:00:00Z"
---

# sonaui AnimatedDropdown（带 shared layout 指示器的下拉）

## 它是什么

[sona UI](https://www.sonaui.com) 组件库中的 **AnimatedDropdown 组件**：使用 **shared layout 指示器**（shared layout indicator）实现下拉面板与触发器之间的平滑动画过渡，开箱即用的 React 组件。

定位：

- **单组件 / 动画效果聚焦**：不是整套 UI 库，而是把「下拉打开 / 关闭」这一动作做到漂亮的独立组件。
- **shared layout 思路**：在面板展开过程中，指示器（如箭头 / 高亮条）通过 shared layout 从触发位置平滑过渡到展开位置。

## 为什么用它 / 适合什么场景

- 需要给现有 UI 加上「下拉打开」过渡，但不想引入完整动画库。
- 想要「触发器 → 面板」一致的视觉关系（指示器平滑迁移）。
- 用 React 项目，想找一个轻量、无副作用的现成组件。

## 关键能力

| 能力 | 说明 |
|------|------|
| Shared layout 指示器 | 触发器与面板之间共享 layout 动画 |
| 平滑过渡 | 下拉打开 / 关闭不生硬 |
| React 组件 | 直接 import 使用 |
| 轻量 | 不是完整动画库，按需取用 |
| 可定制 | 支持配置指示器样式、过渡曲线等 |

## 相关概念

- [Ark UI](./tool-ark-ui.md) — headless 行为层（ARIA / 键盘 / 状态机），sonaui AnimatedDropdown 是更「带视觉」的同类下拉组件
- [transitions.dev](./tool-transitions-dev.md) — 网页过渡效果精选，提供 motion 设计灵感

## 项目链接

- 组件文档：<https://www.sonaui.com/docs/animated-dropdown>
