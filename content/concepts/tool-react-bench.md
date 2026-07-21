---
type: "Tool"
title: "ReactBench（编码 Agent 用的 React 实战评测）"
description: "给编码 Agent 用的 React 实战评测：不仅看测试过没过，还检查会不会引入新的 React 质量问题（性能 / 无障碍 / 可维护性），专门对付「测试全绿但上线就出问题」的 React 代码。"
resource: "https://github.com/millionco/ReactBench"
tags: "[react, benchmark, coding-agent, evaluation, frontend]"
timestamp: "2026-07-20T20:20:00Z"
---

# ReactBench（编码 Agent 用的 React 实战评测）

## 它是什么

[millionco/ReactBench](https://github.com/millionco/ReactBench) 是面向 **AI 编码 Agent** 的 React 项目实战评测：传统单元 / 集成测试只能看功能过没过，而 ReactBench 还会自动评估 Agent 写出来的 React 代码有没有**新的质量问题**——性能瓶颈、无障碍违规、可维护性下降。它解决「测试全绿、但生产出问题」的痛点。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实战项目 | 跑真实 React 项目而非孤立 LeetCode 题 |
| 多维评估 | 同时检查功能正确性、性能、无障碍、可维护性 |
| 编码 Agent 友好 | 可挂到 Codex / Claude Code / Cursor 等 agent 的 CI 里自动跑 |
| 失败 / 退化检测 | 即使老测试全绿，也会抓出新引入的 React 反模式 |

![ReactBench 截图](https://pbs.twimg.com/media/HNgOcUQb0AAq-EB.jpg)

## 相关概念

- Sketchpad MCP（仅同名相关，非同类工具，跳过链接）
- [Loop.js](./tool-loop-js.md) — 目标 → 标准 → Verify 三闭环，本质上是 agent 自验证循环

## 参考链接

- 项目链接: <https://github.com/millionco/ReactBench>
