---
type: Tool
title: "grove（Entelligentsia）"
description: "Entelligentsia 用 Rust 写的双面工具，既是 CLI 也是 MCP Server。基于 tree-sitter 给编码 Agent 提供字节精确、结构化、低 token 消耗的代码库访问能力，支持 27 种语言 + 7 个工具。"
tags: "[mcp, tree-sitter, code-agent, rust, cli]"
timestamp: "2026-07-01T02:25:00Z"
resource: "https://github.com/Entelligentsia/grove"
---

# grove（Entelligentsia）

## 它是什么
Entelligentsia 写的「双面」代码访问工具，左脸是 CLI 命令，右脸是 MCP Server，核心是基于 tree-sitter 语法树给 AI 编码 Agent 提供结构化的代码信息。

## 为什么用它 / 适合什么场景
- 给 Claude Code / Codex / Cursor 配 MCP 时不需要「grep 完传全文」浪费 token
- 想用结构化方式（outline / symbol / callers）而不是纯文本匹配访问代码库
- 大型 monorepo 里想让 Agent 知道「谁调了它 / 它调了谁」而不读全文

## 关键能力
| 能力 | 说明 |
|------|------|
| 双面工具 | 同时支持 CLI 与 MCP Server，无缝接入 Agent |
| tree-sitter 核心 | 语法树解析，不用 grep 也不用读整个文件 |
| 27 种语言 | Python / TS / Rust / Go / Java / C++ 等主流全覆盖 |
| 7 个工具 | outline 看文件骨架 / source 取单个符号源码 / map 看目录依赖 / callers 查调用者 / definition 跳定义 / symbols 搜符号 / check 检查语法错误 |
| 字节精确 | 返回源码片段而不只是名字，Agent 可直接拼到回答里 |
| 低 token | 只给 Agent 需要的结构块，不喂整文件 |

## 与 codebase-memory-mcp 的区别
- **grove**：当次会话的结构化代码访问（MCP 即时查询，无持久化）
- **codebase-memory-mcp**：把代码结构索引入知识图谱（持久化 + 跨会话）

## 相关概念
- [codebase-memory-mcp](tool-codebase-memory-mcp.md) — 持久化代码结构索引 MCP，二者配合做「即时查询 + 长期记忆」
- [DevSpace](tool-devspace-mcp.md) — 自托管 MCP 编程工作台，可承载 grove 等 MCP 工具
- [Aura-IDE](tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台，grove 可作其 MCP 后端
- [Claude Code](tool-claude-code.md) — 支持 MCP 的终端 AI 编码 agent，grove 直接可挂载

## 原始链接
- [项目仓库](https://github.com/Entelligentsia/grove)
- [截图](https://pbs.twimg.com/media/HMCz-4hXAAABs95.jpg)