---
type: Tool
title: "HarnessRouter（HarnessRouter/harnessrouter）"
description: "自托管、兼容 OpenAI Responses API 的统一网关，把 Codex / Claude Code / Hermes 等多个 agent harness 收进一个界面与一套 API 运行"
resource: "https://github.com/HarnessRouter/harnessrouter"
tags: "[agent-harness, openai-compatible, gateway, self-hosted]"
timestamp: "2026-08-19T16:00:00Z"
---

# HarnessRouter（HarnessRouter/harnessrouter）

## 它是什么
[`HarnessRouter/harnessrouter`](https://github.com/HarnessRouter/harnessrouter) 是一个**自托管**、**兼容 OpenAI Responses API** 的统一网关：把 Codex、Claude Code、Hermes 等多种 agent harness 收进同一个界面、同一个 API 后端运行。它解决的是「我装了多个 agent harness，但每次想跑哪个就得装哪家的客户端」的痛点。

## 为什么用它 / 适合什么场景
- 同时在用多个 AI 编码 agent，想在一个面板里切换、对比、调度。
- 自托管合规要求：所有 harness 都跑在自己机器上 / 内网，不出数据。
- 想以 OpenAI Responses API 协议对外提供「统一代理」接口，下游应用按 OpenAI SDK 写法接即可。

## 关键能力
| 能力 | 说明 |
|------|------|
| OpenAI Responses API 兼容 | 下游用 OpenAI SDK 即可调用，零侵入接入 |
| 多 harness 聚合 | Codex / Claude Code / Hermes 等收进同一面板 |
| 自托管 | 数据不外流，可放在内网 |
| 一套 API | 各家 agent 都被抽象成「统一的对话 / 工具调用」接口 |

## 媒体
- ![HarnessRouter 截图](https://pbs.twimg.com/media/HP-rOVta0AAYxdb.jpg)

## 相关概念
- [项目仓库](https://github.com/HarnessRouter/harnessrouter) — 仓库主页
- [dsh-agent-teams](./tool-dsh-agent-teams.md) — dsh 的多代理协作（同领域不同方向）
- [aimux](./tool-aimux.md) — 多家 AI 服务商 HTTP 接口的 Rust 统一封装（粒度到 HTTP API 而非 harness）