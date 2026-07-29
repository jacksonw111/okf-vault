---
type: Tool
title: "Spec-Superflow（AI 编码的规划 → 实现硬闸）"
description: "AI 写代码最烦两件事：还没想清楚就改文件，或规划好但实现跑偏。Spec-Superflow 在规划和实现之间加一道硬闸：先想清楚再动手。"
resource: "https://github.com/MageByte-Zero/spec-superflow"
tags: [ai-coding, spec, planning, workflow, agent-skill, claude-code]
timestamp: "2026-07-29T02:39:00.000Z"
---

# Spec-Superflow

## 它是什么

AI 编码插件，针对两个最常见的痛点：

1. **没想清楚就动手** → AI 一上来就改几十个文件，规划不充分
2. **规划到位但实现跑偏** → 中途逐步偏离原本 spec

解决方案：**在规划（spec）和实现（implementation）之间加一道硬闸**——必须先把 spec 写好、确认，再允许进入实现阶段。

## 工作流

```
[问题] → 写 SPEC → 评审 SPEC → [硬闸] → 写代码 → 验证对照 SPEC → 完成
```

## 与「自由改文件」的差异

| 模式 | 风险 | Spec-Superflow |
|------|------|----------------|
| 改几十个文件不回头 | 中途跑偏，越改越乱 | 必须先把 spec 锁定 |
| 实现到一半跑偏 | 用户被迫接受半成品 | 每步对照 spec 校验 |
| 一次提 PR 几十 commit | 评审困难 | 评审分两段：spec + diff |

## 关键能力

| 能力 | 说明 |
|------|------|
| 规划 → 实现硬闸 | 不通过规划就不能写代码 |
| 适合 coding agent | 与 Claude Code / Codex 风格契合 |
| spec 单独可评审 | 把"做什么"和"怎么做"分两段 |
| 减少返工 | 提前发现 spec 漏洞 |
| 提升 PR 评审质量 | spec + diff 两段式 |

## 原始链接

- [项目仓库](https://github.com/MageByte-Zero/spec-superflow)
- [推文剪藏](https://x.com/QingQ77/status/2082294791749190091)

## 相关概念

- [Metis（编程模型外层包装）](./tool-metis.md) — 类似思路：改之前查资料、改完自动验证
- [Aura-IDE](./tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台，写文件前先显示 diff 审批
- [Metis / Paper Lifecycle](./tool-paper-lifecycle.md) — 论文写作 Codex skills 套件，审稿式体检
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 从 demo 到实盘的 12 条工程原则