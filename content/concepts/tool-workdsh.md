---
type: "Tool"
title: "WorkDSH（DeepSeek Harness 桌面工作台）"
description: "techflag 出品的开源桌面工作台：基于 DeepSeek Harness（DSH），用 TypeScript + Electron 写，把项目、资料库、专家、技能、连接器、任务与成果工作区收进同一处，同时保留 DSH 原生的模型 / 工具 / 会话 / / 命令与 @ 引用。"
resource: "https://github.com/techflag/workdsh"
tags: "[dsh, deepseek-harness, desktop, electron, agent, workspace]"
timestamp: "2026-09-27T21:55:00Z"
---

# WorkDSH（DeepSeek Harness 桌面工作台）

## 它是什么

[WorkDSH](https://github.com/techflag/workdsh) 是 techflag 出品的**开源桌面工作台**：基于 **DeepSeek Harness（DSH）** 之上，用 **TypeScript + Electron** 写成。

核心思路：一个 AI 任务往往需要**资料 + 工作规则 + 能力 + 可检查的成果**，所以 WorkDSH 把以下几样**收进同一个桌面**：

- **项目**（按任务 / 主题分组）
- **资料库**（参考文档 / 上传资料）
- **专家**（持久化的角色 / 人格）
- **技能**（Skill / 工具）
- **连接器**（外部数据源 / MCP）
- **任务与成果工作区**（跑出来的产物）

同时**完整保留 DSH 原生体验**：模型切换 / 工具调用 / 会话管理 / `/` 命令 / `@` 引用。

## 为什么用它 / 适合什么场景

- **重度 DSH 用户**：命令行版 DSH 用着方便但缺少「按项目归档」能力，WorkDSH 直接补齐。
- **多任务并行**：在桌面端同时跑多个 AI 项目，每个项目独立的资料库 / 技能 / 任务。
- **协作 / 交接**：项目 + 资料 + 专家 + 技能被显式组织，比纯命令行更易交接。
- **保留原生**：不想为了「桌面化」放弃 DSH 原生的命令、@引用与会话能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Electron 桌面应用 |
| 后端 | 复用 DeepSeek Harness 全部能力 |
| 前端 | TypeScript |
| 组织维度 | 项目 / 资料库 / 专家 / 技能 / 连接器 / 任务 / 成果 |
| 原生兼容 | 模型 / 工具 / 会话 / `/` 命令 / `@` 引用 |
| 适合 | 重度 DSH 用户、多任务并行场景 |

## 媒体

- ![](https://pbs.twimg.com/media/HTH5KQNbAAAdv29.jpg)

## 相关概念

- [DeepSeek Harness](./term-deepseek-harness.md) — WorkDSH 的底层基础
- [DSH-X（DeepSeek Harness Windows 图形启动器）](./tool-dsh-x.md) — 另一个 DSH 桌面化项目（侧重启动 / 版本管理）
- [Evano Studio](./tool-evano-studio.md) — Electron + Python 本地 AI 桌面工作台，Ollama + 多 Agent + RAG