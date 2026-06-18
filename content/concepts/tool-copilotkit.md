---
type: "Tool"
title: "CopilotKit（生成式 UI 开源方案）"
description: "把 Claude Artifacts「在 app 里实时生成可交互 UI」的能力开源化、组件化：AI agent 输出结构化 JSON → CopilotKit 把它渲染成真实 React 组件；让「生成式 UI」从闭源 demo 变成生产可用的框架。"
tags: "[ai, agent, generative-ui, react, open-source, ai-sdk]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://github.com/CopilotKit/CopilotKit"
---

# CopilotKit（生成式 UI 开源方案）

> 来源：[@IndieDevHailey on X 2026-06-07](https://x.com/IndieDevHailey/status/2063450486762811628)

## 它是什么

[CopilotKit](https://github.com/CopilotKit/CopilotKit) 是一个 **React 组件 + AI Agent 集成框架**，GitHub 33k+ Star，目标是把 Claude Artifacts 那种「**AI 在 app 里实时生成可交互界面**」的能力**开源化、组件化、生产化**。

过去 agent 只能在聊天框画饼（输出 Markdown 文本）；CopilotKit 让 agent 直接在你的产品里**生成按钮、表单、图表、可点可填的真组件**。

## 与 Claude Artifacts 的关系

| 维度 | Claude Artifacts | CopilotKit |
|------|------------------|------------|
| 形态 | 闭源，绑在 Claude.ai | 开源，自托管 / 私有部署 |
| 渲染位置 | Claude.ai 侧栏 | **你自己的产品**内 |
| 集成方式 | 仅 chat 内 | `<CopilotKit>` / hooks / actions 全套 API |
| 触发器 | 仅 Claude | Claude / GPT / 自家 LLM / LangGraph / CrewAI… |
| 控制粒度 | 受限于官方 | 自定义 UI、自定义 action、自定义上下文 |

## 三条最实用路径（来源推文摘录）

| 路径 | 场景 |
|------|------|
| Controlled（受控生成） | UI 完全由你定义，agent 只填值（最安全） |
| Predictive actions | 预判用户下一步动作，直接渲染对应按钮 / 表单 |
| Generative UI | agent 自由组合组件，适合数据探索 / 配置向导 |

## 关键能力

| 能力 | 说明 |
|------|------|
| React 组件库 | `<CopilotKit>`、`<CopilotChat>`、`<CopilotSidebar>`、`<CopilotTextarea>` 等 |
| Generative UI | agent 输出结构化 UI 描述，CopilotKit 渲染成真组件 |
| Actions | 把后端函数注册为「agent 可调用动作」，自动出现为可点按钮 |
| CoAgents（LangGraph 集成） | 复杂多步骤 agent 在前端实时反映状态 |
| 多 LLM 适配 | Anthropic / OpenAI / 自托管 |
| 与 AI SDK 集成 | Vercel AI SDK 的 `useChat` / `streamUI` 一等公民支持 |

## 为什么值得收藏

- **产品体验的代际跳跃**——传统 agent 跑完任务只能给一段文字；CopilotKit 让 agent 把结果直接渲染成可交互 UI（图表、表单、3D）。
- **Generative UI 的开源基线**——不用每次从零造轮子，组件库 + hook 一应俱全。
- **不锁 provider**——Claude / GPT / 自家模型随便换。

## 与本知识库其他概念的关系

- [JSON-Render / HarnessAgent](tool-json-render.md) — 同一波「生成式 UI」思路，定位略偏「实验性 sandbox 渲染」；CopilotKit 更偏生产化 React 集成。
- [Archify](tool-archify.md) — 同样 LLM 输出结构化 JSON → 渲染器消费的范式（架构图方向）。
- [Claude Code](tool-claude-code.md) — 终端 agent；CopilotKit 让「agent 渲染 UI」这件事在 web 前端落了地。

## 相关概念

- [JSON-Render / 生成式 UI](tool-json-render.md) — 同范式，sandbox 偏实验；CopilotKit 偏生产 React 集成
- [Archify](tool-archify.md) — 同 LLM→JSON→渲染 思路，产物是 SVG 架构图
- [Claude Code](tool-claude-code.md) — CopilotKit 不直接接 Claude Code，但生成式 UI 范式同样适用 agent 输出的渲染
