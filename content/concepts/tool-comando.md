---
type: "Tool"
title: "Comando（本地优先的多智能体协作代码编辑器）"
description: "本地优先的多智能体协作代码编辑器，让开发者与 AI 代理在同一工作区协同而不被聊天界面隔离；支持 Codex、Claude、Grok、Kilo、OpenCode 五种 ACP 运行时，分栏并行协作 + 逐块审查。"
tags: "[editor, agent, codex, claude, opencode, electron, rust, ide]"
timestamp: "2026-07-06T06:42:00.000Z"
resource: "https://github.com/jsgrrchg/Comando"
---

# Comando（本地优先的多智能体协作代码编辑器）

## 它是什么

[`Comando`](https://github.com/jsgrrchg/Comando) 是一个**本地优先**的多智能体协作代码编辑器。它让开发者与 AI 代理在**同一工作区**协同，而不是被聊天界面隔离在另一个窗口里。Electron 负责 UI 与编排，Rust 后台负责文件系统、Git、终端与持久化——架构清晰、性能可控。

## 为什么用它

传统的 AI 编码体验是「聊天框 + IDE」两个割裂的窗口，AI 做的修改要切过去肉眼 diff。Comando 把 AI 协作**嵌进编辑器本身**：改动有行内标注、逐块（hunk）审查通过才落地，开发者始终掌控每一步。

## 关键能力

| 能力 | 说明 |
|------|------|
| 五种 ACP 运行时 | Codex、Claude、Grok、Kilo、OpenCode 都可作为后端 |
| 分栏并行协作 | 同时开多个会话 / 终端 / 文件编辑器 / Git 视图 |
| 行内标注 + 逐块审查 | AI 改动逐 hunk 显示 diff，确认后才落盘 |
| Rust 后台 | 文件系统 / Git / 终端 / 持久化都在 Rust 侧，Electron 只管 UI 与编排 |
| 三平台支持 | macOS / Windows / Linux |

![Comando 编辑器](https://pbs.twimg.com/media/HMdiS1xbwAAu-Li.jpg)

## 适用场景

- 想在本地 IDE 里直接调用多个 AI 编码代理而非来回切窗口
- 需要同时运行多个 AI 会话完成并行任务（如：一边让一个 agent 写测试、一边让另一个 agent 改文档）
- 重视每一步修改的可控性与可审查性

## 参考链接

- [项目链接](https://github.com/jsgrrchg/Comando)

## 相关概念

- [Aura-IDE](tool-aura-ide.md) — 另一个本地优先 AI 编码工作台，Planner/Worker 模式
- [Orca Coding IDE](tool-orca-coding-ide.md) — 跨平台 Coding IDE 套壳，并行 worktree + computer use