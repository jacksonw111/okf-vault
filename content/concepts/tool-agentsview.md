---
type: Tool
title: "agentsview"
description: "本地优先的 AI 编码助手会话搜索、分析与 Token 费用跟踪工具。"
resource: "https://github.com/kenn-io/agentsview"
tags: [ai-coding, session-log, search, cost]
timestamp: "2026-07-07T12:00:00Z"
---

# agentsview

## 它是什么
`kenn-io/agentsview` —— 一款 **本地优先的 AI 编码助手会话搜索 / 分析 / Token 费用跟踪工具**。Claude Code / Codex / Gemini CLI 等 agent 把日常会话都存到本地，但缺乏一个"端到端搜索 + 成本视图"工具，agentsview 补上这一环。

## 为什么用它 / 适合什么场景
- 想要快速 **搜索历史上某次对话**："上次我让 Claude 写的那段 dock 配置在哪？"
- 想看 **每月各类 agent 的 Token 与费用分布**。
- 想给本地 agent 数据提供「可逆编辑」和「标签 / 收藏」等管理能力。
- 本地优先：数据不离本机。

## 关键能力
| 能力 | 说明 |
|------|------|
| 跨 agent 搜索 | 同时索引 Claude Code / Codex / Gemini CLI 等本地会话 |
| Token 成本 | 按 agent / 模型 / 项目统计 Token 与费用 |
| 会话分析 | 历史会话可视化与回顾 |
| 本地优先 | 所有数据保存在本机 |
| 多 agent 兼容 | 多模型混合场景下的统一视图 |

## 相关概念
- [Token Tracker](tool-token-tracker.md) — 本地统计各 AI CLI Token 消耗、可视化成本
- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量
- [kcap-cli](tool-kcap-cli.md) — 给 AI 编码助手的可观测性 CLI，会话生命周期 / 工具调用 / token 用量
- [Loop Engineering](tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论 + 三个 CLI
