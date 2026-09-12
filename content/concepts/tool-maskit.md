---
type: "Tool"
title: "Data Maskit（AI 编程工具本地脱敏网关）"
description: "为大模型编程工具（Cursor / Claude Code 等）提供本地隐私脱敏网关：请求出网前自动打码敏感数据（密钥 / 连接串 / 手机号），回复时流式还原占位符；敏感数据不出本机。"
resource: "https://github.com/xiaYuTian11/maskit"
tags: "[privacy, gateway, local, ai-coding, redactor, proxy]"
timestamp: "2026-09-12T22:30:00Z"
---

# Data Maskit

## 它是什么

[xiaYuTian11/maskit](https://github.com/xiaYuTian11/maskit) 是 **AI 编程工具的本地脱敏网关**：夹在 Cursor / Claude Code 这类工具和大模型之间，敏感信息（API 密钥、连接串、手机号）先在本地换成占位符再发出去，回复回来逐字还原。**打字机体验不变**，但敏感数据不出本机。

## 核心特性

| 特性 | 说明 |
|------|------|
| 本地代理 | 跑在自己机器上 |
| 自动打码 | 密钥 / 连接串 / 手机号 |
| 流式还原 | 回复时逐字还原占位符 |
| 兼容工具 | Cursor / Claude Code 等 |
| 打字机体验 | 不影响流式输出 |

## 为什么用它 / 适合什么场景
- 用 AI 编程工具时怕泄露密钥 / 内部数据。
- 团队里大家用同一套 AI 工具但权限不同。
- 第三方 AI 服务不可完全信任。

## 关键能力

| 能力 | 说明 |
|------|------|
| 敏感数据识别 | 自动发现密钥 / 连接串 / 手机号等 |
| 占位符替换 | 发送前替换 |
| 流式还原 | 回复时还原不破坏体验 |
| 工具兼容 | Cursor / Claude Code 等主流 |
| 本地运行 | 隐私数据不出本机 |

## 参考链接

- 项目仓库：<https://github.com/xiaYuTian11/maskit>

## 媒体

- ![](https://pbs.twimg.com/media/HR-syDMbkAA2gWZ.jpg)

## 相关概念
