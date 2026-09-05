---
type: Tool
title: "zvec-grep"
description: "本地优先的 ripgrep + BM25 + 向量检索统一接口（zg 命令），同时作为 MCP 工具供 Codex / Claude Code / Cursor / OpenCode 等 agent 调用"
resource: "https://github.com/zvec-ai/zvec-grep"
tags: [search, ripgrep, bm25, vector, mcp, local-first]
timestamp: 2026-09-05T15:00:00Z
---

# zvec-grep

## 它是什么
`zvec-ai/zvec-grep`（命令行 `zg`）是一款**本地工作区统一搜索层**：基于阿里 zvec，把 **ripgrep（关键词）**、**BM25（语义）** 与**向量检索**统一到一个本地优先的接口；既能直接在终端用 `zg` 搜，也能作为 **MCP 工具** 供 Codex / Claude Code / Cursor / OpenCode 等 AI agent 调用。

## 为什么用它 / 适合什么场景
- 想让本地代码 / 笔记 / 文档被人和 AI agent 用同一套检索层访问（关键词 + 语义 + 向量）。
- agent 调 ripgrep 关键词够了，但找不到「概念相关但用词不同」的文件，希望补语义层。
- 想保留本地优先：数据不出本机。

## 关键能力
| 能力 | 说明 |
|------|------|
| 三模态统一 | ripgrep 关键词 + BM25 语义 + 向量检索统一 API |
| 终端 CLI | `zg` 命令行直接可用 |
| MCP 工具 | 可挂到 Codex / Claude Code / Cursor / OpenCode |
| 本地优先 | 数据与索引留在本机 |
| 阿里 zvec 内核 | 基于 zvec 嵌入/索引基础设施 |

## 媒体
- 视频：<https://video.twimg.com/tweet_video/HRSrbqFbgAAI7rC.mp4>

## 相关概念
- [原始链接](https://github.com/zvec-ai/zvec-grep)