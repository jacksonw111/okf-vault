---
type: Tool
title: "Penpot"
description: "开源的可自托管设计平台，Figma 的开源替代品。所有设计元素用 SVG/CSS/HTML 开放标准表达，开发者可以直接看代码做对接；支持实时协作 / CSS Grid / 设计令牌 / 组件系统，并提供 MCP 服务器与开放 API。"
tags: "[design, figma-alternative, open-source, svg]"
timestamp: "2026-07-01T06:00:00Z"
resource: "https://github.com/penpot/penpot"
---

# Penpot

## 它是什么
开源的可自托管设计平台，被视为 Figma 的最强开源替代品。所有设计元素（图形 / 文字 / 布局）都用 SVG / CSS / HTML 这类开放标准来表达，而不是 Figma 那样的私有格式。开发者可以直接看代码做对接，不再「猜标注」。

## 为什么用它 / 适合什么场景
- 想自托管设计工具并保留数据所有权
- 设计师交付后开发者想直接复制 SVG 代码而不是「导出 PNG」
- 团队不愿为 Figma 付费
- 想把设计稿喂给 AI Agent（开放代码 + MCP 让 Agent 可读可改）
- 注重数据合规与隐私（自托管）

## 关键能力
| 能力 | 说明 |
|------|------|
| 开放标准 | 设计元素全部用 SVG/CSS/HTML 表达 |
| 自托管 | Docker 一键起，数据完全在自己服务器 |
| 实时协作 | 多人同时编辑（类似 Figma） |
| CSS Grid 布局 | 直接用 CSS Grid 而非私有布局 |
| 设计令牌 | Design Tokens 一处定义全局生效 |
| 组件系统 | 组件 + 实例 + 变体支持 |
| MCP 服务器 | 提供 MCP 接入，AI Agent 可读写设计稿 |
| 开放 API | REST + WebSocket 全开放 |
| 浏览器原生 | 不需装客户端，浏览器即开即用 |

## 与 Figma 的对比优势
| 维度 | Penpot | Figma |
|------|--------|-------|
| 授权 | 开源 / 自托管 | 闭源 SaaS |
| 数据所有权 | 自己服务器 | Figma 服务器 |
| 文件格式 | SVG/CSS/HTML 开放 | 私有 |
| 价格 | 免费 | 团队版按席付费 |
| MCP / AI 友好 | ✅ MCP + 开放 API | 部分 |

## 相关概念
- [Vercel Design System](tool-vercel-design-system.md) — 同样强调把设计系统装进代码（.md / tokens）让 AI 可读
- [DESIGN.md 最佳实践](note-design-md-best-practices.md) — 把设计系统装进 .md 喂给 AI 的三原则
- [Hyperagent 设计网格 Skill](tool-hyperagent-design-skill.md) — 用 Müller-Brockmann 网格做设计，可与 Penpot 网格系统配合
- [shadcn themes on 21st.dev](tool-shadcn-themes-21st.md) — shadcn 主题聚合站，主题颜色可在 Penpot 里复刻为 Design Tokens

## 原始链接
- [项目仓库](https://github.com/penpot/penpot)
- [截图](https://pbs.twimg.com/media/HMERJhAWcAAhwk7.jpg)