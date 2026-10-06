---
type: "Tool"
title: "shadcn/ui"
description: "由 shadcn 出品的「可复制粘贴组件」风格 UI 库——不通过 npm 安装，而是用 CLI 把组件源码（Radix UI + Tailwind CSS）拷到你的项目里，让你完全拥有组件代码并自由改；是当下 React 生态最主流的 UI 起点。"
resource: "https://ui.shadcn.com"
tags: "[shadcn, ui, react, tailwind, radix, components]"
timestamp: "2026-10-06T22:51:00Z"
---

# shadcn/ui

## 定义

**shadcn/ui**（又名 shadcn UI）是 shadcn 出品的「**可复制粘贴组件**」风格 UI 库——**不是通过 npm 安装**，而是用 CLI（`npx shadcn@latest add <component>`）把组件源码（基于 Radix UI 行为 + Tailwind CSS 样式）拷到你自己项目的 `components/ui/` 下，让你**完全拥有组件代码**并自由修改。是当下 React 生态最主流的 UI 起点，被 Vercel / Linear / Cal.com / OpenAI 等团队广泛采用。

## 要点

- **官网**：[ui.shadcn.com](https://ui.shadcn.com)
- **形态**：CLI + 组件源码；常驻项目仓库
- **底层依赖**：Radix UI（行为层）+ Tailwind CSS（样式）+ Lucide 图标
- **生态**：
  - **shadcn/ui 主库**：60+ 基础组件
  - **shadcn 衍生**：[`tool-hextaui`](tool-hextaui.md) / Spectrum UI / Cult UI 等同风第三方组件
  - **shadcn 复刻到其他形态**：[`tool-shadercn`](tool-shadercn.md)（Shader 版）
- **典型场景**：现代 React 项目 UI 起点；新组件库默认参考实现

## 相关概念

- [HextaUI](./tool-hextaui.md) — 同 shadcn 风第三方组件库
- [HextaUI Blocks](./tool-hextaui-blocks.md) — HextaUI v3 引入的区块合集
