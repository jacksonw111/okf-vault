---
type: "Tool"
title: "Thinking Orbs（AI / Agent 界面用 React 思考球）"
description: "Jakubantalik/thinking-orbs，给 AI 和 Agent 界面用的「思考球」加载动画 React 组件：六种动画状态、两种尺寸，纯 2D Canvas 绘制，自动适配暗 / 亮主题。"
resource: "https://github.com/Jakubantalik/thinking-orbs"
tags: "[react, ui, loading, animation, ai-interface, agent-ui]"
timestamp: "2026-07-23T08:48:00Z"
---

# Thinking Orbs（AI / Agent 界面用 React 思考球）

## 它是什么

[`Jakubantalik/thinking-orbs`](https://github.com/Jakubantalik/thinking-orbs) 是一个**专门给 AI / Agent 界面用的 React 加载动画组件**——以「思考球（thinking orb）」为视觉主体，传达「AI 正在思考」的状态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 六种动画状态 | 思考 / 等待 / 回复 / 错误 / 完成 / 待确认等 |
| 两种尺寸 | 默认 / 小尺寸，适配不同 UI 密度 |
| 纯 2D Canvas | 不依赖 WebGL / SVG，渲染开销低 |
| 自动暗 / 亮主题 | 跟随系统主题自动切换 |

## 为什么用它

- **专门为 AI 设计**：不像通用 spinner，视觉语义直接表达「AI 思考中」
- **轻量**：纯 Canvas，性能开销低
- **可定制状态**：六种状态覆盖 Agent 全生命周期
- **暗 / 亮主题**：开箱即用

## 适用场景

- AI 聊天界面的「正在思考」loading
- Agent Dashboard 的任务状态指示
- 多 Agent 系统的「哪个 Agent 在跑」标记
- AI IDE 内联等待指示

## 相关概念

- [Number Flow](./tool-number-flow.md) — React 数字滚动组件，适合 AI 用量 / 价格变化场景
- [Liveline](./tool-liveline.md) — React 实时折线图，适合 AI 进度可视化
- [Sonner Toast](./tool-sonner-toast.md) — shadcn 默认的 React toast

## 原始链接

- [项目仓库](https://github.com/Jakubantalik/thinking-orbs)