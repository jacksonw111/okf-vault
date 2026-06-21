---
type: "Tool"
title: "DeepSeek MCP WebSearch（基于 DeepSeek API 的 MCP 搜索）"
description: "为 MCP 兼容客户端（Claude Code、OpenCode 等）提供通过 DeepSeek WebSearch API 进行网页搜索的能力，无需依赖第三方搜索服务，只需一个 DeepSeek API Key 即可开箱即用。"
resource: "https://github.com/chengx-coding/forever-saint-liang-websearch"
tags: "[mcp, deepseek, web-search, claude-code]"
timestamp: "2026-06-21T00:00:00Z"
---

# DeepSeek MCP WebSearch（基于 DeepSeek API 的 MCP 搜索）

## 它是什么

`forever-saint-liang-websearch`。把 **DeepSeek 的 WebSearch API** 包成一个标准 **MCP Server**，让 Claude Code、OpenCode 等 MCP 兼容客户端在需要「联网搜」时直接走 DeepSeek，**不需要再依赖 Tavily / Brave Search 等第三方搜索服务**。

## 关键卖点

| 卖点 | 说明 |
|------|------|
| 一键接入 | 只需一个 DeepSeek API Key |
| 无第三方依赖 | 不依赖 Tavily / Brave / Google CSE |
| MCP 原生 | 任意 MCP 客户端（Claude Code / OpenCode……）直接 `add` |
| 合规 | 数据出 DeepSeek 一家，便于审计 |

## 适用场景

- 想给 Claude Code / OpenCode 加联网搜索，但不想注册 Tavily / Brave。
- 已经在用 DeepSeek API —— 直接复用 API Key。
- 团队对「搜索结果走哪家」有合规要求 —— 限定到 DeepSeek。

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — MCP + Skill 是 Agent 接入外部工具的事实标准
- [CodexPro](tool-codexpro.md) — 同样是 MCP + DeepSeek 生态相关工具
- [a-stock-data](tool-a-stock-data.md) — 同为「数据源 → MCP Skill」的封装思路