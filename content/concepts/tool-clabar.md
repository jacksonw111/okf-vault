---
type: "Tool"
title: "clabar"
description: "macOS 菜单栏小工具：把 Claude 用量（5 小时 / 每周 / 按模型 三类额度）与 Claude Code 会话状态搬到菜单栏，并把权限请求、完成的任务、失败调用转成系统通知。"
resource: "https://github.com/Magir/clabar"
tags: [macos, claude, claude-code, menubar, usage, monitoring]
timestamp: "2026-08-08T20:30:00Z"
---

# clabar

## 它是什么

clabar 是一款 macOS 菜单栏（menubar）小工具，专门监控 Claude / Claude Code 的用量与会话状态。它把 5 小时、每周、按模型三类额度各自的剩余量显示在菜单栏图标上，并把 Claude Code 会话里冒出的权限请求、完成的任务、失败的调用等事件转成系统通知推送过来。

## 为什么用它 / 适合什么场景

- 担心 5 小时 / 每周额度被 Claude Code 默默用完。
- 想在 Claude Code 长时间跑任务时，把权限 / 完成事件变成 macOS 通知。
- 不想打开 ccusage 网页版反复查余额。
- 已经在用 Claude Code，希望把「监控」这件事统一到 macOS 菜单栏。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三类额度显示 | 5 小时 / 每周 / 按模型 三档独立显示 |
| 菜单栏常驻 | macOS 顶部菜单栏图标实时更新 |
| 会话事件通知 | 权限请求 / 完成任务 / 失败调用 转系统通知 |
| Claude Code 适配 | 直接对接 Claude Code 会话状态 |
| 原生 macOS | Swift / SwiftUI 风格，遵守系统勿扰设置 |

## 相关概念

- [tokenscope](./tool-tokenscope.md) — 同样 macOS 菜单栏监控 Claude CLI 用量
- [ai-meter](./tool-ai-meter.md) — 接 ccusage 监控各编码 Agent 剩余预算
- [GlassQuota](./tool-glassquota.md) — macOS 实时显示 Codex / Gemini / Claude 三家 API 剩余用量