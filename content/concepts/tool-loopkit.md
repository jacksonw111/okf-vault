---
type: Tool
title: "loopkit"
description: "为 Claude Code / Cursor / Codex / Gemini CLI 等编码 agent 准备的 33 个实战检验过的技能文件包，让 agent 按需加载、精准执行。"
resource: "https://github.com/Archive228/loopkit"
tags: [agent, skills, coding-agent, opensource]
timestamp: "2026-07-07T12:00:00Z"
---

# loopkit

## 它是什么
`Archive228/loopkit` —— **33 个经过实战检验的技能文件包**，专为 Claude Code / Cursor / Codex / Gemini CLI 等编码 agent 设计：在缺乏结构化技能库时，agent 容易猜测、编造虚假 API 或修复；loopkit 提供**精选小颗粒度 skill 文件**让 agent 按需加载，把"幻觉 API"问题降下来。

## 为什么用它 / 适合什么场景
- 用 Claude Code / Codex / Cursor / Gemini CLI 等编码 agent 时，被「编造出的 API」「错误的修复」卡过。
- 想给 agent 加一份**精选 skill 库**而不是堆一个巨大 SOP。
- 想要 **按需加载**——每次只调一小段上下文完成一件事。

## 关键能力
| 能力 | 说明 |
|------|------|
| 33 个 skill | 实战检验技能，覆盖常见编码任务 |
| 多 agent 兼容 | Claude Code / Cursor / Codex / Gemini CLI |
| 按需加载 | agent 实际需要时才读相关 skill，控制上下文占用 |
| 实战检验 | 每条 skill 都按真实报错 / 修复案例打磨 |
| 开源 | 仓库公开可自部署 |

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — 关于 skill 元层级的概念说明
- [loops.elorm.xyz](tool-loops-elorm-xyz.md) — 几十位大神的 loop engineering 思路集合
- [Loop Engineering](tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论 + 三个 CLI
- [mattpocock/skills](tool-mattpocock-skills.md) — Real Engineers 风格合集
- [NVIDIA Skills](tool-nvidia-skills.md) — NVIDIA 官方 Agent Skills 合集，覆盖 200+ 技能
- [Light-skills](tool-light-skills.md) — 28 个科研全流程 AI Skill
