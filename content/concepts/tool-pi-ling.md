---
type: Tool
title: "pi-ling"
description: "把 Native、DeepSeek Harness、Codex 三套编码 Agent Runtime 放进同一个 Electron 会话——每次工具调用和文件改动写进同一条 SQLite 事件日志供回放审阅。"
resource: "https://github.com/guyi-a/pi-ling"
tags: "[ai-agent, multi-agent, electron, sqlite, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# pi-ling

## 它是什么
一个**多 Agent 统一桌面会话**：把 Native、DeepSeek Harness、Codex 三套编码 Agent Runtime 塞进同一个 Electron 会话，**所有工具调用和文件改动写进同一条 SQLite 事件日志**，供回放审阅。

## 为什么用它 / 适合什么场景
- 同时使用多款编码 Agent Runtime，希望有一个统一的「工作会话壳」把它们管起来。
- 想要所有 agent 的工具调用 / 文件改动落入同一条 SQLite 事件流，便于审计与回放。
- 喜欢 Electron 桌面形态而不是单独的命令行。

## 关键能力
| 能力 | 说明 |
|------|------|
| 形态 | Electron 桌面应用 |
| 整合 Runtime | Native / DeepSeek Harness / Codex |
| 日志 | 单一 SQLite 事件日志 |
| 审计 | 工具调用 + 文件改动全部入库 |
| 回放 | 可基于事件日志重放会话 |

## 相关概念
- [Agent Launcher](tool-agent-launcher.md) — 同样统一管理 6 款 Agent CLI，但更侧重「启动 + 工作台」
- [Agent Beacon](tool-agent-beacon.md) — 跨 Agent session history 中台，偏向 memory + observability

## 项目链接
- 项目主页：<https://github.com/guyi-a/pi-ling>
