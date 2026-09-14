---
type: "Term"
title: "MCP（Model Context Protocol）"
description: "Anthropic 主导推出的开放协议：让 LLM 通过统一接口连接数据源 / 工具 / 服务，被类比为「AI 应用的 USB-C 接口」。"
resource: "https://modelcontextprotocol.io"
tags: "[mcp, protocol, anthropic, llm, tool-use]"
timestamp: "2026-09-14T22:30:00Z"
---

# MCP（Model Context Protocol）

## 它是什么

**MCP（Model Context Protocol）** 是 Anthropic 主导推出的**开放协议**：让 LLM 通过统一接口连接外部数据源、工具、服务。模型 ↔ 工具的对话走 MCP，任何 MCP 兼容客户端（Claude Code / Cursor / Windsurf / Cline …）都能复用同一套 MCP 服务。

社区把它类比为 **「AI 应用的 USB-C 接口」**——一套标准接口，把模型和工具的接入方式从「每个客户端各写各的适配器」统一起来。

## 为什么重要

- **解耦客户端与工具**：工具作者实现一次 MCP 服务，所有兼容客户端可用。
- **跨客户端复用**：同一套工具能跑在 Claude Code / Cursor / Windsurf 里。
- **可组合**：客户端按需订阅多个 MCP 服务，运行时组合。
- **生态加速**：社区 MCP 服务数量快速增长（GitHub / 数据库 / 浏览器 / 文件系统 / 设计工具 …）。

## 与传统 Function Calling 的差异

| 维度 | MCP | 传统 Function Calling |
|------|-----|----------------------|
| 接口标准 | 开放协议，多客户端 | 每个客户端私有的 schema |
| 工具复用 | 服务一次实现多处用 | 每个客户端重写一次 |
| 宿主 | 客户端动态发现 | 启动时静态注册 |
| 生态 | 公共 MCP registry | 各自私域 |

## 相关概念

- [Claude Code](./tool-claude-code.md) — Anthropic 终端原生 agent，原生支持 MCP
- [Artemis（Google 真机 Android 自动化）](./tool-artemis-google-android-automation.md) — 原生 MCP 支持，Claude Code / Cursor / Windsurf 一键接入
- [ThinkingBox（微软智能体评测）](./tool-thinkingbox-ms-agent-eval.md) — 通过 MCP Session Proxy 调度隔离的工具服务

## 参考链接

- 协议官网：<https://modelcontextprotocol.io>
