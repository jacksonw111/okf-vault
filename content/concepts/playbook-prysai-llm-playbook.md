---
type: Playbook
title: "Prysai-LLM-Playbook"
description: "把「只会在聊天框要文字」的人一步步练到能用 Codex 类工具交付真实任务：先把模型 / 上下文 / 工具 / Skill / Agent 概念理清，再靠小实验练出任务表达 / 结果核查 / 交付完整闭环"
resource: "https://github.com/Prysai/Prysai-LLM-Playbook"
tags: "[llm, codex, agent, playbook, learning-path, skills]"
timestamp: "2026-08-22T02:29:00Z"
---

# Prysai-LLM-Playbook

## 它是什么
[`Prysai/Prysai-LLM-Playbook`](https://github.com/Prysai/Prysai-LLM-Playbook) 是一份面向「AI 普通使用者」的学习型 Playbook：把「只会在聊天框里要文字」的人，一步步训练到能安全地使用 Codex 这类 Agent 工具**交付真实任务**——先理清模型、上下文、工具、Skill 与 Agent 的概念边界，再靠小实验练出任务表达、结果核查、交付的完整闭环。

## 为什么适合这类读者
- **产品 / 运营 / 设计**——以前只用 ChatGPT 聊天，想试 Codex / Claude Code 但无从下手。
- **传统开发者**——能写代码但没用过 AI Agent 工具，想理解「Agent 比 IDE 多了什么」。
- **企业内训负责人**——需要一份可拆解、可演示的入门 Playbook 而不是大部头书。

## 学习路径（4 段）

| 阶段 | 目标 | 关键动作 |
|------|------|----------|
| 概念扫盲 | 分清模型 / 上下文 / 工具 / Skill / Agent | 阅读 README 概念图，画出自己的认知地图 |
| 任务表达 | 把模糊需求拆成 Agent 可执行的步骤 | 找 5 个日常任务练习「一句话 → 多步骤指令」 |
| 结果核查 | 能判断 Agent 输出对不对、是否要回滚 | 用 git diff / 单元测试 / 真实复现三种手段交叉验证 |
| 交付闭环 | 把 Agent 产出整合进真实业务流程 | 选一个真实小项目，从头到尾走完交付 |

## 关键原则
- **先小后大**：每个新概念都先在「5 行代码 + 5 行 prompt」的范围里验证。
- **结果可复现**：用确定性输入（fixture / seed）跑 Agent，看输出一致性。
- **回滚优先**：每一步可被 `git checkout` / 撤销，保证 Agent 不会留下「跑不了的状态」。
- **Skill 复用**：把验证过的 prompt 模板沉淀成 Skill，下次直接加载。

## 媒体
- ![](https://pbs.twimg.com/media/HQNmaxhaoAADJRS.jpg)

## 相关概念
- [AI User Roadmap](./tool-ai-user-roadmap.md) — 面向普通 AI 使用者的入门到完成真实任务的学习路线图
- [learn-agent（7-e1even）](./note-learn-agent-zero-to-coding-agent.md) — 从零到完整 coding agent 的实战教程笔记，每个机制都附零依赖可运行的 Node.js 示例
- [Codex Orange Book](./tool-codex-orange-book.md) — 非官方 Codex 全链路指南，更偏深度工具书
