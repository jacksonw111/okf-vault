---
type: "Tool"
title: "ZapFast（Rust 桌面 WhatsApp）"
description: "拿 Rust + egui 写的桌面 WhatsApp，底层走 whatsapp-rust 对接 Web 协议，跨 Linux / macOS / Windows，扫码或填手机号绑手机，历史消息同步下来塞进本地 SQLite 文件。"
resource: "https://github.com/crmne/zapfast"
tags: "[rust, egui, whatsapp, desktop, messaging, sqlite, cross-platform]"
timestamp: "2026-09-16T16:11:00Z"
---

# ZapFast（Rust 桌面 WhatsApp）

## 它是什么

[crmne/zapfast](https://github.com/crmne/zapfast) 是一款**用 Rust + egui 写的桌面 WhatsApp**：底层依赖 `whatsapp-rust` 对接 Web 协议，跨 **Linux / macOS / Windows** 三端运行。扫码或填手机号绑手机后，历史消息同步下来塞进本地一个 **SQLite 文件**。

## 为什么用它 / 适合什么场景

- 想脱离浏览器 / 手机原生客户端、用桌面级窗口聊 WhatsApp。
- 看重消息本地化（SQLite 文件）以便后续做检索 / 备份 / 数据分析。
- 想要一款资源占用低的原生 GUI（egui + Rust）。
- 跨平台体验一致：同一份代码跑 Linux / macOS / Windows。

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust + egui | 原生 GUI、内存占用低 |
| 跨三端 | Linux / macOS / Windows 一套代码 |
| Web 协议接入 | 复用 `whatsapp-rust` 库 |
| 多绑定方式 | 支持扫码或手机号绑定 |
| 本地 SQLite | 历史消息存档本地文件，可备份可检索 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTtIyeagAAoJCr.jpg)

## 相关概念

- [Vaultwarden](./tool-vaultwarden.md) — 同样是「自托管 / 本机优先」思路的代表，与 ZapFast 同属数据归己的桌面工具谱系