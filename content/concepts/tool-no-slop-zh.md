---
type: Tool
title: "no-slop-zh"
description: "用于 Claude Code 与 Codex 的中文文本清理 Skill，在锁定事实与术语的前提下削弱 AI 套话。"
resource: "https://github.com/superchun/no-slop-zh"
tags: [writing, chinese, agent-skill]
timestamp: "2026-07-25T00:00:00Z"
---

# no-slop-zh

用于 Claude Code 与 Codex 的中文文本清理 Skill，在锁定事实与术语的前提下削弱 AI 套话。

## 适用场景

- 需要保留事实、术语和版本号，避免润色改变含义的场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内容锁定 | 保留事实、术语和版本号，避免润色改变含义。 |
| clean 模式 | 输出冷静、简洁的文本。 |
| natural 模式 | 提升自然度但不额外发挥。 |
| Detect 模式 | 只标记问题，不直接修改。 |

## 链接与媒体

- [项目链接](https://github.com/superchun/no-slop-zh)
- [原始链接](https://x.com/QingQ77/status/2080993970893853105)

## 相关概念

- [no-ai-slop](./tool-no-ai-slop.md) — 两者都用于识别和削弱 AI 套话，中文 Skill 与通用规则扫描器可互补。
