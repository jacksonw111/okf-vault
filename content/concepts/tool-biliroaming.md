---
type: "Tool"
title: "BiliRoaming（解除 B 站番剧区域限制的 Xposed 模块）"
description: "Xposed 模块，解除哔哩哔哩客户端番剧区域限制，让大陆用户能看港澳台 / 海外限定番剧；同时附带主题自定义、评论楼层显示、缓存番剧等附加功能。"
resource: "https://github.com/Parsa307/BiliRoaming"
tags: "[bilibili, xposed, anime, region-unlock, hook, android]"
timestamp: "2026-07-08T10:25:00Z"
---

# BiliRoaming

## 它是什么

[BiliRoaming](https://github.com/Parsa307/BiliRoaming) 是一个 **Xposed 模块**，通过 hook 哔哩哔哩客户端，**解除番剧的区域播放限制**——让大陆用户可以观看原本仅限港澳台 / 东南亚地区播放的番剧。

同时附带一批「番剧观看体验优化」的附加功能。

## 关键能力

| 能力 | 说明 |
|------|------|
| 区域解锁 | 解除 B 站番剧「仅限某地区播放」限制 |
| 主题自定义 | 自定义客户端界面主题 |
| 评论楼层显示 | 让被折叠的评论楼层可见 |
| 缓存番剧 | 支持番剧下载 / 离线缓存 |
| Xposed 框架 | 需要已 root + 已装 Xposed 的 Android 设备 |

## 适用前提

- 仅 Android 平台（依赖 Xposed 框架）。
- 设备需 root + 安装 Xposed。
- 部分新版 B 站客户端需要适配 hook 点。

## 媒体

![BiliRoaming 功能预览](https://pbs.twimg.com/media/HMq47ayakAAWrvW.jpg)

## 参考链接

- [项目仓库](https://github.com/Parsa307/BiliRoaming)

## 相关概念

- [Clash Omega](./tool-clash-omega.md) — 同为「解锁 / 代理」相关工具，但走网络层
- [VLESS Bypass](./playbook-vless-bypass-telecom-qos.md) — 同为「突破地区 / 运营商限制」的玩法