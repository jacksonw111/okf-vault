---
type: "Tool"
title: "Terminal Browser（zenbu-labs/terminal-browser）"
description: "把一个网页浏览器直接塞进命令行终端，让编码 Agent 在同一标签页里打开、查看并操作网页；基于 kitty graphics 协议 + Electron 离屏渲染。"
resource: "https://github.com/zenbu-labs/terminal-browser"
tags: [terminal, kitty-graphics-protocol, electron, agent-tools, browser, ghostty, tmux]
timestamp: "2026-08-05T08:25:00Z"
---

# Terminal Browser（zenbu-labs/terminal-browser）

## 它是什么

**Terminal Browser** 把一个**网页浏览器**直接塞进**命令行终端**——让编码 Agent 在**同一个标签页**里打开、查看并操作网页。

原理：

- 终端支持 **kitty graphics protocol**（**ghostty / kitty / tmux / vscode** 都行）
- 用 **Electron 的离屏渲染**读 GPU 上的像素
- 画面吃进命令行**也不掉帧**

## 为什么用它 / 适合什么场景

- 编码 Agent 想直接**截图网页**、**填表单**、**点按钮**——不用切窗口。
- 终端里就能看到完整网页渲染，**所见即所得**。
- 想用 vim / tmux 工作流**不离开终端**。

## 关键能力

| 能力 | 说明 |
|------|------|
| Kitty graphics 协议 | 支持 ghostty / kitty / tmux / vscode 终端 |
| Electron 离屏渲染 | 真实 Chromium 渲染管线 |
| GPU 像素直读 | 不掉帧、流畅 |
| 同标签页操作 | Agent 不用切窗口 |
| 终端内可见 | 不需要 X11 / 远程桌面 |

## 参考链接

- [GitHub 仓库](https://github.com/zenbu-labs/terminal-browser)

## 相关概念

- [Tabminal](./tool-tabminal.md) — 同属「终端 + 浏览器 + AI」组合，但 Tabminal 是把三者收进**网页**，本工具是把浏览器收进**终端**
- [Herdr Browser](./tool-herdr-browser.md) — Herdr 终端面板嵌真实 Chromium 通过 CDP 驱动，本工具对照「kitty graphics vs CDP」