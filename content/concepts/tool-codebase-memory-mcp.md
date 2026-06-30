---
type: Tool
title: "codebase-memory-mcp（基于知识图谱的代码结构索引）"
description: "为 AI 编码代理提供基于知识图谱的代码结构索引——用 tree-sitter + Hybrid LSP 把函数 / 类 / 调用链 / 路由建成持久化图谱，让代理用少数几次查询替代大量逐文件搜索来理解代码库。"
resource: "https://github.com/DeusData/codebase-memory-mcp"
tags: "[mcp, code-intelligence, knowledge-graph, tree-sitter, lsp, ai-coding]"
timestamp: "2026-06-30T15:30:00Z"
---

# codebase-memory-mcp（基于知识图谱的代码结构索引）

## 它是什么

codebase-memory-mcp 是一个面向 AI 编码代理的代码库「记忆」服务器：用 tree-sitter 解析 158 种语言的语法结构，配合 Hybrid LSP 对 9 种语言做类型级语义解析，把函数、类、调用链、路由等信息建成持久化的图谱，让代理能用少数几次精确查询替代大量逐文件搜索来理解代码库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多语言语法解析 | tree-sitter 支持 158 种语言 |
| 类型级语义 | Hybrid LSP 为 9 种语言提供类型 / 符号解析 |
| 持久化图谱 | 函数、类、调用链、路由入图，可跨会话复用 |
| 极速索引 | Linux 内核 3 分钟搞定；结构查询 < 1 毫秒 |
| 单文件部署 | 纯 C 写，发布一个静态二进制文件，macOS / Linux / Windows 全平台 |
| MCP 即插即用 | 装完自动配置 11 种编码代理的 MCP 入口，提供 14 个 MCP 工具 |
| Cypher 查询 | 支持类 Neo4j 的 Cypher 声明式查询 |
| 3D 图谱可视化 | 内置 3D 图谱浏览器 |

## 适用场景

- 大型代码库（百万行级）里给 AI 代理提供「结构记忆」，避免反复 grep / read_file。
- 需要跨语言（混合 Java + Python + Go + Rust 等）一致索引的项目。
- 想要脱离「靠运气找到正确文件」的代理工作流。

## 媒体参考

![](https://pbs.twimg.com/media/HMBe_lubYAAGoS7.jpg)

## 相关概念

- [AIGX](./tool-aigx.md) — 同样面向 AI 编码代理的「per-file 边界索引」上下文格式
- [Repo→Agent](./tool-repo-agent-generator.md) — 把任意 GitHub 仓库生成为带 CLI / MCP / 签名的 Agent 包
- [DevSpace](./tool-devspace-mcp.md) — 自托管 MCP 编程工作台
- [Codex Control Plane MCP](./tool-codex-control-plane-mcp.md) — Codex Desktop 的持久化任务队列 MCP
- [DeepSeek MCP WebSearch](./tool-deepseek-mcp-websearch.md) — 同为 MCP 服务器形态

## 参考链接

- 项目链接：<https://github.com/DeusData/codebase-memory-mcp>