---
type: "Tool"
title: "Diction（iOS 语音键盘网关）"
description: "DictionLabs 开源：给 iOS 做了一块语音键盘，在任意 App 里按住麦克风说话，文字直接落进光标位置；开源的是网关（Go 服务），iOS 键盘 App 闭源上架 App Store。"
resource: "https://github.com/DictionLabs/Diction"
tags: "[ios, voice-keyboard, speech-to-text, self-hosted, golang]"
timestamp: "2026-10-07T04:32:00Z"
---

# Diction（iOS 语音键盘网关）

## 它是什么

[Diction](https://github.com/DictionLabs/Diction) 是 **DictionLabs** 开源的 **iOS 语音键盘网关**——给 iOS 做了一块语音键盘，在任意 App 里按住麦克风说话，文字直接落进光标位置。

开源出来的是 **网关部分**（Go 写的服务），**iOS 键盘 App 本身闭源上架 App Store**。语音转写后端可以放在自己服务器上。

## 为什么用它 / 适合什么场景

- **iOS 用户** 在任何 App 里都想要语音转写
- **隐私敏感**：转写后端可以放自己服务器，不走云 API
- **跨 App 通用**：不绑特定 App，键盘替换系统键盘即可
- **移动办公**：开车 / 走路 / 做饭时只能语音的场景

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | iOS 自定义键盘 + 网关服务 |
| 触发 | 按住麦克风说话 |
| 输出 | 文字直接落进光标 |
| 通用性 | 任意 App 可用 |
| 网关 | Go 写，开源 |
| 后端 | 可自托管 |
| iOS App | 闭源，App Store 上架 |

## 参考链接

- 项目仓库：<https://github.com/DictionLabs/Diction>

## 媒体

- ![](https://pbs.twimg.com/media/HT7JAbrawAAWWX9.jpg)

## 相关概念

无相关概念需要链入。
