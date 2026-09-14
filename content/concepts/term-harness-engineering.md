---
type: "Term"
title: "Harness Engineering（Harness 工程）"
description: "围绕「怎么把 LLM 包成稳定、可观测、可治理的产品」展开的工程实践：沙箱、权限、工具注册、review 流程、子任务委派、规则注入都属于 harness。"
tags: "[harness, agent, engineering, review, sandbox]"
timestamp: "2026-09-14T22:30:00Z"
---

# Harness Engineering（Harness 工程）

## 它是什么

**Harness Engineering** 是围绕**「怎么把 LLM 包成一个稳定 / 可观测 / 可治理的产品」**展开的工程实践。模型权重是引擎，harness 是发动机舱：负责加载上下文、管理工具调用、跑沙箱、做 review、记录日志、调度子任务、注入规则。

Harness 与「prompt engineering」相对——后者关心单条指令怎么写，前者关心**整套 agent 运行环境怎么搭**。

## 核心组件

| 组件 | 作用 |
|------|------|
| 上下文管理 | 检索 / 压缩 / 摘要 / 句柄化 |
| 工具注册 | 工具 schema / 权限 / 沙箱 |
| 子任务委派 | 主 agent 调度子 agent |
| Review | 代码 / 决策的人工或 AI 复审 |
| 规则注入 | AGENTS.md / Skills / Playbook 按需加载 |
| 审计日志 | 所有动作可回放可追责 |
| 退出码 / 重试 | 错误恢复与可恢复性 |
| 速率 / 成本控制 | token / API 限流 |

## 典型项目

- **Claude Code** — Anthropic 的终端 agent harness
- **Pi Coding Agent** — 终端 agent harness
- **OpenAI Codex** — IDE / 云 agent harness
- **open-code-review** — 阿里专做 review 的 harness
- **Pi Review** — Pi 生态 review harness
- **DeepSeek Harness（dsh-*）** — DeepSeek agent 工作流 harness

## 为什么重要

- **稳定性**：光有模型不够，harness 决定 99% 的产品级可靠性
- **可控性**：harness 决定 agent 能做什么、不能做什么
- **可观测**：harness 决定你能不能 debug agent 的行为
- **可演化**：harness 决定加新工具 / 换新模型 / 接新规则的难度

## 相关概念

- [open-code-review（阿里 AI 代码审查助手）](./tool-open-code-review.md) — 专门做 review 的 harness 典型
- [Pi Coding Agent](./tool-pi-coding-agent.md) — 终端 harness
- [Context Engineering](./term-context-engineering.md) — harness 里的核心子系统
- [Sandbox / 沙箱](./term-sandbox.md) — harness 的安全基础
