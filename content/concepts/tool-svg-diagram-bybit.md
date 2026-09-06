---
type: Tool
title: "svg-diagram（Bybit 团队的 Agent SVG 绘图规范 + Linter）"
description: "给 Agent 定一套手写 SVG 图的统一画法，配套零依赖 Linter 验证成品，架构图 / 流程图 / 时序图画出来风格一致。"
resource: "https://github.com/bybit-exchange/svg-diagram"
tags: [svg, diagram, agent-skill, lint, bybit]
timestamp: "2026-09-06T00:00:00Z"
---

# svg-diagram（Bybit 团队的 Agent SVG 绘图规范 + Linter）

## 它是什么

[bybit-exchange/svg-diagram](https://github.com/bybit-exchange/svg-diagram) 是一套**给 Agent 手写 SVG 图的规范 + 零依赖 Linter**：架构图、流程图、时序图都按统一画法画，Linter 负责校验产物是否符合规范，从而让多个 Agent / 多次产出的图风格一致。

定位：

- **风格统一**：Agent 画 SVG 容易每张图风格漂移，svg-diagram 把画法沉淀成可校验的规范。
- **零依赖 Linter**：不引入 Node 工具链或外部服务，纯静态规则校验。

## 为什么用它 / 适合什么场景

- 文档站 / 内部知识库依赖 Agent 产 SVG 图，但图与图之间风格不统一。
- 想给团队立一套「画图规范」，但希望机器可校验而不是靠 code review。
- 不希望引入额外构建 / 服务依赖。

## 关键能力

| 能力 | 说明 |
|------|------|
| 统一画法 | 架构 / 流程 / 时序图都按同一规则画 |
| 零依赖 Linter | 校验成品符合规范，零运行时依赖 |
| 适合 Agent | 直接喂给 Agent 当 Skill |
| 风格一致性 | 多 Agent / 多次产物的视觉风格可控 |

## 相关概念

- [Archify（LLM→JSON→SVG 架构图）](./tool-archify.md) — 同类「Agent 画架构图」思路，Archify 走 JSON→SVG 路径
- [Agent Skills（代理技能包）](./term-agent-skills.md) — svg-diagram 是一种典型的 Skill

## 项目链接

- 项目主页：<https://github.com/bybit-exchange/svg-diagram>
