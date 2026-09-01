---
type: "Tool"
title: "hermes-agent-demo（Spring Boot 4 + Spring AI 2.0 多模型 Agent 运行时）"
description: "基于 Spring Boot 4 / Spring AI 2.0 的多模型 Agent 运行时示例：把子代理、Skills、沙箱执行、MCP 工具与人工审批统一进同一条 SSE 结构化事件流，给 Java 生态一个端到端的 Agent 编排样板。"
resource: "https://github.com/git-syl/hermes-agent-demo"
tags: [agent-runtime, spring-boot, spring-ai, java, mcp, sse, sandbox, human-in-the-loop]
timestamp: "2026-09-01T02:30:00Z"
---

# hermes-agent-demo

## 它是什么
[hermes-agent-demo](https://github.com/git-syl/hermes-agent-demo) 是一个**基于 Spring Boot 4 / Spring AI 2.0 的多模型 Agent 运行时示例**。它把「子代理（sub-agent）/ Skills / 沙箱执行 / MCP 工具 / 人工审批」这几样典型 Agent 组件**统一进一条 SSE 结构化事件流**——前端订阅这一条流就能拿到「代理思考 → 工具调用 → 子代理委派 → 等待审批 → 结果回写」的全部信号。

定位是给 Java / Spring 生态一个端到端的 Agent 编排样板，省去各组件各接各的事件总线、各写各的回调地狱。

## 为什么用它 / 适合什么场景
- Java / Spring 技术栈想落地 Agent：**用同一条 SSE** 把子代理、Skills、工具、人工审批串起来；
- 想要一个**统一事件流**的 Agent 运行时：UI 只需要订阅一个端点就能拿到所有状态变化；
- 想了解 **Spring AI 2.0** 在多模型 / 子代理 / MCP 集成上的当前能力边界；
- 想给 Java 团队引入 Agent 时有一个**可跑的最小骨架**而不是一堆 PPT。

## 关键能力

| 能力 | 说明 |
|------|------|
| Spring Boot 4 基座 | 用最新 Spring 生态做 Agent 运行时 |
| Spring AI 2.0 | 多模型接入（OpenAI 兼容接口） |
| 多模型可切换 | 不同子代理可绑不同模型 |
| 子代理编排 | sub-agent 委派与回传 |
| Skills 机制 | 可复用技能注册 / 调用 |
| 沙箱执行 | 工具调用隔离，避免 prompt 注入打爆宿主 |
| MCP 工具 | Model Context Protocol 工具接入 |
| 人工审批 | Human-in-the-loop，关键动作卡审批 |
| SSE 事件流 | 全部信号走同一条 SSE，前端只订阅一个端点 |
| 结构化事件 | 事件带类型 / payload，前端可类型安全消费 |

## 媒体
![](https://pbs.twimg.com/media/HRBFDipb0AAfiNd.jpg)

## 相关概念
- [Vercel Labs `run`](tool-vercel-labs-run.md) — 同样强调「来宾代码隔离执行」的沙箱思路；`run` 走 worker + QuickJS，hermes-agent-demo 走 Spring 沙箱

## 参考链接
- 项目链接：<https://github.com/git-syl/hermes-agent-demo>