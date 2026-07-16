---
type: "Tool"
title: "hermes-ui（przbadu/hermes-ui）"
description: "把 Hermes 桌面客户端的渲染层抽出来,做成可在浏览器打开、也能装成 PWA 的网页版 UI,连到本机或远程 Hermes 网关使用。"
resource: "https://github.com/przbadu/hermes-ui"
tags: "[hermes, pwa, web-ui, agent-client, browser-extension]"
timestamp: "2026-07-16T07:25:00Z"
---

# hermes-ui

[hermes-ui](https://github.com/przbadu/hermes-ui) 把 **[Hermes 桌面客户端](./tool-hermes-desktop.md)** 的渲染层拆出来,做成「浏览器直开 + 可装 PWA」的 Web 版 UI——既能丢桌面运行,也能塞进浏览器标签,连到本机或远程的 Hermes 网关使用。

## 它解决了什么

Hermes 桌面客户端用着顺手,但有时用户希望在手机平板 / 另一台电脑上也能用——又不想为每个端单独打包一份客户端。hermes-ui 把渲染/交互层做成 PWA,装到桌面看起来跟本地应用一样;在浏览器里则零安装打开就用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器即开 | 静态站点,直接在浏览器访问即可 |
| PWA 安装 | 可「添加到主屏」当本地 App 用,iOS / Android / 桌面均可 |
| 复用 Hermes 网关 | 接本机 / 远程 Hermes 服务,无重复协议实现 |
| 客户端兼容 | 与原生 Hermes Desktop 客户端体验一致 |

## 媒体

视频：

- <https://video.twimg.com/amplify_video/2076946249685876736/vid/avc1/3006x1766/ByhZDJctK9hNblOP.mp4?tag=28>

## 参考链接

- [项目仓库](https://github.com/przbadu/hermes-ui)

## 相关概念

- [Hermes Desktop](./tool-hermes-desktop.md) — 同生态的桌面客户端,本工具是其「Web 化」分流
- [HermitUI](./tool-hermitui.md) — 同样把应用层只做成单文件的极简 UI 思路,与本工具并列参考
