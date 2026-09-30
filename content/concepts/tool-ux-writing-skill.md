---
type: Tool
title: "UX Writing Skill（content-designer 出品）"
description: "开源 Agent Skill：给 Claude Code 等 Agent 注入 UX 文案（按钮、错误提示、空状态、引导语）写作规范，让 Agent 写出的界面文案不再像机翻。"
resource: "https://content-designer.github.io/ux-writing-skill/"
tags: [ux-writing, agent-skills, copy, microcopy, claude-code]
timestamp: 2026-09-30T00:03:52Z
---

# UX Writing Skill

## 它是什么

content-designer 维护的一份**面向 Agent 的 UX 文案 Skill**：把按钮文案、错误提示、空状态、引导语等微文案（microcopy）的写作规范整理成 Agent 可消费的结构化 Skill。让 Claude Code 这类 Agent 在写界面时不再用生硬的机翻口吻。

## 为什么用它 / 适合什么场景

- 让 Agent 生成的 UI 文案更"人话"——尤其是错误提示 / 空状态 / CTA 按钮这种**极短但极重要**的文本。
- 希望团队 / Agent 在不同界面间保持一致的文案语气。
- 配合 Claude Code 使用时希望对输出文案有可控的写作规范约束。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输出形态 | Agent 可消费的 Skill 文件 |
| 覆盖场景 | 按钮文案、错误提示、空状态、引导语等微文案 |
| 适用 Agent | Claude Code 等支持 Skill 的 Agent |
| 维护方 | content-designer（GitHub） |

## 参考链接

- Skill 页：<https://content-designer.github.io/ux-writing-skill/>
- 仓库：<https://github.com/content-designer/ux-writing-skill>

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — UX Writing Skill 是该体系中面向「写作规范」的一个具体 Skill
- [cuellarfr/design-skills](./tool-cuellarfr-design-skills.md) — 同类面向 Claude Code / Cursor 的 Skill 合集，但覆盖范围更广