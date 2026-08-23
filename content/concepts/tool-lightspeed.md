---
type: Tool
title: "lightspeed（去中心化阅后即焚社交应用）"
description: "khydrogenous/lightspeed：文字 / 媒体消息在设备端加密后点对点传输，看一次即全网删除，无需账号、不可被审查的服务器"
resource: "https://github.com/khydrogenous/lightspeed"
tags: [p2p, ephemeral, e2ee, messaging, privacy]
timestamp: "2026-08-23T07:26:00Z"
---

# lightspeed（去中心化阅后即焚社交应用）

## 它是什么

[khydrogenous/lightspeed](https://github.com/khydrogenous/lightspeed) 是一个**去中心化的阅后即焚社交应用**：文字和媒体消息**在设备端加密后点对点传输**，**看一次即全网删除**，**全程无需账号**，也不存在可被审查的服务器内容。

它针对的痛点：发出去的消息想让它真的"只被看一次、之后彻底消失"，而且不想经过任何能读内容或封号的服务器。

## 为什么用它 / 适合什么场景

- 敏感对话场景：消息不应在服务器留下任何痕迹。
- 不想被账号 / 服务器审查 / 封号影响。
- 想要"阅后即焚 + 真正 P2P"双重保证。

## 关键能力

| 能力 | 说明 |
|------|------|
| 设备端加密 | 消息在发出前就已加密，服务器无明文 |
| P2P 传输 | 不经中继服务器直接送达接收端 |
| 阅后即焚 | 看一次即从全网删除 |
| 无账号 | 无身份、无注册、无痕迹 |
| 抗审查 | 服务器无可读内容，自然抗审查 |

## 媒体

- ![](https://pbs.twimg.com/media/HQYAeENaIAA3SM8.jpg)

## 相关概念

- [SimpleX Chat](./tool-simplex-chat.md) — 同样主张「无用户标识符 + 端到端加密」的消息平台
- [Fallegji](./tool-fallegji.md) — 同样基于 P2P / E2EE 的去中心化群聊
- [ssh-clipboard](./tool-ssh-clipboard.md) — 同类点对点直连思路

## 参考链接

- [项目链接](https://github.com/khydrogenous/lightspeed)
