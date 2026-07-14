---
type: "Tool"
title: "telegram-search（groupultra/telegram-search）"
description: "基于 Telegram Search 的 CLI 应用,在终端里搜自己的 Telegram 聊天记录、频道、文件,免 Telegram Desktop。"
resource: "https://github.com/groupultra/telegram-search"
tags: "[telegram, cli, search, terminal, rust]"
timestamp: "2026-07-14T10:01:12Z"
---

# telegram-search

[telegram-search](https://github.com/groupultra/telegram-search) 是一个命令行 Telegram 搜索工具,把桌面客户端的「搜索历史消息 / 文件」能力搬到终端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 聊天记录全文搜索 | 跨私聊 / 群 / 频道 |
| 文件检索 | 按文件名 / 类型查找历史文件 |
| 终端优先 | 适合服务器 / SSH / 多任务工作流 |
| CLI 调用 | 可被 AI agent / 脚本组合 |

## 适合什么场景

- 重度使用 Telegram 但**不想一直开 Desktop 客户端**。
- 在服务器 / 容器 / 终端工作流里需要快速检索历史消息。
- 想把「搜聊天记录」变成可脚本化动作(配合 fzf / ripgrep 思路)。

## 与同类资源的差别

| 资源 | 定位 | telegram-search |
|------|------|------------------|
| Telegram Desktop | GUI 客户端、官方 | CLI 替代品,适合终端党 |
| Telegram CLI(社区) | 多为消息发送 | 搜索为主 |
| Textual / TUI 通用搜索工具 | 搜本地文件 | 跨 Telegram 远程历史 |

## 参考链接

- [项目仓库](https://github.com/groupultra/telegram-search)
- [原始推文](https://x.com/luoling8192/status/2076606567760421249)

## 相关概念

- [agent-lock](./tool-agent-lock.md) — eBPF 限制 AI agent 的目录访问;与本工具结合可让 agent 安全地在终端检索私人聊天记录
