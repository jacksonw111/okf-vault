---
type: Tool
title: "sunshine-send"
description: "diduweiwu/sunshine-send / 阳光快传，Android TV 端基于 NanoHTTPD 的局域网文件快传：开应用就生成二维码 + 上传页面，手机扫码 / 电脑浏览器直传文件，不限格式，免 U 盘免配置。"
resource: "https://github.com/diduweiwu/sunshine-send"
tags: "[android-tv, lan, file-transfer, qrcode, nanohttpd, no-cloud]"
timestamp: "2026-08-01T20:30:00Z"
---

# sunshine-send

## 它是什么

[`diduweiwu/sunshine-send`](https://github.com/diduweiwu/sunshine-send)（阳光快传）是一个跑在 **Android TV** 上的轻量局域网文件快传工具。它用 NanoHTTPD 在电视本地起一个 HTTP 服务，启动就生成**二维码 + 上传页面**，手机扫码或电脑浏览器打开就能传文件，**不限格式**。

## 解决什么痛点

- 想把下载好的电影 / 字幕传到电视，传统流程：插 U 盘 → 拷文件 → 插电视 → 文件管理器打开
- 各种云盘限速、上传隐私文件有顾虑
- 智能电视没法装客户端，但有浏览器就行

## 使用流程

1. 电视装 App 并启动（侧载 APK 也可）
2. 屏幕显示二维码 + IP，手机扫码 / 电脑浏览器打开页面
3. 拖文件或选文件 → 直接传到电视
4. 不限文件类型（视频 / APK / 字幕 / 文档等）

## 核心特性

| 特性 | 说明 |
|------|------|
| 零配置 | 启动即用，不需要登录、不需要云账号 |
| 局域网传输 | 不走公网，速度 = 内网带宽，隐私有保障 |
| 跨端 | 手机 / 电脑 / 平板只要有浏览器就行 |
| 不限格式 | 视频 / APK / 字幕 / 图片 / 文档都行 |
| 极轻量 | NanoHTTPD 是嵌入式 HTTP server，App 体积小 |

## 适合什么场景

- 家里有 Android 电视 / 电视盒子，想频繁传文件过去
- 不想用 U 盘 / 不想用云盘
- 临时给电视装个 APK（侧载应用场景）

## 媒体

![sunshine-send 截图](https://pbs.twimg.com/media/HOhYq75bwAAuIRH.jpg)

## 原始链接

- [项目仓库](https://github.com/diduweiwu/sunshine-send)
- [原始推文](https://x.com/QingQ77/status/2083436062014062593)