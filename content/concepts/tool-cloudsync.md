---
type: Tool
title: "CloudSync Workflow"
description: "把 agent 的记忆 / 配置 / 工作状态同步到云端的 workflow，让多端 / 多 agent 实例共享同一份上下文。"
tags: [cloudsync, sync, agent, memory, configuration]
timestamp: "2026-08-25T19:30:00Z"
---

# CloudSync Workflow

## 它是什么

CloudSync Workflow 是一类把 AI agent 的运行态（memory、config、conversation / todo / skills 等）持久化并同步到云端的工作流。它让多端（桌面 / 笔记本 / Web）、多 agent 实例（同一项目的不同 agent 副本）共享同一份上下文，避免「在 A 机器改的 prompt 在 B 机器找不到」「agent 重启后忘了上次聊到哪」之类的痛点。

## 为什么用它 / 适合什么场景

- **多端跑 agent**：桌面端 + 云端 agent 想要继续上一次对话 / 沿用同一套 skill。
- **团队共享配置**：一组人共用一套 agent 配置 / memory，避免每次新成员从零开始。
- **agent 状态可恢复**：agent 进程崩溃或被替换后，从云端恢复上下文即可继续。
- **多 agent 协作**：一个任务被多个 agent 接力处理，需要把中间状态落到云端共享。

## 关键能力

| 能力 | 说明 |
|------|------|
| 上下文持久化 | 把对话历史、todo、memory 写入云端存储 |
| 配置分发 | 一次性把 API key、prompt、skill 配置同步到所有节点 |
| 冲突解决 | 多个 agent 同时改同一份配置时的合并 / 优先级策略 |
| 加密与权限 | 端到端加密 + 团队 / 个人访问控制 |
| 版本回放 | 历史 memory / config 可回滚、可审计 |

## 相关概念

- [CCSwitch-operations](./tool-ccswitch-operations.md) — 同样解决「配置散落多份难维护」，但专注于本地多 agent 客户端（Claude Code / Codex 等）

## 参考链接

- 原始链接: <待补充>