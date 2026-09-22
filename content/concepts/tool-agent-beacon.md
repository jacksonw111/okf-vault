---
type: Tool
title: "Agent Beacon"
description: "跨 20+ Agent / Harness 的统一会话历史与可观测性中台——把 Claude Code、Codex、Cursor、OpenCode、Cline、Pi 等的 session history 抽取成可复用知识，再以 MCP 或 Skills 喂给下游 Agent。"
resource: "https://github.com/Asymptote-Labs/agent-beacon"
tags: "[ai-agent, observability, memory, mcp, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# Agent Beacon

## 它是什么
一个跨 Agent 统一会话层（Agent Memory + Agent Observability）：

> 把不同 Coding Agent 的完整 session history 收集起来，统一格式、提取可复用知识、记录可观测事件、回放整段会话，并通过 MCP / Skills 再喂给后续 Agent。

支持 Claude Code、Cursor、Codex、OpenCode、Cline、Hermes、Pi、Gemini CLI 等 20+ Agent / Harness。

## 为什么用它 / 适合什么场景
- 同时使用多款 Coding Agent，不想为每个 Agent 单独维护一套记忆。
- 希望 Agent 在新会话里复用之前踩过的坑（调试路径 / 修改习惯 / 纠错记录）。
- 需要把 Agent telemetry 同时发到 Splunk / Datadog / Elastic / Sentinel / S3 / GCS / CloudWatch。
- 需要在 Agent 写代码后做 trace 回放与 token / 工具调用审计。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多 Agent 适配 | 20+ Agent / Harness（Claude Code、Cursor、Codex、OpenCode、Cline、Hermes、Pi、Gemini CLI 等） |
| 会话历史 | 完整记录 prompt / response / tool call / command / 文件修改 / 审批 / MCP / token 使用 |
| 知识抽取 | 从历史会话中提取可复用的项目知识 |
| 回放 | 完整回放一次 Agent session |
| 复用 | 通过 MCP 或 Agent Skills 把知识喂给后续 Agent |
| 数据模型 | 基于 OpenTelemetry |
| 存储 | 默认本地 JSONL（`~/.beacon/endpoint/logs/runtime.jsonl`），不绑定平台 |
| 仪表盘 | CLI `beacon traces` / `beacon endpoint dashboard` |
| 出口 | 可转发到 Splunk / Datadog / Elastic / Sentinel / S3 / GCS / CloudWatch |

## 相关概念
- [Codex Standard DevFlow](playbook-codex-standard-devflow.md) — Codex 工作流；Agent Beacon 跨 Harness 复用记忆能让 Codex 继承 Claude Code 的经验
- [Claude Code](tool-claude-code.md) — Agent Beacon 主适配对象之一
- [OpenTelemetry](term-otel.md) — Agent Beacon 的 telemetry 数据模型底座

## 项目链接
- 项目主页：<https://github.com/Asymptote-Labs/agent-beacon>
