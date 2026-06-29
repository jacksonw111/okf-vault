---
type: Tool
title: "wlctl"
description: "Rust 写的终端网络管理工具，fork 自 impala，集成 WiFi / 热点 / 网卡切换 / VPN / WireGuard 档案管理 / 断网 doctor 排查。"
resource: "https://github.com/aashish-thapa/wlctl"
tags: "[rust, network, tui, vpn, wireguard, networkmanager]"
timestamp: "2026-06-29T16:00:00Z"
---

# wlctl

## 它是什么
wlctl 是一个面向 Linux 桌面（依赖 NetworkManager）的终端网络管理 TUI。fork 自 `impala`，用 Rust 重写后保留并扩展了 WiFi 扫描 / 连接、热点开启、网卡切换、VPN 开关、粘贴 WireGuard 配置自动建档案等能力，并加入了一个 `doctor` 子命令帮你从链路层往上排查断网。

视频演示：<https://video.twimg.com/amplify_video/2071193441086889984/vid/avc1/946x572/uLAtK6ggVUu8oOQa.mp4?tag=28>

## 为什么用它 / 适合什么场景
- **不想在 GNOME Settings / nm-connection-editor 里点来点去**：所有常见网络操作在 TUI 里键位直达，界面会标出**实际走流量的链路**和**本机 IP**，一眼看清哪张网卡正在工作。
- **经常切 VPN / WireGuard**：粘贴 WireGuard 配置即生成档案，免去手敲 ini。
- **断网不知道从哪儿查**：`doctor` 子命令从链路层往上依次检查接口 / IP / 路由 / DNS / 远端连通性，给出定位建议。
- **键位不熟可以改**：`config.toml` 自定义快捷键。

## 关键能力
| 能力 | 说明 |
|------|------|
| WiFi 扫描 / 连接 | 列出可见网络 + 信号强度 |
| 热点开关 | 软 AP 一键起 |
| 网卡切换 | 在多网卡间选主链路 |
| VPN 开关 | 复用 NetworkManager 已建 VPN |
| WireGuard 档案 | 粘贴 conf 自动入库 |
| `doctor` 排查 | 从 L2 到 L7 顺序给出诊断 |
| 实时标出活动链路 | 哪张网卡 / 哪个 IP 在跑流量 |
| 键位自定义 | `config.toml` 改快捷键 |

## 安装前置
- Linux + NetworkManager 在跑（`systemctl status NetworkManager`）
- Rust 工具链（`cargo install wlctl` 或从 release 拿二进制）

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071434983781306798)
- [项目链接](https://github.com/aashish-thapa/wlctl)

## 相关概念
- [HypoMux](./tool-hypomux.md) — Windows 多网卡带宽聚合下载加速，定位与 wlctl 互补
- [3X-UI](./tool-3x-ui.md) — Xray 图形面板，本场景里 wlctl 负责链路切换、3X-UI 负责代理协议本身
- [Hypomux](./tool-hypomux.md) — 类似的多链路场景在 Windows 端的对应实现