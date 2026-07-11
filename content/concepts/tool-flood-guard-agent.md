---
type: Tool
title: "Flood Guard Agent（北京山洪防御辅助决策）"
description: "haogx894-afk 开源的北京市山洪防御辅助决策智能体，基于 Spring AI 构建问答链路，支持 ReAct Agent、Tool Calling 和 SSE 流式响应，后端 Java 17 + Spring Boot 3。"
resource: "https://github.com/haogx894-afk/flood-guard-agent"
tags: "[spring-ai, react, agent, sse, java, emergency-response]"
timestamp: "2026-07-11T20:00:00Z"
---

# Flood Guard Agent（北京山洪防御辅助决策）

## 它是什么

`haogx894-afk/flood-guard-agent` 是一个**面向北京市山洪防御的辅助决策智能体**：

- 基于 **Spring AI** 构建问答链路（Java AI 应用框架）。
- 支持 **ReAct Agent**（推理 + 行动循环）+ **Tool Calling**（让模型调用工具）。
- **SSE 流式响应**（Server-Sent Events，Web 端可实时看到模型逐步输出）。
- 后端 **Java 17 + Spring Boot 3**。

## 为什么用它 / 适合什么场景

- 在 Spring / Java 技术栈上做 AI Agent 应用，想看 Spring AI 落地参考。
- 政府 / 应急 / 气象类垂直领域，需要把 LLM 接到业务问答链路。
- 想看「ReAct + Tool Calling + SSE」在 Java 生态里的典型组合。

## 关键能力

| 能力 | 说明 |
|------|------|
| Spring AI | Java 生态的 AI 应用框架 |
| ReAct Agent | 推理 + 行动循环 |
| Tool Calling | 让模型调用预定义工具（数据查询 / 风险评估） |
| SSE 流式 | Web 端实时逐步输出 |
| 业务领域 | 北京市山洪防御辅助决策 |

## 媒体参考

- 项目截图：

![Flood Guard Agent](https://pbs.twimg.com/media/HM6x5XvbgAAkz3l.jpg)

## 相关概念

- [Agent Sphere](tool-agent-sphere.md) — Java + Spring Boot 的 AI Agent 编排平台
- [DataFoundry Data Agent](tool-datafoundry-data-agent.md) — 企业级数据 Agent 工作台

## 项目链接

- 项目仓库：<https://github.com/haogx894-afk/flood-guard-agent>