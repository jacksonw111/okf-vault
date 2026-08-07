---
type: "Tool"
title: "WebChat"
description: "把任意网页临时变成公共聊天室的去中心化浏览器扩展：访客安装后访问同一站点即可匿名搭话，消息走 WebRTC 端到端加密的点对点通道，不经过中心服务器。"
resource: "https://github.com/molvqingtai/WebChat"
tags: [webrtc, browser-extension, decentralized-chat, p2p, privacy]
timestamp: "2026-08-07T01:27:00Z"
---

# WebChat

## 它是什么

WebChat 是一款浏览器扩展，把任意已加载的网页临时变成该站点访客之间的公共聊天室。访问同一 URL 的人装上扩展后即可匿名搭话，消息沿 WebRTC 端到端加密的点对点线路流动，无中心服务器、无需注册账号，所有内容只留在各自设备上。

## 为什么用它 / 适合什么场景

- 临时性、强语境、低频次的小群体讨论（同一篇文章 / 工具页 / GitHub PR 的共同访客）。
- 不希望聊天内容被第三方留存或可审查的场景。
- 想用同一网页作为「话题上下文」载体，访客进入页面就自动进入话题。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一站一聊天室 | 同一域名/URL 自动构成一个聊天空间，进入页面即加入 |
| WebRTC P2P | 消息通过浏览器原生 WebRTC 直连，加密通道，无中转服务器 |
| 零账号 / 零安装态 | 浏览器扩展本身是唯一客户端状态，刷新即重置匿名身份 |
| 浮动幽灵图标 | 每个网站右下角浮出可点击图标，唤起对应站点的聊天面板 |
| 内容本地化 | 聊天记录只存在访客本地设备，关闭标签页即丢失 |

## 媒体

- 演示视频：<https://video.twimg.com/amplify_video/2084904125196816384/vid/avc1/1736x1080/bRUwkgSn3g06iI1c.mp4?tag=29>

## 相关概念

- [WebRTC](./term-webrtc.md) — 提供端到端加密点对点通道的浏览器原生协议（本概念的核心依赖）
- [Briar](./tool-briar.md) — 类似定位的去中心化 Android 聊天应用，做对比参考