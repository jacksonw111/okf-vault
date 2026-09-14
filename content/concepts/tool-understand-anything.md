---
type: "Tool"
title: "Understand-Anything（代码知识图谱 / 探索工具）"
description: "Lum1104 的开源工具（⭐ 约 8.3 万）：把代码库的整体结构变成「可探索的知识图谱」——文件 / 函数 / 类的连接可视化、依赖关系可追溯、图可搜索 / 可对话，支持 Claude Code / Codex / Cursor。"
resource: "https://github.com/Lum1104/Understand-Anything"
tags: "[codebase-understanding, knowledge-graph, ai-coding, claude-code, codex, cursor]"
timestamp: "2026-09-14T22:30:00Z"
---

# Understand-Anything（代码知识图谱 / 探索工具）

## 它是什么

[Lum1104/Understand-Anything](https://github.com/Lum1104/Understand-Anything) 把**陌生的大型代码库**变成**可探索的知识图谱**：

> 初見の巨大コード、どこから読めばいいか迷う人へ👀

## 关键能力

| 能力 | 说明 |
|------|------|
| 连接可视化 | 文件 / 函数 / 类之间的关系可视化 |
| 依赖关系 | 可追溯依赖链 |
| 图搜索 | 在图里搜想看的部分 |
| 对话式提问 | 对知识图谱提问 |
| 多 agent 兼容 | Claude Code / Codex / Cursor 等 |

## 适合谁

- **刚加入新团队 / 新项目**：从零开始看代码库
- **接手 AI 写的大量代码**：搞清楚它实际写了什么
- **代码评审**：在改之前先看清结构
- **重构**：找到所有受影响的位置

## 场景对比

| 场景 | 用 Understand-Anything |
|------|------------------------|
| 「这个项目从哪儿启动？」 | 看图一目了然 |
| 「改这个函数会影响哪些文件？」 | 沿边查询 |
| 「这段代码谁调用？」 | 反向依赖 |
| 「AI 写的代码我信不过」 | 图里对照看实现 |

## 项目链接

- 仓库：<https://github.com/Lum1104/Understand-Anything>

## 相关概念

- [Birdview（AI 编码工作流的架构可视化）](./tool-birdview.md) — 同类「让 AI 先建图」的思路，但更偏工作流前置
- [Pi Coding Agent](./tool-pi-coding-agent.md) — 可与本工具配合
