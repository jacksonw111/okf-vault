---
type: Tool
title: "CodeGo API（OpenAI 兼容的多模型 API 管理平台）"
description: "Go 写的 API 管理平台，控制面与数据面分离。对外暴露 OpenAI 兼容接口，支持 Claude、Gemini 等多种模型 provider。"
resource: "https://github.com/sh2001sh/CodeGo-Api"
tags: [api-gateway, openai-compatible, multi-model, go, llm-proxy]
timestamp: "2026-07-28T03:07:00.000Z"
---

# CodeGo API

## 它是什么

一个 **Go 写的 LLM API 管理平台**，特点是：

- **控制面 / 数据面分离**：管理（配额、路由、计费、监控）和数据转发（实际调用 LLM）解耦
- **OpenAI 兼容接口**：客户端无需改造，老 SDK 直接用
- **多 provider**：OpenAI、Claude、Gemini 等都可接
- **统一管理**：账号 / 配额 / 路由 / 监控一个面板搞定

## 它适合什么场景

- 自建团队 / 公司的 LLM 网关
- 多 provider 混合调用，按成本 / 性能 / 能力路由
- 老的 OpenAI 客户端想无感切到 Claude / Gemini

## 关键能力

| 能力 | 说明 |
|------|------|
| OpenAI 兼容 | 客户端零改造 |
| 控制面 / 数据面分离 | 运维与转发解耦 |
| 多 provider | Claude / Gemini / OpenAI 等 |
| Go 高性能 | 单二进制部署 |
| 适合企业 / 团队 | 配额 / 计费 / 监控一站 |

## 原始链接

- [项目仓库](https://github.com/sh2001sh/CodeGo-Api)
- [推文剪藏](https://x.com/QingQ77/status/2081939450859331769)

## 相关概念

- [Proxide](./tool-proxide.md) — 任意 Agent 经 MCP / 浏览器接 ChatGPT Pro 网页强模型
- [OpenCode CC](./tool-opencode-cc.md) — 高性能 API 代理，桥接 OpenCode Zen 协议到 Anthropic / OpenAI 兼容
- [animaRouter](./tool-animarouter.md) — 聚合 16+ LLM 提供商免费额度到单一 OpenAI 兼容接口
- [Animarouter（16+ LLM 免费额度聚合）](./tool-animarouter.md) — 同类聚合思路