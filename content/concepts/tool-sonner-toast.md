---
type: Tool
title: "Sonner（toast 通知组件）"
description: "emilkowalski 写的 React toast 通知组件，以 API 极简、设计精致著称，已被绝大多数现代组件库采纳为默认 toast 实现。"
resource: "https://sonner.emilkowal.ski/"
tags: "[toast, notification, react, ui, library]"
timestamp: "2026-07-11T20:00:00Z"
---

# Sonner（toast 通知组件）

## 它是什么

`emilkowalski/sonner` 是一个**React toast 通知组件**。它的卖点是「API 极简 + 设计精致」——

```jsx
toast.success("保存成功");
```

一行就能弹出一个手感、堆叠、消失动画都做得对的 toast。正因如此，它已经成了 **shadcn/ui 等绝大多数现代组件库的默认 toast 实现**。

## 为什么用它 / 适合什么场景

- 不想自己写 toast 状态机（出现 / 消失 / 堆叠 / 队列）。
- 希望通知样式跟得上当代审美，不希望弹出 2015 年那种「灰底圆角」老 toast。
- 想被组件库生态复用——shadcn 等主流库的官方推荐都是 Sonner。

## 关键能力

| 能力 | 说明 |
|------|------|
| 极简 API | 一行 `toast(msg)` 就能弹 |
| 堆叠管理 | 多条通知自动堆叠 + 错峰消失 |
| 类型丰富 | success / error / loading / promise / 自定义 JSX |
| Promise 集成 | `toast.promise(api.save())` 自动按状态切换文案 |
| 主题 | 浅色 / 深色 / 系统跟随 |
| 设计精致 | 入场 / 出场动画细节到位 |

## 相关概念

- [NumberFlow](tool-number-flow.md) — 同作者生态里的数字滚动组件
- [Liveline](tool-liveline.md) — 同生态里的实时图表组件
- [Apple Design Skill](tool-apple-design-skill.md) — emilkowalski 的 WWDC 提炼设计原则 skill
- [Hallmark](tool-hallmark-skill.md) — 同样走「小而精」路线的 AI 编码设计 skill

## 项目链接

- 项目主页：<https://sonner.emilkowal.ski/>