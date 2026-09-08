---
type: Tool
title: "ENZO"
description: "自托管的多模型 LLM 网关：API Key 锁在用户浏览器里、由 ENZO 仅做中转，docker compose up 一把梭即可访问 300+ 模型，并支持可自进化的 Agent。"
resource: "https://github.com/theguysudo/ENZO"
tags: [llm-gateway, self-hosted, multi-provider, agent, privacy]
timestamp: "2026-09-08T00:00:00Z"
---

# ENZO

## 它是什么
ENZO 是 theguysudo 开源的**自托管 LLM 网关**：把多家 provider 的 API Key **留在用户自己浏览器里**，ENZO 服务端只做请求中转、并不存 Key，最大限度避免「把 Key 交给托管服务」的信任问题。`docker compose up` 一键启动，附带 300+ 模型目录可直接调用，并可基于此养出会自进化的 Agent。

## 为什么用它 / 适合什么场景
- 想用多家 provider 又不愿把 Key 托管到别人服务上。
- 想要一个本地/私有部署的统一 LLM 入口，方便多个内部工具接入。
- 想给自研 Agent 一个稳定的模型路由层。

## 关键能力
| 能力 | 说明 |
|------|------|
| Key 在客户端 | 不存 Key、减少泄露面 |
| 中转网关 | 服务端只转发，零持久化 |
| 300+ 模型 | 内置目录，开箱即用 |
| Docker 一键起 | `docker compose up` 启动整栈 |
| 可挂 Agent | 支持自进化 Agent 框架挂接 |

## 参考
- 原始链接：<https://github.com/theguysudo/ENZO>

## 媒体
- ![](https://pbs.twimg.com/media/HRlJXYaboAE9-cA.jpg)

## 相关概念
- [LiteLLM](https://github.com/BerriAI/litellm) — 同思路的多模型代理
- [OpenRouter](https://openrouter.ai/) — 同思路的托管版
