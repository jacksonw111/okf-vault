---
type: "Tool"
title: "Nemos（带分层记忆的 AI 陪伴聊天）"
description: "会真正记住用户的 AI 陪伴聊天系统，AI 角色跨时间记得用户偏好、事件和状态。内置分层记忆引擎，记忆分 5 层存储，检索按主题路由避免无关记忆污染上下文，自带矛盾失效机制（被纠正过的事不会再翻出来）。"
resource: "https://github.com/mmlong818/nemos"
tags: [ai-companion, memory, chat, agent, long-term]
timestamp: "2026-06-24T15:30:00Z"
---

# Nemos（带分层记忆的 AI 陪伴聊天）

## 它是什么

[`mmlong818/nemos`](https://github.com/mmlong818/nemos) 是一个**会真正记住用户的 AI 陪伴聊天系统**。

普通聊天 App 的痛点：换次会话就失忆，AI 角色「上次的你和这次的你是两个人」。Nemos 底层有一套**独立的记忆引擎**，让 AI 角色跨时间记住：

- 你的偏好
- 你说过的事
- 你的近况 / 状态
- 改口之后会自动更新

## 为什么用它 / 适合什么场景

- 想要**长期陪伴型** AI 角色 / 数字伴侣 / 心理疗愈类应用；
- 对「AI 失忆」厌倦的人；
- 关注 RAG / 长期记忆架构的人：分层 + 主题路由 + 矛盾失效是值得参考的工程方案。

## 关键能力

| 能力 | 说明 |
|---|---|
| 分层记忆 | 5 层存储，不是「一股脑丢进向量库」 |
| 主题路由 | 检索按主题路由，避免无关记忆污染上下文 |
| 矛盾失效 | 用户纠正过的事会自动失效，不会再翻出来 |
| 跨时间 | 偏好 / 事件 / 状态 跨会话持续 |
| 改口更新 | 改了口它会跟着更新 |

## 媒体 / 参考链接

- [项目链接](https://github.com/mmlong818/nemos)

## 相关概念

- [EverOS](tool-everos.md) — 统一的本地长期记忆层，让不同 agent 共享与进化记忆
- [Brigade](tool-brigade.md) — 本地多代理协作 + Tideline 共享长期记忆
- [Recall](tool-recall-claude-code.md) — Claude Code 离线持久化项目记忆插件
- [Heartmorrow](tool-heartmorrow.md) — 本地 LLM 约会 + 世界模拟器，同样强依赖长期记忆
