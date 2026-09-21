---
type: "Tool"
title: "CyberGuard（AI Agent 安全响应：批准 → 执行 → 独立验证）"
description: "让 AI Agent 的安全响应先拿到绑定具体目标的批准再下发，动作执行完再用独立探针回头确认状态是否真的恢复，每一步都留可查的审计记录。"
resource: "https://github.com/elsechord/CyberGuard"
tags: "[security, agent, hitl, audit, incident-response, approval]"
timestamp: "2026-09-21T22:00:00Z"
---

# CyberGuard

## 它是什么

[elsechord/CyberGuard](https://github.com/elsechord/CyberGuard) 给 **AI Agent 的安全响应**加一套**强制流程**：

1. **批准**——Agent 想做什么安全动作，先要拿到一份**绑定具体目标**（不是「这台机器」而是「进程 PID 12345」）的批准。
2. **执行**——通过批准后下发动作。
3. **独立验证**——动作完成后，由**独立探针**回头确认**状态是否真的恢复**（不能由 Agent 自己说"好了"）。
4. **审计**——每一步都留可查的记录。

## 解决的问题

- Agent 自动响应**误操作**——把生产环境的健康服务也当成威胁「修」了。
- 自我验证**不可信**——Agent 自己说「修好了」不算修好，需要独立探针。
- **审计 / 合规**——安全动作必须可追溯到「谁批的、批了什么、做了什么、结果怎样」。

## 为什么用它 / 适合什么场景

- SOC / 安全运维想**引入 Agent 自动化**但不愿放弃人工审批与审计。
- 对**生产环境**的安全响应要求**零误操作**。
- 想做**带强制的 HITL（Human-in-the-Loop）**——Agent 不能跳过批准。

## 关键能力

| 能力 | 说明 |
|------|------|
| 目标级批准 | 批准必须绑具体目标（如进程 ID、IP、容器名） |
| 独立验证 | 探针不属于执行 Agent，结果可信 |
| 全程审计 | 批 / 执 / 验三步都有日志 |
| HITL 强制 | Agent 没法跳过批准直接动手 |

## 项目链接

- 仓库：<https://github.com/elsechord/CyberGuard>

## 媒体

![](https://pbs.twimg.com/media/HSonGdXaYAAgNVW.jpg)

## 相关概念

- [AgentStalker](./tool-agent-stalker.md) — 同样把 LLM Agent 当系统而非模型来审计
- [Sandbox（沙箱）](./term-sandbox.md) — Agent 安全执行的标准隔离环境
