---
type: "Tool"
title: "Wake（Agent 会话统一管理）"
description: "Rust + GPUI 写的原生桌面应用，把 Claude Code / Codex / Cursor / Pi 等 20 多个 agent 的会话收进同一窗口，支持全文检索、一键续聊、SSH 远程镜像与 GitHub 风格的活跃热力图统计，全程本地运行。"
resource: "https://github.com/iAmCorey/Wake"
tags: "[agent, cli, session, manager, rust, gpui, desktop, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# Wake（Agent 会话统一管理）

## 它是什么

[Wake](https://github.com/iAmCorey/Wake) 是用 Rust + GPUI 写的原生桌面应用，把多个 CLI agent 的会话收进同一个窗口——本地端是 Claude Code / Codex / Cursor / Pi 等「会话散在不同目录」的统一检索 / 续聊 / 统计面板，同时支持把远程 SSH 主机上的会话镜像过来一起查看。

## 解决什么问题

混用多个 CLI agent 时，会话默认散落在十几个目录下，「找上周某次会话」基本靠猜；Wake 把它们汇总到同一处并提供完整检索与续聊能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨 agent 收口 | 20 多个 agent 的会话统一进同一窗口 |
| 全文检索 | 会话内文本搜索速度很快 |
| 一键续聊 | 在原会话上方继续对话 |
| SSH 远程镜像 | 把远程主机上的会话记录镜像到本地一起浏览 |
| 活跃统计 | GitHub 风格的活跃热力图 + 连续天数，按小时 / 星期 / 月份拆解 |
| 三类榜单 | Agents / Projects / Models 三个榜单在会话数 / token / prompt 之间切换 |
| 本地运行 | 全程本地，不联网不上传 |
| 开源 | MIT 协议 |

## 适用场景

- 同时使用多个 CLI 编码 agent（Claude Code + Codex + Cursor + Pi + ...），需要统一的会话入口
- 想跨本地与远程 SSH 主机查看 / 检索历史会话
- 想看清「哪个模型用得最多 / 哪些项目最烧 token / 哪天最活跃」

## 原始链接
- 项目主页：<https://github.com/iAmCorey/Wake>

## 相关概念
- [DeepSeek Harness 生态（dsh-\*）](./tool-deepseek-harness-rs.md) — 多 agent 终端常见底座