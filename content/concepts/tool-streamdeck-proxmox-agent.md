---
type: "Tool"
title: "StreamDeck Proxmox Agent"
description: "把闲置的 Stream Deck 变成 Proxmox 主机的常亮硬件状态面板：CPU / 内存 / 容器 / 网络 / 服务健康一眼可见。"
resource: "https://github.com/r-morato/streamdeck-proxmox-agent"
tags: "[stream-deck, proxmox, hardware-panel, monitoring, homelab, status]"
timestamp: "2026-09-17T03:48:00Z"
---

# StreamDeck Proxmox Agent

## 它是什么

[r-morato/streamdeck-proxmox-agent](https://github.com/r-morato/streamdeck-proxmox-agent) 是 **r-morato** 开源的 Stream Deck 插件。它把**闲置的 Elgato Stream Deck 硬件**变成一台 Proxmox VE 主机的**常亮硬件状态面板**——CPU、内存、容器、网络流量、服务健康状态一眼可见。

## 关键能力

| 能力 | 说明 |
|------|------|
| CPU / 内存 | 实时显示 Proxmox 宿主机和 LXC / VM 的关键指标 |
| 容器状态 | 列出 LXC 容器运行 / 停止状态，点击可触发动作 |
| 网络流量 | 实时网速（上下行） |
| 服务健康 | 心跳式展示关键服务是否在线 |
| 常亮显示 | Stream Deck 屏幕常亮，无需唤醒 |

## 适合什么场景

- 家里 / 公司有 Proxmox 主机 + 一台闲置 Stream Deck，想给机柜 / 桌面加一块「专业感」的监控副屏的运维 / Homelab 玩家。
- 想把 Stream Deck 从「OBS 直播切场景」扩展为「服务器监控屏」的多功能玩家。
- 研究 Stream Deck SDK / 第三方插件开发的工程师。

## 与相关概念的关系

- [Self-Hosted（自托管）](./term-self-hosted.md) — 该工具是「自托管运维栈 + 硬件副屏」这个特定交集的延伸。
- [Sandbox（沙箱）](./term-sandbox.md) — Proxmox 本身就是沙箱/LXC 隔离方案的承载平台。

## 参考

- 项目链接：<https://github.com/r-morato/streamdeck-proxmox-agent>

![preview](https://pbs.twimg.com/media/HSVtWbOagAAGgJH.jpg)
