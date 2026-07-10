---
type: Tool
title: "friskeval"
description: "在 Claude Code / Codex / Cursor / Gemini CLI / opencode 等智能体发布新技能前，对自身技能目录做路由检查。"
resource: "https://github.com/ryanda9910/friskeval"
tags: [tool, agent-skills, claude-code, codex, cursor, gemini-cli, opencode, routing]
timestamp: 2026-07-10T13:17:00.000Z
---

# friskeval

## 它是什么
发布前的"技能路由体检工具"：在 Claude Code / Codex / Cursor / Gemini CLI / opencode 等 agent 装载新技能之前，先把自身技能目录走一遍路由检查，确保不会有冲突、覆盖或死链。

## 为什么用它 / 适合什么场景
- 一次装多个技能，担心某些 skill 把另一些"屏蔽"或被同名触发器覆盖。
- 自己写了一套 skill 想发布，先自查路由问题再 push。
- 想给团队 / 社区批量安装技能前做安全 / 一致性检查。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多 agent 适配 | Claude Code、Codex、Cursor、Gemini CLI、opencode |
| 路由体检 | 检查技能触发器 / 描述是否有冲突或被覆盖 |
| 发布前自检 | 把"装了但调不到"或"触发错乱"问题前置发现 |
| 跨平台 | 覆盖主流 IDE / CLI 型 agent 生态 |

## 媒体
视频（原始剪藏附件）：
- <https://video.twimg.com/tweet_video/HM1DG8KagAAxKm6.mp4>

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — friskeval 是给 Agent Skills 体系做"发布前体检"的质量门
- [Hallmark](tool-hallmark-skill.md) — Hallmark 给 agent 装"设计感"技能，friskeval 保障这些技能不被路由错乱破坏