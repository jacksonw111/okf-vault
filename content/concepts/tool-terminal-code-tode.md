---
type: Tool
title: "terminal-code / tode（终端里的 VS Code）"
description: "zenbu-labs 开源，把 terminal-browser（终端里能跑的可交互浏览器）和 code-server（浏览器里的 VS Code）串起来，让 VS Code 不开浏览器也能直接在终端里跑，命令名 tode。"
resource: "https://github.com/zenbu-labs/terminal-code"
tags: [terminal, vscode, code-server, tui, ide]
timestamp: 2026-08-21T15:28:00Z
---

# terminal-code / tode（终端里的 VS Code）

## 它是什么
zenbu-labs/terminal-code 是一个把「终端里的浏览器」和「浏览器里的 VS Code」两端互串的复合工具。底层是 code-server（VS Code Web 版），但通过 terminal-browser 在终端里以可交互的方式渲染并接收键盘输入；最终用一个统一的命令 `tode` 启动，直接在命令行里打开一整套 VS Code 体验——不需要 Chromium / Edge / Safari 介入。

## 为什么用它 / 适合什么场景
- 服务器上想编辑文件却不想开图形界面（SSH 进去直接 `tode`）。
- 想保留终端肌肉记忆、又把 VS Code 的 LSP / 补全 / 文件树 / Git 集成带在身边。
- 演示 / 教学：把屏幕分享只开一个终端窗口就够，里面既能编辑也能预览。

## 关键能力
| 能力 | 说明 |
|------|------|
| `tode` 命令 | 一个二进制命令，启动后直接在终端里渲染可交互 VS Code |
| code-server 复用 | 完整继承 VS Code 扩展生态与 LSP，补全 / 定义跳转 / Git 都在 |
| terminal-browser 渲染 | 不依赖本地浏览器，把 Web UI 当 TUI 控件接收键盘 |
| 终端友好 | SSH / tmux / Zellij / 远程开发机场景同样适用 |

## 一句话总结
**VS Code 不开浏览器，直接在终端里跑——`tode` 一条命令。**

## 原始链接
- [zenbu-labs/terminal-code](https://github.com/zenbu-labs/terminal-code) — 原始仓库

## 相关概念
- [Codex CLI](./tool-codex-cli.md) — 另一种「终端里的代码智能体」
- [Pi Coding Agent](./tool-pi-fabric.md) — 同属「终端原生 AI 编码」系