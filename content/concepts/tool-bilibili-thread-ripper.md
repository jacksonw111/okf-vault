---
type: "Tool"
title: "Bilibili-thread-ripper（B 站海外并发下载插件）"
description: "给海外看 B 站卡顿的人用的 Chrome 插件，把视频分段拆成多个字节块并发下载；同时提供油猴脚本支持 Firefox 和 Safari 用户。"
resource: "https://github.com/MrTangLuyao/Bilibili-thread-ripper"
tags: "[bilibili, chrome-extension, userscript, video-download, dash, range-request, firefox, safari]"
timestamp: "2026-09-19T16:00:00Z"
---

# Bilibili-thread-ripper（B 站海外并发下载插件）

## 它是什么

[MrTangLuyao/Bilibili-thread-ripper](https://github.com/MrTangLuyao/Bilibili-thread-ripper) 是给**海外 B 站用户**用的浏览器工具——Chrome 插件形态主发，**同时提供油猴脚本支持 Firefox 和 Safari**。

0.9.x 版本**不再替换 B 站原生播放器**，只**接管底层音视频下载**：把 DASH 分段切成多个 HTTP Range **并发拉取**，再按原顺序交回播放器——所以网页上看到的还是 B 站官方界面，但底层下载是多线程并行的。

## 为什么用它 / 适合什么场景

- 在海外看 B 站**单线程下载卡顿**、又不想装第三方播放器的人。
- 跨浏览器需求：Chrome 插件 + Firefox / Safari 油猴脚本。
- 想保留 B 站原生 UI / 登录态，但底层走加速下载链路。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多 Range 并发下载 | 把 DASH 分段切成多个 Range 并发拉取 |
| 不替换播放器 | 0.9.x 后只接管底层下载，UI 仍是 B 站原生 |
| 跨浏览器 | Chrome 插件 + 油猴脚本（Firefox / Safari） |
| 海外友好 | 解决跨国链路单线程下载的卡顿问题 |

## 与相关概念的关系

- [Chrome Client Cronet](./tool-chrome-client-cronet.md) — 同为 Chrome 端网络层增强，但 chrome-client-cronet 偏通用网络栈替换，本工具专攻 B 站 DASH 多 Range 下载

## 参考

- 项目链接：<https://github.com/MrTangLuyao/Bilibili-thread-ripper>
- 原始推文：<https://x.com/QingQ77/status/2101240379299283052>