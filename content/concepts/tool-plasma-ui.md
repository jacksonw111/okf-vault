---
type: "Tool"
title: "Plasma UI（React 液态玻璃面板组件库）"
description: "React 面板组件库，用 WebGL canvas 渲染液态玻璃材质，视觉参考 Apple Liquid Glass。面板带表面张力，靠近时融合成一体；透过面板看到的内容会被折射；拖动结束后按 24px 网格吸附。"
resource: "https://github.com/CruxGarden/plasma-ui"
tags: "[react, webgl, liquid-glass, ui, panel, apple, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# Plasma UI（React 液态玻璃面板组件库）

## 它是什么

[Plasma UI](https://github.com/CruxGarden/plasma-ui) 是一个 React 面板组件库：用 WebGL canvas 渲染液态玻璃（Liquid Glass）材质，视觉参考 Apple 的 Liquid Glass 设计语言。面板带表面张力、靠近融合、内容折射、拖动结束后按 24px 网格吸附。

## 关键能力

| 能力 | 说明 |
|------|------|
| WebGL canvas 渲染 | 不靠 CSS hack 实现液态玻璃 |
| 表面张力 | 面板靠近时融合成一体 |
| 内容折射 | 透过面板看到的内容会被折射 |
| 24px 网格吸附 | 拖动结束后按 24px 网格 snap |
| Apple Liquid Glass 风格 | 视觉语言参考 Apple |

## 适用场景

- React 项目想要 Apple Liquid Glass 风格的「会呼吸」面板
- 数据可视化 / 设计工具 / 创意工具的浮动面板
- 想用 WebGL 而不是 CSS 实现液态玻璃质感

## 注意点

- WebGL 渲染依赖 GPU，移动端 / 低功耗设备需评估性能
- 视觉风格主观，喜欢 Apple 风格的人会很喜欢，其他人可能觉得过于炫技

## 原始链接
- 项目主页：<https://github.com/CruxGarden/plasma-ui>

## 相关概念
- [Liquid Glass](./tool-liquid-glass.md) — Apple Liquid Glass 设计语言本身