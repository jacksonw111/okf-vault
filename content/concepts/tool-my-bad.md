---
type: Tool
title: "my-bad"
description: "Node.js 开发服务器错误页工具，把原始错误转换为带 sourcemapped 堆栈 / 代码片段 / cause 链 / 组件追踪 / 请求上下文的 JSON 报告"
resource: "https://github.com/danielroe/my-bad"
tags: [nodejs, dev-server, error, debug, sourcemap]
timestamp: 2026-09-05T15:00:00Z
---

# my-bad

## 它是什么
`danielroe/my-bad` 是一款**Node.js 开发服务器错误页工具**（作者 Daniel Roe）：把开发期抛出的原始错误，转换成包含 **sourcemapped 堆栈 / 代码片段 / cause 链 / 组件追踪 / 请求上下文** 的 JSON 报告，输出比默认浏览器错误页更结构化、更适合 IDE / agent 解析。

## 为什么用它 / 适合什么场景
- Node.js / Nuxt / Next 等全栈项目里默认错误页信息不足，调试时反复 devtools 翻栈。
- 想让 AI agent 直接消费错误报告（结构化 JSON 优于纯文本）。
- 希望堆栈回溯能自动 sourcemap 到原始源码（而非编译产物）。

## 关键能力
| 能力 | 说明 |
|------|------|
| sourcemapped 堆栈 | 自动反向映射到源码行 |
| 代码片段 | 报错位置上下文代码片段直接嵌入报告 |
| cause 链 | 沿 `Error.cause` 链展示错误根源链 |
| 组件追踪 | 框架组件栈（如 Vue / React）一并展示 |
| 请求上下文 | 关联错误发生时的请求 URL / headers / body |
| JSON 输出 | 结构化报告，便于 IDE / agent 消费 |

## 媒体
- ![](https://pbs.twimg.com/media/HRbbeG2b0AEua5D.jpg)

## 相关概念
- [原始链接](https://github.com/danielroe/my-bad)