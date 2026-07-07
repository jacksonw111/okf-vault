---
type: Tool
title: "ai_usage_dashboard"
description: "本地运行的 AI 用量仪表板，以游戏血条形式直观展示各 AI 提供商的用量和配额。"
resource: "https://github.com/danleetw/ai_usage_dashboard"
tags: [ai, dashboard, quota, game-ui]
timestamp: "2026-07-07T12:00:00Z"
---

# ai_usage_dashboard

## 它是什么
`danleetw/ai_usage_dashboard` —— 一款 **本地运行的 AI 用量仪表板**：把每个 AI 提供商的用量和配额用 **「游戏血条」** 形式呈现，比数字 / 进度条更具游戏感与状态可读性，让"今天 Claude 还剩多少额度"一眼可读。

## 为什么用它 / 适合什么场景
- 同时订阅多家 AI 服务，想用一个面板总览配额。
- 偏好 **游戏化 UI**，比传统进度条更直观。
- 想要本地运行、不上传使用数据。

## 关键能力
| 能力 | 说明 |
|------|------|
| 游戏血条 | 用 RPG 风格的血条形式展示配额 |
| 多 AI 提供商 | 同一界面查看各家用量 |
| 本地运行 | 数据全在本地 |
| 仪表板形态 | 一块面板总览，比逐个登录服务网站效率高 |

## 相关概念
- [Token Tracker](tool-token-tracker.md) — 本地统计各 AI CLI 工具 Token 消耗、可视化成本
- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量
- [glance（GitHub · Docker · SSH 桌面仪表盘）](tool-glance-dashboard.md) — 三合一开发者桌面仪表盘
