---
type: Tool
title: "CyVisGuard（Agent 工具调用授权层）"
description: "Agent 拿着密钥到处调工具，没人管它该不该做某件事。CyVisGuard 在 Agent 和它要碰的东西之间插一层，每次调用都问一句：谁调的、替谁调的、还能不能继续。"
resource: "https://github.com/flankerhqd/cyvisguard"
tags: [agent, security, authorization, tool-call, guard, zero-trust]
timestamp: "2026-07-29T04:41:00.000Z"
---

# CyVisGuard

## 它是什么

针对一个真实风险：**Agent 拿着密钥到处调工具，没人管它该不该做某件事**。

CyVisGuard 在 **Agent 和它要碰的东西之间插一层**，每次调用都问三个问题：

1. **谁调的？**（agent 身份 / 子代理归属）
2. **替谁调的？**（用户 / 上游代理）
3. **还能不能继续？**（凭证有效 / 上下文允许）

![示意图](https://pbs.twimg.com/media/HOSQqFxbQAAgFyh.jpg)

## 解决的痛点

| 痛点 | CyVisGuard 解法 |
|------|----------------|
| Agent 滥用工具 | 工具调用前置检查 |
| 密钥泄漏后无审计 | 完整调用链路追溯 |
| 子代理越权 | 上下文级授权 |
| 凭证管理混乱 | 集中式授权层 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 工具调用授权层 | Agent → 工具中间拦截 |
| 身份溯源 | 谁调的、替谁调的 |
| 凭证管理 | "还能不能继续"判断 |
| 审计 | 调用链路完整记录 |
| 适合 Agent 时代 | zero-trust 思路 |

## 适用场景

- Agent 系统对接高权限工具（数据库 / 服务器 / 第三方 API）
- 多 Agent 协作场景（子代理越权）
- 需要审计 Agent 行为的合规场景

## 原始链接

- [项目仓库](https://github.com/flankerhqd/cyvisguard)
- [推文剪藏](https://x.com/QingQ77/status/2082325494117380359)

## 相关概念

- [AgentLock](./tool-agent-lock.md) — eBPF LSM 把 AI 代理限制在指定目录
- [AgentStalker](./tool-agent-stalker.md) — 把 LLM Agent 当系统而非模型来审计
- [Cliare（CLI 黑盒审计工具）](./tool-cliare.md) — 给 CLI 打 Agent 就绪评分 + 安全报告
- [Forge Framework](./tool-forge-framework.md) — AI 数据中心与基础设施的安全风险框架