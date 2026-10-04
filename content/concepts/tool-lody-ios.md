---
type: "Tool"
title: "Innei/lody-ios（Lody 的 iOS 客户端）"
description: "Innei 出品的 Lody 社区 iOS 客户端：用 React Native + 自定义 Swift 模块 LodyKit 混合架构，让 iPhone / iPad 用户在移动端接入远程 Lody 服务，进行编码代理聊天 / 代码 diff / 远程工作区浏览。"
resource: "https://github.com/Innei/lody-ios"
tags: "[ios, react-native, swift, lody, code-agent, mobile]"
timestamp: "2026-10-04T10:30:00Z"
---

# lody-ios

## 它是什么

[lody-ios](https://github.com/Innei/lody-ios) 是 **Innei** 出品的 **Lody iOS 客户端**——Lody 官方没有 iOS 客户端，这个项目用一周时间把 React Native + 自定义 Swift 模块 `LodyKit` 的混合架构跑成了 TestFlight 可装的 Beta（要 iOS 26 以上）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 聊天 | 接入远程 Lody 服务，进行编码代理会话聊天 |
| 代码 diff | 在手机上直接看 diff |
| 文件浏览 | 远程工作区浏览 |
| 架构 | React Native（业务层）+ 自定义 Swift 模块 LodyKit（原生层） |
| 系统要求 | iOS 26+ |

## 与官方 Lody 的关系

| 维度 | 官方 Lody | lody-ios |
|------|----------|----------|
| 平台 | 桌面 / 网页 / CLI | iOS / iPadOS |
| 维护方 | Lody 官方 | Innei（社区） |
| 架构 | 原生 | RN + Swift 混合 |

## 适合场景

- 在外用 iPhone 想继续跟桌面 Lody 上的编码代理对话
- iPad 作为副屏看代码 diff

## 参考链接

- 项目链接：<https://github.com/Innei/lody-ios>

## 相关概念

- [Lody 本身](./tool-lody.md) — 桌面 / 团队版 Lody（不同侧重）