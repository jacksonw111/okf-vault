---
type: "Tool"
title: "Obot（企业 AI 治理平台：模型 / MCP / Skills / 凭据 / 审计）"
description: "obot-platform 出品的开源企业 AI 治理平台：用 MCP 和 LLM 网关，把 Claude Code / Codex / Cursor / VS Code 等客户端接到「获准使用」的模型和服务上——管身份 / 权限 / 凭据 / 审计。"
resource: "https://github.com/obot-platform/obot"
tags: "[obot, ai-governance, mcp, gateway, enterprise, audit, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# Obot（企业 AI 治理平台：模型 / MCP / Skills / 凭据 / 审计）

## 它是什么

[Obot](https://github.com/obot-platform/obot) 是 **Obot AI** 出品的**开源企业 AI 治理平台**——用 **MCP** 和 **LLM 网关**把 **Claude Code / Codex / Cursor / VS Code** 等客户端接到「**获准使用**」的模型和服务上。

## 治理对象

| 对象 | 说明 |
|------|------|
| **模型** | 统一管理多个模型供应商 |
| **MCP 服务** | 集中注册与审批 MCP Server |
| **Skills** | 统一管理与下发 Agent Skills |
| **凭据** | 集中保管 / 轮换 API Key / 凭据 |
| **权限** | 谁能调哪个模型、用哪个工具 |
| **审计** | 谁什么时候调了什么 |

## 为什么用它 / 适合什么场景

- 企业里**多个 AI 客户端并存**（Claude Code / Codex / Cursor / VS Code）——需要一个**统一治理层**。
- 想给员工「**自带的 AI 客户端**」装上**公司级护栏**：身份、权限、凭据、审计缺一不可。
- 想自己部署 **MCP Server 和 Agent**——Obot 给你一套**统一的接入方式**。
- 想从「**单点试用**」走向「**企业 AI 治理**」——必须先回答「**谁在用什么模型、跑什么工具、留什么痕**」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 开源治理平台 |
| 协议 | MCP + LLM 网关 |
| 客户端接入 | Claude Code / Codex / Cursor / VS Code |
| 自托管 | 团队可自部署 MCP Server / Agent |
| 治理维度 | 模型 / MCP / Skills / 凭据 / 权限 / 审计 |

## 媒体

- ![](https://pbs.twimg.com/media/HTGXyrFa0AAbvpB.jpg)

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — Obot 的核心协议
- [HarnessRouter](./tool-harness-router.md) — 把多个 Agent Harness 收进同一 API（Obot 在更上游做治理）
- [AegisOps](./tool-aegisops.md) — 企业值班 Agent 故障处置流水线（治理场景的另一面）