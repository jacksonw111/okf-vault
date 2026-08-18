---
type: Tool
title: "dsh-tianshu-tui (huiliyi37/dsh-tianshu-tui)"
description: "官方 DeepSeek Harness 的交互式终端界面（TUI）：自研 ANSI 渲染、流畅滚动，并在官方能力外加 TDD 驱动、证据门、视觉图像模块几条个性化工作流"
resource: "https://github.com/huiliyi37/dsh-tianshu-tui"
tags: [deepseek, harness, dsh, tui, terminal-ui, ansi]
timestamp: "2026-08-18T12:00:00Z"
---

# dsh-tianshu-tui (huiliyi37/dsh-tianshu-tui)

## 它是什么
`huiliyi37/dsh-tianshu-tui` 是官方 DeepSeek Harness 的**交互式终端界面（TUI）**：自研 ANSI 渲染以保证流畅滚动，并在官方能力之上**加了几条个性化工作流**——TDD 驱动、证据门、视觉图像模块。

## 为什么用它 / 适合什么场景
- 在服务器 / SSH 环境下用 DSH，没有 GUI / 浏览器，但想要官方 CLI 之上的可视化滚动体验。
- 偏好「终端原生」工作流，希望 TDD、证据门槛这些纪律化约束直接在 TUI 里强制生效。
- 想给 DSH 加视觉理解能力：自带的视觉图像模块把图片直接送进当前会话。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自研 ANSI 渲染 | 避免依赖 GUI 框架，终端内即可流畅滚动 |
| TDD 驱动工作流 | 会话开始即引导测试先行 |
| 证据门 | 关键结论要求附带证据才放行 |
| 视觉图像模块 | 在 TUI 内直接把图片接入会话 |
| 兼容官方 DSH | 与官方 Harness CLI 并存使用 |

## 媒体
- ![](https://pbs.twimg.com/media/HP5HoeMbUAAs7rt.jpg)

## 相关概念
- [项目链接](https://github.com/huiliyi37/dsh-tianshu-tui) — 仓库地址
