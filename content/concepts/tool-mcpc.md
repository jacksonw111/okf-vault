---
type: "Tool"
title: "mcpc（MCP 服务器命名会话路由）"
description: "手头 MCP 服务器一堆、Agent 每次调工具都要往上下文里灌定义烧 token——mcpc 起个 @命名会话，一条 Bash 命令走 mcpc，调工具读资源走提示词照常用。"
resource: "https://github.com/apify/mcpc"
tags: "[mcp, agent, token-saving, routing, context]"
timestamp: "2026-09-12T22:30:00Z"
---

# mcpc

## 它是什么

[apify/mcpc](https://github.com/apify/mcpc) 是一个 **MCP 服务器命名会话路由**：当 Agent 装了多个 MCP 服务器时，每次调工具都要把工具定义灌进上下文，**烧 token**；mcpc 让 Agent 用 `@命名会话`的方式按需调 MCP，工具定义不进上下文，只在真正调用时才按名加载。

## 核心特性

| 特性 | 说明 |
|------|------|
| 命名会话 | `@mcp_name` 调用对应 MCP |
| 按需加载 | 工具定义不灌上下文 |
| 节省 token | 大幅降低系统 prompt 长度 |
| 兼容现有 | 读资源 / 提示词用法照旧 |

## 为什么用它 / 适合什么场景
- 装了一堆 MCP 服务器，上下文经常被工具定义塞爆。
- 想省 token 又不想丢 MCP 能力。
- 想让 Agent 按需调用不同 MCP，而不是把全部定义都带上。

## 关键能力

| 能力 | 说明 |
|------|------|
| 命名路由 | `@server_name` 语法 |
| 按需加载 | 工具定义不进上下文 |
| 兼容读资源 | 资源读取走提示词 |
| 节省 token | 系统 prompt 大幅瘦身 |

## 参考链接

- 项目仓库：<https://github.com/apify/mcpc>

## 媒体

- ![](https://pbs.twimg.com/media/HR5sVF8bUAA_xb1.jpg)

## 相关概念
