---
type: "Tool"
title: "undo（nvrmnd-png/undo）"
description: "Rust 写的 Shell 工具：拦截 mv / cp / rm 等常用文件命令，把每次操作写入 SQLite 日志，支持一键撤销和重做——给命令行加一道「后悔药」。"
tags: "[rust, shell, cli, undo, redo, sqlite, safety]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/nvrmnd-png/undo"
---

# undo（nvrmnd-png/undo）

## 它是什么

[`undo`](https://github.com/nvrmnd-png/undo) 是 nvrmnd-png 用 Rust 写的**Shell「后悔药」**：

- 拦截常用文件操作命令：`mv` / `cp` / `rm` 等；
- 每次执行都把操作详情写入 SQLite 日志；
- 出问题时，一条命令即可**撤销（undo）/ 重做（redo）**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 命令拦截 | 透明接管 mv / cp / rm，无需改用户习惯 |
| SQLite 日志 | 操作可追溯、可查询 |
| 一键撤销 | undo 回到上一次正确状态 |
| 一键重做 | redo 重新执行被撤销的操作 |
| Rust 实现 | 性能好、单二进制、依赖少 |

## 适合什么场景

- 经常在 Shell 里搬文件、删目录、担心手抖的人；
- 服务器 / 部署环境里做「文件操作保险」；
- 教学 / 演示场景：让学员大胆试错，操作可回滚。

## 演示视频

- [原始视频](https://video.twimg.com/tweet_video/HNfZkUqbMAAuJpe.mp4)

## 参考链接

- [原始链接](https://github.com/nvrmnd-png/undo)

## 相关概念

- [BetterCopy](tool-bettercopy.md) — 同为「命令行文件操作增强」：BetterCopy 让复制变快，undo 让误操作可撤销，两者常一起部署