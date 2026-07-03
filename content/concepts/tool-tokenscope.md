---
type: Tool
title: "tokenscope"
description: "macOS / Windows 菜单栏实时显示 Claude CLI 的 token 用量、费用估算和按模型 / MCP / Skill 的消耗分解；支持日 / 周 / 月切换、成本环形图、年度活动热力图；自动去重流式与重试重复数据；24 小时离线缓存；Homebrew 一键装。"
resource: "https://github.com/HduSy/tokenscope"
tags: "[claude-code, token-usage, cost-tracking, menu-bar, macos, windows, homebrew, mcp, skill]"
timestamp: "2026-07-03T14:38:00Z"
---

# tokenscope

## 它是什么
**macOS / Windows 菜单栏小工具**，实时显示 Claude CLI 的 **token 用量、费用估算和按模型 / MCP / Skill 的消耗分解**。

支持日 / 周 / 月切换，按 **模型**、**MCP 调用**、**Skill 调用** 三种维度分解消耗，配 **成本环形图** 和 **年度活动热力图**。自动去重流式响应与重试产生的重复 token 数据；模型定价从公开 `models` 表和 LiteLLM 获取，**24 小时缓存**，断网也能看历史。

由 HduSy 开发。

## 为什么用它 / 适合什么场景
- 长期用 Claude Code / Codex，担心月底账单爆炸——希望随时看到「今天花了多少」。
- 想分清是**哪个模型**、**哪个 MCP 工具**、**哪个 Skill**最费 token——以便优化。
- 喜欢菜单栏小工具，不愿每次开 CLI 跑 `claude usage`。
- 多人共用一个 Claude API key，想知道团队或个人贡献。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | macOS / Windows |
| 形态 | 菜单栏应用 |
| 实时指标 | token 用量 + 费用估算 |
| 时间维度 | 日 / 周 / 月切换 |
| 消耗分解 | 按模型 / MCP 调用 / Skill 调用 |
| 可视化 | 成本环形图 + 年度活动热力图 |
| 数据清洗 | 自动去重流式响应 + 重试产生的重复 token |
| 定价来源 | 公开 `models` 表 + LiteLLM |
| 离线缓存 | 24 小时缓存（断网可看历史） |
| 安装 | macOS Homebrew 一键；Windows 安装包 |

## 相关概念
- [shuangzi-xubei（双子续杯）](tool-shuangzi-xubei.md) — iPhone 桌面小组件看 Claude Code / Codex 额度；tokenscope 偏 macOS / Windows 菜单栏 + 详细分解
- [Orca（stablyai）](tool-orca-coding-ide.md) — Coding IDE 套壳含 Token 追踪；tokenscope 是独立菜单栏工具
- [Vesta（macOS 终端）](tool-vesta-terminal.md) — macOS 原生终端为 AI 编码多会话设计；tokenscope 不做终端而是监控用量

## 项目链接
- 项目主页：<https://github.com/HduSy/tokenscope>

## 媒体
![](https://pbs.twimg.com/media/HMRSJg4bwAAGk4_.jpg)