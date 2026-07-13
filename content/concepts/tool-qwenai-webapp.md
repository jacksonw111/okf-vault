---
type: Tool
title: "QwenAI-Webapp"
description: "基于 FastAPI + Vue 3 接入阿里云 DashScope（通义千问）的 AI 聊天示例应用，支持流式回复、文件上传与多模态处理，开箱即跑。"
tags: "[qwen, dashscope, fastapi, vue3, chat-app, multimodal, tool]"
timestamp: "2026-07-13T00:00:00Z"
resource: "https://github.com/ChengzQin/QwenAI-Webapp"
---

# QwenAI-Webapp

一个**基于 FastAPI + Vue 3** 接入 **阿里云 DashScope（通义千问）** 的 AI 聊天示例项目——支持**流式回复、文件上传与多模态处理**，开箱即跑。

## 它是什么

- 一个**端到端**的通义千问接入示例：前端 Vue 3 + 后端 FastAPI；
- 通过阿里云 **DashScope**（含 OpenAI 兼容模式）调通义千问；
- 内置**流式回复（SSE）**、**文件上传**与**多模态**对话能力；
- 定位是"**可 fork 即用**"的最小可用 web 聊天骨架。

## 关键能力

| 能力 | 说明 |
|------|------|
| FastAPI 后端 | 异步 Python Web 框架，天然支持 SSE 流式 |
| Vue 3 前端 | Composition API + 简洁聊天 UI |
| DashScope 接入 | 默认走阿里云 DashScope；支持 OpenAI 兼容模式 |
| 流式回复 | SSE / WebSocket 一类机制，逐字返回不卡顿 |
| 文件上传 | 上传图片 / 文档进入多模态上下文 |
| 多模态 | 文字 + 图片组合输入，体验通义 VL 系列视觉理解 |
| 开箱即跑 | README 给齐依赖与启动步骤，少数环境变量即可 |

## 为什么用它 / 适合什么场景

- 想快速**搭一个通义千问的私有聊天站**——可以托管在公司内网、给团队用、给客户演示；
- 想要一个**最小可用**的多模态聊天参考实现（SSE + 文件 + 图片）；
- 用 **DashScope 的 OpenAI 兼容接口**作为标准，目标接入其它兼容模型时可零改动；
- 在**国内服务器**上跑——不用翻墙、不用 OpenAI key，本地体验对齐国际大模型的多模态；
- 做毕业设计 / 课程 demo / 内部 PoC 时需要**完整前后端工程**而不是裸 `curl`。

## 技术栈速览

```
┌──────────────┐     SSE     ┌──────────────┐    HTTPS    ┌──────────────┐
│   Vue 3 UI   │ ◄────────► │ FastAPI 后端 │  ◄────────► │  DashScope   │
│  聊天界面    │   流式回复   │  路由 / 会话  │   API 调用   │  通义千问     │
└──────────────┘             └──────────────┘             └──────────────┘
                                     │
                                     ▼
                              文件上传 + 多模态
```

## 设计哲学

1. **小而完整**——前后端齐全，能直接 `npm run` + `uvicorn` 跑起来；
2. **以 DashScope 为默认**——国内最省心的通义千问接入路径；
3. **多模态一等公民**——文字、图片、文件从一开始就是流程里的角色；
4. **流式不卡顿**——按 token / chunk 推进，不让用户对着空白等。

## 相关概念

- [LocalEyes](tool-localeyes.md) — 给本地纯文本 LLM 加视觉能力的工具，与本工具的"多模态"路线互补
- [OpenTag](tool-opentag.md) — CopilotKit 开源自托管 Slack AI 代理，同样以"OpenAI 兼容"为接口契约