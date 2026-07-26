---
type: "Tool"
title: "OpenSurge for Mac（YTwsy/OpenSurge-for-Mac）"
description: "把 Mac 变成全屋透明代理网关：手机、电视、游戏机从 Mac 拿 DHCP/DNS，每台设备能单独配置走代理还是直连，设备端零配置。"
resource: "https://github.com/YTwsy/OpenSurge-for-Mac"
tags: [macos, proxy, gateway, surge, transparent, dhcp, dns, network]
timestamp: "2026-07-26T03:28:00Z"
---

# OpenSurge for Mac（YTwsy/OpenSurge-for-Mac）

## 它是什么

`YTwsy/OpenSurge-for-Mac` 把 **Mac 变成全屋透明代理网关**：手机、电视、游戏机等从 Mac 拿 **DHCP/DNS**，每台设备能**单独配置走代理还是直连**，**设备端零配置**。

## 为什么用它 / 适合什么场景

- 想把家里「科学上网」从单台电脑扩展到**全屋设备**（电视、IoT、游戏机），但又不想每台设备单独配；
- 希望**按设备粒度**控制走代理还是直连（电视直连海外看流媒体，手机走代理访问外网）；
- 已有 Surge 配置文件，希望在 Mac 上**以网关形式**复用同一套规则。

## 关键能力

| 能力 | 说明 |
|------|------|
| 全屋网关 | Mac 变透明代理网关 |
| DHCP/DNS | 自动给局域网设备下发网络配置 |
| 设备粒度 | 每台设备可单独走代理或直连 |
| 零设备端配置 | 设备无需任何手动操作 |
| Surge 复用 | 沿用已有 Surge 规则 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOC-xvGa0AAUVaR.jpg)

- 项目链接：<https://github.com/YTwsy/OpenSurge-for-Mac>

## 相关概念

- [3X-UI](tool-3x-ui.md) — 同样是代理/翻墙图形面板（Xray 后端，面向服务端/多用户）
- [Lucky](tool-lucky.md) — 同样是网关/网络工具（DDNS+ACME+反代瑞士军刀）
