---
type: "Tool"
title: "PrismSystem"
description: "appariciojunior 写的「白标」设计系统：克隆下来喂一份品牌输入（颜色 / 字体 / logo / 参考图 / Figma 文件），自动生成全套对得上品牌调的 Web / 移动 / 原生 UI 组件，所有产物从同一套 token 取主题。"
resource: "https://github.com/appariciojunior/PrismSystem"
tags: [design-system, white-label, tokens, figma, ai, branding]
timestamp: "2026-08-09T19:35:00Z"
---

# PrismSystem

## 它是什么

[PrismSystem](https://github.com/appariciojunior/PrismSystem) 是一个「白标（white-label）」设计系统：把整套组件库 clone 下来，喂一份**品牌输入**（颜色、字体、logo、参考图、甚至 Figma 文件），它会基于这些 token **生成全套对得上品牌调**的 Web / 移动 / 原生 UI 组件。所有产物都从同一套 token 取主题，代理生成新组件时「想跑偏都难」。

## 为什么用它 / 适合什么场景

- 同时给多个品牌出 UI，但不想每个品牌维护一套组件库。
- 想用 AI 编程代理批量生成 UI，但担心它生成的组件风格跑偏。
- 做 SaaS 产品时，希望支持「租户换肤」（颜色 + logo + 字体 + 字体授权范围）。
- 想在 Figma 与代码之间建立「token 即真理」的同步通道。

## 关键能力

| 能力 | 说明 |
|------|------|
| Token 驱动 | 颜色 / 字体 / 间距 / 阴影全从 token 派生 |
| 品牌输入 | 颜色 / 字体 / logo / 参考图 / Figma 文件多模态输入 |
| 多端产出 | Web / 移动 / 原生组件统一生成 |
| 代理防跑偏 | AI 生成组件强制走 token，无法绕过 |
| 白标友好 | 适合 SaaS 多租户 / 集团多品牌场景 |

## 媒体

![](https://pbs.twimg.com/media/HPMSpJAasAA9Db9.jpg)

## 相关概念

- [Vercel Design System](./tool-vercel-design-system.md) — vercel.com/design.md 公开的设计系统页
- [Astryx](./tool-astryx.md) — Meta 开源设计系统，CSS 变量级换肤
- [Shadcn themes on 21st.dev](./tool-shadcn-themes-21st.md) — 21st.dev 聚合所有 shadcn 社区主题