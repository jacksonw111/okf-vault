---
type: Tool
title: "AceShell（七合一远程连接桌面工具）"
description: "把 SSH / Telnet / 串口 / SFTP / RDP / HTTP / 本地终端七类远程连接统一收进一个跨平台桌面工具，Go + Wails v3 + Vue 3 + xterm.js。"
resource: "https://github.com/dingtongbin/AceShell"
tags: [terminal, ssh, rdp, sftp, cross-platform, desktop, wails]
timestamp: "2026-09-03T00:00:00Z"
---

# AceShell（七合一远程连接桌面工具）

## 它是什么

[AceShell](https://github.com/dingtongbin/AceShell) 是一个跨平台桌面工具，把 **SSH、Telnet、串口、SFTP、RDP、HTTP、本地终端** 七类远程连接统一进同一个界面。技术栈是 Go + Wails v3 + Vue 3，桌面端打包支持 Windows、macOS、Linux。

终端渲染用 [xterm.js](https://xtermjs.org/)，本地终端经 ConPTY / PTY 驱动。会话按树形组织并加密存储，标签页拖拽排序、四象限分屏，RDP 用 IronRDP 全屏渲染、按设备像素比 1:1 缩放。

## 为什么用它 / 适合什么场景

- 日常运维要同时管 Linux 服务器、Windows RDP、网络设备串口、HTTP 接口调试——不想切换 5 个客户端；
- 想要一款能在一台 Mac / Windows / Linux 上都跑得一致的远程连接工具；
- 需要四象限分屏同时观察多个远程会话；
- 想把会话、配置、密钥集中加密存储在本地。

## 关键能力

| 能力 | 说明 |
|------|------|
| 七合一连接 | SSH / Telnet / 串口 / SFTP / RDP / HTTP / 本地终端 |
| 跨平台 | Windows / macOS / Linux 一份代码 |
| 技术栈 | Go + Wails v3 + Vue 3 |
| 终端渲染 | xterm.js |
| 本地终端 | ConPTY / PTY 驱动 |
| 会话管理 | 树形组织 + 加密存储 |
| 多任务分屏 | 标签页拖拽排序 + 四象限分屏 |
| RDP | IronRDP 全屏渲染、按设备像素比 1:1 缩放 |

## 参考链接

- 项目链接：<https://github.com/dingtongbin/AceShell>
- 原始推文：<https://x.com/QingQ77/status/2095428080609206608>

## 相关概念

- [essh](./tool-essh.md) — 终端 SSH 客户端，多会话 + 实时主机指标 + 群组差异对比
- [Kitty Sessionizer](./tool-kitty-sessionizer.md) — 给 kitty 终端补的 tmux-sessionizer 式项目管理
