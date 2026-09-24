---
type: "Tool"
title: "AegisOps（企业值班 Agent 故障处置流水线）"
description: "企业值班人员排查线上故障时，证据散在指标 / 日志 / 调用链 / 变更记录里，处置动作又没有留痕。AegisOps 把取证、诊断、开单、审批和复查收进同一条流水线，Agent 只能读不能改宿主系统。"
resource: "https://github.com/emma-sue/AegisOps"
tags: "[incident, on-call, sre, agent, audit, workflow, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# AegisOps（企业值班 Agent 故障处置流水线）

## 它是什么

[AegisOps](https://github.com/emma-sue/AegisOps) 是面向企业值班 / SRE 场景的 Agent 故障处置流水线：把取证、诊断、开单、审批、复查收进同一条流水线，**Agent 只能读不能改宿主系统**，每一次动作都留痕。

## 它要解决的问题

- 证据散在指标、日志、调用链和变更记录里
- 处置动作没有留痕，事后难复盘
- Agent 误操作的破坏面太大

## 关键能力

| 能力 | 说明 |
|------|------|
| 取证 | 汇总指标 / 日志 / 调用链 / 变更记录 |
| 诊断 | Agent 给假设与下一步建议 |
| 开单 | 自动建工单 |
| 审批 | 关键动作需人审批 |
| 复查 | 处置后留痕，事后可复盘 |
| 只读隔离 | Agent 只能读不能改宿主系统 |

## 适用场景

- 企业值班 / SRE 团队的故障处置流程
- 想把 Agent 引入 incident response 但担心误操作
- 需要完整审计链路（合规 / 复盘）

## 原始链接
- 项目主页：<https://github.com/emma-sue/AegisOps>

## 相关概念
- [Agent 自我验证阶梯](./note-agent-verification-ladder.md) — 把 agent 验证能力阶梯化的方法论
- [OpenMuse](./tool-openmuse.md) — 自托管任务执行台