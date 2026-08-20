---
type: Tool
title: "dsh-rs (xizheyin/deepseek-harness-rs)"
description: "把 DeepSeek Harness 用 Rust 重写成命令行程序 dsh，能在终端里搜代码 / 读文件 / 打补丁 / 跑命令，并保持长会话连续性"
resource: "https://github.com/xizheyin/deepseek-harness-rs"
tags: [deepseek-harness, dsh, rust, cli, coding-agent]
timestamp: 2026-08-20T13:21:00Z
---

# dsh-rs (xizheyin/deepseek-harness-rs)

## 它是什么
[`xizheyin/deepseek-harness-rs`](https://github.com/xizheyin/deepseek-harness-rs) 用 **Rust** 把 **DeepSeek Harness** 重写成一个**命令行程序**，装完后命令就叫 `dsh`。它把"在真实代码仓库里跟 AI 连续干活"这件事压成 CLI：能在终端里搜代码、读文件、打补丁、跑命令，**长会话还能存下来接着聊**。

## 为什么用它 / 适合什么场景
- 想在服务器 / WSL / 远程盒子这种没有浏览器的环境里跑 AI 编码代理。
- 嫌官方 DSH 网页端太重，希望一切通过 SSH 终端完成。
- 已有 Rust 项目，想以最小依赖引入 dsh（编译产物是一个静态二进制）。

## 关键能力
| 能力 | 说明 |
|------|------|
| CLI 优先 | 一个二进制 `dsh`，终端开箱即用 |
| 代码搜索 | 在仓库内搜索符号 / 文本 |
| 文件读写 + 打补丁 | 直接对工作区文件应用编辑 |
| 命令执行 | 在终端里跑任意命令 |
| 会话持久化 | 长对话可存盘，下次从断点接着聊 |
| Rust 重写 | 性能好、单二进制、部署轻 |

## 媒体
- ![dsh-rs 截图](https://pbs.twimg.com/media/HQD2006aoAAuDsy.jpg)

## 相关概念
- [项目仓库](https://github.com/xizheyin/deepseek-harness-rs) — 仓库主页
- [dsh-desktop](./tool-dsh-desktop.md) — DSH 的另一种打包形式（原生桌面窗口）
- [dsh-context](./tool-dsh-context.md) — 同一 DSH 生态的上下文可视化插件
