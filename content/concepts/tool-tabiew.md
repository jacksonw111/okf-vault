---
type: "Tool"
title: "tabiew（TUI 表格数据查看器）"
description: "Rust 写的轻量终端 TUI 工具，能打开 CSV / Parquet / JSON / Excel 等表格数据格式；支持 Vim 快捷键 / SQL 查询 / 模糊搜索 / 脚本功能，内置 400+ 主题。"
tags: "[cli, tui, data, csv, parquet, rust]"
timestamp: "2026-06-27T09:05:00.000Z"
resource: "https://github.com/shshemi/tabiew"
---

# tabiew（TUI 表格数据查看器）

## 它是什么

[`tabiew`](https://github.com/shshemi/tabiew) 是一款**轻量级终端 TUI 应用**，用于查看和查询 **CSV、Parquet、JSON、Excel** 等表格数据文件。Rust 写的，启动快、内存占用低。它支持 Vim 快捷键、SQL 查询、模糊搜索和脚本功能，并内置 400 多套主题。

[演示视频](https://video.twimg.com/tweet_video/HLvDawQa8AAV094.mp4)

## 关键能力

| 能力 | 说明 |
|------|------|
| 多格式 | CSV / Parquet / JSON / Excel |
| Vim 快捷键 | 熟悉的 vim 操作风格 |
| SQL 查询 | 直接在 TUI 里跑 SQL |
| 模糊搜索 | 列 / 行快速模糊过滤 |
| 脚本功能 | 可写脚本复用查询 |
| 400+ 主题 | 大量内置主题 |
| Rust 实现 | 启动快、内存占用低 |

## 适用场景

- 经常需要在终端里快速看一眼 CSV / Parquet 文件，不想启动 Excel / pandas notebook
- 数据科学家 / 分析师做探索性数据分析
- SSH 到远端机器时直接查表

## 参考链接

- [项目链接](https://github.com/shshemi/tabiew)
- [演示视频](https://video.twimg.com/tweet_video/HLvDawQa8AAV094.mp4)

## 相关概念

- [Plaza](tool-plaza.md) — 同样是 TUI 工具，面向包管理
- [lazycron](tool-lazycron.md) — 同样是 TUI 工具，面向 cron 管理