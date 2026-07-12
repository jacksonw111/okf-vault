---
type: Tool
title: "Vela（去 Google 化的安卓地图 / 导航客户端）"
description: "去 Google 化的安卓地图与导航客户端（类似 NewPipe 之于 YouTube），用开放矢量瓦片做底图，再在设备上直接抓取 Google 公开 Web 端点补上 POI、路线与实时路况 ETA，可在无 GMS 的 ROM 上跑。"
resource: "https://github.com/PimpinPumpkin/Vela"
tags: [tool, android, map, navigation, degoogle, foss]
timestamp: 2026-07-12T16:30:00Z
---

# Vela（去 Google 化的安卓地图 / 导航客户端）

## 它是什么
开源安卓地图 / 导航客户端，定位"NewPipe 之于 YouTube"——把 Google Maps 这类闭源、依赖 Google Play Services（GMS）的体验"反"出来：底层用开放矢量瓦片做底图，POI / 路线 / 实时路况 ETA 则从设备上直接抓取 Google 公开 Web 端点补全。无需 GMS，可在去 Google 化的 ROM（LineageOS / GrapheneOS / /e/OS 等）上运行。

## 为什么用它 / 适合什么场景
- 用去 Google 化的安卓 ROM，不想为地图单独装 GMS。
- 想要 NewPipe 之于 YouTube 那样的"开源 + 自托管 + 不依赖 Google 账户"地图体验。
- 关注隐私 / 数据主权，希望地图搜索与导航尽量本地化、不上传个人轨迹。

## 关键能力
| 能力 | 说明 |
|------|------|
| 开放矢量瓦片底图 | 不依赖 Google 瓦片 |
| Google Web 端点抓取 | 补 POI / 路线 / 实时路况 ETA |
| 无 GMS 可跑 | 在去 Google 化的 ROM 上正常运行 |
| 类似 NewPipe | "NewPipe 之于 YouTube" 之于地图 |
| 安卓原生 | APK 安装即可用 |

## 参考链接
- [项目链接](https://github.com/PimpinPumpkin/Vela)
- [原始链接](https://x.com/QingQ77/status/2076134198101094783)

![Vela 截图](https://pbs.twimg.com/media/HM7I2srbEAALqLY.jpg)

## 相关概念
- [IPTV-org（13 万+ 星全球免费 IPTV 直播源大宝库）](tool-iptv-org.md) — 同类"去 Google 化 / 开源内容聚合"思路，定位不同（视频源）