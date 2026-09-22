---
type: Tool
title: "jev-cli"
description: "TypeSafe Jev 的 CLI 客户端——应用代码做快速分类判断时，让 CLI 直接返回概率、选项或打分这类机器可读结果；再由 jev-mcp 通过 stdio 交给 MCP 宿主。"
resource: "https://github.com/tumf/jev-cli"
tags: "[jev, classifier, mcp, typesafe, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# jev-cli

## 它是什么
一个**面向应用代码的 TypeSafe Jev CLI**：本地一次快速分类判断时，不需要让模型写整段话；用 `jev` 直接问，返回的是**概率、选项或打分这类机器可读结果**。

配套的 `jev-mcp` 再把这套判断通过 stdio 交给 MCP 宿主，让 Claude / Codex 等 agent 也能用。

## 为什么用它 / 适合什么场景
- 应用代码需要一个本地的、低延迟的分类 / 判断能力（意图识别 / 标签 / 风险分级等）。
- 不希望每次判断都让 LLM 写完整自然语言回答——更想要结构化输出（概率 / 选项 / 分数）。
- 想把分类能力以 MCP 工具的形式接入 Claude Code / Codex 等 agent。

## 关键能力
| 能力 | 说明 |
|------|------|
| 接口形态 | CLI：`jev` 子命令 |
| 输出 | 机器可读（概率 / 选项 / 打分） |
| MCP 接入 | jev-mcp 通过 stdio 暴露 |
| 模式 | TypeSafe：输入与输出 schema 都强类型 |
| 适用 | 应用代码做快速分类判断 |

## 相关概念
- [Nimble Bespoke](tool-nimble-bespoke.md) — 同样面向「本机类型化判断」场景
- [MCP（Model Context Protocol）](term-mcp.md) — jev-mcp 使用的协议
- [Claude Code](tool-claude-code.md) — 可作为 MCP 宿主调用 jev-mcp

## 项目链接
- 项目主页：<https://github.com/tumf/jev-cli>

## 媒体
- 截图：<https://pbs.twimg.com/media/HStEwKTaUAAYzwo.jpg>
