---
type: "Tool"
title: "TermPair (cs01/termpair)"
description: "在浏览器里端到端加密地查看和控制远程终端，服务器只做盲转发，永远看不到明文内容。Rust 单二进制，自带服务端、客户端和 Web 前端，免 Node / Python / Docker。"
resource: "https://github.com/cs01/termpair"
tags: "[terminal, e2ee, aes-128-gcm, rust, single-binary, remote-shell, xterm.js, blind-relay]"
timestamp: "2026-08-04T20:30:00Z"
---

# TermPair (cs01/termpair)

## 它是什么

[TermPair](https://github.com/cs01/termpair) 是一个**用 Rust 写的终端共享工具**，**单个静态二进制就把服务端、客户端和 Web 前端打包在一起**，支持 Linux / macOS / Windows，**不需要 Node、Python 或 Docker**。

**核心设计是零知识**：终端输出用 **AES-128-GCM** 加密后发给服务器，**服务器作为盲中继只负责转发**，接触不到密钥和明文。

![TermPair 截图](https://pbs.twimg.com/media/HOtlFnpaIAAdqnk.jpg)
![TermPair 截图](https://pbs.twimg.com/media/HOtlGf1bkAId8fq.jpg)

## 加密设计

每个会话生成 **3 把密钥**：

| 密钥 | 用途 |
|------|------|
| 输出密钥 | 加密服务器 → 浏览器的终端输出 |
| 输入密钥 | 加密浏览器 → 服务器的用户输入 |
| 引导密钥 | 通过 URL 的 hash 片段传递，**不经过服务器** |

## 为什么用它 / 适合什么场景

- **零知识**：服务器看不到任何终端内容。
- **单二进制**：免运行时，免安装。
- **跨平台**：Linux / macOS / Windows 同一套用法。
- **浏览器即用**：接收方打开链接就能看 + 操作。

## 用法

| 命令 | 干什么 |
|------|--------|
| `termpair share` | 启动共享，打印链接 |
| `termpair share --read-only` | 只读模式，浏览器只能看不能操作 |

接收方：浏览器打开链接 → xterm.js 实时看终端 → 可直接打字操作（只读模式下只能看）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单二进制 | 服务端 / 客户端 / Web 前端打包在一个 binary |
| 跨平台 | Linux / macOS / Windows |
| 零依赖运行时 | 免 Node / Python / Docker |
| 端到端加密 | AES-128-GCM |
| 盲中继服务器 | 服务器只转发，接触不到明文 / 密钥 |
| 三把密钥分立 | 输出 / 输入 / 引导分开传递 |
| URL hash 传密钥 | 引导密钥不过服务器 |
| 浏览器 xterm.js | 接收方零安装 |

## 参考链接

- [项目仓库](https://github.com/cs01/termpair)

## 相关概念

- [Hop SSH TUI](./tool-hop-ssh-tui.md) — Go 写的终端 SSH 多服务器切换 TUI（多服务器管理场景）
- [qr-data-transfer](./tool-qr-data-transfer.md) — 两台都不能上网的设备间用动态二维码传文件
- [TermBoard](./tool-termboard.md) — Python 项目任务常驻终端界面
