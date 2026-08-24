---
type: Tool
title: "Home KTV (ktv-home)"
description: "自托管家庭局域网 KTV 系统：服务端 Spring Boot + PostgreSQL + FFmpeg，手机扫码点歌，电视端 Android TV 播放。"
resource: "https://github.com/zhayinggang/ktv-home"
tags: [ktv, home-karaoke, self-hosted, spring-boot, android-tv, vue]
timestamp: "2026-08-24T09:45:00Z"
---

# Home KTV (ktv-home)

## 它是什么

[zhayinggang/ktv-home](https://github.com/zhayinggang/ktv-home) 是一套部署在家庭 NAS 或 Linux 主机上的局域网 KTV 系统，由三个部分组成：

- **服务端**：Spring Boot + PostgreSQL + FFmpeg，负责曲库管理、播放队列、转码。
- **手机端**：Vue 3 写的 H5 点歌页 + 管理后台，微信或浏览器扫码即用。
- **电视端**：基于 Media3/ExoPlayer 的 Android TV 客户端，负责画面与音轨播放。

## 为什么用它 / 适合什么场景

- 家里有 NAS + 智能电视，想在客厅搞一套完整的点歌唱歌系统，但不想去 KTV。
- 家人不爱装 App，希望「手机扫码即用」极简入口。
- 想要队列 / 进度 / 逐字歌词 / 音量 / 原唱 vs 伴唱切换在电视与手机之间实时同步。
- 想用同一套局域网基础设施自托管，避免云服务月费。

## 关键能力

| 能力 | 说明 |
|------|------|
| 扫码点歌 | 微信 / 浏览器扫码，无需装 App |
| 实时同步 | 队列 / 进度 / 音量 / 原唱/伴唱状态在手机 ↔ 电视间 WebSocket 同步 |
| 逐字歌词 | 词曲时间轴同步显示 |
| Android TV 客户端 | 基于 Media3/ExoPlayer 原生 TV 应用 |
| FFmpeg 转码 | 服务端统一处理音视频格式 |
| 管理后台 | Vue 3 写成的曲库 / 用户管理界面 |

## 相关概念

- [Jellyfin 类电视客户端](./tool-ocplayer.md) — 类似的「本地媒体 → 电视」自托管方案
- [自托管 NAS 生态](./term-synology-hyper-backup.md) — 家庭 NAS 部署参考

## 参考链接

- [项目链接](https://github.com/zhayinggang/ktv-home)
- ![](https://pbs.twimg.com/media/HQc6jOdbYAAnae0.png)
- ![](https://pbs.twimg.com/media/HQc6k9UbUAAwG4v.jpg)
- ![](https://pbs.twimg.com/media/HQc6pEmboAIVFIQ.jpg)