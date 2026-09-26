---
type: "Tool"
title: "ChatPassport（跨平台 AI 对话迁移的浏览器扩展）"
description: "sxwangsxwang1 开源的 Chrome / Chromium 侧边栏扩展：在 **ChatGPT / Claude / Gemini / DeepSeek** 之间迁移对话文本，**不需要 API key / 账号 / 开发者服务器**。用户先选最近 20/50/100 条或全部可见消息 → 打开目标平台 → 检查完整草稿 → 手动发送。"
resource: "https://github.com/sxwangsxwang1/chatpassport"
tags: "[chatpassport, browser-extension, ai-chat, cross-platform, migration, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# ChatPassport（跨平台 AI 对话迁移的浏览器扩展）

## 它是什么

[ChatPassport](https://github.com/sxwangsxwang1/chatpassport) 是 sxwangsxwang1 开源的 **Chrome / Chromium 侧边栏扩展**——在四大 AI 对话平台之间迁移对话文本：

| 源 ↔ 目标 |
|------|
| ChatGPT |
| Claude |
| Gemini |
| DeepSeek |

## 关键设计

- **不需要 API key**
- **不需要账号**
- **不需要开发者服务器**
- **侧边栏 UI**——在原平台加载对话
- 用户选择**最近 20 / 50 / 100 条**或**全部**可见消息
- 打开目标平台，**等用户输入新问题**
- **手动发送**——绝不自动代发

## 为什么用它 / 适合什么场景

- 一个项目在 **ChatGPT** 上聊了一半，想去 **Claude** 接着试——手动复制粘贴太痛苦。
- 想**横向对比**同一个问题在不同平台的回答——需要把上下文搬过去。
- 担心**自动代发**带来的风险——ChatPassport 只搬运文本，**最终发送必须由用户点**。
- 想用一个**纯前端 / 纯本地**的工具——不依赖开发者服务器。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Chrome / Chromium 浏览器扩展 |
| 平台 | ChatGPT / Claude / Gemini / DeepSeek |
| 隐私 | 不需要 API key / 账号 / 开发者服务器 |
| 选择粒度 | 最近 20 / 50 / 100 条或全部 |
| 操作 | **用户手动发送**（绝不代发） |

## 媒体

- ![](https://pbs.twimg.com/media/HTGWVDDa0AAmlCb.jpg)
- ![](https://pbs.twimg.com/media/HTGWbp8aMAA2NCD.jpg)

## 相关概念

- [Componentry](./tool-componentry.md) — 同为 Chrome 生态的工具类扩展
- [Self-Hosted（自托管）](./term-self-hosted.md) — 不依赖开发者服务器 = 自托管理念