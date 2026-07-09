---
type: Tool
title: "uikit-expt（pmndrs/uikit + 3D 组件实验）"
description: "基于 pmndrs/uikit 的 3D UI 实现实验项目，把 UI 放进 3D 空间里操控（拖拽 / 缩放 / 透视），作为可参考的 3D 界面实现范式。"
resource: "https://github.com/leweyse/uikit-expt"
tags: "[ui, 3d, uikit, pmndrs, frontend, demo]"
timestamp: "2026-07-09T20:50:00Z"
---

# uikit-expt（pmndrs/uikit + 3D 组件实验）

## 它是什么
`leweyse/uikit-expt` 是一个 UI 实验项目，基于 [`pmndrs/uikit`](https://github.com/pmndrs/uikit)（Poimanders 推出的 React-Three-Fiber UI 工具包）做一个 3D 可操控的界面实现：在 3D 空间里悬浮、缩放、透视化普通 UI 元素，作为「最干净的 3D UI 实现」参考范例。

## 为什么用它 / 适合什么场景
- 想给产品加入**空间化展示**（配置面板、监控仪表盘、3D 资产浏览器）的参考实现。
- 想了解 **uikit 的能力上限**——把传统扁平 UI 嵌入 3D 场景如何避免层级冲突、命中区域错乱、性能下降。
- 适合做演示/灵感项目，对生产环境的 3D UI 工程化有借鉴意义。

## 关键能力
| 能力 | 说明 |
|------|------|
| 3D 可操控 UI | 普通 UI 元素在 3D 场景中可拖拽、缩放、旋转 |
| pmndrs/uikit 底层 | 复用 uikit 的 hit-testing / flex 布局进 3D |
| 透明 + 透视 | 面板可透视看到后面的 3D 内容 |
| 实时交互 | 保持原 2D 交互手感（按钮点击、滚动） |

## 媒体参考

视频：
- <https://video.twimg.com/amplify_video/1910714715271012352/vid/avc1/894x720/D44qw7v7FbPb9al5.mp4?tag=14>

## 相关概念
- [Cloudflare Kumo](tool-kumo.md) — Cloudflare 官方 UI 组件库与文档框架（同样面向 dashboard / 工单 / 监控）
- [Kinetics](tool-kinetics.md) — 99 个开源运动效果动画库，CSS + React + AI Prompt 三种版本
- [Solar Wanderer](tool-solar-wanderer.md) — 浏览器内 NASA JPL 精度的实时太阳系 3D 模拟器

## 参考链接
- 项目链接：<https://github.com/leweyse/uikit-expt>
- 底层 uikit：<https://github.com/pmndrs/uikit>
- 在线预览：<https://uikit-expt.vercel.app>
