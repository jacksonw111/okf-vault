---
type: "Tool"
title: "trycompai/crm"
description: "AI Agent 驱动的 CRM：独立部署的 agent 自动查证客户资料、累计记录、预约跟进，研究预算耗尽就自己停，人只需拍板 agent 拿不准的证据。"
resource: "https://github.com/trycompai/crm"
tags: [crm, ai-agent, autonomous, sales, budget-control]
timestamp: "2026-08-08T20:30:00Z"
---

# trycompai/crm

## 它是什么

trycompai/crm 是一款 AI Agent 驱动的 CRM 系统，让一个独立部署的 agent 代替人做客户资料查证、记录累计、跟进预约等例行工作。Agent 有自己的「研究预算」，预算耗尽就自己停手，避免无限调用 API 烧钱；遇到拿不准的证据再让人拍板。

## 为什么用它 / 适合什么场景

- 小团队希望销售流程自动化，但不愿把关键决策交给模型。
- 想用 AI Agent 把客户档案 / 邮件 / 跟进整合进同一系统。
- 关心成本与可控性，希望 agent 在预算耗尽时主动暂停。
- 想做「agent 主动研究 + 人拍板关键证据」的协作范式。

## 关键能力

| 能力 | 说明 |
|------|------|
| 客户资料查证 | agent 自动拉取 / 验证客户公开信息 |
| 记录累计 | 持续积累沟通、邮件、互动历史 |
| 跟进预约 | agent 主动建议下次接触时机 |
| 预算自停 | 研究预算耗尽主动停手，避免失控 |
| 人在关键点拍板 | agent 拿不准时主动让人介入 |
| 独立部署 | 可在自己的基础设施上运行 |

## 相关概念

- [OpenTag](./tool-opentag.md) — CopilotKit 的自托管 Slack AI 代理，同为 agent 接管沟通场景
- [Agent Skills](./term-agent-skills.md) — 给 Agent 加装能力的标准形式
- [12-Factor Agents](./tool-12-factor-agents.md) — Agent 工程化原则