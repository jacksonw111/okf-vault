---
type: "Tool"
title: "lightcraft（Rust 重做 Lightroom 式照片 / RAW 流程）"
description: "storytold 开源的纯 Rust 照片库与 RAW 显影流程，原生支持 macOS / Windows / Linux / 浏览器，并把每个操作暴露成命令，让 AI agent 通过 MCP 驱动整套工作流。"
resource: "https://github.com/storytold/lightcraft"
tags: "[rust, photo, raw, lightroom-alternative, mcp, ai-agent, cross-platform]"
timestamp: "2026-10-06T00:35:00Z"
---

# lightcraft

## 它是什么

[lightcraft](https://github.com/storytold/lightcraft) 是 **storytold** 开源的纯 Rust 照片库与 RAW 显影工具——**对标 Lightroom 的工作流**，原生支持 macOS / Windows / Linux / 浏览器，**并把每个操作暴露成命令**，让 AI Agent 通过 MCP 直接驱动。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实现 | 纯 Rust |
| 平台 | macOS / Windows / Linux / 浏览器四端原生 |
| 操作可编程 | 每个编辑动作都是命令，可脚本调用 |
| AI 集成 | 通过 MCP 让 AI Agent 跑完整套照片工作流 |
| RAW 显影 | 内置 RAW 解码与编辑管线 |
| 跨端一致性 | 同一份工程在四端行为一致 |

## 适合场景

- 想摆脱 Lightroom 订阅，又想要「现代 RAW 流程」
- 摄影师想用 AI Agent 自动化大批量照片调色
- 跨平台用户（Mac + Win + Linux）想要工具通用

## 参考链接

- 项目链接：<https://github.com/storytold/lightcraft>

## 相关概念

- [MCP](./term-mcp.md) — Agent 调用照片工作流的协议