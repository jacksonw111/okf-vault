---
type: Note
title: "Fable 5 案例：1 周把 email canvas 从 ReactFlow 迁到 WASM + Rust"
description: "案例笔记：thomaspark 团队一周内用 Fable 模型把 ReactFlow 邮件画布迁成 WASM + Rust 自研实现，性能从 100+ 邮件 30fps 跳到 1000+ 邮件 60fps，是「Fable 5 当工程师」能力边界的一次现场证据。"
resource: "https://x.com/thomaspark_gg/status/2074985630225076722"
tags: "[fable5, llm, case-study, wasvm, rust, reactflow, agent-coding]"
timestamp: "2026-07-09T20:50:00Z"
---

# Fable 5 案例：1 周把 email canvas 从 ReactFlow 迁到 WASM + Rust

## 背景
thomaspark 在推特公开了一组数据点：一支小团队用 Fable 模型（来自 MiniMax 的代码生成模型系列，[Fable 5](term-fable5.md) 区间），**用一周时间**完成了从 ReactFlow 到自研 **WASM + Rust 邮件画布**的迁移，并且性能从「100+ 邮件到 30fps」提升到「1000+ 邮件稳定 60fps」。

## 关键数据

| 维度 | ReactFlow 旧实现 | WASM + Rust 新实现 | 提升 |
|------|--------------|------------------|------|
| 邮件节点数 | 100+ | 1 000+ | 10× |
| 帧率 | 30fps | 60fps | 2× |
| 实时流式编辑 | 有上限 | 全支持 | — |
| 开发时间 | — | 1 周 | — |

## 能力点
- 能跨语言栈：JS/TS → Rust + WASM，性能关键段下沉到 native。
- 能使用浏览器 + 开发者工具自测和迭代——Fable 5 不只写代码，还自己跑通浏览器调试。
- 适合实时协作型应用（canvas、流式渲染、节点编辑器）的性能重写场景。

## 行业含义
- 「Fable 5 当工程师」已经能完成**真实性能重写**，而非只能生成 demo 级别脚本。
- 与 [tool-fable5-world-demo](../concepts/tool-fable5-world-demo.md) 案例（Braffolk 4km 程序化世界 99% 由 Fable 5 写就）形成「前端 + 性能 / 渲染」两类 Fable 5 输出证据。
- 与 [tool-fable-harness](../concepts/tool-fable-harness.md)（Claude Code 行为协议）配合：先用 harness 规范工作流，再用 Fable 5 当主力模型——这是「前沿 Claude Code + 前沿模型」组合。

## 媒体参考

演示视频：
- <https://video.twimg.com/amplify_video/2074942782175666176/vid/avc1/1816x1080/Riu8HcbMwK7r6hWS.mp4?tag=28>

## 相关概念
- [tool-fable5-world-demo](../concepts/tool-fable5-world-demo.md) — Braffolk 4km 程序化世界 99% 由 Fable 5 写就
- [tool-fable-harness](../concepts/tool-fable-harness.md) — Claude Code 行为协议 / 纪律化流程
- [tool-claude-real-video](../concepts/tool-claude-real-video.md) — 让 AI 真正看懂视频的 Python 工具（也是"AI 读懂多媒体"的另一面）

## 参考链接
- 原始介绍：<https://x.com/thomaspark_gg/status/2074985630225076722>
