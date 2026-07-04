---
type: Tool
title: "Worf"
description: "Worf 是 MIT 开源的本地优先桌面应用:把看板 / 笔记 / OKR / AI 聊天 / Sprint / 终端整合到一个 Electron + React 应用里,数据归本地,不依赖云。"
resource: "https://github.com/champ-patyatawee/worf"
tags: [worf, desktop, local-first, okr, kanban, ai-chat, mit]
timestamp: "2026-07-04T15:00:00Z"
---

# Worf

## 它是什么

Worf(`champ-patyatawee/worf`)是一款本地优先、本地优先、本地优先(Local-First) 的桌面工作台。它把日常工作里会用到的六块功能塞到同一个应用里,不需要切换窗口:

1. **Kanban 看板**:WIP limit / Swimlane / 标签
2. **笔记**:Markdown 编辑器 + 富文本
3. **OKR / 目标管理**:Objective → Key Result 结构化跟踪
4. **AI 聊天**:可接 OpenAI 兼容接口(可指向本地 Ollama / LM Studio 等)
5. **Sprint**:Scrum 周期回顾
6. **终端**:内嵌 xterm.js,可以跑 git / docker / kubectl 等命令

![截图](https://pbs.twimg.com/media/HMTvI-RbsAI7UPg.jpg)

项目链接：<https://github.com/champ-patyatawee/worf>

## 为什么用它

- **不交数据给云**:看板、笔记、OKR、AI 对话记录都存本地,不依赖 Notion / Linear / Slack。
- **一个 app 顶六七个**:减少上下文切换,降低注意力税。
- **AI 真本地可选**:把 AI chat 的 base URL 指向 `http://localhost:11434/v1` 就能用 Ollama,不出门。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地优先存储 | 所有数据存本地 SQLite,无需注册 |
| MIT 协议 | 完全开源,无功能阉割 |
| AI 兼容 OpenAI 协议 | 可指向 OpenAI、Azure、Ollama、vLLM 等任何兼容端点 |
| 多模块整合 | 看板 + 笔记 + OKR + AI + Sprint + 终端合为一 |
| Electron + React | 单机运行,无需服务器 |

## 局限

- 个人开发者的小项目,功能深度暂时不如 Linear / Notion 那么细致(Kanban 没有 automation / 没有 milestone 等高级功能)
- 终端模块只是 xterm 嵌入,不是真 tmux,不适合超长跑任务

## 相关概念

- [linXiv](tool-linxiv.md) — 本地优先学术论文管理,同属「本地优先桌面」类别
- [ackem](tool-ackem.md) — 本地优先 Windows AI 伙伴
- [本地 AI 桌面工作台](tool-local-ai-workbench.md) — Electron + 模型/Agent/路由三件套
- [Worf 仓库](https://github.com/champ-patyatawee/worf) — 项目链接
