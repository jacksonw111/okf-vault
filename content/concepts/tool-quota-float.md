---
type: "Tool"
title: "quota-float（Codex Desktop 额度悬浮小组件）"
description: "轻量悬浮桌面小组件，从本机 Codex Desktop 登录态读取并常驻显示 Codex 的额度、配额与重置时间，无需估算、不改账户。"
resource: "https://github.com/change-42-yhmm/quota-float"
tags: "[codex, openai, desktop, quota, floating-widget]"
timestamp: "2026-07-20T20:20:00Z"
---

# quota-float（Codex Desktop 额度悬浮小组件）

## 它是什么

[change-42-yhmm/quota-float](https://github.com/change-42-yhmm/quota-float) 是挂在桌面上常驻显示的 **Codex 额度监视器**——直接从本机 [Codex Desktop](./tool-codex.md) 登录态读取真实的剩余额度 / 配额 / 重置时间，**不用估算、不改账户**，避免被误报 / 猜数误导。

## 关键能力

| 能力 | 说明 |
|------|------|
| 真实额度 | 直接读 Codex Desktop 登录态，不是估算 |
| 常驻悬浮 | 桌面小窗常驻，瞄一眼即得 |
| 重置时间 | 显示本次配额重置的剩余时间 |
| 不改账户 | 只读，不动账号 / 不改 token |

![quota-float 截图](https://pbs.twimg.com/media/HNhSq9IaYAANfOa.jpg)

## 相关概念

- [AI Meter](./tool-ai-meter.md) — macOS 菜单栏用量应用，通过 ccusage 实时显示各编码 Agent 的剩余预算
- [Token-Tracker](./tool-token-tracker.md) — 本地统计各 AI CLI 的 Token 消耗
- [AI Usage Dashboard](./tool-ai-usage-dashboard.md) — 本地 AI 用量仪表板，游戏血条形式展示

## 参考链接

- 项目链接: <https://github.com/change-42-yhmm/quota-float>
