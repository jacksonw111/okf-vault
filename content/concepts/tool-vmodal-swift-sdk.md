---
type: "Tool"
title: "VModal Swift SDK（iOS / macOS 视频语义搜索）"
description: "想在 iOS 或 macOS App 里搜索视频内容，又不想自己搭向量库和 ML 流水线，VModal Swift SDK 把上传、索引、按语义或画面文字找片段封成强类型接口，开发者只管自己的界面。"
resource: "https://github.com/v-modal/vmodal_sdk_swift_iphoneduo"
tags: "[swift, ios, macos, video-search, sdk, semantic-search]"
timestamp: "2026-09-21T22:00:00Z"
---

# VModal Swift SDK

## 它是什么

[v-modal/vmodal_sdk_swift_iphoneduo](https://github.com/v-modal/vmodal_sdk_swift_iphoneduo) 是面向 **iOS / macOS** 的视频内容搜索 Swift 包——把**上传、索引、按语义或画面文字找片段**这几步封装成**强类型接口**。

## 解决的问题

- App 想加视频内容搜索，过去要自己搭**向量库 + ML 流水线**。
- 想做**按语义找片段**（"找露天的画面"）和**按画面文字找片段**（"找出现 'Sale' 字样的镜头"），都得自己训多模态模型。

## 它提供的能力

| 能力 | 说明 |
|------|------|
| 上传 | SDK 内置客户端上传视频 |
| 索引 | 服务端自动建索引 |
| 语义搜索 | 按自然语言描述找片段 |
| 画面文字搜索 | 按画面中的文字（OCR / ASR）找片段 |
| 强类型接口 | Swift 原生类型，无字符串魔法 |

## 为什么用它 / 适合什么场景

- 做**视频剪辑 / 二次创作 App**需要素材检索。
- 做**教学 / 课程类 App**需要按关键词定位视频片段。
- 想跳过自建向量库 + 多模态流水线的成本，直接拿 SDK 用。

## 关键能力

| 能力 | 说明 |
|------|------|
| Swift SDK | iOS / macOS 原生集成 |
| 强类型 API | 编译期发现错误 |
| 多模态搜索 | 语义 + 画面文字两种入口 |
| 后端托管 | 上传 / 索引 / 检索都由 VModal 平台完成 |

## 项目链接

- 仓库：<https://github.com/v-modal/vmodal_sdk_swift_iphoneduo>

## 媒体

![](https://pbs.twimg.com/media/HSoc2gca4AAxJka.jpg)

## 相关概念
