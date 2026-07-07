---
type: Tool
title: "Token Tracker"
description: "本地统计各 AI 命令行工具 Token 消耗、可视化 AI 使用成本的桌面仪表板。"
resource: "https://github.com/jaywcjlove/Token-Tracker"
tags: [tokens, ai-cost, cli, dashboard]
timestamp: "2026-07-07T12:00:00Z"
---

# Token Tracker

## 它是什么
一款本地运行的桌面仪表板，聚合 Claude Code、Codex CLI、Gemini CLI 等各类 AI 命令行工具的 Token 消耗，专注把 **AI 使用成本** 用直观的可视化方式呈现出来，帮助开发者在多 agent 工作流里掌握每条指令的「真实花费」。

## 为什么用它 / 适合什么场景
- **本地优先**：不上传任何对话历史，所有统计只在本地聚合。
- **多 CLI 兼容**：不以单个 SDK 为中心，直接读各 CLI 输出 / 日志 / 配置目录。
- **成本可视化**：当月 token、费用估算、按模型 / 工具分解。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多 CLI 聚合 | 同时追踪 Claude Code / Codex / Gemini CLI 等 |
| Token 统计 | 输入 / 输出 / 缓存 token 分类计数 |
| 成本估算 | 按各 CLI 默认费率折算人民币/美元 |
| 可视化 | 时间序列图、当日明细、按模型分布 |
| 本地运行 | 数据只在本地，不上传对话内容 |

## 相关概念
- [tokenscope](tool-tokenscope.md) — macOS / Windows 菜单栏实时显示 Claude CLI token 用量，同为「本地优先 token 成本追踪」，一个偏桌面仪表板，一个偏菜单栏弹窗
- [ai_usage_dashboard](tool-ai-usage-dashboard.md) — 本地 AI 用量仪表板，以游戏血条形式展示各 AI 提供商用量 / 配额
- [ai-media-assistant](tool-ai-media-assistant.md) — 文案 / 字幕 / 配图 / TTS 全流程可视化的创作工具
