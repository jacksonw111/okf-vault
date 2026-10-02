---
type: "Tool"
title: "Growth Engineer（GTM 工具 + 打法文档合集）"
description: "GetBrew/growth-engineer：78 家 GTM 公司 + 51 条工作流，全部 markdown，MIT 协议。文件分 Company / Tool / Workflow 三种，agent 读完就能执行 GTM 操作；要求 agent 在发消息 / 花钱 / 改数据前先问用户。"
resource: "https://github.com/GetBrew/growth-engineer"
tags: "[gtm, marketing, growth, agent-skills, mcp, workflow, marketing-automation]"
timestamp: "2026-10-02T10:30:00Z"
---

# Growth Engineer（GTM 工具 + 打法文档合集）

## 它是什么

[Growth Engineer](https://github.com/GetBrew/growth-engineer) 是 GetBrew 出品的**GTM 工具 + 打法 markdown 文档合集**——

- **78 家 GTM 公司**的接入说明
- **51 条跨工具工作流**
- 全部是 markdown 文件
- **MIT 协议**
- agent 读完即可照着执行 GTM 操作（发邮件、跑活动、对接 CRM 等）

## 三种文档类型

| 类型 | 内容 |
|------|------|
| **Company** | 单家 GTM 公司的接入说明：API key 在哪拿、限制是什么、Webhook 怎么收 |
| **Tool** | 单个工具调用：MCP 工具 / CLI 命令 / API 端点 |
| **Workflow** | 跨工具 10 步以内的流程：输入、每步工具配置、步骤顺序 |

## 关键约束

> Workflow 里强制要求 **agent 在发消息、花钱、改数据前先问用户**——这是「防止 agent 乱发邮件 / 乱扣费」的核心守门。

## 为什么用它 / 适合什么场景

| 场景 | Growth Engineer 的好处 |
|------|---------------------|
| 想用 agent 跑 GTM | 一套现成 markdown，agent 读完即可上手 |
| 不想逐家查 API 文档 | Company 文件直接告诉 agent key / 端点 |
| 跨工具组合 | 51 条 Workflow 写好现成跨工具流程 |
| 担心 agent 乱花钱 / 乱发消息 | Workflow 内置「先问用户」守门 |
| 私有化 / 自部署 | markdown 本地读，无外部依赖 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 多家公司覆盖 | 78 家 GTM 公司 |
| 工作流丰富 | 51 条现成 Workflow |
| 三层文件 | Company / Tool / Workflow |
| agent 友好 | markdown 纯文本，agent 直接读 |
| MIT 协议 | 可改、可商用 |
| 安全守门 | Workflow 强制「先问用户」 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105967779509633510>
- 项目链接：<https://github.com/GetBrew/growth-engineer>

## 相关概念

- [Agent Skills](./term-agent-skills.md) — 大伞概念，Growth Engineer 是「GTM 领域」的实例
- [MCP（Model Context Protocol）](./term-mcp.md) — Tool 文件多以 MCP 形式提供
- [Harness Engineering](./term-harness-engineering.md) — 守门约束是 Harness Engineering 的典型实践
