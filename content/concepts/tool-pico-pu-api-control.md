---
type: "Tool"
title: "pico-pu-api-control"
description: "常驻系统托盘的 API 余额仪表盘：轻量、本地优先，定时显示各 AI 服务商的余额与剩余比例，不用打开网页逐个查。"
resource: "https://github.com/ANDRETRIPOL/pico-pu-api-control"
tags: ["tray", "dashboard", "api", "ai-balance", "local-first", "monitoring"]
timestamp: "2026-08-12T02:38:00Z"
---

# pico-pu-api-control

[pico-pu-api-control](https://github.com/ANDRETRIPOL/pico-pu-api-control) 是一个**常驻系统托盘的 API 余额仪表盘**：轻量、本地优先，定时显示各 AI 服务商的余额与剩余比例，不用打开网页逐个查。

## 它是什么

桌面小工具，挂在系统托盘 / 菜单栏里，**周期性轮询**主要 AI 服务商的账户余额 / 用量 / 剩余比例，让你看一眼托盘图标就知道"这个月还有多少 token 可以烧"。

## 为什么用它 / 适合什么场景

- **多 provider 用户**：同时用 OpenAI / Anthropic / Google / 其他服务的人。
- **避免超支**：提前看到余额告警。
- **本地优先**：敏感 API key 不外发，数据不外传。
- **轻量无打扰**：常驻托盘，不弹窗不打扰。

## 关键能力

| 能力 | 说明 |
|------|------|
| 托盘常驻 | 菜单栏 / 系统托盘图标直接看 |
| 多 provider 余额 | 聚合多个 AI 服务商数据 |
| 定时刷新 | 后台周期轮询 |
| 余额 / 剩余比例 | 直观显示还能用多少 |
| 本地优先 | key 与数据本地处理 |

## 媒体

![](https://pbs.twimg.com/media/HPaDaIfaQAA7kY1.jpg)

## 参考链接

- [项目仓库](https://github.com/ANDRETRIPOL/pico-pu-api-control)

## 相关概念

- [GlassQuota](./tool-glassquota.md) — macOS 实时显示 Codex / Gemini / Claude API 剩余用量，同属 API 余额仪表盘
- [Clabar](./tool-clabar.md) — macOS 菜单栏 Claude 用量监控，与本工具同属"菜单栏 + AI 服务监控"范式