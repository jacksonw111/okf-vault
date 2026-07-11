---
type: Tool
title: "Liveline（实时图表组件）"
description: "Benji 维护的实时折线 / 曲线图表 React 组件，专为展示持续变化的数据（股价、心率、CPU 负载、计数器等）设计，无需手动重算坐标轴即可丝滑滚动。"
resource: "https://benji.org/liveline"
tags: "[chart, react, realtime, visualization, library]"
timestamp: "2026-07-11T20:00:00Z"
---

# Liveline（实时图表组件）

## 它是什么

`benji/liveline` 是一个面向 React 的**实时折线图组件**。它专注于「数据点持续往后追加」这一种最常见的图表场景——股票 / 心率 / CPU 负载 / 计数器 / 进度等——把「自动滚动到最新 + 平滑过渡 + 不闪屏」三件事做得开箱即用。

## 为什么用它 / 适合什么场景

- 需要给监控面板 / 数据大屏加一个「持续在动」的曲线。
- 不想为实时图表引入 ECharts / Chart.js 这种大库——Liveline 只做一件事。
- 想要动画「丝滑」而不是「跳变」，但又不想自己写插值。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时追加 | 数据点持续往右追加，曲线自动滚动，无需重算坐标 |
| 丝滑过渡 | 新点入场有动画，不是硬切 |
| 体积小 | 只解决「实时折线」一个场景，依赖少 |
| React / TS | 标准组件，TypeScript 类型齐全 |
| 可主题化 | 颜色 / 线宽 / 间距都可定制 |

## 相关概念

- [NumberFlow](tool-number-flow.md) — 同作者生态里的数字滚动组件，常配合 Liveline 做「数 + 曲线」组合
- [Sonner](tool-sonner-toast.md) — 同生态里的 toast 组件
- [transitions.dev](tool-transitions-dev.md) — 网页过渡效果精选，Liveline 是「数据流」维度

## 项目链接

- 项目主页：<https://benji.org/liveline>