---
type: "Tool"
title: "Loop Engineering（AI agent 循环工程）"
description: "cobusgreyling/loop-engineering：把 AI agent 编成自动循环的方法论 + 三个 CLI 工具（loop-audit / loop-init / loop-cost）+ 7 个生产模式（L1 报告 → L2 半自动 → L3 全自动）。"
tags: "[ai, agent, loop-engineering, automation, methodology]"
timestamp: "2026-06-27T03:58:00.000Z"
resource: "https://github.com/cobusgreyling/loop-engineering"
---

# Loop Engineering（AI agent 循环工程）

## 它是什么

[`Loop Engineering`](https://github.com/cobusgreyling/loop-engineering) 是一套**把 AI agent 编成自动循环**的方法论——**不**再每次自己写提示词，而是设计一套系统来调度 agent 干活。核心是**五个构件 + 记忆**：定时任务触发、工作树并行、技能固化、MCP 接真实工具、子 agent 分头干活再相互验证。

![Loop Engineering](https://pbs.twimg.com/media/HLt9KlJbMAEsCkN.jpg)

## 核心构件

| 构件 | 角色 |
|------|------|
| 定时任务触发 | 按节奏拉起 agent 循环 |
| 工作树并行 | 多任务并行推进 |
| 技能固化 | 把成功经验沉淀为可复用 Skill |
| MCP 接真实工具 | 让 agent 能调用真实世界工具 |
| 子 agent 分头验证 | 多 agent 相互校验提高质量 |
| 记忆 | 跨循环保留上下文与经验 |

## 三个 CLI 工具

| CLI | 用途 |
|-----|------|
| `loop-audit` | 给项目打分，看够不够格上循环 |
| `loop-init` | 一键搭起一个 loop 工程脚手架 |
| `loop-cost` | 算 Token 花销 |

## 七个生产模式（从轻到重）

| 级别 | 模式 |
|------|------|
| L1 | 纯报告模式（只读 / 只生成） |
| L2 | 半自动（agent 提议，人审批） |
| L3 | 全自动（agent 闭环执行） |
| L4+ | 更高自治级别（含示例模板） |

建议路径：**L1 起步 → 跑稳 → L2 → 跑稳 → L3**。

## 适用场景

- 想把 agent 从「人写一句 → agent 跑一次」升级到「持续运转的循环」
- 需要一套方法论 + 模板 + 工具来避免每次重新设计 agent
- 关心 Token 成本与项目成熟度评估

## 参考链接

- [项目链接](https://github.com/cobusgreyling/loop-engineering)

## 相关概念

- [loops.elorm.xyz](tool-loops-elorm-xyz.md) — 同一类「loop engineering」思路的多人合集
- [Loops（jwangkun/loops）](tool-loops-jwangkun.md) — 100 个 AI 自动化循环模板