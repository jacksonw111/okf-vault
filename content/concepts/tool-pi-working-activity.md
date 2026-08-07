---
type: Tool
title: "pi-working-activity"
description: "Pi 命令行 AI 助手的状态行扩展：监听工具执行事件，把干巴巴的「Working…」状态行换成实时动态——正在跑什么、进度到哪、还剩多久都看得见，顺带掺进俏皮文案和彩蛋。"
resource: "https://github.com/ccch1mneyyy/pi-working-activity"
tags: [pi, cli-ux, status-line, animation, agent-ux, terminal]
timestamp: 2026-08-06T06:30:00Z
---

# pi-working-activity

## 它是什么

ccch1mneyyy 开源的 Pi 扩展，把 Pi 默认的「Working...」干巴巴文本换成有信息量、有节奏感的状态行。

## 为什么用它 / 适合什么场景

- 跑长任务时盯着 Pi 的状态行干等，心里没底到底在跑什么 / 还剩多久。
- 想给状态行加进度感、活动感，但不想为这点小事装一个 GUI。
- 喜欢俏皮文案 / 彩蛋点缀 CLI 体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 工具事件监听 | 钩入 Pi 工具执行事件流 |
| 实时动态状态 | 正在跑什么 / 进度到哪 / 还剩多久 |
| 俏皮文案 / 彩蛋 | 不止信息，还有点小趣味 |

## 相关概念
- [Cobalt Spark](./tool-cobalt-spark.md) — 极简 Oh My Zsh 主题，闪电符号分隔上下文与命令
- [Pi-tbox](./tool-pi-tbox.md) — Pi 扩展工具开关面板，集中列出 + 分组开关 + 跨会话持久