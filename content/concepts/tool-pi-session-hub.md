---
type: "Tool"
title: "pi-session-hub（统一 6 家 AI 编码工具的会话历史）"
description: "Gateton 开源的 Pi 扩展：把 Claude Code / Codex / OpenCode / Crush / JCode / Pi 六种 AI 编码工具的本地会话历史收进一个全屏列表，可搜、可免费读，也可把上下文直接接回当前对话继续写代码。"
resource: "https://github.com/Gateton/pi-session-hub"
tags: "[pi, session-history, ai-coding, multi-agent, search, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# pi-session-hub（统一 6 家 AI 编码工具的会话历史）

## 它是什么

[pi-session-hub](https://github.com/Gateton/pi-session-hub) 是 Gateton 开源的 **Pi 编码代理扩展**——把本机 **6 种 AI 编码工具**的本地会话历史**汇总成全屏列表**：

| 工具 | 状态 |
|------|------|
| Claude Code | ✅ |
| Codex | ✅ |
| OpenCode | ✅ |
| Crush | ✅ |
| JCode | ✅ |
| Pi | ✅ |

每行标好**来源工具 / 项目 / 最近活动时间 / 模型**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Pi 扩展 |
| 覆盖 | 6 种主流 AI 编码工具 |
| 视图 | 全屏列表 |
| 元数据 | 来源工具 / 项目 / 模型 / 最近活动 |
| 搜索 | 全文搜索 |
| 阅读 | 免费读历史会话 |
| 续写 | 把上下文直接接回当前对话继续写代码 |

## 为什么用它 / 适合什么场景

- 同时用**多套 AI 编码工具**，不想为翻历史来回切窗口。
- 想要**「统一历史」+「跨工具续写」** 的工作流——A 工具写到一半，B 工具接着写。
- 想把 AI 编码会话作为**项目记忆**沉淀下来（每行带项目 + 模型 + 时间）。
- 已经在用 **Pi**，需要一个轻量扩展而不是再装一个独立应用。

## 媒体

- ![](https://pbs.twimg.com/media/HTGaCPsaQAAArKi.png)

## 相关概念

- [Pebrel](./tool-pebrel.md) — 把 AI 编码 CLI 当一等公民的终端 UI
- [portlist](./tool-portlist.md) — 同代产物：AI 工具感知的端口管理
- [pi-tty7-tab-namer](./tool-pi-tty7-tab-namer.md) — 另一个 Pi 扩展（自动给终端 Tab 命名）