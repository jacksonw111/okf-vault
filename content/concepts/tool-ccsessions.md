---
type: "Tool"
title: "ccsessions（miskiewiczm/ccsessions）"
description: "Claude Code 终端会话的 TUI 管理器——快速浏览、预览、恢复和管理 Claude Code 终端会话，把历史会话一览无余。"
resource: "https://github.com/miskiewiczm/ccsessions"
tags: "[claude-code, tui, session-manager, terminal, ai-coding]"
timestamp: "2026-07-31T20:30:00Z"
---

# ccsessions（miskiewiczm/ccsessions）

[ccsessions](https://github.com/miskiewiczm/ccsessions) 是 **Claude Code 终端会话的 TUI 管理器**：快速**浏览、预览、恢复和管理** Claude Code 的历史会话——让你不必滚动找上次对话，直接在一个 TUI 内一览所有会话，挑一个继续。

## 它是什么

- **TUI（终端 UI）** 工具，无浏览器依赖
- **浏览**：列出所有本地 Claude Code 会话
- **预览**：在选定会话里读消息或摘要
- **恢复**：挑一条回到 Claude Code 继续对话
- **管理**：删除、归档、重命名会话

## 为什么用它 / 适合什么场景

| 痛点 | ccsessions 的回应 |
|------|--------------------|
| 终端找上次会话要 ctrl+R 翻半天 | TUI 列表直接挑 |
| Claude Code 退出后会话难找回 | 自动索引所有历史会话 |
| 多个并行任务会话混杂 | 一处看全部，按项目 / 时间筛 |
| 想恢复某次会话上下文 | 一键 resume，无需重描述项目背景 |

## 关键能力

| 能力 | 说明 |
|------|------|
| TUI 浏览 | 终端原生界面，无需浏览器 |
| 预览会话 | 看历史消息或摘要 |
| 恢复会话 | 一键回到 Claude Code 继续 |
| 管理操作 | 删除 / 归档 / 标签 |
| 启动快 | 一行命令进入 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent，ccsessions 直接管它的会话
- [juggler](./tool-juggler-ai.md) — 可视化工作台式 AI 编码 agent，与 ccsessions 一处会话历史 TUI 一处 UI
- [Pi Exa](./tool-pi-exa.md) — Pi 终端 AI 编程 agent 的 Exa 搜索扩展，ccsessions 的「管会话」思路可直接迁移过去
- [happy-claude-code（共享 Claude Code）](./tool-happier.md) — 远程串流 / 共享 Claude Code，与 ccsessions 形成「终端全本地 vs 远程协同」互补
