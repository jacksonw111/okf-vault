---
type: "Tool"
title: "SSHBool"
description: "基于 Tauri v2 + Rust 的桌面工作区，把 SSH 终端、SFTP 文件传输、远程文件编辑、服务器监控、数据库查询合并到一个应用里。"
resource: "https://github.com/omarsenusi/sshbool"
tags: ["tauri", "rust", "ssh", "sftp", "desktop", "server-management", "database"]
timestamp: "2026-08-12T12:39:00Z"
---

# SSHBool

[SSHBool](https://github.com/omarsenusi/sshbool) 是基于 **Tauri v2 + Rust** 的桌面工作区，把运维日常需要的几样东西——SSH 终端、SFTP 文件传输、远程文件编辑、服务器监控、数据库查询——合并到一个应用里。

## 它是什么

一个跨平台的桌面端"服务器工作台"，取代"开好几个客户端分别连不同服务"的零散模式。在同一个界面里既能敲命令、又能拖文件、还能改远程代码、做系统监控、跑数据库查询。

## 为什么用它 / 适合什么场景

- **运维日常一体化**：开一个窗口就能干完 SSH + SFTP + 文件编辑 + 数据库。
- **Tauri 体积小、跨平台**：原生 Rust 内核，比 Electron 系轻量。
- **远程文件就地编辑**：不必下载到本地再上传。
- **服务器 + 数据库**：常见操作不必切到 Navicat / DataGrip。

## 关键能力

| 能力 | 说明 |
|------|------|
| SSH 终端 | 内置终端仿真，远程命令直跑 |
| SFTP 文件传输 | 拖拽上传下载 |
| 远程文件编辑 | 直接在应用里编辑服务器上的代码 |
| 服务器监控 | CPU / 内存 / 负载等指标可视化 |
| 数据库查询 | 跑 SQL 不用切数据库客户端 |
| Tauri v2 + Rust | 跨平台原生桌面，小巧 |

## 媒体

![](https://pbs.twimg.com/media/HPakO8naUAAy4PE.jpg)

## 参考链接

- [项目仓库](https://github.com/omarsenusi/sshbool)

## 相关概念

- [Pixshell](./tool-pixshell.md) — 跨平台原生 SSH/SFTP 客户端，macOS Swift + Windows WPF 双端，与 SSHBool 同属原生 SSH 客户端
- [Hop (SSH TUI)](./tool-hop-ssh-tui.md) — 终端 SSH 多服务器切换 TUI
- [LSPanel](./tool-lspanel.md) — Tauri 搭的 PHP 本地开发环境桌面面板