---
type: "Term"
title: "WebRTC"
description: "Web Real-Time Communication：浏览器原生支持的实时音视频与数据通道协议，无需插件即可在浏览器间建立 P2P 连接。"
resource: "https://webrtc.org/"
tags: [webrtc, web-standard, p2p, real-time, browser]
timestamp: "2026-08-08T20:00:00Z"
---

# WebRTC

## 定义

WebRTC（Web Real-Time Communication）是 W3C / IETF 推动的浏览器原生实时通信协议，让浏览器无需插件即可建立点对点（P2P）连接，承载音视频通话、低延迟数据传输等场景。

## 要点

- 浏览器原生支持，Chrome / Firefox / Safari / Edge 全覆盖。
- 通过 STUN / TURN 解决 NAT 穿透，建立 P2P。
- 内置 DTLS-SRTP，端到端加密。
- 主要 API：`RTCPeerConnection` / `RTCDataChannel` / `getUserMedia`。
- 与 WebSocket 不同：WebRTC 是真正的 P2P（数据不流过中转服务器，除非用 TURN）。

## 适用场景

- 视频会议（Google Meet / Zoom Web 都基于 WebRTC）。
- 文件 / 数据 P2P 传输（如 WebChat 这类站点临时聊天室）。
- 远程桌面 / 屏幕共享。
- 实时游戏 / 协作工具。

## 相关概念

- [WebChat](./tool-webchat.md) — 用 WebRTC DataChannel 做站点临时聊天室的浏览器扩展