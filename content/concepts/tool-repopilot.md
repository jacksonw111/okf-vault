---
type: "Tool"
title: "RepoPilot"
description: "把软件项目从需求沟通到交付验收整条链路，交给模拟产品 / 架构 / 开发 / 测试等角色的 LangGraph Agent 协作体跑完，人只在关键门禁上把关。"
resource: "https://github.com/HHqm/RepoPilot"
tags: [langgraph, multi-agent, software-engineering, devflow, codex, code-automation]
timestamp: "2026-08-07T07:15:00Z"
---

# RepoPilot

## 它是什么

RepoPilot 是一个把软件项目「需求 → 架构 → 开发 → 测试 → 验收」全链路交给一组 LangGraph Agent 协作体跑完的开源工具。它让多个 Agent 分别扮演产品、架构、开发、测试等角色相互协作，人只在关键门禁上把关，避免 Agent 在工程里「各自为政」产出。

## 为什么用它 / 适合什么场景

- 想用 AI Agent 流水线把小型 / 中型项目从需求一口气跑到交付。
- 已有 LangGraph 经验，希望以「角色化协作」而非「单 Agent 多工具」方式组织 Agent。
- 团队里人手不足，希望 Agent 顶掉「先把骨架跑通」这段劳动密集型工作。
- 想把工程门禁（架构评审 / 测试通过 / 验收）作为唯一人介入点，最大化 Agent 覆盖。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多角色 Agent 协作 | 产品、架构、开发、测试等角色以独立 Agent 形式存在 |
| LangGraph 编排 | 用 LangGraph 描述 Agent 之间的对话与状态传递 |
| 端到端覆盖 | 从需求沟通到交付验收一条链贯通 |
| 人把关门禁 | 关键节点（架构、测试、验收）交人审，不让 Agent 全权 |
| 角色化分工 | 避免「万能 Agent」导致的产出风格漂移 |
| 代码仓库内置 | 项目内运行，把代码作为 Agent 协作的载体 |

## 媒体

- ![RepoPilot 协作流程示意](https://pbs.twimg.com/media/HPAb6Q3bIAAJj2Q.jpg)

## 相关概念

- [Codex Standard Devflow](./playbook-codex-standard-devflow.md) — 同样关注大型项目协作与门禁，但侧重 Codex skill 流程化而非多角色 Agent
- [LongHorizon-Harness](./tool-longhorizon-harness.md) — 长程代理脚手架，把记忆、工具、技能、评测做成一整套
- [LangGraph](./tool-langgraph.md) — 本工具的 Agent 编排框架