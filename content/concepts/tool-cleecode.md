---
type: "Tool"
title: "CleeCode（Rust 终端 IDE，编辑器 + 终端同窗）"
description: "Rust 写的终端 IDE，基于 ratatui/crossterm：编辑器、文件树与真 shell 终端共处一窗，免切换；200+ 语言高亮、多标签、分屏、列选、git 面板、LSP 支持。"
resource: "https://github.com/msavox/cleecode"
tags: [rust, tui, terminal, ide, editor, ratatui, lsp]
timestamp: "2026-08-31T16:00:00Z"
---

# CleeCode

## 它是什么

[CleeCode](https://github.com/msavox/cleecode) 是 [msavox](https://github.com/msavox) 用 **Rust** 编写的**终端 IDE**，界面基于 [`ratatui`](https://ratatui.rs/) + [`crossterm`](https://github.com/crossterm-rs/crossterm)。最与众不同的设计：**编辑器 + 文件树 + 真正的 shell 终端共处一窗**，中央不再需要切换。

## 为什么用它 / 适合什么场景

- **想要 Neovim + 终端一体化**：vim 党频繁切换窗口的痛点解决方案；
- **极客极简**：纯 TUI，所有操作键盘可达；
- **多语言项目**：200+ 语言高亮 + LSP 支持，应对各种栈；
- **远程服务器开发**：ssh 进 Linux 服务器，IDE 直接跑在远程。

## 关键能力

| 能力 | 说明 |
|------|------|
| 同窗三件套 | 编辑器 / 文件树 / shell 终端一窗共处 |
| 200+ 语言高亮 | 覆盖主流语言 |
| 多标签 + 分屏 | 一窗多 buffer |
| 正则搜索替换 | 包括 capture group |
| 代码折叠 + 列选 | 编辑器标准能力 |
| git 面板 | 可视化 diff / stage / commit |
| LSP 支持 | 代码补全 / 跳转 |
| Markdown 工具条 | Markdown 文件上浮一条按钮条，按钮显示实际写入字符 |

## 媒体

- 项目截图：![](https://pbs.twimg.com/media/HRBBv4taYAALt0H.jpg)
- 项目截图：![](https://pbs.twimg.com/media/HRBBxYza0AAbytB.jpg)

## 相关概念

- [Lody](tool-lody.md) — 多 AI 编码 Agent 协作的桌面工作空间

## 参考链接

- 项目链接：<https://github.com/msavox/cleecode>