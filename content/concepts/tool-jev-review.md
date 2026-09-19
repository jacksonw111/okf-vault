---
type: "Tool"
title: "jev-review（编码 agent 的本地 MCP 代码质量评分循环）"
description: "本地运行的 MCP 服务器，给 Claude Code、Codex、Cursor、OpenCode 等编码智能体提供结构化的代码质量评分循环。"
resource: "https://github.com/NiazMorshed2007/jev-review"
tags: "[mcp, code-review, jev, claude-code, codex, cursor, opencode, local-server]"
timestamp: "2026-09-19T16:00:00Z"
---

# jev-review（编码 agent 的本地 MCP 代码质量评分循环）

## 它是什么

[NiazMorshed2007/jev-review](https://github.com/NiazMorshed2007/jev-review) 是一个**本地运行的 MCP 服务器**——它把 TypeSafe 的 Jev 评估服务封装成可被 Claude Code / Codex / Cursor / OpenCode 等编码智能体直接调用的工具，输出**结构化的代码质量分数**，形成「生成 → 评分 → 修正」的闭环。

通过 `npx plugins add` 从 GitHub 直接安装；运行时是**本地 Node.js 20+ 进程**，经 stdio 暴露一个 `jev_review` 工具。

## 为什么用它 / 适合什么场景

- 在编码 agent 的工作流里加一道**机器化的质量闸**：每轮生成都自动给个分，分低就回头改。
- 想跨 IDE（Claude Code / Codex / Cursor / OpenCode）共享同一套评分口径，避免每个 agent 各评各的。
- 不想把代码贴到云端做评审——评分走本地 MCP。
- 想要比纯 LLM「自评」更稳定、更可量化的代码 review 入口。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地 MCP 服务器 | 跑在用户机子上，stdio 暴露 `jev_review` 工具 |
| 多编码 agent 兼容 | Claude Code / Codex / Cursor / OpenCode |
| 结构化质量分 | 不是「感觉好不好」，而是具体数值与维度 |
| npx 插件化安装 | 一行命令从 GitHub 拉到本地 |
| TypeSafe Jev 模型 | 复用成熟的 Jev 评估服务 |

## 与相关概念的关系

- [JEV Ultrafast（browser-use 极速浏览器自动化）](./tool-jev-ultrafast.md) — 同样基于 Jev 评估模型，但 jev-ultrafast 用在浏览器自动化，jev-review 用在代码质量打分
- [MCP（Model Context Protocol）](./term-mcp.md) — jev-review 是典型的 MCP server，遵循 MCP 协议暴露工具

## 参考

- 项目链接：<https://github.com/NiazMorshed2007/jev-review>
- 原始推文：<https://x.com/QingQ77/status/2101174948416848376>