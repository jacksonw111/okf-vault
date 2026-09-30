---
type: Tool
title: "CodeDiff（Rust 写的语法感知代码 diff 工具）"
description: "Rust 写的代码 diff 工具：先用 tree-sitter 把源码拆成语法树再比较，只高亮真正变化的片段；整行重写会被切成局部修改、搬走的代码块直接标 move，不冒充"一删一增"。打包 24 种语言语法。"
resource: "https://github.com/ivankovic/codediff"
tags: [diff, code-review, rust, tree-sitter, syntax-aware, move-detection]
timestamp: 2026-09-30T06:43:00Z
---

# CodeDiff

## 它是什么

**CodeDiff** 是 [ivankovic](https://github.com/ivankovic) 维护的 Rust 写的代码 diff 工具——核心差异点是不按"行"比较，而是按**语法结构**比较。

- 先用 **tree-sitter** 把源码拆成语法树。
- 整行重写时切成几段**局部修改**展示，不假装是"整行删除 + 整行新增"。
- 跨位置搬走的代码块直接标 `move`，不让它冒充"一删一增"。
- 识别不出的扩展名回退到纯文本逐行 diff。
- 二进制文件只给一行提示，不输出无意义乱码。

打包的 tree-sitter 语法覆盖 24 种语言：C、Go、Python、Rust、TypeScript 等常见语言都能结构化比对。

## 为什么用它 / 适合什么场景

- 看过太多 GitHub PR 上"明明只改了一个变量，整行被红绿覆盖"的体验，希望看到真正的局部变化。
- 在做 code review 时希望快速识别"代码被搬走了"还是"代码被重写了"。
- 跨语言项目里希望对不同语言有统一的语法感知 diff。
- 想要一个 Rust 写的高性能本地 diff 工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实现 | Rust |
| 解析器 | tree-sitter |
| 比较单位 | 语法节点（而非行） |
| 语言覆盖 | 24 种（tree-sitter 打包语法） |
| Move 检测 | 是 |
| 未知扩展名回退 | 纯文本逐行 |
| 二进制文件 | 一行提示，不展开 |

## 参考链接

- 仓库：<https://github.com/ivankovic/codediff>

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HTXyDadagAAOSrW.mp4>

## 相关概念

- [diff 与 patch 工具](./tool-wrk2.md) — 通用负载测试工具，同为 Rust CLI 思路的对应