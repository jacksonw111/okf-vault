---
type: "Tool"
title: "tokentab"
description: "sequilade 写的本地 CLI：扫描 Claude Code / Codex / Cursor / Gemini CLI 留在磁盘上的会话日志，把 token 用量与花费算出，按模型 / 项目 / 日期 / 任务类别拆开列。纯本地运行，无云端依赖。"
resource: "https://github.com/sequilade/tokentab"
tags: [token-usage, cli, claude-code, codex, cursor, gemini-cli, cost-tracking]
timestamp: "2026-08-09T19:35:00Z"
---

# tokentab

## 它是什么

[tokentab](https://github.com/sequilade/tokentab) 是一个本地跑的 CLI：扫描各大 AI 编码助手（Claude Code / Codex / Cursor / Gemini CLI）在磁盘上留下的会话日志，提取 **token 用量与花费**，按**模型 / 项目 / 日期 / 任务类别**四维度拆开列出。**纯本地**，不向云端上报。

## 为什么用它 / 适合什么场景

- 想看「我这个月到底在 AI 编程上花了多少」——把分散在不同 CLI 里的 token 用量汇总到一张表。
- 想对比 Claude Sonnet / Opus / Haiku / GPT-4o 实际成本占比。
- 想在团队里分摊 AI 编程花费（按项目维度）。
- 想识别「哪类任务特别费 token」（任务类别维度），用以优化 prompt。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 CLI 兼容 | Claude Code / Codex / Cursor / Gemini CLI 的本地日志格式都解析 |
| 四维度拆分 | 模型 / 项目 / 日期 / 任务类别 |
| 本地运行 | 无云端上报，纯解析本地磁盘文件 |
| 可视化输出 | 表格 / 图表按维度展示 |
| 成本估算 | 基于各家公开 API 价格估算 USD / CNY |

## 媒体

![](https://pbs.twimg.com/media/HPK5r4AakAAmiKI.jpg)

## 相关概念

- [agentacct](./tool-agentacct.md) — 类似的本地 token 用量 + 费用仪表盘
- [GlassQuota](./tool-glassquota.md) — macOS 菜单栏实时显示 Codex / Gemini / Claude 三个 API 剩余额度