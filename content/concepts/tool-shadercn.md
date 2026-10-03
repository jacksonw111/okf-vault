---
type: "Tool"
title: "ShaderCN（shadcn 风格的 Shader 组件库）"
description: "把 shadcn/ui「源码即组件 / 可改可持」模式复刻到 Shader 领域：把常用 WebGL / GLSL 着色器（背景 / 过渡 / 卡片质感）做成可复制源码的组件，按 shadcn 流程装到 React 项目。"
resource: "https://www.shadercn.run/"
tags: "[shader, webgl, glsl, shadcn, react, components, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# ShaderCN

## 它是什么

[ShaderCN](https://www.shadercn.run/) 把 **shadcn/ui** 的「源码即组件 / 可改可持」模式复刻到 **Shader（着色器）** 领域——把常用 WebGL / GLSL 着色器（背景 / 过渡 / 卡片质感 / 渐变动画等）做成可复制源码的组件，按 shadcn 的流程装到 React 项目。

## 为什么用它 / 适合什么场景

- **不必从零写 GLSL**：背景流动、卡片光效、按钮流光这些效果都要写 shader，ShaderCN 帮你起手。
- **可改源码**：shader 包不好定制，源码即组件就能想改哪改哪。
- **典型场景**：SaaS Landing / 创意类官网 / 活动页 / 交互装置。

## 关键能力

| 能力 | 说明 |
|------|------|
| 交付方式 | 源码复制（shadcn 风格） |
| 适用栈 | React + WebGL / GLSL |
| 覆盖范围 | 背景 / 过渡 / 卡片质感 等常用 shader |
| 自由度 | 与 shadcn 一样，组件不满意直接改 |

## 参考链接

- 项目链接：<https://www.shadercn.run/>

## 相关概念

- [RTEcn](./tool-rtecn-space.md) — 同类「shadcn 模式复刻到 RTE」思路
- [Arc Library](./tool-arc-library.md) — 同类源码化组件库
