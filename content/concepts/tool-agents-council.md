---
type: Tool
title: "agents-council"
description: "0xwilliamortiz/agents-council，给 Claude Code / Codex CLI 加的「召集议会」Skill——一个问题同时发给多个本地 CLI（codex exec / gemini 等），主机 Agent 当主席把各方意见揉成一份建议；不额外花钱因为用的是本地 CLI 而非 SDK 直调 API。"
resource: "https://github.com/0xwilliamortiz/agents-council"
tags: "[agent-skill, multi-agent, council, codex, claude-code, gemini, npx]"
timestamp: "2026-07-22T12:32:00Z"
---

# agents-council

## 它是什么

[`agents-council`](https://github.com/0xwilliamortiz/agents-council) 是一个装到 Claude Code 或 Codex CLI 的 Skill，为本地主机 agent 添加**「召集议会」能力**：把同一个问题同时发给多个已配置好的本地 AI CLI（如 `codex exec`、`gemini` 等），让它们各自独立回答，最后由主机 agent 当**主席**把各方意见揉成一份建议。

## 关键设计

| 维度 | 说明 |
|------|------|
| 触发方式 | 在 Claude Code / Codex CLI 中调用 Skill |
| 执行机制 | 调用本地 CLI 子进程，不直调 SDK / API |
| 协作模式 | 多 CLI 并行 + 主席汇总 |
| 安装方式 | `npx` 一行命令，自动检测当前环境有哪些 CLI 可用，生成对应配置 |
| 成本 | **不额外花钱**——用的是本机已有的 CLI 与它们的订阅 / token |

## 适用场景

- 重要决策想听多个模型的不同看法；
- 编码 / 架构 / 设计问题，希望多角度交叉验证；
- 想用现有 Claude / Codex / Gemini CLI 订阅做「模型委员会」，而不额外买 API。

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [MCO（多 AI 编程代理编排层）](tool-mco.md) | 中立编排层 | 偏任务调度，本工具偏「同一问题多模型回答」 |
| [agents-council](tool-agents-council.md) | Skill（议会模式） | 偏决策辅助 |
| [managed-agents](tool-managed-agents.md) | 本地多 Agent runtime | 偏长时间运行的 agent 集群 |

## 媒体

![](https://pbs.twimg.com/media/HNy5tELboAAVVD3.jpg)

## 原始链接

- [项目仓库](https://github.com/0xwilliamortiz/agents-council)

## 相关概念

- [MCO](tool-mco.md) — 同时调度多种 CLI 编码代理，本工具聚焦在「同一问题多模型交叉回答」
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 的概念元定义
- [opencode-cc](tool-opencode-cc.md) — 让不同 CLI 共享 API 协议，本工具让不同 CLI 共享「一次提问」