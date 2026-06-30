---
type: Tool
title: "SimpleX Chat（无用户标识符的消息平台）"
description: "首个不使用任何用户标识符（无用户名、无手机号、无账号 ID）的消息平台，通过双层加密协议 + 独立中继服务器架构保护通信内容和元数据，让无人能知道你和谁在聊、何时在聊。"
resource: "https://github.com/simplex-chat/simplex-chat"
tags: "[messaging, privacy, encryption, open-source, chat]"
timestamp: "2026-06-30T15:30:00Z"
---

# SimpleX Chat（无用户标识符的消息平台）

## 它是什么

SimpleX Chat 是首个**不依赖任何用户标识符**的消息平台：没有用户名、没有手机号、没有账号 ID。通过双层加密协议和独立的中继服务器架构，从协议层保护通信内容与元数据——没有人（包括 SimpleX 自己）能知道你和谁在聊、何时在聊。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零用户标识符 | 无用户名 / 手机号 / 账号 ID |
| 双层加密 | 内容与元数据都加密 |
| 中继服务器架构 | 通过独立中继节点转发，不暴露通信图 |
| 平台 | iOS / Android / macOS / Windows / Linux / Web / CLI |
| 协议开放 | 全栈开源 |
| 双工支持 | 1:1 消息、群组、文件、语音 / 视频通话 |

## 适用场景

- 隐私敏感场景（新闻源、举报渠道、政治异议、跨境隐私通信）。
- 想从协议层杜绝「用户被关联 / 通信被图分析」的可能。
- 不想依赖中心化账号体系（手机号 / 邮箱）的即时通信需求。

## 与常见 IM 的区别

| 平台 | 用户标识符 | 服务器能否看到元数据 |
|------|-----------|---------------------|
| Signal / Telegram | 手机号 / 用户名 | 部分可见 |
| Matrix | 用户名（@xxx） | 服务器可见通信图 |
| SimpleX Chat | **无任何标识符** | 服务器**无法看到通信图** |

## 相关概念

- [Cloud Mail](./tool-cloud-mail.md) — 自托管邮件，强调单域名无限收发
- [SimpleRelay](./tool-simplerelay.md) — 自托管 SMTP 中继
- [EasySNI](./tool-easysni.md) — SNI / XRay / 域名前置单文件面板

## 参考链接

- 项目链接：<https://github.com/simplex-chat/simplex-chat>