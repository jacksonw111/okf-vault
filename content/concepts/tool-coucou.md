---
type: "Tool"
title: "Coucou（Mac 刘海 / 状态栏的 AI Agent 监控面板）"
description: "Louis-CFM 出品的 Mac 状态栏 / 刘海（Dynamic Island）小工具：把 Claude Code 等 AI 编码 Agent 的运行状态、权限审批、聊天内容搬进 Mac 刘海或屏幕顶部，不用切窗口就能盯住。"
resource: "https://github.com/Louis-CFM/coucou"
tags: "[macos, notch, dynamic-island, menubar, ai-agent, status-monitor, claude-code]"
timestamp: "2026-10-02T01:48:00Z"
---

# Coucou（Mac 刘海 / 状态栏的 AI Agent 监控面板）

## 它是什么

[Coucou](https://github.com/Louis-CFM/coucou) 是 Louis-CFM 出品的 **Mac 状态栏 / 刘海（Dynamic Island）小工具**——把 Claude Code 等 AI 编码 Agent 的**运行状态、权限审批请求、聊天内容**搬进 Mac 刘海（Notch）或屏幕顶部，**不用切窗口就能盯住 agent**。

## 为什么用它 / 适合什么场景

| 场景 | Coucou 的好处 |
|------|--------------|
| 跑 Claude Code 长任务 | 不切走也能看 agent 在干啥 |
| 等待权限审批 | 审批请求直接弹到刘海，点一下就同意 / 拒绝 |
| 多 agent 并行 | 状态栏里同时挂多个 agent 的进度 |
| 写代码时开别的 app | agent 状态常驻顶部，不抢主区 |
| 笔记本刘海党 | 把刘海当 mini HUD 用 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 刘海（Notch）渲染 | 在 Mac 刘海里叠 HUD |
| 状态显示 | 跑 / 等待 / 出错 等状态图标 |
| 权限审批 | 审批请求直达刘海，点按即批 |
| 聊天摘要 | 在刘海里展示 agent 简短对话 |
| 多 agent | 同时挂多个 |
| 始终置顶 | 不抢主工作区 |

## 使用流程

1. 装上 Coucou，跑 Claude Code（或其他 agent）
2. agent 在跑 → 刘海里出现状态气泡
3. agent 请求权限 → 刘海里弹审批按钮
4. 一键同意 / 拒绝，回到主工作区

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105836413728038920>
- 项目链接：<https://github.com/Louis-CFM/coucou>
- 视频：<https://video.twimg.com/tweet_video/HTlTi_-bEAAKy-r.mp4>

## 相关概念

- [Claude Code](./tool-claude-code.md) — Coucou 的主目标 agent
- [Harness Engineering](./term-harness-engineering.md) — 「权限审批」是 Harness Engineering 的核心环节
