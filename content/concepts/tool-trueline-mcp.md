---
type: "Tool"
title: "trueline-mcp（带哈希校验的 AI 编码精准改文件 MCP）"
description: "MCP 插件，给 AI 编码助手做「带哈希校验的精准改文件 + 按需读文件」——既节省上下文，又防止代码被偷偷改坏。"
resource: "https://github.com/rjkaes/trueline-mcp"
tags: "[mcp, ai-coding, file-edit, hash-check, safety, context-saving]"
timestamp: "2026-07-08T09:15:00Z"
---

# trueline-mcp

## 它是什么

[trueline-mcp](https://github.com/rjkaes/trueline-mcp) 是一个 **MCP（Model Context Protocol）插件**，让 AI 编码助手在改文件时**先校验、后写入**。

核心思路：
- 给 AI 一把「**带哈希指纹的手术刀**」——改文件前先记下要改区块的哈希，改完再核对，确保**改的真的是这块、没改坏其它地方**。
- 同时把「读整文件」拆成「按需读指定行 / 指定代码块」，**减少上下文浪费**。

## 解决的问题

| 痛点 | trueline-mcp 的解法 |
|------|--------------------|
| AI 改完文件，悄悄改了不该改的地方 | 哈希校验：写入前/后比对，确保改对地方 |
| AI 改错位置 / 改到陈旧内容 | 行号 + 范围 + 哈希联合定位 |
| 一次操作把整个文件读进上下文 | 按需读取指定行 / 函数 |
| 多回合编辑后文件已变 | 哈希变化能立即发现 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 哈希校验 | 改前快照哈希 + 改后校验 |
| 精准改文件 | 按行号 / 代码块改写 |
| 按需读 | 只读需要的片段，省 token |
| MCP 协议 | 接入任何支持 MCP 的编码 agent（Claude Code / Cursor / 等） |
| 防篡改 | 拒绝改坏时立即报错 |

## 参考链接

- [项目仓库](https://github.com/rjkaes/trueline-mcp)

## 相关概念

- [Claude Code](./tool-claude-code.md) — trueline-mcp 可作为 Claude Code 的 MCP 工具使用
- [Codebase Memory MCP](./tool-codebase-memory-mcp.md) — 同为 MCP 生态的「代码上下文增强」工具