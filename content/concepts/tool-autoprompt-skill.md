---
type: Tool
title: "autoprompt-skill（编码 agent 自拆目标 + 并行质检）"
description: "Spielewoy 开源：给编码智能体补一层「自己拆目标、并行干活、独立质检」的执行框架，Terminal-Bench 2.1 实测把 agentic 编码任务失败次数从 29 降到 16（60/89 → 73/89），代价约 3 倍耗时、2 倍 token。"
resource: "https://github.com/Spielewoy/autoprompt-skill"
tags: [agent, code, eval, terminal-bench, opencode, quality]
timestamp: 2026-08-21T11:25:00Z
---

# autoprompt-skill（编码 agent 自拆目标 + 并行质检）

## 它是什么
autoprompt-skill 是一个给编码智能体（OpenCode / Codex / Claude Code 等）外挂的执行框架：让 agent 自己拆解大目标为并行子任务，每条子任务跑完后还要再过一道独立质检关。它不是单一 prompt，而是一组可挂载到现有 agent 的「编排纪律」。

## 实测效果（Terminal-Bench 2.1）
| 模式 | 解决率 | 失败次数 | 耗时 | Token |
|------|------|------|------|------|
| OpenCode 裸跑 | 60 / 89 | 29 | 1x | 1x |
| OpenCode + Autoprompt | 73 / 89 | 16 | ~3x | ~2x |

「失败次数近半」是这套框架的核心收益：靠「拆目标 + 并行 + 独立质检」三件套，把一次大任务里被边界 case / 上下文漂移搞砸的概率压下来。代价是更长的执行时间和更多 token。

## 为什么用它 / 适合什么场景
- 现有编码 agent 在 benchmark 上「能解决大多数题，但总有几道卡死」的工程实践场景。
- 长链路任务（如重构 / 大型功能实现 / 跨多文件改动）希望「先求成功率再谈效率」。
- 想要一个可量化的「让 agent 更稳」外挂，看 benchmark 决定是否启用。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自拆目标 | Agent 自己把大任务拆成可并行子任务 |
| 并行执行 | 子任务并行处理，整体 wall-clock 比串行短 |
| 独立质检 | 每条子任务完成后单独由「质检代理」把关 |
| 可挂载 Skill | 作为 Skill 单元挂到 OpenCode / Codex / Claude Code 等 |
| 量化收益 | Terminal-Bench 2.1 有公开数据 |

## 一句话总结
**给编码 agent 加一层「拆目标 + 并行 + 独立质检」纪律——失败次数减半，代价是 3 倍时长和 2 倍 token。**

## 原始链接
- [Spielewoy/autoprompt-skill](https://github.com/Spielewoy/autoprompt-skill) — 原始仓库

## 相关概念
- [Orca 工单编排流程](./concepts/playbook-orca-ticket-orchestration.md) — 同属「让 agent 多步协作」的工程实践
- [Loop.js](./concepts/tool-loop-js.md) — 目标 + 执行 + 验证三件事同一种 prompt，独立只读 Verify agent 判定