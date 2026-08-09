---
type: "Tool"
title: "mycontext"
description: "openTrinity 写的「个人 AI 上下文」工具：把散落在 IM / 文档 / 日历 / 会议里的工作信息整理成一份私有的个人上下文，让 AI 直接基于它工作，而非每次从空白提示词开始。"
resource: "https://github.com/openTrinity/mycontext"
tags: [ai-context, personal-knowledge, prompt-engineering, productivity]
timestamp: "2026-08-09T19:35:00Z"
---

# mycontext

## 它是什么

[mycontext](https://github.com/openTrinity/mycontext) 是一个「**个人 AI 上下文**」工具：把散落在 **IM / 文档 / 日历 / 会议**里的工作信息整理成一份**私有的个人上下文**，让 AI 直接基于它工作——而非每次从空白提示词开始。

## 为什么用它 / 适合什么场景

- 每次给 AI 写 prompt 都要重复一遍「我是谁 / 我在做什么 / 哪些事优先」。
- 想让 AI 持续记得「昨天会议决定的 / 这周 deadline / 跟某某聊到一半的事」。
- 想保护隐私：上下文在自己机器上整理，**不上传云端**。
- 想把个人工作上下文做成「可编辑、可审计」的资产，而非依赖平台内置记忆。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多源聚合 | IM / 文档 / 日历 / 会议信息汇总 |
| 个人上下文 | 整理为「AI 可直接消费」的结构化上下文 |
| 隐私优先 | 数据不上传云端，本地整理 |
| AI 接入 | 输出格式让主流 LLM 直接消费 |

## 媒体

![](https://pbs.twimg.com/media/HPPl9VDa0AEBAzE.jpg)

## 相关概念

- [second-brain-cloudflare](./tool-second-brain-cloudflare.md) — Cloudflare Workers 上的开源共享记忆层，MCP 协议
- [EchoesVault](./tool-echoes-vault-opencode.md) — OpenCode 持久记忆插件
- [MemTensor / memmy-agent](./tool-memmy-agent.md) — 跨 AI 编程代理共享长期记忆中间层