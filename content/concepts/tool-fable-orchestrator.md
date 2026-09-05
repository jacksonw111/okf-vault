---
type: Tool
title: "fable-orchestrator"
description: "把 Codex 任务拆分给多模型协作：Claude Fable 5.1 规划与最终裁决，GPT-5.6 Luna 常规实现，DeepSeek V4 Flash 高吞吐循环迭代"
resource: "https://github.com/codejunkie99/fable-orchestrator"
tags: [multi-model, orchestrator, codex, claude, gpt, deepseek, agent]
timestamp: 2026-09-05T15:00:00Z
---

# fable-orchestrator

## 它是什么
`codejunkie99/fable-orchestrator` 是一款**多模型分工的编码任务编排器**：把 Codex 任务拆开，分给三个不同模型协作——**Claude Fable 5.1** 负责规划与最终裁决、**GPT-5.6 Luna** 负责常规实现、**DeepSeek V4 Flash** 负责循环迭代与高吞吐实现。

## 为什么用它 / 适合什么场景
- 单一模型在「规划 + 裁决 + 常规 + 高吞吐循环」全流程都表现一般时，按模型特长分工。
- 想要用同一份任务描述同时验证多个模型的强项。
- 想降低单模型 token 成本（让便宜模型做机械活）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 模型分工 | 规划 / 裁决 / 常规实现 / 循环迭代四角色对应四个模型 |
| Claude Fable 5.1 | 规划与最终裁决 |
| GPT-5.6 Luna | 常规实现 |
| DeepSeek V4 Flash | 高吞吐循环迭代 |
| Codex 任务兼容 | 任务可来自 Codex，或以 Codex 为执行端 |

## 媒体
- ![](https://pbs.twimg.com/media/HRVr7Y-agAA0JGd.jpg)

## 相关概念
- [原始链接](https://github.com/codejunkie99/fable-orchestrator)