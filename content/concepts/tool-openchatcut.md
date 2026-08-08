---
type: "Tool"
title: "OpenChatCut"
description: "把对话式 AI Agent 与专业多轨时间线放进同一个本地视频工程：让 Codex / Claude Code 与内置 Agent 直接读取、剪辑并导出可继续编辑的真实视频项目，桥接「一次性 AI 生成」与「传统剪辑器」两大盲区。"
resource: "https://github.com/0xsline/OpenChatCut"
tags: [video-editing, ai-agent, codex, claude-code, multi-track]
timestamp: "2026-08-08T20:30:00Z"
---

# OpenChatCut

## 它是什么

OpenChatCut 把「对话式 AI Agent」与「专业多轨视频时间线」放进同一个本地工程。它桥接当下两大盲区：一次性 AI 视频生成器（Sora / Veo / Runway 等）出片后无法再改，传统剪辑器又没法让 AI 直接参与编辑。Codex / Claude Code 和 OpenChatCut 内置 Agent 可以直接读取工程、剪辑片段并导出可继续编辑的真实视频项目（FCPXML / EDL / OpenTimelineIO 等）。

## 为什么用它 / 适合什么场景

- 想让 AI agent 直接参与视频剪辑（粗剪 / 字幕 / 重组），而不是「先 AI 生成再人工重做」。
- 希望 AI 改完的工程还能在 DaVinci Resolve / Premiere / Final Cut 里继续精细修。
- 想用自然语言驱动多轨时间线（替换片段 / 重新排序 / 加转场）。
- 在本地工作流里跑，不希望视频数据上云。

## 关键能力

| 能力 | 说明 |
|------|------|
| 对话式 Agent | 用自然语言指挥 agent 操作时间线 |
| 多轨时间线 | 视频 / 音频 / 字幕 / B-roll 多轨道 |
| 主流 Agent 兼容 | Codex / Claude Code / 内置 Agent |
| 导出真实工程 | 输出 FCPXML / EDL / OpenTimelineIO |
| 本地优先 | 视频素材和工程文件留在本机 |
| 双向操作 | 既能「AI 改传统工程」，也能「传统剪辑 AI 辅助」 |

## 相关概念

- [FableCut](./tool-fablecut.md) — 浏览器内视频编辑器（时间线为 JSON，Agent 经 MCP 直接剪）
- [OpenMontage](./tool-openmontage.md) — 首个开源 agentic 视频制作系统（自然语言到成片）
- [blockout](./tool-blockout-previs.md) — 用灰盒场景做 AI 视频生成的 previs