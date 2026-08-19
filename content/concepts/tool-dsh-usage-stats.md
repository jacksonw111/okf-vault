---
type: Tool
title: "dsh-usage-stats（Ychris12138/dsh-usage-stats）"
description: "为 DeepSeek Harness 网页端补的多供应商账户余额 + Token 用量监测，把各家后台分散的余额 / 额度 / 用量统计收进同一个侧边栏面板"
resource: "https://github.com/Ychris12138/dsh-usage-stats"
tags: "[deepseek-harness, dsh, usage, billing, multi-vendor]"
timestamp: "2026-08-19T16:00:00Z"
---

# dsh-usage-stats（Ychris12138/dsh-usage-stats）

## 它是什么
[`Ychris12138/dsh-usage-stats`](https://github.com/Ychris12138/dsh-usage-stats) 给 DeepSeek Harness（dsh）网页端**补一块**官方没做的面板：把多个 AI 服务商（DeepSeek / 火山方舟 / 硅基流动 等）后台分散的**账户余额、剩余额度、Token 用量统计**拉到 dsh 的同一个侧边栏里看。

## 为什么用它 / 适合什么场景
- 用 dsh 跑任务但要切换多家 API provider 时，每个供应商都得单独登录后台看余额，麻烦。
- 想在 dsh 内一眼看到「当前会话还剩多少额度」，避免任务跑到一半 429。
- 多账号分发请求时需要一个总览，而不是每家分别盯。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多供应商聚合 | 一个侧边栏汇总多家 AI 服务的余额与额度 |
| Token 用量统计 | 不只是余额，也呈现一段时间内的消耗趋势 |
| 原生集成 dsh | 作为 dsh 网页端的扩展面板插入，不另起应用 |
| 减少突发中断 | 跑任务时能提前看到快用尽的额度并切换账号 |

## 媒体
- ![dsh-usage-stats 截图](https://pbs.twimg.com/media/HP5IiEwaUAA51XG.jpg)

## 相关概念
- [项目仓库](https://github.com/Ychris12138/dsh-usage-stats) — 仓库主页
- [tokenscope](./tool-tokenscope.md) — 菜单栏实时显示 AI CLI 用量，按模型 / MCP / Skill 分解
- [ai_usage_dashboard](./tool-ai-usage-dashboard.md) — 游戏血条风格 AI 用量仪表盘