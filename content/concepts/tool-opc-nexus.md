---
type: Tool
title: "OPC-Nexus"
description: "给单人公司和独立开发者用的本地优先桌面 AI Agent 管理器：Agent 创建、任务编排、多引擎接入、消息渠道集成，一个工作台搞定"
resource: "https://github.com/h4dex/opc-nexus"
tags: [agent, local-first, desktop, orchestrator, solo, indie]
timestamp: 2026-08-17T16:00:00Z
---

# OPC-Nexus

## 它是什么

`h4dex/opc-nexus` 是面向 **One-Person Company（单人公司）/ 独立开发者**的**本地优先**桌面 AI Agent 管理器。在一个工作台里完成：
- **Agent 创建**（不同角色 / 不同任务的 agent）
- **任务编排**（任务派发、状态追踪）
- **多引擎接入**（接入多家 LLM / agent runtime）
- **消息渠道集成**（IM / 邮件 / Webhook 等）

定位：把「一个独立开发者需要的整套 AI 助理能力」收进一个本地应用。

## 为什么用它 / 适合什么场景

- 单人公司 / 独立开发者想用 AI agent 但又不想依赖云端大平台。
- 想要一个工作台同时管多个 agent（销售 / 开发 / 文案 / 客服）。
- 想本地优先运行（数据不出门）+ 跨引擎接入（不绑死某家 LLM）。
- 想要把任务、agent、消息渠道接到一起统一管。

## 关键能力

| 能力 | 说明 |
|------|------|
| Agent 创建 | 自定义多角色 agent |
| 任务编排 | 派发 / 跟踪 / 协作 |
| 多引擎接入 | 接入多家 LLM / agent runtime |
| 消息渠道集成 | IM / 邮件 / Webhook |
| 本地优先 | 数据本地，可离线 |
| 桌面 GUI | 一个工作台统一操作 |

## 媒体

- ![](https://pbs.twimg.com/media/HPvTqlmboAAjlN3.jpg)

## 原始链接

- [项目仓库](https://github.com/h4dex/opc-nexus)

## 相关概念

- [Foundry](./tool-foundry.md) — 同样面向独立开发者 / 单人公司的 AI 数字公司平台，但 Foundry 偏自动生成组织层级，OPC-Nexus 偏本地工作台
- [Evano Studio](./tool-evano-studio.md) — 同样是 Electron + Python 本地 AI 桌面工作台，OPC-Nexus 更聚焦「单人公司」场景