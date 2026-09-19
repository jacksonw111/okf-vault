---
type: "Tool"
title: "jev-mcp（8 个 Jev 判断工具的 MCP server）"
description: "给 Agent 提供 8 个基于 TypeSafe Jev 模型的判断工具，做验真、筛注入、排序分类这类机械检查。"
resource: "https://github.com/jkudish/jev-mcp"
tags: "[mcp, jev, classification, prompt-injection, fact-check, agent-tool]"
timestamp: "2026-09-19T16:00:00Z"
---

# jev-mcp（8 个 Jev 判断工具的 MCP server）

## 它是什么

[jkudish/jev-mcp](https://github.com/jkudish/jev-mcp) 是一个**给 Agent 提供 8 个判断工具的 MCP server**——底层基于 TypeSafe 的 Jev 模型，封装出适合 agent 直接调用的**机械性检查工具**：

- 验真（fact-check）
- 筛注入（prompt-injection filter）
- 排序分类（rank / classify）
- 其他 5 类判断类操作

## 为什么用它 / 适合什么场景

- 给通用 agent 加一道**机器化的判断闸**：每个输出都跑一遍 jev-mcp 的工具再交给用户。
- 在 RAG / 检索链路上对**检索结果做排序 / 分类**，避免把垃圾片段喂给 LLM。
- 需要给 LLM 输出做**注入检测 / 真伪复检**，又不想自己训练分类器。
- 想跨 agent（Claude Code / Codex / Cursor 等）共享同一套 Jev 判断标准。

## 关键能力

| 能力 | 说明 |
|------|------|
| 8 个判断工具 | 验真 / 筛注入 / 排序 / 分类 等覆盖常见机械检查 |
| MCP 协议 | 任何支持 MCP 的 agent 都能直接调用 |
| TypeSafe Jev 模型 | 复用成熟的 Jev 评分基础设施 |
| 轻量机械判断 | 不需要大模型生成解释，直接给分 / 给结论 |

## 与相关概念的关系

- [MCP（Model Context Protocol）](./term-mcp.md) — jev-mcp 是一个标准的 MCP server
- [JEV Ultrafast（browser-use 极速浏览器自动化）](./tool-jev-ultrafast.md) — 同基于 Jev 模型，jev-ultrafast 用在浏览器自动化打分，jev-mcp 用在通用判断

## 参考

- 项目链接：<https://github.com/jkudish/jev-mcp>
- 原始推文：<https://x.com/QingQ77/status/2101223266845421971>