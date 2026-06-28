---
type: "Tool"
title: "OpenSeek（MoonBit DeepSeek 编程助手框架）"
description: "用 MoonBit 写的编程助手基础库，后端驱动是 DeepSeek。项目分数据、网络、Agent 编排与命令行四层，纯数据层不依赖网络便于测试。"
tags: "[moonbit, deepseek, ai-coding, cli]"
timestamp: "2026-06-27T23:52:00Z"
resource: "https://github.com/moonbitlang/openseek"
---

# OpenSeek（MoonBit DeepSeek 编程助手框架）

## 它是什么

OpenSeek 是 **MoonBit 语言官方仓库**出的一个编程助手基础库 + CLI。后端由 **DeepSeek** 模型驱动，定位类似 Claude Code / Codex CLI，但用国产语言 MoonBit 实现，方便研究 MoonBit 生态如何在 AI 编程代理场景下承接。

## 架构分层

| 层 | 职责 |
|----|------|
| Data（数据） | 纯数据结构与解析，**不依赖网络**，便于单元测试 |
| Network（网络） | DeepSeek API 客户端与流式响应处理 |
| Agent（编排） | 工具调用循环、上下文管理、子任务委派 |
| CLI（命令行） | 终端 REPL 与命令分发 |

清晰的层次让**纯数据层可被单独测试**，是相对一般 AI 编程代理工具的结构性优势。

## 关键能力

- MoonBit 原生：示范一种新兴语言如何构建 AI 编程代理
- DeepSeek 后端：兼容 DeepSeek 的 OpenAI 风格 API
- 工具调用框架：预留 Agent 编排接口
- 模块化：可作为其他 MoonBit AI 应用的底层库

## 参考链接

- [项目仓库](https://github.com/moonbitlang/openseek)
- [原始链接](https://x.com/QingQ77/status/2071018741060731200)

## 相关概念

- [Claude Code](tool-claude-code.md) — 终端 AI 编码代理的代表，OpenSeek 是其 MoonBit 生态的对应物
- [LilBot Agent](tool-lilbot-agent.md) — 另一类轻量终端 TUI 编码代理