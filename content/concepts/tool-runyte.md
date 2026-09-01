---
type: "Tool"
title: "Runyte（终端里的开发工作区：编辑器 + 文件 + 终端 + Git 一体化）"
description: "Rust 写的终端编辑器兼开发工作区：模态编辑、selection-first + 多重光标、按键风格像 Helix（Vim 常用动作有别名）；文件浏览器、终端会话、Git 和语言工具共用同一批面板、命令和主题，Tab 切换、一处剪贴板、可在不同 Git worktree 之间跳转。"
resource: "https://github.com/runyte/runyte"
tags: [terminal-editor, rust, helix, vim, modal-editing, git, ide, tui]
timestamp: "2026-09-01T00:30:00Z"
---

# Runyte

## 它是什么
[Runyte](https://github.com/runyte/runyte) 是一个**终端里的开发工作区**：把**模态编辑器、文件管理器、终端复用、Git 和可分离的持久会话**全部装进同一个 TUI 界面。Rust 写的，主打「**selection-first + 多重光标**」，按键风格像 **Helix**，Vim 常用动作也都给了别名。

与「编辑器 + 终端复用器」的常见组合不同，Runyte 把「文件浏览器 / 终端会话 / Git / 语言工具」做成**同一批面板、同一套命令、同一套主题**——一处剪贴板、什么都能**模糊搜索**，还能在**不同 Git worktree 之间跳转**。

## 为什么用它 / 适合什么场景
- 想把「**编辑器 + 文件管理 + 终端复用 + Git**」**集中**到一个 TUI 里，少开几个窗口；
- 喜欢 **Helix 风格**的选择优先 + 多重光标，又想有 Vim 别名兼容；
- 想在终端里**跨 Git worktree** 跳转——主仓开发、热修复仓切换不用切换窗口；
- 想用一个**面板、命令、主题统一**的环境，而不是「每个插件各搞一套」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模态编辑 | Helix 风格选择优先 + 多重光标 |
| Vim 别名 | Vim 常用动作都有别名 |
| 文件浏览器 | 内置文件树面板 |
| 终端复用 | 多 shell session 同窗口 |
| Git 集成 | 同面板跑 Git 操作 |
| 语言工具 | LSP / 诊断共享主题 |
| 统一剪贴板 | 跨面板一处剪贴 |
| 模糊搜索 | 什么都能模糊搜索 |
| Git worktree 跳转 | 在多个 worktree 间快速切换 |
| 可分离会话 | 持久会话可脱离重连 |
| Rust 实现 | 性能与并发安全 |

## 媒体
![](https://pbs.twimg.com/media/HRBE3-waQAAUPBq.jpg)

## 相关概念
- [CleeCode](tool-cleecode.md) — 同样是「编辑器 + 文件树 + shell」一体化的终端 IDE；CleeCode ratatui 风格、Runyte Helix 风格
- [Shoin / 書院](tool-shoin.md) — 同为终端编辑器；Shoin 是极简 Markdown 编辑器、Runyte 是完整工作区

## 参考链接
- 项目链接：<https://github.com/runyte/runyte>