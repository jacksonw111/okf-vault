---
type: "Playbook"
title: "Agent 网关隔离模式（RAG + Java 网关 + 人工确认卡）"
description: "电商售后场景的 Agent 隔离模式：通过 RAG 只做政策举证，Java 网关做事实与写入权威，人工确认卡做交易关口——让售后 Agent 在本地可复跑，避免大模型直连业务库带来的不可信写入。"
resource: "https://github.com/Eleven617/mall-ai-after-sales-platform"
tags: "[agent, ai-gateway, rag, isolation, ecommerce, playbook]"
timestamp: "2026-09-11T22:00:00Z"
---

# Agent 网关隔离模式（RAG + Java 网关 + 人工确认卡）

## 它解决什么问题

电商售后场景里，大模型 Agent **直接连业务库**会带来三个不可信问题：

1. **幻觉写入**：模型编一个不存在的退款单号。
2. **越权操作**：模型绕开权限做了不该做的状态变更。
3. **不可审计**：没人知道模型到底跑了什么 SQL。

## 解决方案：三段隔离

[mall-ai-after-sales-platform](https://github.com/Eleven617/mall-ai-after-sales-platform) 给出的范式：

| 层 | 角色 | 工具 |
|----|------|------|
| **RAG** | 只做**政策举证**（查 FAQ / 售后政策） | 向量库 + 文档检索 |
| **Java 网关** | 事实与写入的**唯一权威** | 严格校验 + 业务库读写 |
| **人工确认卡** | 交易关口 | UI 卡 / 短信 / 工单 |

模型只负责「**理解 + 拼 payload**」，**永远不能直接写业务库**。所有写入必须经 Java 网关校验，所有交易动作必须经人工确认卡。

## 为什么用它 / 适合什么场景

- 任何 **LLM 需要写业务库** 的场景：客服、CRM、ERP、订单系统。
- 想给企业内部的 AI 集成加 **零信任** 层。
- 想避免「把数据库密码扔给 LLM」的安全事故。

## 关键能力

| 能力 | 说明 |
|------|------|
| 模型无直连 | LLM 不持有数据库账号 |
| 写入必经网关 | Java 层做 schema / 权限 / 业务规则校验 |
| 关键动作必经人 | 退款 / 改地址 / 改单价走人工确认 |
| 完全可复跑 | RAG 数据 + 网关逻辑都是确定性的 |
| 可审计 | 每一步都有结构化日志 |

## 落地边界

- **适合学 Agent 网关隔离模式**：拆三层 + 谁干啥 + 数据流。
- **不适合直接当生产客服**：缺客服状态机、缺工单系统、缺 SLA。

## 参考链接

- 项目仓库：<https://github.com/Eleven617/mall-ai-after-sales-platform>

## 媒体

- ![](https://pbs.twimg.com/media/HR0Y-cTbgAAWlcP.jpg)

## 相关概念

- [auth.md](./tool-auth-md.md) — 面向 LLM / agent 的服务鉴权说明书约定
- [Docker](./tool-docker.md) — 网关层典型部署底座
- [Open GENAI](./tool-open-genai.md) — 日本数字厅 GENAI 本地化版（同为企业级 AI 网关）
</content>
</invoke>