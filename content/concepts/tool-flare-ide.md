---
type: Tool
title: "Flare（以代码依赖图谱为核心的 IDE）"
description: "AlgoNoRhythm 开源：把代码库实时画成一张依赖图谱，AI 代理在 IDE 里「看图干活」、人在「图谱视图」上审阅代理改了什么；文件当节点、导入关系当连线，Canvas / Wheel / Districts 三种视图。"
resource: "https://github.com/AlgoNoRhythm/Flare"
tags: [ide, agent, graph, code-review, canvas, dependency-graph]
timestamp: 2026-08-21T01:58:00Z
---

# Flare（以代码依赖图谱为核心的 IDE）

## 它是什么
Flare 是一个把「代码库」以**依赖图谱**为第一公民呈现给用户和 AI 代理的 IDE：文件是节点，导入关系是连线。它专为配合 Claude / Codex / OpenCode 这类 AI 编码代理设计——代理一边改文件，图谱一边实时更新；每次改动存进本地「影子历史」，人可以随时对比、回滚、审阅代理到底改了什么。

## 为什么用它 / 适合什么场景
- 想直观看到「这次改动影响哪些文件 / 哪些模块」而不是从聊天记录里拼上下文。
- AI 代理跑长任务时希望「随时看一眼全局」，避免局部优化撕裂整体。
- 想要一种「图谱 + 文件编辑器」混合 IDE，替代纯文本 / 纯聊天的工作方式。

## 关键能力
| 能力 | 说明 |
|------|------|
| 文件即节点 | 文件 = 图谱节点，导入 = 边 |
| 实时渲染 | 代理改动 → 图谱同步更新 |
| 三视图 | Canvas（自由画布）/ Wheel（环形）/ Districts（区域） |
| 影子历史 | 每次改动入栈，可对比可回滚 |
| AI 友好 | Claude / Codex / OpenCode 等代理无缝接入 |
| 桌面 + Web | 可装桌面应用，也可浏览器访问 |

## 一句话总结
**「把代码库画成图谱给 AI 看」——Flare 让 AI 在图上干活、人在图上审阅。**

## 原始链接
- [AlgoNoRhythm/Flare](https://github.com/AlgoNoRhythm/Flare) — 原始仓库

## 媒体
- ![Flare 图谱界面](https://pbs.twimg.com/media/HQFjGMGbsAAEDgo.jpg)

## 相关概念
- [codebase-memory-mcp](./tool-codebase-memory-mcp.md) — 用知识图谱索引代码结构，给 AI 代理用
- [AIGX](./tool-aigx.md) — AI 编程代理上下文格式，per-file 边界索引