---
type: "Note"
title: "《一本 pi-agent-core 架构的中文书》"
description: "一本从源码出发解读 pi-agent-core 架构的中文书：把「一个 agent 循环被做成一个库」讲清楚，每一处论断都带 文件:行号 引文，读者不用打开编辑器就能核对。"
tags: "[pi-agent, architecture, book, source-reading, agent-loop]"
timestamp: "2026-08-15T02:12:00Z"
resource: "https://github.com/antinomie-lab/pi-book"
---

# 《一本 pi-agent-core 架构的中文书》

## 它是什么

`antinomie-lab/pi-book` 是一本中文电子书，从源码层面解读 `pi-agent-core`（Pi Coding Agent 的核心库）的架构。核心论点只有一个：**「一个 agent 循环被做成一个库」**——把 OpenAI / Anthropic / 其他 LLM 调用、工具调用、上下文管理、多步决策打包成可被代码直接调用的库函数。

最突出的写作约定是「**每处论断带 `文件:行号` 引文**」：读者无需打开 IDE 翻代码，就能直接定位论据。

> ![](https://pbs.twimg.com/media/HPpfc8vbUAAjWtO.jpg)

## 这本书讲了什么（按章节思路梳理）

| 章节 | 主题 |
|------|------|
| 第 1 章 | 整体目标：为什么「agent 循环 = 一个库」 |
| 第 2 章 | 入口与生命周期：怎么启动一次 agent 循环 |
| 第 3 章 | 工具系统：工具如何注册、描述、执行 |
| 第 4 章 | 上下文 / 消息管理：多轮对话与 token 控制 |
| 第 5 章 | Provider 抽象：兼容多家 LLM 的统一接口 |
| 第 6 章 | 流式 / 中断 / 取消：长任务与可恢复性 |
| 第 7 章 | 错误与重试：让 agent 在真实生产里不碎 |
| 第 8 章 | 扩展点：技能 / 钩子 / 子代理 |

## 适合谁读

- 想从源码角度理解 Pi Coding Agent 内部工作的人。
- 想自己写一个「agent 循环 = 库」的人（把它当范本抄）。
- 已经用 Pi 跑编码代理、想理解「为什么它这么跑」的中文读者。

## 与其它 Pi 生态文档的差异

- 与 `note-dg-ai-pi-agent-tutorial.md` 那种「操作教程」不同，这本更偏**架构 + 源码**。
- 与 `pi-coding-agent` 仓库自带的英文 README 相比，本书**中文 + 带行号引文**，门槛更低。

## 参考链接

- [项目链接](https://github.com/antinomie-lab/pi-book)

## 相关概念

- [note-dg-ai-pi-agent-tutorial](note-dg-ai-pi-agent-tutorial.md) — Pi Agent 中文教程（偏操作）
- [pi-claude-bridge](tool-pi-claude-bridge.md) — Pi 接入 Claude Code 的桥接扩展（库形态的典型应用）
- [pi-task](tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展