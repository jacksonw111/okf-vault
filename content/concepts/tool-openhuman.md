---
type: "Tool"
title: "openhuman（Rust 写的本地 Agent Harness + Markdown 记忆树 + Obsidian vault）"
description: "tinyhumansai/openhuman：Rust 开源 Agent Harness，把本机邮件 / 文档 / 聊天 / 仓库等数据压成带评分的 Markdown 记忆树存进 SQLite，并镜像为一个可翻可改的 Obsidian vault；TokenJuice 在工具输出送进模型前先压缩，官方称最高省 80% token。"
resource: "https://github.com/tinyhumansai/openhuman"
tags: "[agent-harness, rust, obsidian, memory, local-first, token-compression]"
timestamp: "2026-09-20T18:00:00Z"
---

# openhuman

## 它是什么

[tinyhumansai/openhuman](https://github.com/tinyhumansai/openhuman) 是一个 **Rust 写的开源 Agent Harness**，目标是让 agent 在一个同步周期内拿到用户的**完整本地上下文**——邮件、文档、聊天、仓库——把「等几周才认识你」的冷启动期压到几分钟。

## 它怎么工作

1. **抓取**：每隔约 20 分钟自动跑一次，把本机的邮件、文档、聊天、仓库等数据收下来。
2. **评分**：原始数据被加工成**带评分的 Markdown 记忆树**，每条记忆有相关性 / 新鲜度评分。
3. **存储**：评分后的记忆树落进 **SQLite**，便于 agent 高效查询。
4. **镜像**：同一份记忆树被镜像成一个 **Obsidian vault**，人类可直接打开翻、改、删。
5. **压缩**：**TokenJuice** 子模块把工具输出送进模型之前先压一遍，官方宣称最高省 80% token。

## 为什么用它 / 适合什么场景

- 想给自己的 agent 装上「**长期 / 跨会话 / 跨数据源**」的记忆层，而不是每次都从零开始。
- 看重「记忆可见、可改」——能直接在 Obsidian 里审阅 agent 学到了什么、删掉错的、补充缺的。
- 模型上下文窗口吃紧，想在**入模前先把无关 / 重复 / 旧的 token 砍掉**。
- 不想把数据交给云端，记忆树全在本地 SQLite。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动抓取 | 默认每 20 分钟一次，把本机多源数据合到记忆树 |
| 评分记忆树 | Markdown 节点带相关度 / 新鲜度评分 |
| SQLite 后端 | 适合 agent 高频查询 |
| Obsidian 镜像 | vault 形态，人可读可改 |
| TokenJuice 压缩 | 工具输出入模前压缩，最高省 80% token |
| 完全本地 | 数据全在 `~/.openhuman` 一类本地目录 |

## 项目链接

- 仓库：<https://github.com/tinyhumansai/openhuman>

## 媒体

![](https://pbs.twimg.com/media/HSnvtmDaYAAV1j0.png)

## 相关概念

- [Obsidian](./tool-obsidian.md) — openhuman 把记忆树镜像成 Obsidian vault
- [Obsidian 新手 Vault 模板](./tool-ivy-obsidian-template.md) — 同为 Obsidian 起手方式的另一类资源
- [EverOS](./tool-everos.md) — 同类思路：统一的本地长期记忆层，让不同 agent 共享
- [Harness Engineering（Harness 工程）](./term-harness-engineering.md) — openhuman 是 Agent Harness 的一种具体实现
