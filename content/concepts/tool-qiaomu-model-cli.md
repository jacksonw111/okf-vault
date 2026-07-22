---
type: Tool
title: "qiaomu-model-cli"
description: "joeseesun/qiaomu-model-cli，把本机 Grok CLI（grok-4.5）、Kimi Code CLI（K3 1M）、Claude Code CLI（Fable 5）串起来的统一封装，支持 batch（并行独立）和 dual（先后依赖）两种模式，三家流式事件实时往终端和日志吐。"
resource: "https://github.com/joeseesun/qiaomu-model-cli"
tags: "[cli, multi-model, grok, kimi, claude-code, batch, orchestration]"
timestamp: "2026-07-22T13:34:00Z"
---

# qiaomu-model-cli

## 它是什么

[`qiaomu-model-cli`](https://github.com/joeseesun/qiaomu-model-cli) 把本机已装的多个 AI 编码 CLI 串起来：
- **Grok CLI**（grok-4.5）
- **Kimi Code CLI**（K3 1M）
- **Claude Code CLI**（Fable 5 / 默认模型）

不用一条条手写参数，也不用挨个等一家跑完再启动下一家。

## 两种执行模式

| 模式 | 适用场景 | 说明 |
|------|----------|------|
| **batch** | 独立任务 | 同时启动多个并行任务，不互相依赖 |
| **dual** | 有先后依赖的任务 | 上游结果作为下游输入，串行 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 真正并行 | batch 模式下多任务同时开工，不串行等待 |
| 流式输出 | 三家的流式事件实时往终端和日志里吐，不缓存到结束 |
| 统一封装 | 一个 CLI 调用多家，不用记各家的参数语法 |
| 日志合并 | 多家输出统一进日志，便于事后审计 |

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [MCO](tool-mco.md) | 中立编排层 | 偏长期任务 / 多 agent |
| [agents-council](tool-agents-council.md) | Skill | 偏同一问题多模型回答 |
| qiaomu-model-cli | CLI 统一封装 | 偏「一条命令调用多家」，粒度更细 |

## 原始链接

- [项目仓库](https://github.com/joeseesun/qiaomu-model-cli)

## 相关概念

- [MCO](tool-mco.md) — 同时调度多种 CLI 编码代理，本工具聚焦在「同一 CLI 调用多家」
- [agents-council](tool-agents-council.md) — Skill 形式的「议会」，本工具是 CLI 形式的「批量调用」
- [opencode-cc](tool-opencode-cc.md) — 把不同模型协议桥接为同一协议，本工具在 CLI 层做类似但更轻量的封装