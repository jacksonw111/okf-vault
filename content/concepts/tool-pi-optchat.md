---
type: "Tool"
title: "Pi-OptChat（摘要二叉树持久化记忆）"
description: "jonaslsaa 出品：给 Pi 装的「不要靠上下文压缩硬撑」的记忆外挂——每条 profile 都是一条不结束的对话，记忆攒在一棵摘要二叉树里，每轮开局上下文是空的、只带一份封顶 128 KB 的记忆视图，agent 用 zoom / date 翻原话、用 search 找原文。"
resource: "https://github.com/jonaslsaa/pi-optchat"
tags: "[pi, long-context, memory, summary-tree, agent]"
timestamp: "2026-10-08T23:50:00Z"
---

# Pi-OptChat

## 它是什么

[Pi-OptChat](https://github.com/jonaslsaa/pi-optchat) 是 jonaslsaa 开源的 **Pi 长会话外挂**：

- 每个 **profile** = 一条「不会结束的对话」
- 记忆持久化在**一棵摘要二叉树**里，不靠上下文压缩硬撑
- 每轮开局**上下文是空的**，只携带一份封顶 **128 KB** 的记忆视图
- Agent 通过 `zoom` / `date` 翻原话；通过 `search`（默认关）拿纯文本大小写不敏感地在原始消息里找，**翻的是原文不是摘要**

## 解决什么问题

长会话的两大老问题：

1. **上下文被压缩 → 信息丢失**：Pi 默认在上下文窗口接近爆时压缩历史，丢掉细节
2. **会话重启 → 记忆归零**：换个 profile 重新开始，前面的对话全没了

Pi-OptChart 的解法：**不压缩原文，只压缩「记忆视图」**。原文一字不丢地存在树里，Agent 想要细节随时翻回去。

## 关键能力

| 能力 | 说明 |
|------|------|
| Profile 隔离 | 每条 profile 独立记忆 |
| 摘要二叉树 | 记忆层级化、可 zoom 翻原话 |
| 128 KB 记忆视图 | 每轮开局携带的记忆封顶 |
| zoom / date 翻页 | Agent 按需回查历史 |
| search（默认关） | 在原始消息里大小写不敏感地找 |
| 原文保留 | 翻回去是原文，不是被截短的摘要 |
| 装完即用 | Pi 装上插件即生效 |

## 适合谁

- 跑长任务（数小时 / 数天）的 Pi 用户
- 跑多线任务、要按主题 / 项目拆 profile 的用户
- 不愿接受「上下文压缩 = 细节丢失」的 Pi 用户

## 参考链接

- 项目链接：<https://github.com/jonaslsaa/pi-optchat>

## 媒体

![](https://pbs.twimg.com/media/HUEwtZObkAA7ONh.jpg)

## 相关概念

- [Pi Agent](./term-pi-agent.md) — 上游：Pi 的会话模型
- [Harness Engineering](./term-harness-engineering.md) — 长任务持久化是 Harness Engineering 的核心议题之一