---
type: Tool
title: "Comail（Tauri 2 桌面邮件客户端）"
description: "Tauri 2 写的桌面邮件客户端（Mac / Windows / Linux），主打键盘操作，支持 Gmail、Microsoft 365 和任意 IMAP，邮件全量本地 SQLite 存储，本机可搜索可语义搜索，断网照常读、搜、写、归类。"
resource: "https://github.com/NextOSP/comail"
tags: [email, tauri, desktop, keyboard-driven, local-first, sqlite, semantic-search]
timestamp: "2026-07-28T00:22:00.000Z"
---

# Comail

## 它是什么

**Tauri 2** 写的桌面邮件客户端，主打：

- **跨平台**：macOS / Windows / Linux 一套代码
- **键盘流**：操作全程可用快捷键完成（无需鼠标）
- **多协议**：Gmail、Microsoft 365、任意 IMAP 邮箱
- **本地优先**：邮件全量存在本地 SQLite
- **离线可读可写**：没网也能读、搜、写、归类
- **本机搜索 + 语义搜索**：检索完全在本机跑

![截图示例](https://pbs.twimg.com/media/HOKCl8zaMAAX4gH.jpg)

## 为什么用它

| 痛点 | Comail 解法 |
|------|------------|
| 网页邮件吃资源、键盘操作弱 | 原生桌面 + 键盘流设计 |
| Gmail 隐私问题 | 邮件全量本地 SQLite |
| 没网就抓瞎 | 离线读写 + 本地搜索 |
| 跨平台一致体验 | Tauri 2 一套代码，三平台 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台桌面 | Tauri 2，体积小、性能好 |
| Gmail / M365 / IMAP | 三种主流邮件源都支持 |
| 本地 SQLite 存储 | 数据不依赖云，断网照常 |
| 语义搜索 | 本机跑 embeddings |
| 键盘驱动 | 致敬 Gmail 旧版的快捷键传统 |

## 原始链接

- [项目仓库](https://github.com/NextOSP/comail)
- [推文剪藏](https://x.com/QingQ77/status/2081897926792814708)

## 相关概念

- [Comando（本地优先多智能体协作编辑器）](./tool-comando.md) — 同样 Electron + Rust 的本地优先架构思路
- [Cue（macOS AI 副驾）](./tool-cue.md) — 浮动屏幕上的 AI 副驾，看 / 听会议
- [BiliMusic（B 站音乐播放器）](./tool-bili-music-electron.md) — Electron 把 B 站音乐包装成本地桌面应用
- [WaLinux（Linux 原生 WhatsApp）](./tool-walinux.md) — 同类 Tauri 2 桌面化通讯思路