---
type: Tool
title: "dsh-desktop (bruc3van)"
description: "把 DeepSeek Harness 官方 Web UI 原样装进原生桌面窗口，普通用户不用装 Node.js、不用敲命令即可使用完整 Harness"
resource: "https://github.com/bruc3van/dsh-desktop"
tags: [deepseek, harness, dsh, desktop, webview]
timestamp: 2026-08-16T16:00:00Z
---

# dsh-desktop (bruc3van)

## 它是什么
`bruc3van/dsh-desktop` 是一个把 **DeepSeek Harness (DSH)** 官方 Web UI **原样嵌入原生桌面窗口** 的桌面封装。区别于从头重写 UI 的桌面壳项目，它的核心策略是「**官方 Web UI 怎么长，桌面里就怎么长**」，目标受众是**不想装 Node.js / 不想敲任何命令**的普通用户。

## 为什么用它 / 适合什么场景
- 把 DeepSeek Harness 推荐给完全没装过 Node.js 的同事 / 家人。
- 不想记本地端口、每次开浏览器还要 `localhost:xxxx`。
- 想要官方 Web UI 的所有功能（多模态、文件上传、会话历史）保持原状。
- 桌面常驻、把 DeepSeek 当系统级 AI 助手用。

## 关键能力
| 能力 | 说明 |
|------|------|
| 原生桌面窗口 | macOS / Windows 下原生窗口体验，不再是浏览器标签页 |
| Web UI 1:1 | 不重写不魔改，官方更新即跟随 |
| 零依赖启动 | 用户不需要预装 Node.js / npm / 命令行工具链 |
| 内核自动拉起 | 点开图标 → 拉起 DSH → 在窗口内显示 Web UI |

## 媒体
- ![](https://pbs.twimg.com/media/HPvKAyQaYAA2_18.jpg)

## 相关概念
- [项目链接](https://github.com/bruc3van/dsh-desktop)