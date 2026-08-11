---
type: "Tool"
title: "pi-peer（shift-labs-ai/pi-peer）"
description: "让同一台机器上跑多个 pi 会话时,会话之间能互相发现并互发消息,不再需要手动从一个终端复制粘贴到另一个;提供 list_peers / message_peer 两个工具,消息为纯文本、最多 32 KB、不带对话历史。"
resource: "https://github.com/shift-labs-ai/pi-peer"
tags: "[agent, pi, peer-to-peer, inter-session, messaging, local]"
timestamp: "2026-08-11T16:00:00Z"
---

# pi-peer

[pi-peer](https://github.com/shift-labs-ai/pi-peer) 让同一台机器上跑多个 pi 会话时,**会话之间能互相发现并互发消息**,不用再手动从一个终端复制粘贴到另一个。

项目链接：<https://github.com/shift-labs-ai/pi-peer>

## 它是什么

装在 pi 里的**会话互联层**:每次启动会话自动向其他会话注册,其他会话能看到它闲不闲、在哪个目录干活;每个会话拿到两个工具——`list_peers`(列其他会话状态)和 `message_peer`(按名字给对方发纯文本)。

## 为什么用它 / 适合什么场景

- **多 agent 协作**:不需要人当传话筒,模型自己决定什么时候联系同伴。
- **不污染上下文**:消息只是文字,最多 32 KB,不带对话历史、不带文件,接收方"取走"才算送达。
- **送达状态可观察**:未取走的邮件显示排队,发信方分得清"在投递"与"已送达"。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动注册 | pi 启动即向其他会话广播存在 |
| 状态可见 | 别人能看到它闲不闲、在哪个目录干活 |
| 两个工具 | `list_peers` / `message_peer` |
| 纯文本消息 | 最多 32 KB,不带历史、不带文件 |
| 投递语义 | 接收方取走才算送达,未取显示排队 |
| 模型自主决策 | 由模型判断何时调用对端 |

## 参考链接

- [项目仓库](https://github.com/shift-labs-ai/pi-peer)

## 相关概念

- [Pisper](./tool-pisper.md) — Pi 多会话桌面 / 终端客户端,本工具是其"会话间通信"的细分路线
- [Agent Swarms](./tool-agent-swarms.md) — 多 agent 协作的高层模式