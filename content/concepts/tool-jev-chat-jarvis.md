---
type: "Tool"
title: "jev-chat-jarvis（手机聊天意图助手）"
description: "用系统无障碍服务只读手机屏幕上的对话，交给 Jev 判断对方意图并生成 3 条候选回复，一键填入输入框——发不发由用户自己点，避免 AI 越权代发。"
resource: "https://github.com/jev-chat/jev-chat-jarvis"
tags: "[mobile, accessibility, intent-recognition, jev, chat-assistant, open-source]"
timestamp: "2026-09-23T22:35:00Z"
---

# jev-chat-jarvis（手机聊天意图助手）

## 它是什么

[jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis) 是一个**手机聊天意图识别与回复候选工具**：

> 手机上聊天时用系统无障碍服务只读屏幕上的对话，交给模型判断对方意图并给出 3 条候选回复，一键填进输入框，发不发由用户自己点。

## 为什么用它 / 适合什么场景

- 在手机上收到需要「**想一下怎么回**」的消息（工作 / 谈判 / 情绪场景），需要 AI 帮忙起草几种语气选择。
- 想避免 AI 越权代发——所有回复必须由人手动点发送。
- 借助系统无障碍服务做只读抓屏，不需要 root / 截屏权限。

## 关键能力

| 能力 | 说明 |
|------|------|
| 数据获取 | 系统无障碍服务只读屏幕对话 |
| 意图识别 | 模型判断对方意图 |
| 候选回复 | 生成 3 条备选回复 |
| 填入 | 一键写入输入框 |
| 发送 | 用户手动确认（AI 不直接发） |

## 与同类工具的差异

| 维度 | jev-chat-jarvis | 普通聊天 AI |
|------|-----------------|-------------|
| 触发 | 屏幕上读到对话 | 手动输入 prompt |
| 决策 | 候选回复 + 人工发送 | 模型直接生成 |
| 权限 | 无障碍只读 | 通常需要 API key |

## 项目链接
- 项目主页：<https://github.com/jev-chat/jev-chat-jarvis>

## 媒体
![jev-chat-jarvis 截图 1](https://pbs.twimg.com/media/HSyhphTbkAAKIKe.jpg)
![jev-chat-jarvis 截图 2](https://pbs.twimg.com/media/HSyhrXla8AAeG3R.jpg)
