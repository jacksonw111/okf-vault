---
type: Tool
title: "Hyalite"
description: "纯 CSS + SVG 模拟 Apple 液态玻璃（liquid glass）效果的 Web 引擎，Chromium 可用，其它浏览器退回普通模糊。"
resource: "https://github.com/VII-Cae/hyalite--liquid-glass"
tags: "[css, svg, liquid-glass, web-effects, frontend]"
timestamp: "2026-09-07T13:22:00Z"
---

# Hyalite

## 它是什么
一个纯 CSS + SVG 实现的"液态玻璃"（liquid glass）Web 引擎。所谓 liquid glass 是 Apple 在其系统中推广的视觉效果：背景模糊 + 折射感 + 微高光，让半透明面板看起来像有厚度和弧度的玻璃。Hyalite 在 Web 上用 CSS 与 SVG 模拟这种质感，无需 canvas / WebGL / 大型依赖。

## 适用性
- **Chromium 全功能**：完整液态玻璃效果
- **其它浏览器**：自动降级为普通模糊（不报错、不破图）

## 关键能力
| 能力 | 说明 |
|------|------|
| 纯 CSS + SVG | 不依赖 WebGL / canvas |
| 零依赖 | 一个仓库即用 |
| 浏览器降级 | 非 Chromium 自动回退 |
| Demo 完善 | GitHub Pages 直接看效果 |

## 适用场景
- 网站 Hero 区 / 卡片叠层想要高级感
- 不想引入 Three.js / WebGL 但又想做"玻璃感"前端
- 个人作品集 / 落地页

## 参考
- 仓库：<https://github.com/VII-Cae/hyalite--liquid-glass>
- Demo：<https://vii-cae.github.io/hyalite--liquid-glass/demo/index.html>

## 相关概念
- [liquid-glass](tool-liquid-glass.md) — React 零依赖液态玻璃折射组件
- [Astryx](tool-astryx.md) — Meta 开源设计系统，CSS 变量级换肤