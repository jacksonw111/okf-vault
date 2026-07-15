---
type: "Tool"
title: "scroggo（nates/scroggo）"
description: "自托管的 ListenBrainz 兼容 scrobble 服务,Go 写,单二进制加 SQLite 即可,把 Web Scrobbler / navidrome / gonic 等客户端的听歌记录全部收进本地数据库。"
resource: "https://github.com/nates/scroggo"
tags: "[music, scrobble, listenbrainz, self-hosted, go, sqlite]"
timestamp: "2026-07-15T10:17:00Z"
---

# scroggo

[scroggo](https://github.com/nates/scroggo) 是一个**自托管、ListenBrainz 兼容的 scrobble 服务**。用 Go 写成,单个二进制 + SQLite 就能跑,接住 Web Scrobbler、navidrome、gonic 这些 ListenBrainz 客户端上报的播放记录,**统统一份本地听歌史**。

## 它解决了什么

主流 scrobble 服务(Libre.fm / ListenBrainz 主站)要么第三方托管存你的播放史、要么部署门槛高。scroggo 单文件单数据库跑起来,**听歌记录完全自己掌控**,同时保持对所有 ListenBrainz 客户端的协议兼容。

## 关键能力

| 能力 | 说明 |
|------|------|
| ListenBrainz 兼容 | 所有支持该协议的客户端/Web Scrobbler 都能上报 |
| 单二进制部署 | Go 编译产物 + SQLite,无外部依赖 |
| 播放历史归一 | 多端数据都进同一份本地数据库 |
| 隐私友好 | 数据不出本机 |

## 媒体

![](https://pbs.twimg.com/media/HNJ0bPYaEAA7SYb.jpg)

## 参考链接

- [项目仓库](https://github.com/nates/scroggo)

## 相关概念

- [navifsp](./tool-navifsp.md) — 同为自托管音乐生态工具,本工具管「听歌历史」,navifsp 管「盘符挂载」
