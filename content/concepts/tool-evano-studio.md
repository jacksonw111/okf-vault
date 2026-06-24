---
type: "Tool"
title: "Evano Studio（本地 AI Agent 桌面工作台）"
description: "Electron + Python 本地优先桌面应用，让普通用户无需命令行就能创建、运行和管理本地 AI Agent；基于 Ollama 跑本地模型，提供 Agent 创建 / 多轮对话 / 多 Agent 团队 / 知识库 RAG / 本地图片生成 / 日程任务 / Discord 集成。"
resource: "https://github.com/RaulMandujano/evano-studio"
tags: [ai-agent, desktop, local-first, ollama, electron, rag]
timestamp: "2026-06-24T15:30:00Z"
---

# Evano Studio（本地 AI Agent 桌面工作台）

## 它是什么

[`RaulMandujano/evano-studio`](https://github.com/RaulMandujano/evano-studio) 是一个**本地优先的 AI 桌面应用**，让普通用户无需接触命令行就能创建、运行和管理本地 AI Agent。

技术栈：Electron（前端）+ Python（后端），基于 [Ollama](https://ollama.com/) 跑本地模型（支持 Gemma / Qwen / Llama / Mistral 等）。

## 为什么用它 / 适合什么场景

- **零付费 API / 零云服务**：所有模型推理都跑在本机；
- **图形化创建 Agent**：不需要写配置文件，UI 拖拽即可；
- **多 Agent 团队协作**：可以同时跑多个 agent 协同处理任务；
- **RAG 知识库**：内置本地知识库检索增强；
- **附加功能**：本地图片生成 + 日程任务 + Discord 集成。

## 关键能力

| 能力 | 说明 |
|---|---|
| 本地模型 | 通过 Ollama 跑 Gemma / Qwen / Llama / Mistral |
| Agent 创建 | 图形化无需代码 |
| 多轮对话 | 持久化会话历史 |
| 多 Agent 团队 | 多 agent 协同任务 |
| 知识库 RAG | 本地向量库 + 检索增强 |
| 本地图片生成 | 内置图像生成 |
| 日程任务 | 内置定时 / 提醒 |
| Discord 集成 | 跨平台消息推送 |

## 媒体 / 参考链接

- [项目链接](https://github.com/RaulMandujano/evano-studio)

## 相关概念

- [本地 AI 桌面工作台](tool-local-ai-workbench.md) — Electron + 模型/Agent/路由三件套的同类工作台
- [AQBot](tool-aqbot.md) — Tauri 2 多服务商对话 + Agent + API 网关三件套
- [Lumina](tool-lumina-agent-runtime.md) — 端侧 AI Agent 轻量运行时（与本工具组合可做桌面端 agent 容器）
- [Brigade](tool-brigade.md) — 本地多 AI 代理协作框架 + Tideline 长期记忆
