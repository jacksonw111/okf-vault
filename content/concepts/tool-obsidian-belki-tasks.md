---
type: Tool
title: "obsidian-belki-tasks"
description: "受 Todoist 启发的 Obsidian 任务管理插件，任务以本地 Markdown 文件形式存在 vault 中。"
resource: "https://github.com/aribuga/obsidian-belki-tasks"
tags: "[obsidian, todoist, task-management, markdown, plugin]"
timestamp: "2026-07-19T04:06:00Z"
---

# obsidian-belki-tasks

## 它是什么

aribuga/obsidian-belki-tasks 是一个 Obsidian 插件，把 **Todoist 的交互模式** 带到本地 Markdown 工作流中。任务以**普通 .md 文件**形式存在 vault 里（不依赖第三方任务服务），同时拥有 Todoist 风格的快速录入、标签、过滤、重复任务等体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地 Markdown | 任务以 .md 文件存储，可被 Git 版本管理、被任何编辑器编辑 |
| Todoist 风格 UI | 快速录入、#标签 + @项目、智能过滤语法 |
| 自然语言日期 | 输入「明天下午 3 点」自动转日历字段 |
| 重复任务 | 支持 cron 式与自然语言式重复规则 |
| 完全离线 | 不依赖任何第三方服务，数据全在 vault |

## 适合谁

- Todoist 重度用户想减少订阅费、把任务留在本地
- Obsidian 用户希望 vault 既当知识库又当 GTD 系统
- 重视数据主权、不愿把任务数据同步到第三方云

## 与已有 Obsidian 工具的差别

- [Niamos](./tool-niamos.md) — Obsidian 第二大脑模板（PARA + Claude Code）
- [obsidian-knowledge-agent](./tool-obsidian-knowledge-agent.md) — 六阶段 AI 管道自动整理 Obsidian 笔记
- [NoteBrain CLI](./tool-notebrain-cli.md) — Obsidian vault 离线索引到本地 ChromaDB
- obsidian-belki-tasks 的差异点：**专做任务管理**，对标 Todoist 而非笔记整理

## 媒体预览

![](https://pbs.twimg.com/media/HNaWJDLbAAAiCPv.jpg)

## 相关概念

- [Obsidian](./tool-obsidian.md) — 知识库编辑器
- [tudo](./tool-tudo.md) — 终端下的待办 + Markdown 笔记本二合一 TUI

## 参考链接

- 项目链接: <https://github.com/aribuga/obsidian-belki-tasks>