---
type: Tool
title: "OpenWiki"
description: "LangChain 团队开发的命令行工具，为 AI 编程代理生成和维护代码库文档；扫描代码库生成结构化 openwiki/ 文档目录，并在 AGENTS.md / CLAUDE.md 中自动添加提示词，让代理需要上下文时自动查阅。"
resource: "https://github.com/langchain-ai/openwiki"
tags: "[documentation, code-wiki, cli, ai-agent, context, agents-md, claude-md, langchain]"
timestamp: "2026-07-03T08:16:00Z"
---

# OpenWiki

## 它是什么
**LangChain 团队**开发的命令行工具，专门为 AI 编程代理（Claude Code / Codex / Cursor 等）**生成和维护代码库文档**。

两种入口：
- **交互式 CLI**：逐步向导式生成
- **一句命令**：CI / 脚本里直接跑

会扫描整个代码库，生成结构化的 `openwiki/` 文档目录；同时自动在 `AGENTS.md` / `CLAUDE.md` 中追加提示词，让代理在需要上下文时自动查阅这些文档（避免重复扫描或凭空编造）。

## 为什么用它 / 适合什么场景
- 想给 AI 代理一份「项目说明书」——架构、模块、关键约定、调用关系，但懒得手写。
- 项目变大后，AI 代理常常「迷失」——找不到相关文件或不知道项目约定，需要自动化的代码库文档。
- 已有 `AGENTS.md` / `CLAUDE.md`，想用工具自动生成并持续同步其中的「项目知识」段落。
- 用 LangChain / LangGraph 等 LangChain 生态工具，希望官方支持的代码库文档格式。

## 关键能力
| 能力 | 说明 |
|------|------|
| 出品方 | LangChain 团队 |
| 入口 | 交互式 CLI / 一句命令 |
| 输出 | 结构化的 `openwiki/` 文档目录 |
| 自动集成 | 写入 `AGENTS.md` / `CLAUDE.md` 提示词 |
| 触发 | 代理需要上下文时自动查阅生成的文档 |
| 覆盖 | 扫描整个代码库 |
| 形态 | CLI 工具 |

## 相关概念
- [Codebase Memory MCP](tool-codebase-memory-mcp.md) — 基于知识图谱的代码结构索引 MCP；OpenWiki 是文档形式，codebase-memory-mcp 是结构化图谱
- [Obsidian Knowledge Agent](tool-obsidian-knowledge-agent.md) — 把 PDF / 论文转 Obsidian 笔记；OpenWiki 把代码库转 wiki
- [Open Knowledge（Inkeep）](tool-open-knowledge.md) — WYSIWYG Markdown 知识库；OpenWiki 是面向 AI 代理的代码库文档

## 项目链接
- 项目主页：<https://github.com/langchain-ai/openwiki>

## 媒体
![](https://pbs.twimg.com/media/HMRNn7SacAAQo9_.jpg)