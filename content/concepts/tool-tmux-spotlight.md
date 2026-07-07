---
type: Tool
title: "tmux-spotlight"
description: "纯 Bash + fzf 的轻量 tmux 插件，提供 macOS Spotlight 风格的应用切换体验，按下快捷键弹出圆角窗口显示所有标签页的实时内容预览。"
resource: "https://github.com/MeinardEdrei/tmux-spotlight"
tags: [tmux, productivity, plugin]
timestamp: "2026-07-07T12:00:00Z"
---

# tmux-spotlight

## 它是什么
`MeinardEdrei/tmux-spotlight` —— 纯 Bash + fzf 实现的 **轻量 tmux 插件**，把 **macOS Spotlight 风格的应用切换体验** 带入 tmux：按下快捷键后弹出圆角窗口，内含所有标签页的 **实时内容预览**，并对齐成整齐的纵向网格。

## 为什么用它 / 适合什么场景
- 工作流重度依赖 tmux，想用 **可视化预览** 切换标签页而非猜编号。
- 不想装额外重量级工具，仅用现有 fzf 即可。
- 适合密集跑多标签页（log / build / REPL / htop）的开发者。

## 关键能力
| 能力 | 说明 |
|------|------|
| Spotlight 风格 UI | 圆角窗口 / 实时预览 / 纵向网格对齐 |
| 实时标签预览 | 直接看到每个标签页中的内容缩略 |
| 纯 Bash + fzf | 不引入额外重型依赖 |
| 快捷键集成 | tmux 内任意时刻按绑定键即可调出 |
| 轻量 | 几乎没有额外资源开销 |

## 相关概念
- [tmux-workbench](tool-tmux-workbench.md) — Rust 写的 tmux 会话记忆管理器
- [mux（Claude Code tmux 插件）](tool-mux-claude-tmux.md) — tmux 浮动面板管理多个 Claude Code 会话
- [Tree Style Tab（rammcodes 类似的 IDE 风格树组件）](tool-trees-rammcodes.md) — IDE 风格文件树组件
