---
type: "Tool"
title: "Agent Skills（Addy Osmani Microsoft Build 现场分享的 Skills 集合）"
description: "Addy Osmani 在 Microsoft Build 现场分享的开源 Agent Skills 项目：用 Define → Plan → Build → Verify → Review → Ship 六阶段方法，45 分钟把「习惯追踪应用」从一句话想法做到浏览器验证、代码评审和重构。"
resource: "https://x.com/i/article/2099656487400542208"
tags: "[agent-skills, microsoft-build, addy-osmani, workflow, methodology]"
timestamp: "2026-09-15T03:10:00Z"
---

# Agent Skills（Addy Osmani Microsoft Build 现场分享的 Skills 集合）

## 它是什么

Microsoft Build 现场，Addy Osmani 演示了一套**开源 Agent Skills 项目**：用 **6 阶段工作流**（Define → Plan → Build → Verify → Review → Ship），**45 分钟**把「**习惯追踪应用**」从一句话想法做到**浏览器验证、代码评审、重构**的完整流程。

## 六阶段方法

| 阶段 | 作用 |
|------|------|
| **Define** | 需求澄清：从一句话想法到明确范围 |
| **Plan** | 任务规划：拆解为可执行的子任务 |
| **Build** | 实现：Agent 写代码 |
| **Verify** | 验证：在浏览器里真实跑 |
| **Review** | 评审：代码评审与可读性检查 |
| **Ship** | 上线：可发布的产物 |

## 为什么值得关注

- 「**45 分钟**」是 Addy 现场演示的真实耗时——证明**六阶段流水线足够高效**。
- 六阶段里 **Verify 与 Review 是亮点**：很多 Agent 项目止步于「**能跑**」，Addy 在 Verify 阶段就引入**真实浏览器验证**，Review 阶段进一步做可读性检查。
- 这套 Skills **演示的是「**怎么把流程编排到 Agent**」**，而非单条 Skill 的奇技淫巧——可作为团队内部 AI 编码 SOP 的样板。

## 关键能力

| 能力 | 说明 |
|------|------|
| 完整 6 阶段流程 | Define → Plan → Build → Verify → Review → Ship |
| 真实浏览器验证 | 不止是「能跑」，是「能跑且对」 |
| 内置代码评审 | Review 阶段自动代码评审与重构 |
| 现场演示可复用 | 45 分钟完整 demo，可作模板 |

## 项目链接

- 现场文章：<https://x.com/i/article/2099656487400542208>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Addy 演示的是 Skills 的工程化实践
- [Harness Engineering（Harness 工程）](term-harness-engineering.md) — 围绕 LLM 的工程实践，Skills 是其核心载体之一
- [pstack](tool-pstack.md) — 同类「**给 Agent 一整套工作剧本**」思路