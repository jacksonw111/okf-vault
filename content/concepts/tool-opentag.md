---
type: Tool
title: "OpenTag"
description: "CopilotKit 开源的自托管 Slack AI 代理，在 Slack 内 @ 它即可阅读线程、回答问题、调用工具、渲染丰富结果，支持人工审批关键操作。"
resource: "https://github.com/CopilotKit/OpenTag"
tags: "[slack, ai-agent, copilotkit, self-hosted, mcp]"
timestamp: "2026-06-29T16:00:00Z"
---

# OpenTag

## 它是什么
OpenTag 是 CopilotKit 推出的开源 Slack AI 代理，定位类似「Claude in Slack 的开源自托管替代品」。部署在自己服务器上后，在 Slack 任意频道里 `@它` 即可：自动理解上下文、回答问题、调用外部工具、在对话里渲染表格和柱状图等富文本，并支持关键操作前的人工审批。

## 为什么用它 / 适合什么场景
- **不想把团队对话数据交给第三方 AI 助手**：自托管部署，对话与上下文不出自己的服务器。
- **想给 Slack 装一个有「动手能力」的代理**：不只是聊天，能调工具（查数据库 / 改工单 / 触发 webhook）。
- **关键操作要审批**：自动审批敏感操作（删库、转账、发公告）前先 @ 某人确认。

## 关键能力
| 能力 | 说明 |
|------|------|
| Slack 内 @ 触发 | 在任意频道 @OpenTag 即启动 |
| 上下文理解 | 自动读取线程历史 |
| 工具调用 | 通过 MCP / 自定义工具接外部系统 |
| 富文本渲染 | 在 Slack 对话里渲染表格、柱状图等 |
| 人工审批 | 关键操作前需要指定人员确认 |
| 自托管 | Docker / 云 VM 部署，对话数据自主可控 |
| 开源协议 | CopilotKit 出品，跟其生成式 UI 生态对齐 |

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071620959488921894)
- [项目链接](https://github.com/CopilotKit/OpenTag)

## 相关概念
- [CopilotKit](./tool-copilotkit.md) — 生成式 UI 开源框架，OpenTag 在 Slack 内的富文本渲染基于 CopilotKit 能力
- [AgentSpace](./tool-agentspace.md) — HKUDS 出品的人 + AI 代理团队协作平台，与 OpenTag 共享「团队协作 + AI 代理」的产品思路但载体不同