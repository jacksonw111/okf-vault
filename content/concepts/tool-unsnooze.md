---
type: Tool
title: "unsnooze"
description: "针对 Claude Code、Codex、Grok、Qwen、Kimi、OpenCode、Antigravity 等 AI 编码会话的\"用量墙\"恢复工具：在 5 小时 / 每周额度归零那一刻自动唤醒被中断的会话；终端侧走 tmux/Zellij，桌面端走 VS Code 扩展与独立 app。"
tags: "[quota, rate-limit, recovery, claude-code, codex, tmux, vscode, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/saaranshM/unsnooze"
---

# unsnooze

针对 **Claude Code、Codex、Grok、Qwen、Kimi、OpenCode、Antigravity** 等 AI 编码会话的**"用量墙"恢复工具**——在 **5 小时 / 每周额度归零那一刻**自动唤醒被中断的会话。终端走 **tmux / Zellij**，桌面端走 **VS Code 扩展**与独立 **app**。

## 它是什么

- 一个**专门对付"用量墙"**的工具：当 Claude Code / Codex 等因为**5 小时窗口**或**周配额**耗尽而**挂起（snooze）**会话时，本工具在**额度恢复的那一刻**自动把会话**唤醒（unsnooze）**；
- 跨**多厂商 / 多客户端**：Claude Code、Codex、Grok、Qwen、Kimi、OpenCode、Antigravity 都在覆盖范围；
- 双形态：**终端用户**走 tmux / Zellij 集成；**桌面用户**走 VS Code 扩展 + 独立 app。

## 关键能力

| 能力 | 说明 |
|------|------|
| 用量墙识别 | 检测各厂商 5 小时窗口 / 周配额耗尽状态 |
| 跨厂商 | Claude Code / Codex / Grok / Qwen / Kimi / OpenCode / Antigravity |
| 定时唤醒 | 在额度恢复时刻自动恢复被挂起的会话 |
| tmux / Zellij | 终端侧：与会话复用层集成 |
| VS Code 扩展 | 桌面侧：编辑器里直接管理 |
| 独立 app | 桌面侧：脱离编辑器也能用 |

## 为什么用它 / 适合什么场景

- **Claude Code / Codex 重度用户**经常被 **5 小时限额**和**周配额**卡住——本工具让你不必**盯着倒计时**，到点自动续；
- 跑**长任务**（迁移、重构、批量改文件）不希望**半夜额度恢复时还要爬起来**手动 resume；
- 同时用**多个 AI 编码 CLI**（Claude Code + Codex + Qwen 之类），希望**统一处理**它们的额度周期；
- **团队 / 多人共享**：把恢复策略做成一个工具，成员各自挂上；
- 把"**额度周期管理**"从**人工**变成**基础设施**——类似 cron 把定时任务自动化。

## 设计哲学

1. **额度墙不是终点**——它只是暂停，本工具负责"取消暂停"；
2. **跨厂商通用**——各家窗口不同，但"恢复时唤醒"是同一个动作；
3. **不替代模型**——只做"状态管理"，不抢 AI CLI 本身的会话；
4. **终端 + 桌面双形态**——选哪种工作流都行。

## 预览

![](https://pbs.twimg.com/media/HNEsYh5agAAMKsn.jpg)

## 相关概念

- [shuangzi-xubei（双子续杯）](tool-shuangzi-xubei.md) — iPhone 桌面小组件，锁屏一眼看 Claude Code / Codex 额度，与本工具"额度管理"主题一致
- [TokenUsageInsights](tool-token-usage-insights.md) — AI CLI Token 战情室 + Session 还原看板，从"看清额度"角度补全本工具的"管理额度"