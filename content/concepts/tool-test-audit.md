---
type: "Tool"
title: "test-audit（OpenClaw 的 Agent 测试审计 Skill）"
description: "openclaw/openclaw 自带的 Agent Skill：让 Agent 在动手写测试前先回答「该不该加这个测试」四问，过关才加——目的不是写得越多越好，而是让 Agent 自觉避开无意义 / 重复 / 高维护成本的测试。"
resource: "https://github.com/openclaw/openclaw/blob/main/.agents/skills/test-audit/SKILL.md"
tags: "[agent-skill, test-audit, test-strategy, openclaw, code-quality, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# test-audit（OpenClaw 的 Agent 测试审计 Skill）

## 它是什么

[test-audit](https://github.com/openclaw/openclaw/blob/main/.agents/skills/test-audit/SKILL.md) 是 [openclaw/openclaw](https://github.com/openclaw/openclaw) 项目**自用**的 Agent Skill——核心任务：**告诉 Agent 什么测试应该加、什么测试是垃圾不应该加**。

工作流：Agent 在准备写测试时，**先回答四个问题**判断这个测试是否值得加，过了才动笔。

## 为什么用它 / 适合什么场景

- 想给 Coding Agent 装一条「**别瞎加测试**」的护栏——Agent 容易为了交差写一堆断言稀烂、覆盖度虚高的测试。
- 团队里反复出现「**改一行测试要改 10 个 case**」「**Mock 把所有路径都打穿了**」这类维护性灾难。
- 推崇 **「测试该写什么、不该写什么」** 的策略层决策，而不是只给「用什么框架」的工具层决策。
- 想要一个**复用度高**的 Skill 模板——可以贴到 Claude Code / Codex / Cursor / Hermes 等任意 Agent Harness。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Agent Skill（Markdown 文档） |
| 输入 | Agent 当前要写的测试上下文 |
| 输出 | 四个问题的答案 + 是否落笔 |
| 定位 | 测试**策略层**判断（该不该加）而非框架层（怎么写） |
| 复用 | 不绑定特定 Agent Harness |

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 格式本身的标准与生态
- [OpenClaw 营销 Skills](./tool-openclaw-marketing-skills.md) — 同一个 OpenClaw 生态下的另一组 Skills
- [本地 AI 工作台](./tool-local-ai-workbench.md) — 可接入 OpenClaw 的桌面工作台