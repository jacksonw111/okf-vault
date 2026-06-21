---
type: "Tool"
title: "Codex Control Plane MCP（Codex Desktop 任务队列）"
description: "一个 Python MCP 服务器，给 Codex Desktop 加一层持久化的任务队列：提交任务后立刻拿到 operationId，之后轮询进度即可，不必把 MCP 连接一直开着。"
resource: "https://github.com/aresyn/codex-control-plane-mcp"
tags: "[mcp, codex, queue, async, python]"
timestamp: "2026-06-21T00:00:00Z"
---

# Codex Control Plane MCP（Codex Desktop 任务队列）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的 Python MCP 服务器：在 **Codex Desktop** 上加一层 **持久化任务队列**。原本 Codex Desktop 的 MCP 调用是「请求 → 等待响应」的同步模型，长任务容易超时；现在可以提交任务后立刻拿到 `operationId`，然后轮询进度，**不必保持长连接**。

## 工作流

1. 提交任务 → 立刻返回 `operationId`
2. 关闭 MCP 连接 / 去做别的事
3. 一段时间后用 `operationId` 轮询 → 拿结果

## 关键卖点

- **断线不丢任务**：任务在队列里持久化，断了也能续。
- **长任务友好**：跑半小时的训练 / 编译 / 爬取都可以丢进去。
- **MCP 原生**：就是个标准 MCP server，Codex Desktop 直接 `add`。

## 适用场景

- Codex Desktop 跑长任务（CI / 训练 / 大批量爬取），不想挂着窗口等。
- 想在 MCP 之上做「任务 → 通知 → 取结果」的异步工作流。

## 媒体

![Codex Control Plane 截图](https://pbs.twimg.com/media/HLJFXYMa0AEzLo8.jpg)

## 相关概念

- [CodexPro](tool-codexpro.md) — 同样是 Codex 生态 MCP 工具，面向 ChatGPT Web
- [DevSpace](tool-devspace-mcp.md) — 同样做本地 MCP 桥，但同步模型
- [MCP（Model Context Protocol）](term-agent-skills.md) — 这些工具的协议底座