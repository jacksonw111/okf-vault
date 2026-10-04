---
type: "Tool"
title: "live-panel-skill（编码 Agent 的实时面板 Skill）"
description: "ythx-101 维护的 Claude Code / Codex Skill：把编码 Agent 的当前任务状态、上下文、输出流集中显示在浮动面板里，方便人随时介入。"
resource: "https://github.com/ythx-101/live-panel-skill"
tags: "[agent, skill, claude-code, codex, observability, dashboard]"
timestamp: "2026-10-04T01:00:00Z"
---

# live-panel-skill

## 它是什么

[live-panel-skill](https://github.com/ythx-101/live-panel-skill) 是 **ythx-101** 维护的 Claude Code / Codex **实时面板 Skill**——给编码 Agent 加一个浮动面板，实时显示当前任务状态、上下文、输出流。

## 为什么用它

编码 Agent 在 IDE / 终端里跑时，人对它的运行状态只能靠「盯着终端流」做粗略判断；live-panel 把状态 / 上下文 / 输出集中显示在一处。

## 典型场景

- 长任务跑到一半想看 Agent 现在在哪一步
- 同时跑多个 Agent 时区分哪个在做什么
- 教学 / 录屏场景下让观众看清 Agent 内部状态

## 参考链接

- 项目链接：<https://github.com/ythx-101/live-panel-skill>

## 相关概念

- [Vibe Watch（在 awesome-esp32 收录）](./note-awesome-esp32.md) — 把类似面板放到物理硬件上