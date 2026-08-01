---
type: Tool
title: "go2rtc"
description: "AlexxIT/go2rtc，超轻量、零依赖、Go 单二进制的摄像头流媒体服务器：RTSP/WebRTC/RTMP/HLS/HomeKit 协议互通，0.5 秒内延时，可对接 Home Assistant / Frigate，能跑在树莓派上。"
resource: "https://github.com/AlexxIT/go2rtc"
tags: "[go, camera, rtsp, webrtc, home-assistant, frigate, self-hosted, iot]"
timestamp: "2026-08-01T20:30:00Z"
---

# go2rtc

## 它是什么

[`AlexxIT/go2rtc`](https://github.com/AlexxIT/go2rtc) 是一个**超轻量、零依赖、单文件二进制**的摄像头流媒体服务器，用 Go 写成。它把家用监控摄像头常见的协议壁垒打穿——同一路摄像头可以同时被 RTSP / WebRTC / RTMP / HLS / HomeKit 客户端访问，且延时可压到 **0.5 秒以内**。

## 解决什么痛点

- 摄像头延时高（走云端就 1-3 秒起跳）
- 跨平台推流卡顿
- 多种协议不兼容（米家 / Wyze / 萤石 / 海康 RTSP 各自一套）
- 智能家居平台（Home Assistant / Frigate）集成繁琐

## 核心卖点

| 卖点 | 说明 |
|------|------|
| 零延迟推流 | RTSP → WebRTC / MSE，延时压到 < 0.5 秒 |
| 协议万能 | RTSP / RTMP / WebRTC / HomeKit / HLS 全互通 |
| 双向语音对讲 | 支持小米 / Wyze 等多品牌摄像头反向音频 |
| 无缝集成 | 直接对接 Home Assistant、Frigate，自带 FFmpeg 按需转码 |
| 私有化 | 完全本地运行，不走云端，隐私可控 |
| 极轻量 | 单二进制文件，资源占用低，可跑在树莓派 |

## 适合什么场景

- 家里有多品牌监控摄像头（米家 / Wyze / 萤石 / RTSP 摄像头）想统一一个 App 看
- 想在 Home Assistant / Frigate 里调用摄像头，但原生协议不通
- 需要把摄像头延时压到亚秒级（看猫、看宠物、对讲）
- 不想把家庭摄像头视频流送上云

## 与同类工具的差异

| 工具 | 形态 | 差异 |
|------|------|------|
| [Streamflix](./tool-streamflix.md) | 客户端 | Android TV / 手机侧的流媒体聚合客户端 |
| [go2rtc] | 服务端 | 摄像头侧协议转换 + 延时压缩 |

## 媒体

![go2rtc 项目截图](https://pbs.twimg.com/media/HOm5_7JaIAA37ZU.png)

## 原始链接

- [项目仓库](https://github.com/AlexxIT/go2rtc)
- [原始推文](https://x.com/Wen_Zw/status/2083492227406574024)

## 相关概念

- [Streamflix](./tool-streamflix.md) — 终端侧的流媒体聚合客户端，go2rtc 是它适合接入的「协议适配服务端」