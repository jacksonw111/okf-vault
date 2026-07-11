---
type: Tool
title: "Smart Task Assistant（LangGraph 任务助手）"
description: "Navyachhokar 开源的 AI 工作流应用，基于 LangGraph 与 FastAPI，把用户请求分类后由多节点图生成计划、经评审节点迭代修订，最终通过 REST 接口返回结构化结果。"
resource: "https://github.com/Navyachhoker/smart-task-assistant"
tags: "[langgraph, fastapi, agent, workflow, python]"
timestamp: "2026-07-11T20:00:00Z"
---

# Smart Task Assistant（LangGraph 任务助手）

## 它是什么

`Navyachhoker/smart-task-assistant` 是一个**基于 LangGraph + FastAPI 的 AI 工作流应用**：

1. **分类节点**——把用户请求分类，决定走哪条图分支。
2. **计划节点**——多节点图协作生成执行计划。
3. **评审节点**——对计划迭代修订（可重试）。
4. **REST 接口**——最终返回结构化结果（JSON）。

## 为什么用它 / 适合什么场景

- 想用 LangGraph 构建一个「分类 → 计划 → 评审 → 输出」的多节点工作流。
- 想要一个能跑起来的参考实现，而不是从零搭 LangGraph。
- 后端暴露 REST API 给前端 / 其他服务调用。

## 关键能力

| 能力 | 说明 |
|------|------|
| LangGraph | 多节点图工作流引擎 |
| FastAPI | Python REST 后端 |
| 分类 → 计划 → 评审 | 三段式图编排 |
| 迭代修订 | 评审节点可触发重跑 |
| 结构化输出 | 最终结果以 JSON 暴露 |

## 相关概念

- [Vibe Trading](tool-vibe-trading.md) — 同样基于多 Agent 协作的 AI 应用（金融场景）
- [OpenOPC](tool-openopc.md) — 港大开源的多 Agent 虚拟公司框架
- [Yuxi](tool-yuxi.md) — RAG + 知识图谱 + LangGraph 多智能体编排的多租户平台

## 项目链接

- 项目仓库：<https://github.com/Navyachhoker/smart-task-assistant>