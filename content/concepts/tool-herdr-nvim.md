---
type: Tool
title: "herdr-nvim（把 Neovim 嵌进 herdr 工作区）"
description: "ChmaraX/herdr-nvim：把 Neovim 直接嵌入 herdr 工作区，让编辑器 / AI agent 改过的文件 / 代码批注在同一处打通"
resource: "https://github.com/ChmaraX/herdr-nvim"
tags: [neovim, herdr, editor-integration, coding-agent, code-review]
timestamp: "2026-08-23T11:40:00Z"
---

# herdr-nvim（把 Neovim 嵌进 herdr 工作区）

## 它是什么

[ChmaraX/herdr-nvim](https://github.com/ChmaraX/herdr-nvim) 把 **Neovim 直接嵌入 herdr 工作区**，让**编辑器**、**AI agent 改过的文件**、**代码批注**在同一处打通——AI 改了什么、审了什么、留了什么批注，全在一个工作台里。

## 为什么用它 / 适合什么场景

- 用 herdr（终端 AI 编码 agent）做开发，但同时还想用 Neovim 的编辑能力。
- 想把 AI 改的代码 + 人工批注整合到一个工作区，不用在两个工具间来回切。
- 喜欢 Neovim 的键位 / 生态，又不愿放弃 AI 编码助手。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内嵌 Neovim | herdr 工作区里直接调出 nvim |
| 文件改动贯通 | AI 改的文件立即出现在 Neovim 里 |
| 代码批注贯通 | 批注与编辑器共用上下文 |
| 与 herdr 协同 | 同 herdr 的会话 / 任务状态挂钩 |

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2091361887531446272/vid/avc1/1920x1080/WSuqWrsMaUCDTXFN.mp4?tag=29>

## 相关概念

- [herdr-reviewr](./tool-herdr-reviewr.md) — 同 herdr 生态的代码审查侧栏
- [juggler](./tool-juggler-ai.md) — 同样「可视化工作台 + 编辑器一体化」的 AI 编码 agent
- [PeakCode](./tool-peakcode.md) — 多代理会话统一 GUI + Git 工作流

## 参考链接

- [项目链接](https://github.com/ChmaraX/herdr-nvim)
