---
type: Tool
title: "Minke (lencx/Minke)"
description: "把 DeepSeek Harness 装进一个本地优先的桌面工作台，对话 / 文件 / 终端 / 网页工具在同一个窗口里使用"
resource: "https://github.com/lencx/Minke"
tags: [deepseek-harness, dsh, desktop, local-first, workbench]
timestamp: 2026-08-20T09:15:00Z
---

# Minke (lencx/Minke)

## 它是什么
[`lencx/Minke`](https://github.com/lencx/Minke) 是一个**本地优先的桌面工作台**，把 **DeepSeek Harness (DSH)** 作为后端集成进来，让**对话、文件、终端、网页工具**都在**同一个窗口**里用——不必开浏览器 + IDE + 终端三件套。

## 为什么用它 / 适合什么场景
- 想在一个桌面应用里集中操控 dsh 的所有功能，而不是页面之间切换。
- 喜欢「本地优先 + 桌面体验」，不想每次都连远端。
- 需要把 dsh 与文件 / 终端 / 网页工具联动（边跑 AI 边改代码）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 本地优先桌面工作台 | 不依赖浏览器，桌面应用形态 |
| 集成 dsh 后端 | 把 DSH 作为对话引擎 |
| 多面板合一 | 对话 + 文件 + 终端 + 网页工具同窗 |
| 美观 | 桌面 UI 视觉与交互明显打磨过 |

## 媒体
- ![Minke 桌面截图](https://pbs.twimg.com/media/HQDN1sZbgAAKNxD.jpg)

## 相关概念
- [项目仓库](https://github.com/lencx/Minke) — 仓库主页
- [dsh-desktop](./tool-dsh-desktop.md) — 另一种把 dsh 包装成桌面的项目（用 WebView 1:1 套壳官方 Web UI）
- [deepseek-harness-desktop](./tool-deepseek-harness-desktop.md) — 同期其它 dsh 桌面壳
