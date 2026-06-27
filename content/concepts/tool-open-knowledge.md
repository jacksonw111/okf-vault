---
type: "Tool"
title: "Open Knowledge（Inkeep 的 Markdown 编辑器 + LLM 知识库）"
description: "Inkeep 开源的所见即所得 Markdown 编辑器 + LLM 知识库，深度集成 Claude / Codex / Cursor 等 AI agent，自带 MCP、Skills 与 agent 搜索，AI 可直接在知识库里读写文档。"
tags: "[knowledge-base, markdown, ai, agent, mcp, skills]"
timestamp: "2026-06-27T06:35:00.000Z"
resource: "https://github.com/inkeep/open-knowledge"
---

# Open Knowledge（Inkeep 的 Markdown 编辑器 + LLM 知识库）

## 它是什么

[`Open Knowledge`](https://github.com/inkeep/open-knowledge) 是 Inkeep 开源的**所见即所得 Markdown 编辑器 + LLM 知识库**。它把漂亮的 WYSIWYG Markdown 编辑器和知识库体验打包在一起，同时**深度集成 Claude、Codex、Cursor 等 AI agent**，让 AI 直接在知识库里读写文档，而不是把文档导出来再交给 agent。

![Open Knowledge 界面](https://pbs.twimg.com/media/HLuFrQ2aQAAZZZd.png)

## 关键能力

| 能力 | 说明 |
|------|------|
| WYSIWYG 编辑 | 所见即所得 Markdown 体验 |
| AI 集成 | 深度接入 Claude / Codex / Cursor |
| MCP | 内置 MCP，agent 可被结构化调用 |
| Skills | 内置 Skills 机制，可执行领域流程 |
| Agent 搜索 | agent 可在知识库内全文 / 语义检索 |
| 双向读写 | AI 不仅能读，还能在知识库里直接写文档 |

## 适用场景

- 团队 / 个人需要一个「Markdown 体验好 + AI 能力强」的知识库前端
- 想让 Claude / Codex 直接成为知识库的一部分，而不是外挂工具
- 既要 WYSIWYG 给非技术同事用，又要给 agent 提供结构化 API

## 参考链接

- [项目链接](https://github.com/inkeep/open-knowledge)

## 相关概念

- [OKF 是什么](term-okf.md) — 知识库底层的文件格式约定，本工具的运行载体可以是 OKF
- [Obsidian](tool-obsidian.md) — 另一类以 Markdown 为核心的本地优先知识库
- [Cabinet](tool-cabinet.md) — 同样定位「Obsidian + AI 代理」的组合