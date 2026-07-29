---
type: Tool
title: "OpenFic（Agent + RAG 驱动的长篇小说写作工具）"
description: "中长篇写作上下文太长，OpenFic 用 Agent 系统 + RAG 帮你管百万字级的人物关系和剧情线。Python 后端 + 跨平台前端，三种装法（Docker / pip / 桌面版），数据全在本地。"
resource: "https://github.com/syrizelink/OpenFic"
tags: [writing, agent, rag, novel, local-first, multiplatform]
timestamp: "2026-07-28T13:30:00.000Z"
---

# OpenFic

## 它是什么

针对中长篇写作的工程化工具：

- **痛点**：上下文太长（百万字级别），常规 LLM 装不下
- **解法**：**Agent 系统 + RAG** + 多层压缩缓存

不是"抽卡式一键出文"——它把人物关系 / 剧情线 / 设定 / 角色卡全部结构化，Agent 在需要时拉相关上下文。

![截图示例](https://pbs.twimg.com/media/HOSOm9QaMAA7lc2.jpg)

## 架构

| 组件 | 说明 |
|------|------|
| Python 后端 | Agent 系统 + RAG |
| 跨平台前端 | 桌面 App |
| 三种装法 | Docker / pip / 桌面 |
| 数据本地 | 不上云 |
| 支持主流模型 API | OpenAI / Anthropic / ... |

## 关键能力

| 能力 | 说明 |
|------|------|
| 百万字级上下文 | RAG + 多层压缩缓存 |
| 设定 / 角色 / 工作流可改 | 不绑死模板 |
| 数据本地 | 隐私 + 离线可用 |
| 多种模型 API | 不锁定 provider |
| Agent 系统 | 不只是聊天 |

## 原始链接

- [项目仓库](https://github.com/syrizelink/OpenFic)
- [推文剪藏](https://x.com/QingQ77/status/2082096234484179082)

## 相关概念

- [Hammer（Kotlin 本地优先故事编辑器）](./tool-hammer-story-editor.md) — 同类本地优先写作工具
- [OpenMontage](./tool-openmontage.md) — 视频 agentic 制作系统
- [Files.md](./tool-files-md.md) — 本地优先 .md 笔记应用
- [Casting Workflow（番茄短篇指纹互消绕查重）](./tool-casting-workflow.md) — 同属写作 / 内容生成工具