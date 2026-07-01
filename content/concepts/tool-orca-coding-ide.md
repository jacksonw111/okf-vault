---
type: Tool
title: "Orca（stablyai）"
description: "stablyai 开源的 Coding IDE 套壳，跨 Mac/Win/Linux 全平台，支持 Claude Code / Codex / pi / opencode 等所有主流 Coding agent CLI，主打「最强大套壳」+ 并行 worktree + computer use + 登录态浏览器 + 移动端远程控制。"
tags: "[coding-ide, agent, desktop, multi-platform]"
timestamp: "2026-07-01T13:30:00Z"
resource: "https://github.com/stablyai/orca"
---

# Orca（stablyai）

## 它是什么
stablyai 开源的 Coding IDE 桌面应用，定位是「Codex App 的开源平替/超越品」。跨 Mac/Win/Linux 三平台，内嵌真实 Chromium + Design Mode，能套 Claude Code / Codex / pi / opencode 等所有主流 Coding agent CLI。

## 为什么用它 / 适合什么场景
- 想给编码 Agent 一个图形界面而非纯终端
- 同时跑多个 Agent（CC + Codex + pi）并对比结果
- 想在 IDE 内直接做「computer use」（类似 Codex 的电脑操作能力）
- 想远程控制本机的编码工作流（手机端 Orca Mobile App）
- 想在浏览器里调试 Agent 在登录态下的操作（@chrome 风格）

## 关键能力
| 能力 | 说明 |
|------|------|
| 跨平台 | Mac / Windows / Linux 全平台同一体验 |
| 多 Agent 兼容 | Claude Code / Codex / pi / opencode 等主流 CLI 全支持 |
| 并行 worktree | 同一时刻跑多个 Agent 在不同 worktree 互不干扰 |
| Computer use | Agent 能直接操作电脑（类似 Codex app） |
| 登录态浏览器 | 类似 Codex @chrome，Agent 可在已登录的浏览器里操作 |
| 内嵌 Chromium + Design Mode | 浏览器内可视化编辑页面 |
| Orca Mobile | 手机端 App 远程控制电脑 |
| 自动化 | 定时任务 / loop engineering |
| 语音输入 | 桌面端按住说话直接喂给 Agent |
| iOS / Android 模拟器 | 在桌面里跑移动端模拟器调试移动 web |
| 远程主机控制 | 管理远程机器的 Agent |
| Token 使用追踪 | 全局可视化每个 Agent 消耗 |
| GitHub / Linear 原生集成 | PR / issue / 看板里直接开 |
| orca CLI | 命令行版本，CI / 脚本友好 |

## 相关概念
- [Aura-IDE](tool-aura-ide.md) — 另一种 Planner/Worker 双智能体本地编码工作台
- [Claude Code](tool-claude-code.md) — Orca 主要承接的 CLI 之一
- [PeakCode](tool-peakcode.md) — 多 Agent 会话统一 GUI，可与 Orca 形成「GUI 套壳 + 多代理面板」组合
- [pi-desktop](tool-pi-desktop.md) — Pi Coding Agent 原生桌面外壳（更轻量、更聚焦 Pi）

## 原始链接
- [项目主页](https://www.onorca.dev/)
- [项目仓库](https://github.com/stablyai/orca)
- [截图 1](https://pbs.twimg.com/media/HMCJKM8WgAAGnBr.jpg)
- [截图 2](https://pbs.twimg.com/media/HMCJSr6XgAExKc7.jpg)
- [截图 3](https://pbs.twimg.com/media/HMCJaZiWAAIpz5H.jpg)
- [截图 4](https://pbs.twimg.com/media/HMCJe1xXcAAD-rE.jpg)