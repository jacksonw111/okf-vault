---
type: Tool
title: "ai-website-cloner（给 AI 编码 Agent 用的网站复刻模板）"
description: "一个给 AI 编码 Agent 用的模板 / 工作流：给定线上网站，自动拆成带 TypeScript 类型的 React 组件，再复刻重建。"
resource: "https://github.com/UHolli/ai-website-cloner"
tags: "[ai-coding, react, typescript, website-clone, template, agent]"
timestamp: "2026-07-09T20:50:00Z"
---

# ai-website-cloner（给 AI 编码 Agent 用的网站复刻模板）

## 它是什么
`UHolli/ai-website-cloner` 是一个面向 AI 编码 Agent 的**网站复刻模板/工作流**：给定一个线上网站，自动化流程把页面拆解成带 TypeScript 类型的 React 组件，再在本地重建一遍。

## 为什么用它 / 适合什么场景
- 想**给现有网站做 1:1 复刻**：UI 还原、组件化、可继续迭代。
- 想把 AI 编码 agent 接到结构化的「网站→组件」流程上，避免它随便挑工具拼接。
- 适合：原型设计、UI 借鉴、内部工具迁移、设计稿到代码工作流的起点。
- 对比手写克隆：手动拆组件耗时长 + 类型容易丢；本工具自动化且保留 TS 类型。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自动拆组件 | 给定网址 → 产出 React 组件树 |
| TypeScript 类型 | 组件 props / state 都带类型 |
| 复刻重建 | 在本地工程里重建页面 |
| AI-Agent 模板 | 流程为编码 agent 优化，可直接交给 agent 跑 |

## 相关概念
- [Toolcraft](tool-toolcraft.md) — 创意类应用 starter kit，自带 AGENTS.md 让 agent 直接出视觉工具
- [Componentry](tool-componentry.md) — 组件目录站，按类别聚合高质量交互组件
- [BuilderIO / agent-native](tool-builder-io-agent-native.md) — agent-ready 前端仓库模板

## 参考链接
- 项目链接：<https://github.com/UHolli/ai-website-cloner>
