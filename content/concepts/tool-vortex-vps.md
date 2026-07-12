---
type: Tool
title: "Vortex（终端里的 VPS 管理工具）"
description: "跑在终端里的 VPS 管理工具：连上 SSH 后会把自带监控程序传到远程服务器上，实时查看 CPU、内存等系统状态。"
resource: "https://github.com/berkayyytech/vortex"
tags: [tool, terminal, vps, ssh, monitoring, tui]
timestamp: 2026-07-12T16:30:00Z
---

# Vortex（终端里的 VPS 管理工具）

## 它是什么
一个跑在终端里的 VPS 管理工具。用户 SSH 登上一台远程 VPS 后，Vortex 会在本地终端自动加载一个远端监控程序，把 CPU、内存、负载、网络等系统状态实时呈现出来——免去另开 Web 控制面板或自己 `top`/`htop` 的麻烦。

## 为什么用它 / 适合什么场景
- 运维多台 VPS，每次都要 SSH 进去再开 htop / nethogs，重复且割裂。
- 希望在终端里直接看到所有 VPS 的资源水位，不依赖 Web 面板 / 不暴露额外端口。
- 不想装臃肿的 Ansible / Zabbix / Prometheus 套件，仅需轻量实时状态查看。

## 关键能力
| 能力 | 说明 |
|------|------|
| 终端原生 | 跑在 TUI 里，无需打开浏览器 |
| 自动部署监控 | 连上 SSH 后自传监控程序到远程服务器 |
| 实时状态 | CPU / 内存 / 负载 / 网络等系统状态实时刷新 |
| 多 VPS 切换 | 通过 SSH 配置即可在多台机器之间快速切换 |

## 参考链接
- [项目链接](https://github.com/berkayyytech/vortex)
- [原始链接](https://x.com/QingQ77/status/2076311365468541395)

视频：<https://video.twimg.com/amplify_video/2076084957651611648/vid/avc1/632x480/XsXGa6q5ph-mTKG9.mp4?tag=28>

## 相关概念
- [Glance Dashboard（macOS 三合一开发者桌面仪表盘）](tool-glance-dashboard.md) — 同类「开发者运维仪表盘」思路，但走 macOS 原生 GUI 路线