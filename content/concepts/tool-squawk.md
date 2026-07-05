---
type: "Tool"
title: "Squawk（macOS 智能通知 for Claude Code）"
description: "让 Claude Code 在 macOS 上发通知时更聪明：用户看着终端时不发声、没在看才弹窗；还能直接在通知里回复文本或点批准按钮。"
tags: "[macos, notification, claude-code, ai-coding, ux]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/nov1n/squawk"
---

# Squawk（macOS 智能通知 for Claude Code）

## 它是什么

[`Squawk`](https://github.com/nov1n/squawk) 是给 **Claude Code** 写的 macOS 智能通知代理：让 Claude Code 在需要等用户决策时**更聪明地发通知**——你**盯着终端时**保持安静不打扰，**没在看**才弹窗；通知里**直接回复文本**或**点批准按钮**即可继续。

## 视频演示

视频：
- <https://video.twimg.com/amplify_video/2073300555724963840/vid/avc1/1320x1012/ItB7gVTNpfXQ1uvt.mp4?tag=28>

## 关键能力

| 能力 | 说明 |
|------|------|
| 注视检测 | 通过 macOS 焦点判断用户是否在看终端 |
| 静默模式 | 用户在场时不弹窗，避免打断专注 |
| 智能弹窗 | 用户离开时再弹通知 |
| 通知内回复 | 在 macOS 通知里直接输入文本回复 |
| 一键批准 | 通知里点按钮即可批准工具调用 |
| Claude Code 集成 | 作为 Claude Code 的通知层，无需改源码 |

## 解决的痛点

- Claude Code 长任务跑完时会**频繁弹窗**，频繁打断用户专注
- 普通 macOS 通知**没有快捷回复**，要切回终端才能输入
- 每次「批准 / 拒绝」都要切窗口，节奏割裂
- 想让通知**符合 macOS HIG** 而不是简单 beep

## 适用场景

- 日常重度使用 Claude Code 跑长任务的开发者
- 想让 Claude Code 的通知体验接近 Apple 原生应用
- 经常离开座位又怕错过重要决策（如权限请求、阻塞问题）

## 参考链接

- [项目链接](https://github.com/nov1n/squawk)

## 相关概念

- [Claude Code](tool-claude-code.md) — Squawk 服务的目标工具
- [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — tmux 浮动面板管理多个 Claude Code 会话
- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量