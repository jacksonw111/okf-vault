---
type: "Tool"
title: "Novel Studio (Xiaoyangy/novel-studio)"
description: "用 Go 写的本地优先开源 AI 长篇小说创作引擎，面向连载、整本短篇与故事工作室。流程是先冻结全书卷—章—章纲，再逐章推演当前弧所有角色选择与后果，一弧封存后才逐章渲染、逐章审核，正文只看到主视角有权知道的事实。"
resource: "https://github.com/Xiaoyangy/novel-studio"
tags: "[ai-writing, novel, local-first, go, fiction, story-engine, long-form]"
timestamp: "2026-08-04T20:30:00Z"
---

# Novel Studio (Xiaoyangy/novel-studio)

## 它是什么

[Novel Studio](https://github.com/Xiaoyangy/novel-studio) 是一个**用 Go 写的本地优先开源 AI 长篇小说创作引擎**，面向连载、整本短篇与故事工作室。

**核心流程：**

1. **冻结**全书卷 → 章 → 章纲
2. **推演**当前弧所有角色选择与后果
3. **一弧封存**后才逐章渲染
4. **逐章审核**——正文只看到主视角有权知道的事实

![Novel Studio 截图](https://pbs.twimg.com/media/HOxgVR9bkAEAInA.jpg)

## 为什么用它 / 适合什么场景

- **连载一致性**：先把卷—章—章纲冻结，避免 AI 长篇写到一半角色 OOC、剧情自相矛盾。
- **视角纪律**：正文只暴露主视角有权知道的事实，避免"全知叙事"的常见 AI 写作 bug。
- **本地优先**：Go 写的本地引擎，敏感稿件不出本机。
- **逐章审核**：每章独立可审可改，不阻塞创作流。

## 关键能力

| 能力 | 说明 |
|------|------|
| 卷—章—章纲冻结 | 先建好结构再动笔 |
| 弧级推演 | 当前弧内所有角色选择 + 后果预演 |
| 弧封存 | 一弧封存后才逐章渲染 |
| 视角隔离 | 正文只暴露主视角有权知道的事实 |
| 逐章审核 | 每章独立可审可改 |

## 参考链接

- [项目仓库](https://github.com/Xiaoyangy/novel-studio)

## 相关概念

- [OpenFic](./tool-openfic.md) — Agent + RAG 驱动的中长篇小说写作工具，百万字级上下文
- [Hearth (NL Game)](./tool-hearth-nl-game.md) — 自然语言描述想玩的游戏，AI 代理现场建好
- [Hammer Story Editor](./tool-hammer-story-editor.md) — Kotlin 本地优先跨平台故事编辑器
