---
type: "Tool"
title: "magic-compact（OpenCode 的无损上下文压缩插件）"
description: "为 OpenCode 提供无损上下文压缩，避免智能体在会话压缩后丢失工作记忆；保留用户消息原样，把每个旧助手轮次单独压缩成摘要，大段工具输入输出裁剪但缓存到本地，可通过 read_omitted_content 调出来。"
tags: "[opencode, agent, context, compression, plugin]"
timestamp: "2026-07-06T02:31:00.000Z"
resource: "https://github.com/aerovato/magic-compact"
---

# magic-compact（OpenCode 的无损上下文压缩插件）

## 它是什么

[`magic-compact`](https://github.com/aerovato/magic-compact) 是 **OpenCode** 的一个上下文压缩插件。它**不走** OpenCode 内置那种「把整段对话打成一条摘要」的粗暴路子——而是做**无损压缩**：

- **保留用户消息原样**：用户的提问永远不被压缩
- **旧助手轮次单独压缩**：每个历史 assistant turn 单独生成摘要
- **工具输入输出缓存**：大段工具 I/O 裁剪掉不进入上下文，但**缓存在本地**
- **可重新调取**：智能体需要时通过 `read_omitted_content` 工具重新拉回被裁掉的部分

## 它解决什么

长会话中 AI 编码代理经常因为上下文膨胀而：

- 丢掉早期决策与设计意图（关键 bug 来源）
- 重复读文件 / 重复工具调用（浪费 token）
- 关键工具输出被截断导致推理错误

magic-compact 通过「摘要 + 缓存」组合，既保持上下文窗口不爆，又允许智能体**回头查证**任何历史细节。

## 关键能力

| 能力 | 说明 |
|------|------|
| 用户消息保留 | 用户输入永远完整 |
| 助手轮次单独摘要 | 每轮一个摘要，便于检索 |
| 工具 I/O 裁剪 + 本地缓存 | 上下文窗口不被大块输出淹没 |
| read_omitted_content | 智能体按需调回被裁内容 |

![截图 1](https://pbs.twimg.com/media/HMdfwwnbwAAvHY-.jpg) ![截图 2](https://pbs.twimg.com/media/HMdf3CPbMAA8mzl.jpg)

## 适用场景

- OpenCode 长会话（多文件、多任务）后期频繁「忘了前面说过什么」
- 想在上下文窗口与信息保真度之间找平衡
- 不希望压缩后 agent 反复重读文件浪费 token

## 参考链接

- [项目链接](https://github.com/aerovato/magic-compact)

## 相关概念

- [cognee](tool-cognee.md) — 开源可自托管的 AI 智能体持久长期记忆平台，知识图谱引擎
- [nemos](tool-nemos-memory.md) — 五层记忆存储 + 主题路由的 AI 陪伴聊天系统
- [Echoes Vault](tool-echoes-vault-opencode.md) — OpenCode 持久记忆插件，会话结束自动记决策