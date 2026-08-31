---
type: "Tool"
title: "Tailwind CSS"
description: "Utility-first 的 CSS 框架——直接在 HTML/JSX 写原子类（class=\"flex p-4 bg-blue-500\"），由构建时工具生成最终 CSS；放弃自定义样式表，拥抱组合式 utility 类。"
resource: "https://tailwindcss.com/"
tags: [css, framework, utility-first, frontend, design-system]
timestamp: "2026-08-31T23:10:00Z"
---

# Tailwind CSS

## 它是什么

[Tailwind CSS](https://tailwindcss.com/) 是由 **Tailwind Labs**（同团队维护 Heroicons / Headless UI）开发的 **utility-first CSS 框架**。核心理念：不写自定义 CSS，而是在 HTML/JSX 上直接组合原子类（`flex`、`p-4`、`bg-blue-500`、`hover:underline`），由构建时工具扫描源文件、按需生成最终 CSS。

与 Bootstrap / Material UI 这类「语义化组件库」相反，Tailwind 把**视觉控制权完全交回开发者**——不预设组件外观，只提供原子工具。

## 为什么用它 / 适合什么场景

- **设计系统统一**：原子类让全站间距 / 配色 / 字号一致，避免「每个开发者各写一套 CSS」的漂移；
- **零运行时**：CSS 在构建期生成，浏览器只需加载一份轻量 stylesheet；
- **设计 token 化**：通过 `tailwind.config.js` 把品牌色 / 字号 / 断点集中为 token，与 Figma 设计稿对齐；
- **与组件库互补**：shadcn/ui、Ark UI、Moduix 等组件库都默认走 Tailwind 作为样式层。

## 关键能力

| 能力 | 说明 |
|------|------|
| Utility 类 | `flex`、`grid`、`p-4`、`text-lg` 等数千个原子类 |
| 响应式前缀 | `sm:` / `md:` / `lg:` 断点前缀做响应式 |
| 状态前缀 | `hover:` / `focus:` / `dark:` 等变体修饰 |
| 配置驱动 | `tailwind.config.js` 集中管理 token / theme / plugin |
| JIT 引擎 | 仅扫描到的类才会进入最终 CSS，体积小 |
| 生态 | shadcn/ui、Headless UI、Heroicons 等同团队 / 同生态 |

## 相关概念

- [Moduix](tool-moduix.md) — 默认以 Tailwind 作为样式层的框架无关组件库
- [Biome](tool-biome.md) — 内置 `useSortedClasses` 规则自动整理 Tailwind 类顺序

## 参考链接

- 项目链接：<https://tailwindcss.com/>