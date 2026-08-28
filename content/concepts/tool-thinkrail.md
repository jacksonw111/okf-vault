---
type: Tool
title: "ThinkRail（JetBrains 出品的 Pi 编码 Agent 桌面客户端）"
description: "JetBrains 给自己的 Pi 编码 Agent 出的客户端：引擎直接嵌入应用进程跑（模型选择 / skills / 上下文压缩交给 Pi），工作区与编辑器由 ThinkRail 自己管。"
resource: "https://github.com/JetBrains/thinkrail"
tags: [jetbrains, pi-agent, coding-agent, desktop, ide, embedded-engine]
timestamp: "2026-08-27T02:14:00Z"
---

# ThinkRail

## 它是什么
[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail) 是 **JetBrains 给自己 Pi 编码 Agent 出的桌面客户端**。架构分工清晰：

- **Pi 引擎（agent 核心）**：模型选择、Skills 调度、上下文压缩——这部分由 Pi 自己负责；
- **ThinkRail（客户端）**：工作区管理、编辑器集成、文件浏览——这部分由 JetBrains 自己实现。

**Pi 引擎直接嵌入到 ThinkRail 应用进程里运行**，不像一般客户端那样把 agent 跑成外部子进程通信。

## 为什么用它 / 适合什么场景
- 想用 Pi 编码 Agent 又不想挂着 IDE / 终端窗口；
- 想让 JetBrains 系（IntelliJ / WebStorm 等）的项目结构、文件跳转、运行配置直接被 agent 利用；
- 关注 Pi 这条 JetBrains 自家 agent 路线的演进，想给它一个正式桌面入口。

## 关键能力
| 能力 | 说明 |
|------|------|
| 引擎嵌入 | Pi 引擎跑在应用进程内 |
| 模型选择 | 由 Pi 自己管理 |
| Skills 调度 | 由 Pi 引擎决定 |
| 上下文压缩 | 由 Pi 自己压缩 |
| 工作区 | 由 ThinkRail 管 |
| 编辑器 | 由 ThinkRail 管 |
| 出品方 | JetBrains（IDE 大厂） |

## 相关概念
- [pi-agent-desktop](tool-pi-agent-desktop.md) — 第三方给 Pi 编程 Agent 出的独立窗口客户端，与 ThinkRail 思路一致；一个官方一个社区
- [Claude Code](tool-claude-code.md) — 终端原生 AI 编码 agent，与 ThinkRail / pi-agent-desktop 是不同入口但解决同类问题

## 参考链接
- 项目链接：<https://github.com/JetBrains/thinkrail>
