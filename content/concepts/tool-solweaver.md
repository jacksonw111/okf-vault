---
type: "Tool"
title: "Solweaver（Codex 多 Agent 协作的责任分配框架）"
description: "jay7793 出品的 Codex 多 Agent 框架：把责任压在 Sol（主代理）一头；活少它自己干，派 Terra/Luna 等子代理划算才派；风险足够高才加独立评审。"
tags: "[agent, codex, multi-agent, orchestration, responsibility, delegation]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/jay7793/solweaver"
---

# Solweaver（Codex 多 Agent 协作的责任分配框架）

## 它是什么

[`Solweaver`](https://github.com/jay7793/solweaver) 是 jay7793 给 **Codex** 写的多 Agent 协作框架，针对典型痛点：「**多 Agent 协作最后没人对结果负责**」。

设计原则：
- **Sol（主代理）兜底所有责任**——任务完成、评估、整合
- **能少就少**：活不复杂就让 Sol 自己干，不无脑派子代理
- **派 Terra / Luna** 等子代理才算「合算」（成本 / 时间 / 质量权衡）
- **风险足够高**才加**独立评审**环节
- 子代理之间有清晰分工而非互相拿皮球

## 为什么用它 / 适合什么场景

- 想在 Codex 里做多 Agent 协作，但不想看到「三个子代理各交一份报告就完事了」
- 需要给 AI 编码任务一个**单一问责点**（Sol）
- 想自动按任务复杂度伸缩 Agent 数量，避免「小活也启动 4 个 agent」的浪费

## 关键能力

| 能力 | 说明 |
|------|------|
| 单点问责 | Sol 兜底所有责任 |
| 成本感知 | 划算才派子代理 |
| 风险感知 | 高风险才加独立评审 |
| 子代理分工 | Terra / Luna 角色清晰 |
| 集成 Codex | 直接挂到 Codex harness |

## 媒体

![](https://pbs.twimg.com/media/HQiOV33b0AEULCx.jpg)

## 参考链接

- [项目链接](https://github.com/jay7793/solweaver)
