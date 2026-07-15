---
type: "Tool"
title: "lazyrsync（westpoint-io/lazyrsync）"
description: "rsync 的终端前端,基于 ratatui + Rust,配置只填一次,运行前 dry-run 预览,危险开关(如 --delete)双重确认。"
resource: "https://github.com/westpoint-io/lazyrsync"
tags: "[rsync, tui, ratatui, rust, backup, sync]"
timestamp: "2026-07-15T03:17:00Z"
---

# lazyrsync

[lazyrsync](https://github.com/westpoint-io/lazyrsync) 是给 rsync 套的**终端界面**,底层 ratatui + Rust,想法是「在命令行也能有 GUI 那种踏实感」:配置只存一次,真跑之前先把要改的东西看明白,像 `--delete` 这种会删东西的开关确认两遍才放过去。

## 它解决了什么

rsync 命令极强但极容易写错,尤其涉及 `--delete` / `--exclude` / 路径尾斜杠等隐藏语义,一个 typo 就可能删库。lazyrsync 把高频配置变成表单 + dry-run 预览,把危险操作从「靠记忆力确认」变成「界面强制二次确认」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 配置持久化 | 只填一次,profile 保存 |
| Dry-run 预览 | 实际跑之前先看会改什么 |
| 危险开关二次确认 | `--delete` 等必须额外确认 |
| Ratatui TUI | 终端里原生体验 |

## 媒体

- 视频: <https://video.twimg.com/tweet_video/HNJpjLTbIAETn1P.mp4>

## 参考链接

- [项目仓库](https://github.com/westpoint-io/lazyrsync)

## 相关概念

- [Orca 票务调度 playbook](./playbook-orca-ticket-orchestration.md) — 同为「在 TUI 里把容易出错的工作流加界面护栏」的实践样本
