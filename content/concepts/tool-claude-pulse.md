---
type: Tool
title: "claude-pulse"
description: "本地运行的 Claude Code 仪表盘，实时展示 Claude 用量与上下文占用，可恢复丢失的会话，并支持用手机远程审批工具调用。"
resource: "https://github.com/nikitadoudikov/claude-pulse"
tags: "[claude-code, dashboard, usage-tracking, mobile-approval, session-recovery]"
timestamp: "2026-07-19T11:43:00Z"
---

# claude-pulse

## 它是什么

nikitadoudikov/claude-pulse 是一个**本地运行的 Claude Code 仪表盘**，给终端 AI 编码会话补一个网页视图。它把当前会话的 token 用量、上下文窗口占用、运行状态实时投到浏览器，同时提供「恢复被中断的会话」与「手机端远程审批工具调用」两条额外能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时用量视图 | token 消耗 / 上下文窗口占用 / 当前模型 |
| 会话恢复 | 找回因断电 / kill 而丢失的 Claude Code 会话 |
| 移动审批 | 手机扫码或访问页面远程批准工具调用，不用守在终端前 |
| 本地优先 | 仪表盘本身跑在用户机器上，调用日志不上云 |

## 适合谁

- 长时间跑 Claude Code 任务、不在电脑前时希望远程围观进度
- 5 小时窗口用满被踢后希望快速续上之前的会话
- 担心 Agent 自动执行破坏性工具，希望随时按需叫停

## 与类似工具的差别

- [Token-Tracker](./tool-token-tracker.md) — 统计各 AI CLI Token 消耗
- [ai-meter](./tool-ai-meter.md) — macOS 菜单栏用量监控
- [Squawk](./tool-squawk.md) — macOS 智能通知代理
- claude-pulse 的差异点：**专为 Claude Code 设计 + 移动端审批 + 会话恢复** 三件套

## 媒体预览

![](https://pbs.twimg.com/media/HNbjW6qagAAgm1Z.jpg)

## 相关概念

- [Claude Code](./tool-claude-code.md) — Anthropic 终端 AI 编码 agent
- [Squawk](./tool-squawk.md) — macOS 智能通知代理

## 参考链接

- 项目链接: <https://github.com/nikitadoudikov/claude-pulse>