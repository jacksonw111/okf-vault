---
type: "Tool"
title: "ThinkWatch-Lite（本地 LLM 网关：脱敏出站请求 + 拦截危险工具调用）"
description: "ThinkWatchProject 出品的本地网关：把出站请求里的 API 密钥 / 私钥 / JWT / 身份证 / 银行卡号先换成占位符，再在客户端运行前拦截「下载即执行 / 外发凭据 / 写开机启动项」的危险工具调用。"
resource: "https://github.com/ThinkWatchProject/ThinkWatch-Lite"
tags: "[llm-gateway, privacy, security, local-first, open-source]"
timestamp: "2026-10-03T00:00:00Z"
---

# ThinkWatch-Lite

## 它是什么

[ThinkWatch-Lite](https://github.com/ThinkWatchProject/ThinkWatch-Lite) 是 **ThinkWatchProject** 出品的**本地 LLM 网关**——在用户的机器上做两层保护：

1. **脱敏出站请求**：把 API 密钥、私钥、JWT、身份证号、银行卡号先替换成占位符再发给 LLM 提供商
2. **拦截危险工具调用**：客户端运行前识别并掐断「下载即执行 / 外发凭据 / 写开机启动项」的工具调用

## 为什么用它 / 适合什么场景

- **中转站可见一切**：LLM 中转站能看见你发出去的每个字、也能改回来——本地网关是最后一道防线。
- **金融 / 医疗 / 政企合规**：敏感信息不能直接发给云端。
- **Agent 时代的新攻击面**：Coding Agent 跑得快，危险工具调用也跑得快——人工审核跟不上，必须前置拦截。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 本地网关 |
| 脱敏 | API Key / 私钥 / JWT / 身份证 / 银行卡 → 占位符 |
| 拦截 | 下载即执行 / 外发凭据 / 写开机启动项 |
| 部署 | 用户本机 |

## 参考链接

- 项目链接：<https://github.com/ThinkWatchProject/ThinkWatch-Lite>

## 相关概念

- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — ThinkWatch 是 Harness 中「安全护栏」方向
- [Abide](./tool-abide-rubric.md) — 同类「用决策模型做软规则检查」思路
