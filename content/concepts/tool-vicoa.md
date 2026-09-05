---
type: Tool
title: "Vicoa"
description: "把 8 种编码 Agent（Claude Code / Codex / OpenCode / Gemini / Cursor / Copilot / Kimi / Hermes）收进同一工作区，每个 Agent 各占一个 git worktree 与分支，可同时改同一个仓库"
resource: "https://github.com/vicoa-ai/vicoa"
tags: [coding-agent, multi-agent, git-worktree, ide, orchestrator]
timestamp: 2026-09-05T15:00:00Z
---

# Vicoa

## 它是什么
`vicoa-ai/vicoa` 是一个**多编码 Agent 协作工作区**：把 Claude Code / Codex / OpenCode / Gemini / Cursor / Copilot / Kimi / Hermes 八种 AI 编程 agent 收进同一个项目视图，每个 agent 各占一个 **git worktree 与独立分支**，可以并行对同一仓库提改动，再做合并 / 比对。

## 为什么用它 / 适合什么场景
- 同时跑多个 AI 编码 agent 想做方案对比（A 改 vs B 改），用 git worktree 隔离不互相污染。
- 不愿意为每个 agent 各自维护一份本地副本，希望集中调度。
- 想在一个 UI 里同时盯多个 agent 的进度与产物。

## 关键能力
| 能力 | 说明 |
|------|------|
| 8 种 Agent 接入 | Claude Code / Codex / OpenCode / Gemini / Cursor / Copilot / Kimi / Hermes |
| git worktree 隔离 | 每个 agent 一个独立 worktree，避免代码互相覆盖 |
| 分支独立 | 每个 agent 跑在自己分支，便于对比 / merge |
| 同时改同一仓库 | 多 agent 并行，无需串行等待 |
| 统一工作区 | 单一入口调度所有 agent |

## 媒体
- ![](https://pbs.twimg.com/media/HRVz6Qsa4AAYpY9.jpg)

## 相关概念
- [原始链接](https://github.com/vicoa-ai/vicoa)