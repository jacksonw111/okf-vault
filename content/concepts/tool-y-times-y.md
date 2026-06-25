---
type: Tool
title: "y-times-y / y（可自我修改的桌面编程智能体）"
description: "可自我修改的桌面编程智能体应用：默认聊天窗口 + 内置 Modify 系统可实时编辑 UI、改完看到 diff，满意保留、不满意回滚；并行运行 Claude Code 与 Codex。"
resource: "https://github.com/y-times-y/y"
tags: [agent, desktop, claude-code, codex, self-modifying, tauri]
timestamp: "2026-06-25T12:14:00Z"
---

# y-times-y / y

## 它是什么

一个**可自我修改的桌面编程智能体应用**。它假设「软件应该能用着用着就自己变」：默认界面是聊天窗口，但内置一套 Modify 系统，**允许实时编辑应用自身的 UI**。改完能立刻看到 diff，满意就保留，不满意就一键回滚。

另一个关键能力：**并行**运行 Claude Code 和 Codex 两个编码 agent。

## 为什么用它

- 把「agent 写 UI → 用户审 UI → 落盘」压成一个**本地闭环**，不用切 IDE。
- 自我修改意味着 agent 与自己运行的环境**没有边界**，对原型期非常友好。
- 多 agent 并行让你「用最强模型写一份 + 用便宜模型做对照」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 默认 UI | 聊天窗口 |
| Modify 系统 | 实时编辑 UI 的可视化 diff |
| 回滚 | 不满意可一键恢复 |
| 多 agent | 并行 Claude Code + Codex |
| 桌面 | 本地应用（无云端依赖） |

## 媒体

![](https://pbs.twimg.com/media/HLoOEP1aYAAsv8R.jpg)

## 相关概念

- [Aura-IDE](./tool-aura-ide.md) — 同为「写文件前先显示 diff 让用户审批」的本地 AI 编码工作台，思路相近但 y 更激进（允许改自身 UI）
- [PeakCode](./tool-peakcode.md) — 多 AI 编码代理会话统一 GUI，y 的多 agent 并行思路可对照
- [Claude Code](./tool-claude-code.md) — y 内嵌的编码 agent 之一
- [CodexPro](./tool-codexpro.md) — 另一个被并行使用的编码 agent