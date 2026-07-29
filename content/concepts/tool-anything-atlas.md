---
type: Tool
title: "AnythingAtlas（Agent 里的结构化学习地图生成器）"
description: "直接跑在 Claude Code / Codex 等 Agent 框架里。告诉它想学什么、有多少时间，它会主动追问、全网找资源、筛选，最后输出 Markdown 加 HTML 的学习图谱。"
resource: "https://github.com/Liuziyu77/AnythingAtlas"
tags: [agent-skill, learning-path, claude-code, codex, study-guide]
timestamp: "2026-07-29T09:45:00.000Z"
---

# AnythingAtlas

## 它是什么

帮初学者在海量资料中找到**最佳学习路径**的工具——为任何主题规划**结构化的学习地图**。

直接跑在 **Claude Code / Codex** 这类 Agent 框架里。流程：

1. 用户：「我想学 X，我有 N 小时」
2. Agent 主动追问（澄清学习目标 / 当前水平）
3. 全网找资源
4. 筛选与排序
5. 输出 **Markdown + HTML** 的学习图谱

![截图示例](https://pbs.twimg.com/media/HOSRiP0bMAAzE9y.jpg)

## 与「awesome-list」的区别

| Awesome List | AnythingAtlas |
|--------------|---------------|
| 静态资源合集 | 动态规划的学习路径 |
| 没有顺序 | 按时间 / 难度排序 |
| 一份文档装下 | Markdown + HTML 双格式 |
| 一次性写好 | Agent 持续追问细化 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 跑在 Agent 框架里 | Claude Code / Codex |
| 主动追问 | 不止被动接收输入 |
| 资源筛选 | 全网找 + 评估 |
| 时间预算感知 | "我有 10 小时" / "我有 100 小时" |
| 双格式输出 | Markdown + HTML 图谱 |
| 学习路径 | 不只是资源列表 |

## 原始链接

- [项目仓库](https://github.com/Liuziyu77/AnythingAtlas)
- [推文剪藏](https://x.com/QingQ77/status/2082401998255915377)

## 相关概念

- [Light Skills](./tool-light-skills.md) — 28 个科研全流程 AI Skill，从文献调研到投稿返修
- [AnythingAtlas 与 Study Dost AI 同属"学习辅助"维度](./tool-study-dost-ai.md) — STEM 学习助手，分步 / 类比 / 视觉三种讲法
- [Mathematical Atlas / 数学图谱类资源](./note-front-end-resources.md) — 思路类似：把领域画成图谱
- [Self-Directed Learning Tools（类似 Inky Bird Frame）](./tool-inky-bird-frame.md) — 不同形态的学习 / 复习工具