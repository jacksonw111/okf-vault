---
type: "Tool"
title: "Hairline（等距线框动画组件库）"
description: "Lucas Marques 写的 TypeScript 库——19 个等距线框图形做成能直接挂到 DOM 上的组件和函数，**全靠指针驱动**（柱子抬升 / 卡片弹起 / 保险柜转盘转起来 / 传送带减速），不拉任何依赖；适合给页面加「跟鼠标走的线框动画」又不想引入 3D 渲染栈。"
resource: "https://github.com/lucasmarkes/hairline"
tags: "[animation, isometric, line-art, web, ui]"
timestamp: "2026-10-06T22:51:00Z"
---

# Hairline（等距线框动画组件库）

## 它是什么

**Hairline** 是 Lucas Marques 写的 TypeScript 库——把 19 个**等距线框（isometric line-art）**图形做成能直接挂到 DOM 上的组件和函数，**全靠指针驱动**：柱子抬升、卡片弹起、保险柜转盘转起来、传送带减速。装完不拉任何依赖，纯函数 + DOM。

## 为什么用它 / 适合什么场景

- **零 3D 依赖**：用 SVG / Canvas 2D 画等距线框，避开 three.js 栈
- **指针驱动**：鼠标移动时图形响应，无需写交互代码
- **轻量**：~20 KB，零依赖，可塞任何页面
- **现代 UI 装饰**：登录页 / 落地页 / 产品介绍页的等距线框装饰

## 关键能力

| 能力 | 说明 |
|------|------|
| 19 个图形 | 等距盒子 / 卡片 / 保险柜 / 传送带等 |
| 指针驱动 | 鼠标 hover/move 触发形变 / 动画 |
| 零依赖 | 纯 TypeScript + DOM |
| 组件 + 函数 | 既可作为 React 组件，也可作纯函数调用 |
| 轻量 | ~20 KB |

## 参考链接

- 项目链接：<https://github.com/lucasmarkes/hairline>

## 相关概念

- [Hairline UI Microinteractions](./tool-hairline-ui.md) — 同主题相关
- [Dioramas](./tool-dioramas.md) — three.js 版的 3D 落地页套件
