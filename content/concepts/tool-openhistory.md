---
type: Tool
title: "OpenHistory（ztratar/openhistory）"
description: "把 Mac 上你允许的活动攒成一份本地时间线，随时能搜回「昨天做完什么 / 哪件事还没收尾」，本地 AI 代理也能按授权查看脱敏记录"
resource: "https://github.com/ztratar/openhistory"
tags: "[mac, activity-timeline, local-ai, memory, privacy]"
timestamp: "2026-08-22T00:28:00Z"
---

# OpenHistory

## 它是什么
[`ztratar/openhistory`](https://github.com/ztratar/openhistory) 把 Mac 上你**显式允许**的活动（应用使用、文件改动、窗口焦点等）攒成一份**本地**时间线，让你随时能搜回「昨天做完什么、哪件事还没收尾」——同时按授权向本地 AI 代理暴露**脱敏后**的记录，让 AI 帮回忆、帮梳理今天的工作，但所有数据仍住在本机。

## 为什么用它 / 适合什么场景
- 工作节奏快，想不起来「上午第三个会之后我到底改了什么」——给本地代理一段脱敏历史即可问出来。
- 不想把活动数据传云，但又希望 AI 助手能基于「我最近做的事」给建议。
- 想做个人「时间审计」：每天 / 每周回看自己的真实活动流。

## 关键能力
| 能力 | 说明 |
|------|------|
| 本地存储 | 全部活动数据存在本机，不上传云端 |
| 可授权读取 | 用户显式授权哪些应用 / 哪些字段纳入时间线 |
| AI 代理可读 | 本地 LLM 代理可按授权读脱敏后的历史 |
| 可搜可回溯 | 按时间 / 应用 / 文件路径等维度快速回查 |
| 隐私优先 | 关键字段本地脱敏后才暴露给模型 |

## 媒体
- ![](https://pbs.twimg.com/media/HQNmNJEa0AAN3hb.jpg)

## 相关概念
- [Ackem](./tool-ackem.md) — 本地优先 Windows 桌面 AI 伙伴（Electron），同属「本地 AI 看本地数据」思路
- [HermitUI](./tool-hermitui.md) — 把隐私放在第一位的本地 AI 聊天界面，单 HTML 默认不存聊天记录
- [Nemos](./tool-nemos-memory.md) — 带分层记忆的 AI 陪伴聊天，5 层存储 + 主题路由 + 矛盾失效
