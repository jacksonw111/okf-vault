---
type: Tool
title: "BanyanCode（终端 AI 编程多代理循环工程）"
description: "终端里的 AI 编程多代理编排系统。你下一条指令，它自动分解成多个子代理并行干活（探索 / 写代码 / 查资料），串成完整工作流。基于 OpenCode 和 Effect，TypeScript 写。"
resource: "https://github.com/EkagraAgarwal/BanyanCode"
tags: [multi-agent, terminal, typescript, opencode, effect, orchestration]
timestamp: "2026-07-28T02:49:00.000Z"
---

# BanyanCode

## 它是什么

跑在终端里的 **AI 编程多代理编排系统**——专攻**循环工程（loop engineering）**：

1. 你下一条指令
2. 它自动拆活（探索代码库的、写代码的、查资料的）
3. 多子代理并行跑
4. 自动验证 + 回退重试
5. 跨会话记忆 + 代码图谱索引

技术栈：

- **TypeScript** 写
- 基于 **OpenCode** 和 **Effect**
- 支持 **npm** 安装 + 一键脚本

![示意图](https://pbs.twimg.com/media/HOKWNHna8AAr8eT.png)

## 关键能力

| 能力 | 说明 |
|------|------|
| 多代理并行 | 一个指令 → 多个子代理 |
| 自动拆活 | 探索 / 写代码 / 查资料 |
| 跨会话记忆 | 不必每次重新累积上下文 |
| 代码图谱索引 | 加速探索 |
| 自动验证 + 回退 | 出错自动重试 |
| 终端原生 | TUI 形态 |
| TypeScript + OpenCode + Effect | 现代栈 |

## 适用场景

- 大型代码库重构
- 跨多个文件的功能实现
- 需要并行调研 + 实现 + 测试的任务
- 想"少指挥几个 prompt"的工作流

## 原始链接

- [项目仓库](https://github.com/EkagraAgarwal/BanyanCode)
- [推文剪藏](https://x.com/QingQ77/status/2081934920952295681)

## 相关概念

- [Loop Engineering](./tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论 + 三个 CLI
- [MCO（多 AI 编程代理编排层）](./tool-mco.md) — 中立编排层，同时调度多种 CLI 代理
- [pi-hive](./tool-pi-hive.md) — Pi 的层次化多智能体团队协作工具
- [firstmate](./tool-firstmate.md) — 目录结构 + 规则组合，把终端编码 AI 变「大副」