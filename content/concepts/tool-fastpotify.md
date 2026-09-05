---
type: Tool
title: "FastPotify"
description: "Rust 原生 Spotify 客户端，解决官方桌面版内存占用高、启动慢的问题，保留本地播放与 Spotify Connect 控制"
resource: "https://github.com/crmne/fastpotify"
tags: [spotify, client, rust, native, music]
timestamp: 2026-09-05T15:00:00Z
---

# FastPotify

## 它是什么
`crmne/fastpotify` 是一款**Rust 写的 Spotify 原生客户端**，目标是对抗官方桌面版「内存占用高 + 启动慢」两大痛点，同时保留**本地播放能力**与对 **Spotify Connect** 的控制能力。

## 为什么用它 / 适合什么场景
- 官方 Spotify 桌面客户端太重（Electron / Chromium 拖慢老机器）时，换 FastPotify 拿同等体验。
- 想在低功耗笔记本 / 树莓派 / 旧设备上跑 Spotify。
- 喜欢 Rust 原生客户端的「秒开 + 低内存」体感。

## 关键能力
| 能力 | 说明 |
|------|------|
| Rust 原生 | 单二进制、低内存、启动快 |
| 本地播放 | 直接在客户端播放音乐 |
| Spotify Connect | 可作为 Connect 设备被其他端点控制 |
| 轻量替代 | 替换官方臃肿客户端 |

## 媒体
- ![](https://pbs.twimg.com/media/HRWTvSia4AA85iD.jpg)

## 相关概念
- [原始链接](https://github.com/crmne/fastpotify)