---
type: Tool
title: "Skill_MAS（元技能进化的多智能体编排）"
description: "通过进化一份单一的元技能文件（SKILL.md），让 LLM 自动设计与编排多智能体系统（MAS），无需人工逐个手搭。"
resource: "https://github.com/linhh29/Skill_MAS"
tags: [agent-skills, multi-agent, mas, meta-skill, codex]
timestamp: "2026-06-25T05:22:00Z"
---

# Skill_MAS（元技能进化的多智能体编排）

## 它是什么

一个把「**多智能体系统（MAS）设计与编排**」**自动化**的项目。它的核心思想是：

- 维护**单一**的元技能文件（`SKILL.md`）。
- 让 LLM **自动**基于这个元技能，设计并编排出一个完整的多智能体系统。
- 元技能本身可**进化**（meta-evolution），随着使用反馈不断变好。

传统做法：人写 N 个 SKILL.md / agent prompt，互相手搭。
Skill_MAS 的做法：人写 1 个 meta-SKILL.md，让模型去**生成**那 N 个。

## 为什么用它 / 适合什么场景

- 不想手动设计 agent 拓扑——把「该有几个 agent、各自干什么」交给模型。
- 多智能体系统的**起点模板**——先让模型草拟一份，再人工调整。
- 「Skill 本身也是被 Skill 编排的对象」——一种自指式设计。

## 关键看点

| 维度 | 说明 |
|------|------|
| 输入 | 单一 meta-SKILL.md |
| 输出 | 自动设计 + 编排的 MAS |
| 机制 | 元技能可进化（feedback-driven） |
| 价值 | 把「MAS 设计」从手搭活变成 prompt 活 |

## 媒体

![](https://pbs.twimg.com/media/HLjGS-ya0AAkLd4.jpg)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill_MAS 站在 Agent Skills 之上，进化的是「**meta-Skill**」
- [ORGII](./tool-orgii.md) — Rust + Tauri 多 Agent 协作框架；Skill_MAS 是「**自动生成**」一整套 ORGII 类的拓扑
- [Brigade](./tool-brigade.md) / [AgentCrew](./tool-agent-crew.md) — 都是 Skill_MAS 输出形态的可能候选
- [pi-task](./tool-pi-task-delegation.md) — 单 agent 内的子任务委派；Skill_MAS 是多 agent 拓扑层面的委派