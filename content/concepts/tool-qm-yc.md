---
type: Tool
title: "QM (Y Combinator)"
description: "Y Combinator 开源的多人智能体框架，给初创公司用。每个员工有隔离工作区，能在 Slack 频道、群聊、项目里和智能体协作；人和房间各自带作用域，记忆 / 文件 / 密钥 / 权限 / 定时任务 / Web 应用 / 持久化沙箱互不干扰。"
resource: "https://github.com/yc-software/qm"
tags: [agent, multi-tenant, slack, yc, harness, typescript, startup]
timestamp: "2026-08-03T06:11:00Z"
---

# QM (Y Combinator)

## 它是什么
QM（`yc-software/qm`）是 Y Combinator 开源的**多人智能体框架**，给初创公司用。**让整个公司共用一个智能体**：每个员工有自己的隔离工作区，也能在频道和项目里一起协作，而不是各养各的个人助理。

人和房间各自带作用域，记忆、文件、密钥、权限、定时任务、Web 应用和持久化沙箱互不干扰。核心是**无头 TypeScript / Node 服务**，harness 和模型走接口，Pi、OpenCode、Codex、Claude Code 随时换。

![QM 协作示意](https://pbs.twimg.com/media/HOreKdJaQAAKQV2.jpg)

## 为什么用它 / 适合什么场景
- **企业级 agent 共享**：替代「每个员工各养各的 Claude Code」的资源浪费与上下文割裂。
- **作用域隔离**：人 / 房间 / 项目三层作用域，记忆 / 文件 / 密钥互不泄漏。
- **harness 解耦**：底层 CLI / 模型可替换，未来切新模型不需要重写 harness。
- **频道原生**：集成 Slack、群聊、项目，agent 已成为组织一员。

## 关键能力

| 能力 | 说明 |
|------|------|
| 工作区隔离 | 每位员工独立的记忆 / 文件 / 密钥作用域 |
| 多人协作 | Slack 频道、群聊、项目里一起把 agent 当协作者 |
| 无头服务 | 类型化接口，harness / 模型 / CLI 全部可替换 |
| 持久化沙箱 | 长期任务 / 后台 agent 有独立运行环境 |
| 定时任务 | 跨员工 / 跨项目的定时 agent 工作流 |
| Web 应用 | agent 可部署出页面 UI 供内部使用 |

## 项目链接
- <https://github.com/yc-software/qm>

## 相关概念
- [Cloudflare Durable Objects Agent](./tool-cloudflare-durable-objects-agent.md) — Cloudflare Durable Objects + R2 + pi 跑 agent runtime 的另一套企业级范式
- [Limboo](./tool-limboo.md) — 给多 AI 编程代理搭统一安全工作区的本地桌面 App
- [CyvisGuard](./tool-cyvisguard.md) — Agent 工具调用授权层，zero-trust 风格
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 技能包的概念元定义
