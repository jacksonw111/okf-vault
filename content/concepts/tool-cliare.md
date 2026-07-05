---
type: "Tool"
title: "Cliare（CLI 审计工具 for AI Agent）"
description: "Rust 写的 CLI 审计工具，通过黑盒运行时探测为命令行界面生成证据驱动的命令索引、就绪评分与安全审查报告，让 AI agent 不需要反复试错就能可靠使用终端命令。"
tags: "[cli, audit, ai-agent, rust, evaluation, tool-readiness]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/modiqo/cliare"
---

# Cliare（CLI 审计工具 for AI Agent）

## 它是什么

[`Cliare`](https://github.com/modiqo/cliare) 是一个用 **Rust** 写的 CLI 审计工具，通过**黑盒运行时探测**评估一个命令行界面是否适合 AI agent 使用。它把 CLI 当作黑盒测试，记录运行过程中的真实行为，推断命令结构，发现副作用，然后生成：

- **命令索引**（机器可读的命令清单）
- **问题清单**（哪些命令会让 agent 误用）
- **评分卡**（Agent Readiness Score，量化可用性）
- **角色报告**（不同 agent 角色下的适配建议）

![Cliare 截图](https://pbs.twimg.com/media/HMW5Kp5awAAAmrn.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 黑盒运行时探测 | 不读源码，纯靠运行 CLI 收集行为证据 |
| 命令结构推断 | 从真实调用中归纳命令模板与参数 |
| 副作用发现 | 自动识别哪些命令有不可逆效果（删文件 / 写生产 / 触发部署） |
| Agent 就绪评分 | 给 CLI 打分：能不能直接交给 agent 跑 |
| 角色报告 | 针对不同 agent 角色（编码 / DevOps / 数据）的适配建议 |
| Rust 性能 | 大 CLI（成百命令）也能在分钟内完成审计 |

## 解决的问题

- AI agent 接到一个陌生 CLI，**靠「试错」探索**会浪费大量 token + 可能误操作
- 传统 linter / type checker 只能看代码层面，看不到运行时行为
- 缺一个**客观指标**判断「这个 CLI 到底能不能放心交给 agent」
- 团队引入新工具时，想量化评估风险

## 适用场景

- 企业引入新 CLI 工具前的安全审查
- AI agent 平台做工具上架前的可观测性评估
- 给现有 CLI 做「Agent 适配改造」前的现状摸底
- 学术研究：度量 CLI 工具对 LLM 的友好度

## 参考链接

- [项目链接](https://github.com/modiqo/cliare)

## 相关概念

- [SkillSpec](tool-skillspec.md) — 把 AI Agent 的 Skills 当可遵守 / 可测试 / 可验证的契约，与 Cliare 都属于「让 AI 工具更可控」的方向
- [codebase-memory-mcp](tool-codebase-memory-mcp.md) — 代码结构索引 MCP，给 agent 提供结构化的代码库视图，与 Cliare 给 agent 提供结构化的 CLI 视图互补