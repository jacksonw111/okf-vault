---
type: Tool
title: "xan（Rust 写的「CSV 魔术师」命令行工具）"
description: "一个用 Rust 写的命令行 CSV 处理工具（「CSV 魔术师」），能极快、低内存地处理上 GB 的 CSV，并自带表达式语言、终端可视化以及词典统计、图论乃至抓取等社科向扩展。"
resource: "https://github.com/medialab/xan"
tags: [tool, csv, rust, cli, data-processing, social-science]
timestamp: 2026-07-12T16:30:00Z
---

# xan（Rust 写的「CSV 魔术师」命令行工具）

## 它是什么
Rust 写的命令行 CSV 处理工具，定位「CSV 魔术师」：处理速度极快、内存占用极低，能轻松吃下 GB 级 CSV 文件。除了常规的筛选 / 排序 / 聚合，还内置表达式语言、终端可视化，并提供词典统计、图论、网页抓取等社会科学场景向的扩展。

## 为什么用它 / 适合什么场景
- 用 Python pandas 处理 GB 级 CSV 太慢 / 太吃内存，想换 Rust 工具。
- 社会科学 / 计算传播学场景，需要词典统计、共现矩阵、图论分析等现成命令。
- 希望工具用 `awk` / `cut` 风格熟悉，但比传统 Unix 工具更适合 CSV 真实场景（带表头、字段内嵌逗号、引号转义等）。

## 关键能力
| 能力 | 说明 |
|------|------|
| 高性能 | Rust 写的引擎，处理 GB 级 CSV 不爆内存 |
| 表达式语言 | 内置 DSL，写自定义过滤 / 派生列 |
| 终端可视化 | ASCII 直方图 / 透视表直接在终端渲染 |
| 词典统计 | 社科场景常用的词频 / 共现 / TF-IDF |
| 图论 | 把 CSV 视为边表，做网络分析 |
| 网页抓取扩展 | 把 HTML 表格转 CSV，再继续处理 |

## 参考链接
- [项目链接](https://github.com/medialab/xan)
- [原始链接](https://x.com/QingQ77/status/2076250464312508475)

![xan 终端示意](https://pbs.twimg.com/media/HM8JVJObsAA4kDh.jpg)

## 相关概念
- [NLS（Go 写的现代化 ls）](tool-nls.md) — 同为 Rust 写的现代化 CLI 工具，但走 Nushell 风格表格路线
- [Tudo（终端下的待办 + Markdown 笔记本二合一 TUI）](tool-tudo.md) — 同为 TUI 风格个人效率工具，定位完全不同