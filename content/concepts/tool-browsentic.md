---
type: "Tool"
title: "browsentic（给本机 Chrome 套一层 agent 皮）"
description: "让本机已登录的 Chrome 直接接受 Claude Code、Codex 或 Antigravity 的操控，不必另开一个无头浏览器，也不用申请 API key——给开着的 Chrome 加层 agent 皮，省掉配 Playwright 和申请 key 那点活。"
resource: "https://github.com/imshaikot/browsentic"
tags: "[chrome, agent, playwright, browser-automation, claude-code, codex]"
timestamp: "2026-09-21T22:00:00Z"
---

# browsentic

## 它是什么

[imshaikot/browsentic](https://github.com/imshaikot/browsentic) 给**已经开着的 Chrome**套一层 **agent 控制皮**——**不另开无头浏览器**，**不申请 API key**。

## 解决的问题

- Claude Code / Codex / Antigravity 想接管浏览器，过去要么起一个**无头浏览器**（再登录、再切 cookie），要么**申请各家云端 API key**（额度、配额、网络又是一堆事）。
- 用户本机的 Chrome 已经登录了各种网站（Google 账号、Notion、Slack、企业内网），这套登录态直接用最省事。

## 它的做法

- 给**已运行的 Chrome**接一层 agent 协议。
- 复用既有登录态 / 扩展 / 书签 / 历史。

## 为什么用它 / 适合什么场景

- 不想为了**一次性任务**起无头浏览器。
- 想直接用本机的**真实登录态**完成需要鉴权的网页操作。
- 不想折腾各家云端 API key 的**额度申请与配额管理**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 接管本机 Chrome | 不开无头浏览器，复用登录态 |
| 跨 agent 兼容 | Claude Code / Codex / Antigravity |
| 无需 API key | 走本地控制通道 |
| 零配 Playwright | 不需要单独搭浏览器自动化栈 |

## 项目链接

- 仓库：<https://github.com/imshaikot/browsentic>

## 媒体

![](https://pbs.twimg.com/media/HSs38V7bYAAldQH.jpg)

## 相关概念

- [Obscura（Rust 无头浏览器）](./tool-obscura-headless-browser.md) — 同样是面向 agent 的浏览器，但走反检测 + 无头路线
- [Claude Code](./tool-claude-code.md) — 数据源之一，被它操控的目标
