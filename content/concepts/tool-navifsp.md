---
type: "Tool"
title: "navifsp（louislam/navifsp）"
description: "Windows 小工具,借 WinFSP 把 Navidrome 音乐服务挂成磁盘或文件夹,让 Foobar2000 等本地播放器直接当本地曲库用。"
resource: "https://github.com/louislam/navifsp"
tags: "[navidrome, winfsp, foobar2000, music, virtual-drive, windows]"
timestamp: "2026-07-15T04:29:00Z"
---

# navifsp

[navifsp](https://github.com/louislam/navifsp) 是个 Windows 小工具,借助 [WinFSP](https://winfsp.dev/) 把 [Navidrome](https://www.navidrome.org/) 音乐服务**挂载成本地磁盘或文件夹**,让 Foobar2000 等本来只认本地文件系统的播放器可以直接当本地曲库浏览和播放。

## 它解决了什么

很多本地 HiFi 播放器只走「文件夹」模型,对 Subsonic / Navidrome 这种 HTTP 音乐服务不友好。navifsp 用文件系统驱动把远程服务翻译成本地盘符,播放器不用改造,直接当本地库用。

## 关键能力

| 能力 | 说明 |
|------|------|
| FUSE 风格挂载 | 基于 WinFSP,把 HTTP 接口翻译成本地 NTFS |
| 全文件系统观感 | 列表 / 元数据 / 封面图都在文件属性里 |
| Foobar 等可用 | 老牌播放器天然支持 |
| Windows 原生 | 不依赖 WSL |

## 媒体

![](https://pbs.twimg.com/media/HNJsYcTbcAAFMFb.jpg)

## 参考链接

- [项目仓库](https://github.com/louislam/navifsp)

## 相关概念

- [Navidrome 音乐生态](./tool-orca-music-player.md) — 同作者 louislam 在 Navidrome 音乐服务器领域的另一工具,生态相关
- [Billi/LX Music Electron](./tool-bili-music-electron.md) — 其他把云端音乐接入本地场景的工具样本
