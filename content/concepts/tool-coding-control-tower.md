---
type: Tool
title: "coding-control-tower"
description: "mohan-n-swamy/coding-control-tower，给同时跑多个 AI 编码 agent（Claude Code / Codex / Cursor 等）的开发者用的本地面板，直接从会话记录、PR 描述和 git 仓库拉数据，显示 NOW / NEEDS YOU / resume packet / 当日 token 用量。"
resource: "https://github.com/mohan-n-swamy/coding-control-tower"
tags: "[ai-coding, dashboard, multi-agent, claude-code, codex, observability]"
timestamp: "2026-07-22T00:38:00Z"
---

# coding-control-tower

## 它是什么

[`coding-control-tower`](https://github.com/mohan-n-swamy/coding-control-tower) 是一个本地面板，专为同时跑多个 AI 编码 agent 的重度用户设计。它**直接读取**本地 Claude Code / Codex 等会话日志、PR 描述以及 git 仓库状态，**不需要给 agent 额外打标签或插桩**就能汇总视图。

## 解决什么痛点

- 同时跑 5–10 个 AI 编码 agent 会话时，记不清哪个在等你、哪个卡住、哪个能收尾；
- 切换项目时不知道上次断在哪一步；
- 想知道今天各家 agent 的 token 消耗情况。

## 关键视图

| 视图 | 内容 |
|------|------|
| NOW | 当前正在跑的会话 |
| NEEDS YOU | 停下来等用户回话的会话 |
| resume packet | 每个项目「断在哪一步」的恢复包（上下文 + git 状态 + PR 链接） |
| 当日 token | 跨 agent 的当日 token 用量汇总 |

## 数据来源（无需手动标记）

- Claude Code / Codex 会话日志
- GitHub PR 描述与状态
- git 仓库本身（branch / dirty / commit）

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) | tmux 浮动面板 | 只服务 Claude Code，靠快捷键唤出 |
| coding-control-tower | 本地 Web 面板 | 多 agent、读 PR + git + token 全景 |

## 媒体

![](https://pbs.twimg.com/media/HNq-04hbAAAdWJF.jpg)

## 原始链接

- [项目仓库](https://github.com/mohan-n-swamy/coding-control-tower)

## 相关概念

- [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — 同为多 Claude Code 会话管理工具，但 mux 是 tmux 内嵌面板，本工具是独立本地 dashboard
- [MCO（多 AI 编程代理编排层）](tool-mco.md) — 同时调度多种 CLI 编码代理，本工具聚焦在「调度完之后的可视化观察」
- [kcap-cli](tool-kcap-cli.md) — 同为 AI 编码会话可观测性 CLI，但偏结构化日志而非面板