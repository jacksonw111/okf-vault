---
type: "Tool"
title: "warp-lite（去掉 Warp 产品面的终端）"
description: "terzigolu 开源：把 Warp 终端里的 AI agent / 云同步 / 登录 / 遥测等产品面拆掉，只留下 block 终端本身；给不想要云绑定与厂商功能的 macOS 用户一个轻量化 Warp-like 选择。"
resource: "https://github.com/terzigolu/warp-lite"
tags: "[terminal, warp, macos, de-bloat, open-source]"
timestamp: "2026-10-06T00:35:00Z"
---

# warp-lite

## 它是什么

[warp-lite](https://github.com/terzigolu/warp-lite) 是 **terzigolu** 开源的「Warp 终端减负版」——macOS 上 Warp 终端绑了 AI agent / 云同步 / 登录 / 遥测，warp-lite 从源码里把这些**产品面拆掉**，只留下 block 终端本身。

## 关键能力

| 能力 | 说明 |
|------|------|
| Block 终端 | 保留 Warp 标志性的命令 / 输出分块 UI |
| 去云 | 关闭云同步、登录、遥测 |
| 去 AI | 不嵌入 Warp 自家的 AI agent |
| 本地优先 | 不发数据回厂商 |

## 适合场景

- 喜欢 Warp 的 block 体验但不愿被锁定到云
- 公司 / 法规不允许登录 / 同步 / 上报
- 想跑 Warp UI 但用 OpenAI / Anthropic API 自接

## 参考链接

- 项目链接：<https://github.com/terzigolu/warp-lite>

## 相关概念

- [Warp](./tool-warp.md) — 原版
- [Ghostty](./tool-ghostty.md) — 同为现代终端