---
type: Tool
title: "pi-posthorse"
description: "Pi coding agent 的 fitchmultz fork 扩展，提供免摘要的原生上下文窗口延续能力，支持自动翻页、持久笔记与历史恢复。"
resource: "https://github.com/fitchmultz/pi-posthorse"
tags: "[pi-agent, context-window, compaction, persistence]"
timestamp: "2026-09-07T13:10:00Z"
---

# pi-posthorse

## 它是什么
为 Pi coding agent 的 fitchmultz fork 提供"免摘要"原生上下文延续能力的扩展。"Post Horse" 寓意像驿马一样把超长会话的历史搬过去。

## 解决的痛点
主流长会话方案普遍靠"摘要压缩"维持上下文窗口，结果是细节丢失、引用断链、需要回看原文。pi-posthorse 走另一条路：

- **不摘要**：保留原文
- **自动翻页**：上下文窗口满了就把旧消息翻到"卷宗"里
- **持久笔记**：关键决策 / 文件路径 / 用户偏好落盘
- **历史恢复**：需要时按需拉回翻页历史

## 关键能力
| 能力 | 说明 |
|------|------|
| 免摘要 | 上下文延续不靠摘要压缩 |
| 自动翻页 | 老消息自动归档 |
| 持久笔记 | 决策 / 路径 / 偏好落盘 |
| 历史恢复 | 按需拉回翻页内容 |
| 适配 fitchmultz fork | 与 Pi Agent fork 配套 |

## 参考
- 项目链接：<https://github.com/fitchmultz/pi-posthorse>

## 相关概念
- [magic-compact](tool-magic-compact.md) — 走"摘要 + 缓存"路线的 OpenCode 上下文压缩插件
- [Recall](tool-recall-claude-code.md) — Claude Code 离线持久化项目记忆
- [EchoesVault](tool-echoes-vault-opencode.md) — OpenCode 插件会话结束自动记决策