---
type: Tool
title: "TokenUsageInsights（AI CLI Token 戰情室 / Session 还原看板）"
description: "AI CLI Token 用量与 Session 还原看板：读取本机 Antigravity / Copilot / Codex / Claude Code 等日志，集中展示每日 / 月度 / 年度 Token 消耗、费用估算与完整会话时间轴。"
resource: "https://github.com/doggy8088/TokenUsageInsights"
tags: [tool, token-usage, dashboard, cost-tracking, ai-cli]
timestamp: 2026-07-12T16:30:00Z
---

# TokenUsageInsights（AI CLI Token 戰情室 / Session 还原看板）

## 它是什么
本机运行的 Token 用量与会话还原看板：从本机 Antigravity / Copilot / Codex / Claude Code 等 AI CLI 日志中自动抽取数据，集中展示每日 / 月度 / 年度 Token 消耗、费用估算，并把每个会话的时间轴完整还原出来（供回顾 / 调试）。

## 为什么用它 / 适合什么场景
- 同时使用多款 AI CLI（Claude Code + Codex + Copilot），需要在统一面板里看总体用量 / 成本。
- 想回顾某个会话里 agent 做了什么（还原时间轴），而 CLI 本身没提供友好的回放。
- 关心每月账单，想按日 / 周 / 月拆分费用，识别异常消耗。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多 CLI 汇聚 | 读取 Antigravity / Copilot / Codex / Claude Code 等日志 |
| 多维度统计 | 每日 / 月度 / 年度 Token 消耗 |
| 费用估算 | 按模型单价换算费用 |
| Session 还原 | 完整还原会话时间轴，便于回顾与审计 |
| 本机运行 | 数据不外传 |

## 参考链接
- [项目链接](https://github.com/doggy8088/TokenUsageInsights)
- [原始链接](https://x.com/QingQ77/status/2076118846923051138)

![TokenUsageInsights 看板截图](https://pbs.twimg.com/media/HM7IeA6awAAatXX.jpg)

## 相关概念
- [AI Usage Dashboard（本地 AI 用量仪表板）](tool-ai-usage-dashboard.md) — 同类本地 AI 用量仪表板，但用「游戏血条」形式呈现
- [Token Tracker（本地统计各 AI CLI Token 消耗与可视化成本）](tool-token-tracker.md) — 同类 CLI Token 用量统计工具
- [QuickAI Claude Cost（本地 Claude Code transcript 剖析工具）](tool-quickai-claude-cost.md) — 同样聚焦 Claude Code transcript 拆解，按任务 / 子代理 / 模型维度统计
- [Retok（分析 Claude Code / Codex CLI 日志估算 token 成本）](tool-retok.md) — 同类日志分析 + 节省建议工具