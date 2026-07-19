---
type: Tool
title: "files.md（zakirullin）"
description: "本地优先的 .md 笔记应用，浏览器直接打开就能用、数据全留在自己机器上，主打类聊天的随手记、任务清单、日记，外加可选的同步和 Telegram 机器人。"
resource: "https://github.com/zakirullin/files.md"
tags: "[markdown, notes, local-first, browser, telegram-bot, privacy]"
timestamp: "2026-07-19T03:46:00Z"
---

# files.md（zakirullin）

## 它是什么

zakirullin/files.md 是一个**本地优先的 .md 笔记应用**，把整个应用做成一组**浏览器直接打开就能跑的静态文件**：HTML + JS + 数据 = 自己机器上的一个目录。无需后端、无需注册、无需同步服务——数据始终留在本机。

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器即用 | 双击 index.html 即可使用，不依赖任何后端 |
| 类聊天记录 | 每条笔记像一条聊天消息，时间序排列 |
| 任务清单 | 内置 todo / 完成态切换 |
| 日记 | 按日期自动组织，类 Day One 体验 |
| 可选同步 | 通过用户自配的同步服务（iCloud / Syncthing 等）跨设备 |
| Telegram 机器人 | 可选配 Telegram bot，从手机快速记录到本机 |

## 适合谁

- 极简主义：不想装 Electron / 不想要云同步的笔记用户
- 隐私优先：所有笔记数据都在自己的硬盘上
- 跨设备同步：愿意自己跑 Syncthing / rclone 的人

## 与已有笔记工具的差别

- [HermitUI](./tool-hermitui.md) — 单 HTML 文件本地 AI 聊天界面（聊天方向）
- [lengyi-markdown-editor](./tool-lengyi-markdown-editor.md) — 纯前端单 HTML Markdown 编辑器（编辑器方向）
- [SpringNote](./tool-springnote.md) — Flutter + Rust 桌面懒人知识库（桌面 App 方向）
- files.md 的差异点：**类聊天流的笔记 + 任务清单 + 日记三合一**，且对 Telegram 输入友好

## 媒体预览

![](https://pbs.twimg.com/media/HNUspVea0AA62QH.jpg)

## 相关概念

- [HermitUI](./tool-hermitui.md) — 单 HTML 文件本地 AI 聊天界面
- [SpringNote](./tool-springnote.md) — Flutter + Rust 桌面懒人知识库
- [tudo](./tool-tudo.md) — 终端下的待办 + Markdown 笔记本二合一 TUI

## 参考链接

- 项目链接: <https://github.com/zakirullin/files.md>