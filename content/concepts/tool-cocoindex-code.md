---
type: Tool
title: "cocoindex-code"
description: "cocoindex-io 开源的 AST 语义代码搜索引擎，专为编码 Agent 设计。装好后 Claude Code / Codex / Cursor 等可直接调用定位相关代码，节省 70% token 并提升搜索速度，支持 30+ 语言。"
tags: "[code-search, ast, agent, rust]"
timestamp: "2026-07-01T03:50:00Z"
resource: "https://github.com/cocoindex-io/cocoindex-code"
---

# cocoindex-code

## 它是什么
cocoindex-io 开源的 AST 语义代码搜索引擎，专为编码 Agent 设计。底层 Rust 写的 CocoIndex 引擎做增量索引，安装后即插即用地让 Claude Code / Codex / Cursor 等 Agent 直接调用它定位相关代码片段。

## 为什么用它 / 适合什么场景
- 想给编码 Agent 装一个「懂得代码结构」而不是 grep 的搜索后端
- 当前 Agent 在大代码库里靠文件读取 + grep 浪费 token
- 想让搜索结果带有语义上下文（函数签名 / 类继承 / 调用关系）而不是字符串匹配

## 关键能力
| 能力 | 说明 |
|------|------|
| AST 语义搜索 | 基于抽象语法树而非字符串匹配，理解代码结构 |
| 节省 70% token | 官方数据，定位相关代码消耗 token 比纯 grep 显著少 |
| 30+ 语言 | Python / TS / JS / Rust / Go / Java / C++ / Ruby / PHP 等主流全覆盖 |
| Rust 引擎 | 底层 CocoIndex 用 Rust 写，速度快 / 内存占用低 |
| 增量索引 | 只处理改过的文件，不用每次全量重建 |
| Agent 即插即用 | Claude Code / Codex / Cursor 直接调用，无需额外胶水代码 |

## 与 grove 的互补
- **grove**：基于 tree-sitter 的结构化代码访问工具（MCP 协议，按需查询）
- **cocoindex-code**：基于 AST 的语义搜索引擎（增量索引 + 语义检索）

两者都可挂到 Agent 上，前者适合「我需要看这个函数定义」、后者适合「我需要找所有跟 X 相关的代码」。

## 相关概念
- [grove（Entelligentsia）](tool-grove-tree-sitter.md) — tree-sitter 结构化代码访问，与 cocoindex-code 互补
- [codebase-memory-mcp](tool-codebase-memory-mcp.md) — 持久化代码知识图谱，另一种代码索引方案
- [Aura-IDE](tool-aura-ide.md) — Planner/Worker 双智能体本地编码工作台，可作为 cocoindex-code 的前端

## 原始链接
- [项目仓库](https://github.com/cocoindex-io/cocoindex-code)
- [截图](https://pbs.twimg.com/media/HMEPjv-W4AArjjz.jpg)