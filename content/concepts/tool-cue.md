---
type: "Tool"
title: "cue（Blueturboguy07/cue）"
description: "开源 macOS AI 副驾，浮动在屏幕上，能「看」屏幕内容、「听」会议音频；屏幕共享时自动隐藏，避免把敏感画面泄漏给对端。"
tags: "[macos, ai-copilot, screen-awareness, audio, privacy, floating-window]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/Blueturboguy07/cue"
---

# cue（Blueturboguy07/cue）

## 它是什么

[`cue`](https://github.com/Blueturboguy07/cue) 是 Blueturboguy07 开源的 macOS AI 副驾，**以「悬浮窗」形态常驻在屏幕上**：

- 能「看」屏幕：抓取屏幕内容作为上下文；
- 能「听」：拾取会议 / 系统音频，让 AI 实时理解；
- **屏幕共享时自动隐藏**——避免把敏感画面 / 桌面意外泄漏给视频会议对端。

## 关键能力

| 能力 | 说明 |
|------|------|
| 浮动 UI | 永远在屏幕上方的副驾窗口 |
| 屏幕感知 | 截图 / OCR 给 AI 做上下文 |
| 音频感知 | 系统音频（会议 / 视频）作为输入 |
| 隐私护栏 | 屏幕共享时自动隐藏 |
| 本地优先 | 开源、可自部署，数据可控 |

## 适合什么场景

- 开会时希望 AI 实时帮忙做总结、记 action items；
- 屏幕共享前担心「桌面有未完成的工作 / 隐私窗口」的人；
- 想做一个「始终在场」的桌面 AI 副驾，但拒绝云端 SaaS。

## 参考链接

- [原始链接](https://github.com/Blueturboguy07/cue)

## 相关概念

- [Cabinet](tool-cabinet.md) — 同样是「AI + 桌面常驻」的思路；Cabinet 偏 Obsidian / 第二大脑，cue 偏 macOS 系统级副驾
- [forkd](tool-forkd.md) / [clawk](tool-clawk.md) — cue 跑在本机，Agent 操作本机时同样需要沙箱边界；forkd/clawk 给的是隔离层