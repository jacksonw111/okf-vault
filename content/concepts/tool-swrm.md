---
type: "Tool"
title: "Swrm（接口绑定的隐私 BitTorrent TUI 客户端）"
description: "Go 写的终端 BitTorrent 客户端（Bubble Tea），全程键盘操作，无搜索 / 索引器；可把所有流量绑到指定接口（tun0 / wg0），接口掉线立即暂停传输，零 IP 泄漏风险。"
resource: "https://github.com/ManasvinYadav/swrm"
tags: [go, tui, bittorrent, privacy, bubble-tea, terminal]
timestamp: "2026-08-31T16:00:00Z"
---

# Swrm

## 它是什么

[Swrm](https://github.com/ManasvinYadav/swrm) 是 [ManasvinYadav](https://github.com/ManasvinYadav) 用 **Go** 写的**终端 BitTorrent 客户端**，界面基于 [Bubble Tea](https://github.com/charmbracelet/bubbletea)，**全程键盘操作**。

特点：

- **无搜索 / 无索引器**：磁力链接 / infohash / 本地 `.torrent` 文件，给什么下什么；
- **接口绑定**：把所有 BT 流量绑死在指定接口（如 `tun0`、`wg0`），接口掉线**立即暂停全部传输**——这是给 VPN / WireGuard 用户的核心卖点，**真实 IP 永远不会泄漏**；
- **零依赖网络栈**：不调用系统路由表，只走你给的接口。

## 为什么用它 / 适合什么场景

- **VPN 用户下 BT**：BT 默认走系统路由 → 真实 IP 泄漏 → RIAA / 监管找上门。Swrm 强制走 VPN 接口解决；
- **极简终端党**：不喜欢 qBittorrent / Transmission 的 GUI；
- **无索引器** = 不依赖中心化的 BT 搜索站，**反审查友好**。

## 关键能力

| 能力 | 说明 |
|------|------|
| Bubble Tea TUI | 终端 GUI，全键盘 |
| 无索引器 | 只下用户主动给的种子 |
| 接口绑定 | 流量锁死 `tun0` / `wg0` |
| 自动暂停 | 接口掉线立即停所有传输 |
| Go 单二进制 | 跨平台、低资源 |

## 媒体

- 项目截图：![](https://pbs.twimg.com/media/HRAyi3sagAAfdcS.png)

## 相关概念

（暂无关联项目可链。）

## 参考链接

- 项目链接：<https://github.com/ManasvinYadav/swrm>