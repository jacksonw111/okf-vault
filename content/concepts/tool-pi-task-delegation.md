---
type: "Tool"
title: "pi-task（Pi 编码 Agent 的子任务委派扩展）"
description: "pi-task = heyhuynhgiabuu/pi-task：给 Pi 编码 Agent 加上「委派子任务」能力的扩展。让 Pi 能派生出专门干活的子代理，前台跑就等着拿结果，后台跑不耽误主会话；后台任务在 TUI 显示进度条，跑完自动把结果塞回给父代理。"
resource: "https://github.com/heyhuynhgiabuu/pi-task"
tags: "[pi, agent, subagent, task-delegation, tui, async]"
timestamp: "2026-06-21T16:12:00Z"
---

# pi-task（Pi 编码 Agent 的子任务委派扩展）

## 它是什么

**pi-task**：给 [Pi](https://github.com/badlogic/pi-mono) 编码 Agent 加上的**子任务委派扩展**。让 Pi 能派生出一个（或多个）专门干活的子代理：**前台模式**等子代理跑完拿结果，**后台模式**不打断主会话继续交互。后台任务在 Pi 的 TUI 里显示进度条，跑完了自动把结果塞回父代理。

## 为什么用它 / 适合什么场景

- 长任务（跑测试、生成报告、批量改文件）不想阻塞主对话。
- 想让 Pi「并行开多个 worker」——一个写代码、一个查文档、一个跑测试。
- 想要一个轻量、原生的「子代理」机制，而不是接 LangGraph / AutoGen 这种重型框架。

## 关键能力

| 能力 | 说明 |
|------|------|
| 子代理派生 | Pi 可派生子代理执行子任务 |
| 前台模式 | 同步等待子代理返回结果 |
| 后台模式 | 异步执行，主会话不阻塞 |
| 进度可视化 | 后台任务在 Pi TUI 显示进度条 |
| 结果回传 | 后台任务完成后，结果自动塞回父代理上下文 |

## 适用边界

- 依赖 Pi 这个特定 Agent 框架（不是 Claude Code / Cursor 的扩展）。
- 子代理的数量 / 资源消耗需要 Pi 主进程做调度，OOM 风险仍归 Pi。

## 媒体

- 截图：![](https://pbs.twimg.com/media/HLS_fgwbkAA3C5i.png)

## 相关概念

- [Claude Code](tool-claude-code.md) — 同为「终端编码 Agent」，但 Claude Code 走 Anthropic 协议；pi-task 给的是 Pi 这个 Agent
- [ORGII](tool-orgii.md) — 同为「多 Agent 协作框架」的思路，但 ORGII 是 Rust + Tauri 的独立应用
- [Vercel Eve 框架](tool-vercel-eve-framework.md) — 同为「Agent 框架 / 扩展点」的思路，但 Eve 走 filesystem convention