---
type: "Tool"
title: "marko-md（Claude 输出 Markdown 阅读 / 勾选回写）"
description: "baberjaved 出品：给 Claude 写出来的 Markdown（实施计划、报告、规范、操作手册）一个比终端和纯文本编辑器更合适的阅读界面，支持在界面里勾任务后导出回写。"
resource: "https://github.com/baberjaved/marko-md"
tags: "[markdown, claude, reader, task-tracker, editor]"
timestamp: "2026-09-28T23:50:00Z"
---

# marko-md（Claude 输出 Markdown 阅读 / 勾选回写）

## 它是什么

[marko-md](https://github.com/baberjaved/marko-md) 是 baberjaved 出品的 Markdown 阅读 / 编辑器：专门为 **Claude 写出来的 Markdown**——实施计划、报告、规范、操作手册——提供一个**比终端和纯文本编辑器更合适的阅读界面**。

核心特色是**支持在界面里勾任务后导出回写**：Claude 生成的 `- [ ]` 任务列表，用户在阅读界面里打钩后导出，覆盖回原文件，让 Agent 下次跑时知道进度。

## 为什么用它 / 适合什么场景

- Claude 输出的实施计划太长，纯文本 / 终端**读起来累**。
- 想**手动勾掉已完成任务**、并把勾选状态回写到原文件，下次 Agent 自动接续。
- 团队 / 个人项目大量产出「计划 + 任务清单」型 Markdown，需要统一阅读体验。
- 不想自己写脚本处理 checkbox 状态。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Markdown 阅读 / 编辑界面 |
| 输入 | Claude 输出的实施计划 / 报告 / 规范 / 操作手册 |
| 输出 | 勾选状态导出回写原文件 |
| 适合 | 长篇 Markdown 文档 / 任务清单 |
| 出品 | baberjaved |

## 媒体

- ![](https://pbs.twimg.com/media/HTO63C_acAAmbiL.jpg)

## 相关概念

- [Obsidian](./tool-obsidian.md) — OKF 的天然编辑器（marko-md 的定位是「Claude 输出的专用阅读器」，更轻量）
- [Markdown Fetch Protocol](./note-markdown-fetch-protocol.md) — 跨 Agent 共享 Markdown 的标准协议