---
type: "Tool"
title: "LifeOS（danielmiessler/LifeOS）"
description: "用 TypeScript + Bash 写的 AI 助手外挂框架,跑在 Claude Code / Cursor 等编码代理上;核心思想是 TELOS + 七段算法循环(OBSERVE→THINK→PLAN→BUILD→EXECUTE→VERIFY→LEARN),把记忆 / 技能 / 上下文塞给 AI,让它从当前状态自动推进到理想状态。"
resource: "https://github.com/danielmiessler/LifeOS"
tags: "[agent, life-os, telos, claude-code, cursor, memory, skills, framework]"
timestamp: "2026-08-11T16:00:00Z"
---

# LifeOS

[LifeOS](https://github.com/danielmiessler/LifeOS) 把**记忆、技能、上下文**塞给 AI,让它在生活与工作中按你的目标**自己往前推**——从当前状态一直走到理想状态。基于 TypeScript + Bash 写,跑在 Claude Code / Cursor 这类编码代理上。

项目链接：<https://github.com/danielmiessler/LifeOS>

## 它是什么

一个给 AI 助手加外挂的**框架级 Skill 包**,核心思想:**TELOS 框架 + 七段算法循环(OBSERVE→THINK→PLAN→BUILD→EXECUTE→VERIFY→LEARN)**。整个系统打包成单个 skill 分发,内置:

- **Cortex** — 持久记忆
- **Synapse** — 输入路由
- **Pulse** — 统一守护进程
- **ISA 文档体系** — 配套文档架构
- **49 个子技能**

## 为什么用它 / 适合什么场景

- **跨目标推进**:不只回答问题,而是把"当前→目标"的路一步步走完。
- **可分发 Skill 包**:整个系统以 skill 形式分发,装到 Claude Code / Cursor 即可上手。
- **结构化循环**:七段式循环让 agent 行为可观察、可中断、可恢复。

## 关键能力

| 能力 | 说明 |
|------|------|
| TELOS 框架 | 自带"为什么这样做"的语义层 |
| 七段算法循环 | OBSERVE→THINK→PLAN→BUILD→EXECUTE→VERIFY→LEARN 闭环 |
| 单 skill 分发 | 整套框架打包为一个 skill,装上即用 |
| Cortex 持久记忆 | 跨会话记住用户上下文与历史 |
| Synapse 输入路由 | 智能路由输入到合适的处理单元 |
| Pulse 守护进程 | 统一管理 agent 生命周期 |
| ISA 文档体系 | 与框架配套的结构化文档 |
| 49 个子技能 | 开箱即用的具体技能集 |
| 跨编码代理 | Claude Code / Cursor 等兼容 |

## 媒体

![](https://pbs.twimg.com/media/HPVUHTdbgAEfLea.jpg)

## 参考链接

- [项目仓库](https://github.com/danielmiessler/LifeOS)

## 相关概念

- [Agent Skills(代理技能包)](./term-agent-skills.md) — skill 包的标准语义,LifeOS 是其大规模落地实例
- [Claude Code](./tool-claude-code.md) — 终端原生 AI 编码 agent,LifeOS 主要运行平台之一
- [Better Harness](./tool-better-harness.md) — 五维审计 AI 编码工作流,与 LifeOS 的"循环推进"思路互补
- [MyContext](./tool-mycontext.md) — 同样把散落上下文整理给 AI 用的工具