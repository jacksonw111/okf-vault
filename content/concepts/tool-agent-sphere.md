---
type: Tool
title: "agent-sphere"
description: "agent-sphere 是基于 Java 21 + Spring Boot 3.4 的 AI Agent 编排平台:LLM 决策引擎 + ReAct 循环 + 多级记忆 + 多模型路由 + 内置工具 / MCP / SSE。"
resource: "https://github.com/nullpointexception-i/agent-sphere"
tags: [agent-sphere, java, spring-boot, agent, mcp, orchestration]
timestamp: "2026-07-04T15:00:00Z"
---

# agent-sphere

## 它是什么

`nullpointexception-i/agent-sphere` 是一个基于 Java 21 + Spring Boot 3.4 的 AI Agent 编排平台。它把「感知 → 规划 → 执行 → 反馈」做成完整闭环,核心是 LLM 驱动的决策引擎,支持多家模型(OpenAI、DeepSeek、智谱等),并提供内置工具调用、MCP 协议接入、CLI、浏览器操作、SSE 实时推送等能力。

![配图](https://pbs.twimg.com/media/HMW4XmVbcAA1sMZ.jpg)
![配图](https://pbs.twimg.com/media/HMW4ZjqawAA51f-.jpg)

项目链接：<https://github.com/nullpointexception-i/agent-sphere>

## 为什么用它 / 适合什么场景

- **JVM 技术栈团队优先**:大部分 agent 框架是 Python / TypeScript 写的;agent-sphere 给 Spring Boot 团队一个熟悉的栈。
- **企业可观测性 + 灰度**:Spring 生态原本就内置 metrics / actuator / Sleuth,Agent 调用链天然可观测。
- **国产模型顺滑接入**:作者明确写了支持 DeepSeek、智谱,这点对国内场景很实际。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多模型路由 | OpenAI / DeepSeek / 智谱 等切换;支持故障回退 |
| ReAct 执行循环 | 经典 Reason + Act 推理框架 |
| 多级记忆 | 短期对话 / 长期语义 / 工具结果三层存储 |
| MCP 协议 | 客户端 / 服务端都支持,生态互通 |
| 内置工具调用 | shell / http / file / 浏览器操作可由 LLM 调度 |
| CLI / API 双入口 | 命令行直接开会话;REST + SSE 实时流 |
| 浏览器自动化 | 自然语言指令驱动浏览器操作 |

## 典型架构

```
+---------- AgentController ----------+     +-- 内置工具 --+
|                                    |     | shell        |
|   Planner (LLM) ── 决策 ── Actor   |     | http / file  |
|              ↑               ↓     |     | browser      |
|         Memory ── 多级索引        |     +--------------+
|              ↓                     |
|        MCP Client / Server         |
+------------------------------------+
```

## 相关概念

- [Cotal](tool-cotal.md) — 多智能体开放协议框架
- [ORGII](tool-orgii.md) — Rust + Tauri 多 Agent 协作框架
- [Brigade](tool-brigade.md) — 多模型可切换的本地 Agent 团队
- [EverOS](tool-everos.md) — 多 Agent 共享长期记忆层
- [agent-sphere 仓库](https://github.com/nullpointexception-i/agent-sphere) — 项目链接
