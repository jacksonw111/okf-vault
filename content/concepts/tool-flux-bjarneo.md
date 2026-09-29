---
type: "Tool"
title: "Flux（bjarneo/flux，Omarchy 跨设备同步工具）"
description: "把 Omarchy 桌面和 Android 手机 / Mac 连起来：局域网或 Tailscale 上互传文件 / 剪贴板 / 通知，还能远程输入和投屏；桌面默认防火墙不需要开新规则。"
resource: "https://github.com/bjarneo/flux"
tags: "[omarchy, file-sync, clipboard, tailscale, kdeconnect, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# Flux（bjarneo/flux，Omarchy 跨设备同步工具）

## 它是什么

[Flux](https://github.com/bjarneo/flux) 是 bjarneo 开源的跨设备同步工具：把 Omarchy（Arch + Hyprland）桌面与 Android 手机 / Mac 连接起来，在局域网或 Tailscale 上互传文件、剪贴板、通知，还能远程输入和投屏。

## 关键能力

| 能力 | 说明 |
|------|------|
| 文件互传 | 桌面 ↔ 手机 / Mac 互传文件 |
| 剪贴板同步 | 一端复制，另一端粘贴 |
| 通知同步 | 手机通知推送到桌面 |
| 远程输入 | 从桌面控制手机，或反过来 |
| 投屏 | 桌面 / 手机内容互相投屏 |
| 网络灵活 | 局域网 + Tailscale 私网 |
| 防火墙友好 | 桌面默认防火墙不需要开新规则 |

## 适用场景

- Linux 桌面用户（特别是 Omarchy）想和手机 / Mac 协同
- 想要 KDE Connect 的开源轻量替代
- 用 Tailscale 组私网、不想配置端口

## 媒体预览

视频：<https://video.twimg.com/amplify_video/2104749462996541440/vid/avc1/1920x1080/5v5coQBw82l_ncoN.mp4?tag=29>

## 原始链接

- 项目主页：<https://github.com/bjarneo/flux>

## 相关概念

- [Omarchy iCloud Photos](./tool-omarchy-icloud-photos.md) — Omarchy 桌面 Quickshell + QML 原生窗口浏览 iCloud 相册
- [Omarchy Blue Hour Theme](./tool-omarchy-blue-hour-theme.md) — Omarchy 桌面主题，与 Flux 同为 Omarchy 生态