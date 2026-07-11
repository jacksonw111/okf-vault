---
type: Tool
title: "Apple Design Skill（/apple-design）"
description: "emilkowalski/skills 仓库里的 /apple-design Skill，从 Apple WWDC 视频里提炼 17 条设计与动效原则，用于审查既有作品或在新建项目时一次性做对。"
resource: "https://github.com/emilkowalski/skills"
tags: "[design, skill, wwdc, apple, motion, agent-skills]"
timestamp: "2026-07-11T20:00:00Z"
---

# Apple Design Skill（/apple-design）

## 它是什么

`emilkowalski/skills` 仓库里的 **`/apple-design` Skill**：把 Apple 历届 WWDC 视频里关于设计原则与动效的内容**梳理成 17 条可操作的原则**，打包成 Agent Skills 协议的 Skill 文件。

调用时：

- **审查既有作品**——让 agent 拿这 17 条过一遍当前 UI / 动效，标出偏离点。
- **新建项目时**——让 agent 在动笔前先按这 17 条校准设计语言。

## 为什么用它 / 适合什么场景

- 想给 AI 编码 agent 注入「Apple 级的设计直觉」，而不是让它默认产出 shadcn / Tailwind 默认样式。
- 团队 / 个人做 iOS / macOS / 跨端 UI 时，希望「动效与微交互」一开始就在合格线以上。
- 与 [Hallmark](tool-hallmark-skill.md)（通用设计纪律）形成「通用 + 平台特化」组合。

## 关键能力

| 能力 | 说明 |
|------|------|
| 来源权威 | 直接提炼自 Apple WWDC 官方视频，避免二手解读走样 |
| 17 条原则 | 设计 + 动效各占一定比例，可直接当 checklist 用 |
| Agent Skills 协议 | `npx skills add emilkowalski/skills` 一行装 |
| 双场景 | 既可审查既有作品，也可在新建时一次性做对 |
| 配套生态 | 与同一作者的 [Sonner](tool-sonner-toast.md) / [NumberFlow](tool-number-flow.md) / [Liveline](tool-liveline.md) 形成「设计 + 组件」闭环 |

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — 本概念遵循的协议
- [Hallmark](tool-hallmark-skill.md) — 通用 AI 编码设计 Skill，与 /apple-design 形成「通用 + 平台特化」
- [Vibecoded Design Tells](tool-vibecoded-design-tells.md) — 反面教材：AI 生成网站的设计痕迹排行
- [Vercel Design System](tool-vercel-design-system.md) — vercel.com/design.md 公开设计系统页

## 项目链接

- 项目仓库：<https://github.com/emilkowalski/skills>