---
type: Tool
title: "Dashi Taskboard"
description: "给 Codex 用的本地优先、跑在浏览器里的任务看板：能直接嵌进 Codex 侧栏，让 agent 和协作者跟踪每期 issue 的进度，而不是把状态记在对话里。"
resource: "https://github.com/chuspeeism/dashi-taskboard"
tags: [codex, task-board, kanban, local-first, browser, issue-tracking, agent-ux]
timestamp: 2026-08-06T15:30:00Z
---

# Dashi Taskboard

## 它是什么

chuspeeism 开源的 Codex 任务看板，可作为浏览器应用单独跑，也能嵌进 Codex 侧栏，把「agent 干了什么 / 下一步干啥」从对话历史里拎出来。

## 为什么用过它 / 适合什么场景

- 你用 Codex（OpenAI 的 CLI 编程 Agent）跑长流程，嫌状态全塞在对话里翻不到。
- 想让 agent 与人类协作者都能直观看到每期 issue 进度。
- 想本地优先部署一个看板，不依赖 SaaS。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地优先 + 浏览器 | 跑在本机的 Web 应用，浏览器访问 |
| Codex 侧栏嵌入 | 直接挂进 Codex 侧栏，无需切换窗口 |
| 任务 / Issue 看板 | 跟踪每期 issue 状态、进度 |
| 协作可读 | agent 与人协作都能看同一份状态 |

## 相关概念
- [Sol Advisor](./tool-sol-advisor.md) — Codex 原生 subagent 双角色，Sol 管架构+验收 / Terra 负责实现
- [Pi Livecraft](./tool-pi-livecraft.md) — 给 Pi 终端 AI 助手套一个随时能被模型改的 React 网页界面
- [Codexloom](./tool-codexloom.md) — 把 Codex 一条线程延续成跨任务累积知识的领域 Agent