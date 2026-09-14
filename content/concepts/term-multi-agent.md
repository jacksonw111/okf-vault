---
type: "Term"
title: "Multi-Agent（多智能体协作）"
description: "把多个 LLM agent 放在一起协同解决复杂任务的设计范式：通过角色分工、消息传递、共享状态或账本，实现单一 agent 难以达到的能力。"
tags: "[multi-agent, agent, orchestration, collaboration, llm]"
timestamp: "2026-09-14T22:30:00Z"
---

# Multi-Agent（多智能体协作）

## 它是什么

**Multi-Agent（多智能体协作）** 是把**多个 LLM agent 放在一起协同解决复杂任务**的设计范式。每个 agent 可以有不同角色、不同上下文、不同工具；通过**消息传递 / 共享状态 / 共享账本**等机制协作。

对比单一 agent，多 agent 的核心价值是把**任务拆分 + 角色分工 + 视角多样化**变成系统的内禀属性。

## 经典架构

| 架构 | 说明 |
|------|------|
| Supervisor-Worker | 一个 supervisor agent 拆任务派给多个 worker agent |
| Peer-to-Peer | 同级 agent 互发消息对等协作 |
| Pipeline / Chain | agent 串联成流水线，前一个的输出是下一个的输入 |
| Ledger-based | 通过共享文件系统 / 账本解耦，零训练自编排（GVS5H） |
| Hierarchical | 多层 agent：顶层规划 → 中层分解 → 底层执行 |

## 适用场景

- 复杂任务需要**多视角**（代码评审 + 安全审计 + 性能测试）
- 单一上下文窗口**装不下**完整任务
- 想用**多个较弱开源模型**协作逼近闭源强模型效果
- 需要**专业化分工**（前端 / 后端 / 测试 agent 各管一摊）

## 已知陷阱

- **通信开销**：agent 之间消息传递可能放大 token 消耗
- **死循环**：agent 互相等回复 / 互相否决
- **错误传播**：上游 agent 的幻觉会被下游放大
- **去重困难**：同一问题被多个 agent 重复处理

## 代表项目

- **GVS5H** — 账本式零样本自编排
- **AutoGen** — 微软多 agent 框架
- **CrewAI** — 角色化多 agent 编排
- **LangGraph** — 多 agent 状态图编排
- **ChatDev** — 虚拟软件公司多 agent 协作
- **MetaGPT** — 多 agent 软件工程团队

## 相关概念

- [GVS5H（账本式零样本多 agent 自编排）](./tool-gvs5h-multi-agent-orchestration.md) — 通过共享账本的多 agent 实现
- [Farcaster（多 coding agent 统一桌面）](./tool-farcaster-multi-agent-desktop.md) — 多 coding agent 的桌面协同

## 参考链接

- Anthropic Building Effective Agents：<https://docs.anthropic.com/en/docs/agents-and-tools/building-effective-agents>
