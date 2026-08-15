---
type: "Tool"
title: "Celldock for Mac（QDC507 蜂窝模块客户端）"
description: "插上 QDC507 蜂窝模块，Mac 就能直接用蜂窝网收发短信、打电话、存录音，还能把连接做成 SOCKS5 代理共享出去，全程不需要浏览器中转或另装通讯软件。"
tags: "[macos, cellular-modem, sms, voice, socks5-proxy]"
timestamp: "2026-08-15T09:20:00Z"
resource: "https://github.com/celldock/celldock-for-mac"
---

# Celldock for Mac（QDC507 蜂窝模块客户端）

## 它是什么

`celldock/celldock-for-mac` 是给 macOS 用的 QDC507 蜂窝模块客户端。QDC507 是一种 USB / 雷电口蜂窝模块（类似 4G/5G 上网卡，但带 SIM 卡槽），插到 Mac 上后，Celldock 让系统**直接通过蜂窝网**：

- 收发 SMS 短信（不依赖 iMessage / 第三方 App）
- 拨打 / 接听语音电话（带录音）
- 把蜂窝连接共享为 SOCKS5 代理（其它设备可走 Mac 上网）

整个流程无需浏览器中转，也不用装微信 / FaceTime 等通讯软件。

> ![](https://pbs.twimg.com/media/HPphKWda8AADfjG.jpg)
> ![](https://pbs.twimg.com/media/HPphK1MaYAAxdor.jpg)

## 为什么用它 / 适合什么场景

- **Mac 用户的蜂窝能力**：macOS 默认不带原生短信 / 电话，Celldock 给 Mac 补齐这块。
- **做硬件测试 / 自动化**：CI、IoT 测试经常需要蜂窝链路，Celldock 直接出 SMS / 通话能力。
- **共享代理**：把蜂窝网共享成 SOCKS5，让没有 SIM 卡的设备也能上网。

## 关键能力

| 能力 | 说明 |
|------|------|
| 蜂窝短信 | 通过 QDC507 直接收发 SMS |
| 蜂窝通话 | 拨打 / 接听语音，自动录制 |
| SOCKS5 代理 | 把蜂窝链路共享给其它设备 |
| 无浏览器中转 | 数据走模块本身，不经网页 |
| 不装第三方 App | 不依赖微信 / FaceTime / iMessage |
| 录音存档 | 通话录音自动存到本地 |

## 与相关工具的差异

| 工具 | 介质 | 能力 |
|------|------|------|
| macOS Messages | Wi-Fi + iPhone 中继 | 短信 / iMessage |
| Celldock + QDC507 | 直插 Mac 的蜂窝模块 | 短信 / 通话 / 录音 / SOCKS5 |
| [HttpSMS](tool-httpsms.md) | 闲置 Android 手机 + HTTP | 把手机变成短信 API |
| **Celldock** | **Mac + 蜂窝模块** | **完整蜂窝能力 + 共享代理** |

## 适用人群

- 想给 Mac 加原生短信 / 电话能力的用户。
- 需要在 Mac 上做 SMS 自动化测试 / IoT 联调的开发者。
- 想把蜂窝网当备用网络的远程办公 / 差旅用户。

## 参考链接

- [项目链接](https://github.com/celldock/celldock-for-mac)

## 相关概念

- [HttpSMS](tool-httpsms.md) — 自托管短信网关，把闲置 Android 手机改造成 HTTP 短信 API
- [MacTools](tool-mac-tools.md) — 免费开源 macOS 菜单栏工具集