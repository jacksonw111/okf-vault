---
type: "Tool"
title: "cli-faq-shortcuts（从 agent 会话历史挖重复提问生成短命令）"
description: "从本机的 Claude Code 和 Codex 会话历史里挖出反复输入的提问，按意图聚成簇，再写成项目里的短命令。"
resource: "https://github.com/kishormorol/cli-faq-shortcuts"
tags: "[claude-code, codex, agent-history, command-shortcuts, cli, mining]"
timestamp: "2026-09-21T22:00:00Z"
---

# cli-faq-shortcuts

## 它是什么

[kishormorol/cli-faq-shortcuts](https://github.com/kishormorol/cli-faq-shortcuts) 从**本机**的 Claude Code 与 Codex 会话历史里**挖反复输入的提问**，按意图**聚成簇**，再写成**项目里的短命令**。

## 关键流程

1. 读本机 Claude Code / Codex 的会话历史（不联网）。
2. 找出**反复出现的提问模式**（"按口径统计上周订单"跑了 5 次、"把这段日志转成 CSV"跑了 3 次）。
3. 按意图**聚类**——把同一意图的不同措辞归到一簇。
4. 为每簇**生成一条短命令**（项目内可调用的脚本 / Makefile target）。

## 为什么用它 / 适合什么场景

- 每天都在重复相同意图的提问，但措辞每次略有差异。
- 想把**口头提问**沉淀为**可重复执行**的命令。
- 项目级的"我的常用查询"——把 CLI 命令 + 自然语言意图打包。

## 关键能力

| 能力 | 说明 |
|------|------|
| 读本机历史 | 不联网，纯本地处理 |
| 多 agent 兼容 | Claude Code + Codex |
| 意图聚类 | 同一意图的不同措辞归一 |
| 项目级落地 | 输出可直接放进项目的 Makefile / scripts/ |

## 项目链接

- 仓库：<https://github.com/kishormorol/cli-faq-shortcuts>

## 媒体

![](https://pbs.twimg.com/media/HStDipza4AAHReP.jpg)

## 相关概念

- [Claude Code](./tool-claude-code.md) — 它的会话历史是数据源之一
