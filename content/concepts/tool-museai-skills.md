---
type: "Tool"
title: "MuseAI-Skills（muse 个人 Agent 的 68 技能全套公开）"
description: "win4r 出品：把 muse 个人 Agent 的 68 个技能定义、连接器权限清单和 Linux 容器启动脚本原样扒下来，供人阅读研究——可以把它当作一份「个人 AI Agent 技能栈样板」参考。"
resource: "https://github.com/win4r/MuseAI-Skills"
tags: "[agent-skills, open-source, personal-agent, muse, linux-container]"
timestamp: "2026-09-28T23:50:00Z"
---

# MuseAI-Skills（muse 个人 Agent 的 68 技能全套公开）

## 它是什么

[MuseAI-Skills](https://github.com/win4r/MuseAI-Skills) 是 win4r 出品的开源仓库：**把 muse 个人 Agent 的 68 个技能定义、连接器权限清单和 Linux 容器启动脚本原样扒下来**，供人阅读研究。

它本身**不是「又一个 Agent 框架」**，而是 muse 个人 Agent 项目的**技能清单与运行模板的导出**：你可以把它当作一份「**个人 AI Agent 技能栈样板**」参考——看看一个生产级个人 Agent 会装哪些 Skill、用什么连接器权限、跑在什么容器里。

## 为什么用它 / 适合什么场景

- 想参考一个**生产级个人 Agent** 的技能 / 连接器 / 容器结构怎么设计。
- 想用 **68 个 Skill 的现成清单**当起点，自己挑需要的拼装。
- 想了解 muse 项目对 Linux 容器 + 启动脚本的组织方式。
- 研究型项目——研究 Agent Skill 设计模式、权限清单的最小可工作子集。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 公开仓库（技能 / 连接器 / 启动脚本） |
| 数量 | 68 个技能定义 |
| 容器 | Linux 容器启动脚本 |
| 适合 | 个人 Agent 技能栈参考 |
| 出品 | win4r |

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 的定义 / 通用术语
- [awesome-dsh-plugin](./tool-awesome-dsh-plugin.md) — 同类「生态汇总」思路，但聚焦 DSH 周边