---
type: Tool
title: "Frp Manager（frp 内网穿透管理系统）"
description: "Bai2001 开源的本地桌面内网穿透管理系统，基于 frp，由服务端控制面 + Wails/Vue 桌面客户端组成，集中管理服务器、隧道和 frpc/frps 进程。"
resource: "https://github.com/Bai2001/frp-manager"
tags: "[frp, nat, tunnel, self-hosted, wails, vue, desktop]"
timestamp: "2026-07-11T20:00:00Z"
---

# Frp Manager（frp 内网穿透管理系统）

## 它是什么

`Bai2001/frp-manager` 是一个**本地桌面版的 frp 内网穿透管理系统**，由两部分组成：

- **服务端控制面**：集中管理所有 frp 服务器、隧道、frpc / frps 进程。
- **桌面客户端**：Wails + Vue 写的 GUI，本地启停 / 监控隧道。

底层仍是 [fatedier/frp](https://github.com/fatedier/frp) 这套成熟内网穿透工具，本项目解决的是「frp 命令行分散在多台机器上不好管」的问题。

## 为什么用它 / 适合什么场景

- 用 frp 做了多条内网穿透隧道，但机器一多配置文件就散落各处。
- 想要 GUI 集中启停 / 监控，而不是 SSH 到每台机器改 `frpc.ini`。
- 自托管运维团队管理多家分公司 / 多台 NAS 的内网穿透。

## 关键能力

| 能力 | 说明 |
|------|------|
| 集中管理 | 服务端控制面统一管所有 frp 服务器 / 隧道 |
| 桌面 GUI | Wails + Vue，本地可视化操作 |
| 进程管理 | 启停 frpc / frps 进程 |
| 隧道监控 | 看每条隧道状态 |

## 相关概念

- [3X-UI](tool-3x-ui.md) — Xray 图形面板，类似「代理类工具的 GUI 集中管理」
- [Sub-Store Cloudflare](tool-sub-store-cloudflare.md) — Cloudflare Workers 部署的订阅聚合工具
- [Proxide](tool-proxide.md) — 内网代理 / 反向代理工具

## 项目链接

- 项目仓库：<https://github.com/Bai2001/frp-manager>