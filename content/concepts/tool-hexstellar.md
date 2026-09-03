---
type: Tool
title: "HexStellar（AI 算硬问题搜索空间的云端平台）"
description: "AI 只会描述意图、算不了硬问题的搜索空间。HexStellar 把难题接过来算：agent 把模型翻译成 JSON 提交云端，返回带确证标签和收据的答案。"
resource: "https://github.com/brayonpi/hexstellar"
tags: [ai, optimization, cloud, agent, solver]
timestamp: "2026-09-03T00:00:00Z"
---

# HexStellar（AI 算硬问题搜索空间的云端平台）

## 它是什么

[HexStellar](https://github.com/brayonpi/hexstellar) 是一个让 AI Agent 能算**硬问题搜索空间**的云端平台：

- 现有的 LLM agent 善于「描述意图、写代码、调用工具」，但对真正的搜索 / 优化问题（如组合优化、约束求解、数值难算题）只能硬算，效果差；
- HexStellar 提供云端算力，把 agent 给出的问题描述（翻译为 JSON）提交上去，**返回带确证标签（verification labels）和收据（receipts）的答案**；
- agent 调用接口像调一个求解器，但拿到的是带可验证证据的结果，便于审计 / 复现。

## 为什么用它 / 适合什么场景

- 想给 AI agent 接上传统 solver / optimizer 的算力（而不是让模型死磕搜索空间）；
- 业务里有组合优化 / 排产 / 路径 / 约束满足类硬问题，希望 AI 当前端；
- 想要带 verification 的可审计结果，而不只是「AI 给出的数字」；
- 偏好 JSON 接口与 agent 协议对接，而非自建 UI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 云端求解 | 把难题提交云端算力算 |
| Agent 友好 | 输入输出皆 JSON，agent 易接入 |
| 确证标签 | 返回带 verification labels 的答案 |
| 收据 | 每条结果附收据，便于审计 / 复现 |

## 参考链接

- 项目链接：<https://github.com/brayonpi/hexstellar>
- 原始推文：<https://x.com/QingQ77/status/2095378503810072741>

## 相关概念

- [Quantspace](./tool-quantspace.md) — 量化研究空间管理
- [Loop Engineering](./tool-loop-engineering.md) — 把 AI agent 编成自动循环的方法论 + CLI 工具
