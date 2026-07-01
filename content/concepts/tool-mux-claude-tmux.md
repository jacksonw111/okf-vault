---
type: Tool
title: "mux（Claude Code tmux 插件）"
description: "fashton28 写的 tmux 插件，给 Claude Code 多会话管理用。一个快捷键唤出浮动面板，列出所有正在跑的 Claude Code 会话，按等待时间倒排，一眼定位需要处理的会话。"
tags: "[tmux, claude-code, plugin, session-manager]"
timestamp: "2026-07-01T07:10:00Z"
resource: "https://github.com/fashton28/mux"
---

# mux（Claude Code tmux 插件）

## 它是什么
fashton28 写的 tmux 插件，专为 Claude Code 重度用户设计。当同时开多个 Claude Code 会话（不同项目 / 不同任务），一个快捷键就能在 tmux 浮动面板里看到所有会话状态。

## 为什么用它 / 适合什么场景
- 同时开多个 Claude Code 会话，记不清哪个在等、哪个卡了
- 经常从一堆终端窗口里找需要回应的那个
- 已经在用 tmux 作为开发环境

## 关键能力
| 能力 | 说明 |
|------|------|
| 浮动面板 | 按快捷键即呼出，覆盖在当前 pane 之上 |
| 全会话列表 | 一屏展示所有正在跑的 Claude Code 会话 |
| 状态分类 | 「等你输入」/「跑完」/「卡住」三种状态一目了然 |
| 按等待时间倒排 | 最久没回应的排最前，优先处理 |
| 纯 tmux 原生 | 不开额外端口 / 不依赖 Node / 不需要 Docker |

## 相关概念
- [Claude Code](tool-claude-code.md) — mux 服务的目标 Agent
- [Claude Code best practice](tool-claude-code-best-practice.md) — 60k+ 星 Claude Code 资源合集，多会话管理是其中重要议题
- [Orca](tool-orca-coding-ide.md) — 另一种多 Agent 并行管理方案，但走 GUI 而非终端

## 原始链接
- [项目仓库](https://github.com/fashton28/mux)
- [截图](https://pbs.twimg.com/media/HMEg9U0WQAAByLS.jpg)