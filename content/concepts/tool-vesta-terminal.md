---
type: Tool
title: "Vesta"
description: "macOS 原生终端，Swift/AppKit 写，直接调 GhosttyKit（libghostty）的 Metal 渲染引擎；最大特点是 session 持久化（vestad 守护进程 hold PTY 与最近 256KB 输出，应用退出再开 Shell 内容原样恢复），并可直接用现有 ~/.config/ghostty/config。"
resource: "https://github.com/vestaterm/Vesta"
tags: "[terminal, macos, ghostty, session-persistence, swift, ai-coding-agent]"
timestamp: "2026-07-02T09:10:00Z"
---

# Vesta

## 它是什么
macOS 原生终端应用，Swift + AppKit 写。底层**不 fork Ghostty**，而是直接调 GhosttyKit（libghostty）的 Metal 渲染引擎。

## 为什么用它 / 适合什么场景
- macOS 上跑 AI 编程 agent（Claude Code、Codex CLI、pi 等）需要**多会话并行**且**session 不丢**——Vesta 专为这种场景设计。
- 想用 Ghostty 的渲染速度与配置（直接复用 `~/.config/ghostty/config`），但不喜欢 Ghostty 的某些会话管理行为。
- 应用退出再打开，Shell 状态、滚动位置、最近 256KB 输出都原样恢复。

## 关键能力
| 能力 | 说明 |
|------|------|
| 平台 | macOS 原生 |
| 技术栈 | Swift + AppKit + libghostty (Metal) |
| 配置兼容 | 直接用现有 `~/.config/ghostty/config`，无需额外配 |
| Session 持久化 | `vestad` 守护进程 hold PTY 与最近 256KB 输出 |
| 恢复 | 应用退出再打开 Shell 和内容原样恢复 |
| 多会话 | 可并行开多个 AI agent 会话 |
| CLI 控制 | 可用 CLI 脚本控制 |
| 形态 | macOS 原生终端（非 Ghostty 分支） |

## 相关概念
- [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — 同为「Claude Code 多会话管理」思路；mux 是 tmux 插件，Vesta 是终端本体
- [Ghostty](tool-lex-ghostty-shaders.md) — 终端本身（这里有 lex-ghostty-shaders 是 shader 主题）
- [pi-desktop](tool-pi-desktop.md) — Pi Coding Agent 桌面外壳；Vesta 是终端，pi-desktop 是 Pi 的壳

## 项目链接
- 项目主页：<https://github.com/vestaterm/Vesta>

## 媒体
![](https://pbs.twimg.com/media/HMHgv2maIAAmx-a.jpg)