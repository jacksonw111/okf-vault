---
type: Tool
title: "comet (zeronsh/comet)"
description: "把 Claude Code / Codex / Cursor 等编码 agent 收拢到本机控制：会话存在自己电脑上、免账号；仅在需要多设备同步时才登录"
resource: "https://github.com/zeronsh/comet"
tags: [coding-agent, cli, local-control, session, privacy]
timestamp: "2026-08-18T12:00:00Z"
---

# comet (zeronsh/comet)

## 它是什么
`zeronsh/comet` 是一个**本机控制台**，把 Claude Code、Codex、Cursor 这类编码智能体收拢到一处：会话历史、状态、配置都存在用户自己的电脑上，**默认无需注册账号**；只有希望多设备同步时才登录账号同步。

## 为什么用它 / 适合什么场景
- 不愿意把编码会话交给云端，但又想在一个统一界面里管理多个 agent。
- 多设备（笔记本 / 台式机）需要同步历史会话，且仍希望「默认本地、显式同步」。
- 想给团队一个「agent 工作台」雏形：每个成员本地一份，跨设备协作走同步层。

## 关键能力
| 能力 | 说明 |
|------|------|
| 本机会话 | 会话数据存在用户自己的机器上，不默认上云 |
| 免账号启动 | 装上即可用，登录是可选的同步动作 |
| 多 agent 收拢 | 同一界面管理 Claude Code / Codex / Cursor 等 |
| 按需云同步 | 需要多设备时才登录同步，最小化上传 |

## 媒体
- ![](https://pbs.twimg.com/media/HP5GogzacAAnDz-.jpg)

## 相关概念
- [项目链接](https://github.com/zeronsh/comet) — 仓库地址
