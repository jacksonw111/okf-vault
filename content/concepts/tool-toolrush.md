---
type: Tool
title: "ToolRush"
description: "面向 AI agent harness 的运行时优化器：模型吐词远快于 harness 干活，ToolRush 专门消除「读文件 / 搜内容 / 跑终端」过程中反复的进程创建与调度开销。"
resource: "https://github.com/OnlyTerp/toolrush"
tags: [agent, harness, performance, cli, tool-runtime]
timestamp: "2026-09-08T00:00:00Z"
---

# ToolRush

## 它是什么
ToolRush 是面向 AI agent harness 的**工具运行时加速器**。观察到模型吐词速度远快于 harness 实际干活的速度，而 harness 在「读文件 / 搜内容 / 跑终端」上的每一跳都要重新 fork 进程或重新调度，ToolRush 专门治这笔开销。

## 为什么用它 / 适合什么场景
- 你跑 Claude Code / Codex CLI / 自研 harness，发现 agent 总是「吐出一大段文字、然后卡几秒、再继续」——卡的时间全在工具调用上。
- 想给 harness 加一层工具预热/缓存/并行而不动 harness 本身。
- 想看工具级 profile，找出每个工具调用具体卡在哪一步。

## 关键能力
| 能力 | 说明 |
|------|------|
| 进程复用 | 工具调用走预热好的进程池，不每次 fork |
| 并行批处理 | 多个小读操作合并/并行 |
| 调度开销削减 | 减少 harness ↔ 工具之间反复序列化的成本 |
| 提速 | 直观效果：agent "思考-干活"循环更顺 |

## 参考
- 原始链接：<https://github.com/OnlyTerp/toolrush>

## 媒体
- ![](https://pbs.twimg.com/media/HRlD9u5bgAAREyk.jpg)

## 相关概念
- [Claude Code](./tool-claude-code.md) — 典型 harness
- [Codex CLI](https://github.com/openai/codex) — 同类 harness
