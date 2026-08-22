---
type: Tool
title: "HuntClaw（tigerlang/huntclaw）"
description: "用 Zig 写的查找替换工具，把速度做到极致，260KB 单二进制零依赖，相同机器同一批数据下 7 测 6 胜 ripgrep / GNU grep / sed / sd"
resource: "https://github.com/tigerlang/huntclaw"
tags: "[zig, cli, search, replace, ripgrep-alternative, perf]"
timestamp: "2026-08-22T03:30:00Z"
---

# HuntClaw

## 它是什么
[`tigerlang/huntclaw`](https://github.com/tigerlang/huntclaw) 是用 Zig 写的命令行查找替换工具：**把速度推到极致，功能与排版都让位**——二进制约 260 KB，无运行时依赖，跟 ripgrep / GNU grep / sed / sd 四家在同一台机器同一批数据上对比，七个测试场景拿下六个，匹配越密集、文件越大优势越明显，最快能差一个数量级。

## 为什么用它 / 适合什么场景
- 需要在大仓库（百万行级代码、GB 级日志、巨型数据集）里频繁做替换，又嫌 ripgrep 慢。
- 想要个真正零依赖、能直接 scp 到服务器就用的单文件二进制工具。
- 对 SIMD / Boyer-Moore-Horspool 这类底层算法在生产 CLI 里如何落地感兴趣的工程师。

## 关键能力
| 能力 | 说明 |
|------|------|
| 极小体积 | Zig 静态编译输出约 260 KB，单二进制可移植 |
| 零运行时 | 不依赖 libc++、不依赖第三方库，静态链接即跑 |
| 算法堆栈 | Boyer-Moore-Horspool 跳表 + 双字节 SIMD 预过滤 + 单趟构建输出 |
| 目录并行 | 目录扫描跨线程并行 |
| 对比基准 | 7 测 6 胜 ripgrep / GNU grep / sed / sd |

## 媒体
- ![](https://pbs.twimg.com/media/HQOPss6aQAAiufk.jpg)

## 相关概念
- [ax](./tool-ax-cli-scraper.md) — 同样定位「给 AI 用的极简命令行工具」，但方向是抓取 / 省 token
- [nls](./tool-nls.md) — Go 写的现代化 ls，Nushell 风格表格，也是「CLI 重做一遍」思路
