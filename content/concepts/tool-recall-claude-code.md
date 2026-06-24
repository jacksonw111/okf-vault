---
type: "Tool"
title: "Recall（raiyanyahya/recall）"
description: "Claude Code 的离线持久化项目记忆插件：本地记录会话日志，用 TextRank 压缩为摘要，彻底告别每次冷启动重新解释。"
resource: "https://github.com/raiyanyahya/recall"
tags: [claude-code, memory, offline, local-first, summarization]
timestamp: "2026-06-23T15:30:00Z"
---

# Recall（raiyanyahya/recall）

## 它是什么

Claude Code 的本地记忆插件。它会抓取 Claude Code 每次会话的日志，然后离线用 TextRank 算法把它们压缩成一段一段的「项目摘要」——下次开新会话时，这些摘要会自动注入系统提示，免去每次都从头解释项目背景。

## 为什么用它 / 适合什么场景

- **冷启动焦虑**：每次开新会话都要把项目结构、约束、近期决策再讲一遍？
- **隐私敏感**：项目代码和上下文完全留在本机，不外发任何模型调用；
- **省 token**：摘要长度可控，不会撑爆上下文窗口；
- **多项目切换**：在多个 repo 间反复横跳时，自动带上对应上下文。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动日志 | 静默接管 Claude Code 会话日志 |
| TextRank 摘要 | 本地无外部 API 调用的算法压缩 |
| 摘要注入 | 新会话开局自动携带 |
| 完全离线 | 不调用任何云端模型 / API |
| 隐私保护 | 数据只留本机，不浪费订阅令牌 |

## 媒体 / 原始链接

- 项目链接：<https://github.com/raiyanyahya/recall>

## 相关概念

- [Claude Code](tool-claude-code.md) — Recall 直接为其扩展的底层 agent
- [EverOS](tool-everos.md) — 同属「为 AI 代理提供统一长期记忆层」的赛道（EverOS 更通用，Recall 专攻 Claude Code）
- [Vercel Labs Personal AI Template](tool-vercel-personal-ai-template.md) — 另一种「持久化个人助手记忆」的实现路径