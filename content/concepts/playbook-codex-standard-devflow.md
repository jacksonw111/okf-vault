---
type: "Playbook"
title: "Codex Standard Devflow"
description: "把 Codex 跑大型项目时的会话记忆、产出把关、子过程协作做成一条按阶段推进的开发管线 + G0–G5 五道门禁；装成 Codex skill 后，每个项目可直接调用。"
resource: "https://github.com/qi-mouren/codex-standard-devflow"
tags: [codex, agent-skill, devflow, gated-pipeline, coding-agent]
timestamp: "2026-08-07T06:14:00Z"
---

# Codex Standard Devflow

## 它是什么

Codex Standard Devflow 是一套面向大型项目的 Codex 编程流程规范：把项目开发拆成若干阶段，每阶段配 G0–G5 五道门禁（验收关卡），并把整套流程装成 Codex 的 skill，使每个新项目加载 skill 后即可复用同一条工程主线。它针对 Codex 在大型项目里「会话记忆丢失、产出无人把关、子过程协作混乱」的常见痛点。

## 为什么用它 / 适合什么场景

- 用 Codex 跑中型以上代码库，单次任务往往要跨多个 PR / 多轮迭代。
- 想给 Codex 的工作流加上「明确的阶段划分 + 门禁」，而不是放任它自由发挥。
- 希望团队里所有 Codex 实例遵循同一套工程节奏，便于横向对比与回溯。
- 已经在用 Codex skill 机制，想要一份即装即用的标准开发流。

## 适用场景

- 用 Codex 启动一个全新中型项目（多模块 / 多 PR 序列）。
- 对存量项目做「分阶段重构 / 改造」，需要为每阶段设验收关卡。
- 团队里多人 / 多 Codex 实例并行推进同一项目，希望节奏一致。

## 前置条件

- 已安装 Codex CLI 或可在 IDE 内调用 Codex。
- 已加载本 skill（按 Codex skill 规范安装）。
- 项目使用 Git 管理（流程依赖分支 / commit / PR 作为阶段切分点）。

## 阶段门禁（G0–G5）

| 门禁 | 目的 |
|------|------|
| G0 — 立项 / 上下文 | 锁定需求边界、识别调用方、列出关键文件 |
| G1 — 设计 / 接口 | 输出模块划分 + 接口契约，对齐数据模型 |
| G2 — 实现 / 子任务 | 拆分子任务、并行或串行执行，每个子任务独立可验证 |
| G3 — 自检 / 评测 | 跑测试 / 类型检查 / lint / 业务评测脚本 |
| G4 — 评审 / 产出把关 | 由人或 reviewer 评估产出，对照 G1 契约 |
| G5 — 集成 / 部署 | 合并分支、跑集成测试、准备发版 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 阶段化推进 | 把单次大型任务切成可独立验收的小阶段 |
| 五道门禁 | 防止「一步到位」的盲目产出 |
| Codex skill 化 | 装一次，到处复用 |
| 会话记忆连续 | 通过门禁记录保留上下文，避免下一次启动「归零」 |
| 子过程协作 | 多个 Codex 子任务在同一项目下有清晰边界与产出契约 |

## 媒体

- ![Devflow 流程示意](https://pbs.twimg.com/media/HPAb04TbYAA7Dj_.jpg)

## 相关概念

- [Codex](./tool-codex.md) — 本流程的目标 Agent 平台
- [Codex Work Starter](./tool-codex-work-starter.md) — 给非开发者的稳妥起步路线，与本工具互补
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程化的原则清单，可作为本流程的设计依据