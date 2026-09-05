---
type: Tool
title: "Proqi"
description: "终端原生的 prompt 编辑器，把下一条指令、截图和备选方案存成独立可恢复的 thought，可精修、重排、复制或提交给指定 AI 编码 agent"
resource: "https://github.com/oborchers/proqi"
tags: [prompt, tui, coding-agent, terminal, editor]
timestamp: 2026-09-05T15:00:00Z
---

# Proqi

## 它是什么
`oborchers/proqi` 是一款**给多 AI 编码 agent 用户准备的终端原生 prompt 编辑器**：让用户把下一条指令、截图、备选方案存为「独立可恢复的 thought」，在 thought 上精修 / 重排 / 复制 / 提交到指定 agent，避免在 agent 的单行输入框里反复删改。

## 为什么用它 / 适合什么场景
- 同时跑多个 coding agent（Codex / Claude Code / Cursor / OpenCode…），需要为每个 agent 准备不同版本的 prompt。
- 单行输入框难以承载多段长 prompt + 截图 + 备选方案，需要富文本式的草稿区。
- 希望每个「待发指令」都像 git commit 一样可恢复、可重排、可比较。

## 关键能力
| 能力 | 说明 |
|------|------|
| Thought 模型 | 每条 prompt 是一条独立可恢复的 thought，可命名 / 编辑 / 删除 |
| 截图附件 | 可把截图纳入 thought，作为指令的视觉补充 |
| 多备选方案 | 在同一主题下保留多个候选 prompt，按需选用 |
| 重排 / 复制 / 提交 | 可精修、重排、复制或直接喂给指定 agent |
| 终端原生 | 完全跑在终端内，无 GUI 依赖 |

## 媒体
- ![](https://pbs.twimg.com/media/HRWlCLqbAAAmN0t.jpg)

## 相关概念
- [原始链接](https://github.com/oborchers/proqi)