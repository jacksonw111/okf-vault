---
type: "Tool"
title: "Douchat（多 agent CLI 统一桌面聊天窗口）"
description: "把多个 agent CLI（Claude Code、Codex、Gemini CLI、Cursor CLI 等）收进同一个桌面窗口：能单聊也能拉群一起干活，省去开多个终端来回切换。"
resource: "https://github.com/QingQ77/douchat"
tags: "[agent, cli, desktop-app, multi-agent, chat, claude-code, codex, gemini-cli, collaboration]"
timestamp: "2026-10-02T13:18:00Z"
---

# Douchat（多 agent CLI 统一桌面聊天窗口）

## 它是什么

[Douchat](https://github.com/QingQ77/douchat) 把本机装好的多个 agent CLI（Claude Code、Codex、Gemini CLI、Cursor CLI 等）**收进同一个桌面窗口**——既能单聊一个 agent，也能把多个 agent 拉进同一个群聊里协作，避免来回切终端。

## 为什么用它 / 适合什么场景

| 场景 | Douchat 的好处 |
|------|----------------|
| 装了多个 agent CLI | 一个窗口全管，不用开 4 个终端 |
| 多 agent 协作 | 同一个群里让 Claude 写代码、Codex 审 PR、Gemini 做调研 |
| 上下文切换成本高 | 一屏看完所有 agent 的输出与状态 |
| 想给非技术同事看 | 桌面 GUI 比纯终端易上手 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 CLI 集成 | Claude Code / Codex / Gemini CLI / Cursor CLI 等 |
| 单聊模式 | 一对一 |
| 群聊模式 | 拉多个 agent 一起干 |
| 桌面 GUI | 比纯终端易用 |
| 状态共享 | 一个窗口里看到所有 agent 的状态 |

## 与「多终端分屏」对比

| 维度 | 多终端分屏 | Douchat |
|------|-----------|---------|
| 切换成本 | 鼠标点或快捷键 | 一个窗口里切会话 |
| 跨 agent 协作 | 难（要复制粘贴上下文） | 群聊里直接 @ 多个 |
| 历史 / 上下文 | 各 terminal 各管各 | 统一保存 |
| 上手 | 极客风 | 普通用户也能用 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2106010309789978920>
- 项目链接：<https://github.com/QingQ77/douchat>

## 相关概念

- [Multi-Agent](./term-multi-agent.md) — 大伞概念
- [PeakCode](./tool-peakcode.md) — 同类「多 agent 统一 GUI」工具
- [Brigade](./tool-brigade.md) — 本地 AI 代理团队 + 共享长期记忆
- [Claude Code](./tool-claude-code.md) — Douchat 收编的目标之一
