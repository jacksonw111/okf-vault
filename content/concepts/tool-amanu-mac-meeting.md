---
type: "Tool"
title: "amanu（Mac 会议自动记录器）"
description: "在 macOS 上自动录制 Zoom、Google Meet 等在线会议，盯麦克风占用触发开录 / 挂断自动停，不装虚拟声卡、不碰内核扩展；生成带说话人的文字记录和总结。"
resource: "https://github.com/gsamat/amanu"
tags: "[macos, meeting, transcription, automation, microphone, oss]"
timestamp: "2026-09-16T16:09:00Z"
---

# amanu（Mac 会议自动记录器）

## 它是什么

[gsamat/amanu](https://github.com/gsamat/amanu) 是一款 **macOS 上的开源会议自动记录器**。它盯着麦克风占用自动开录、通话挂断自动停，**不往会议里派机器人**、不装虚拟声卡、不碰内核扩展。录制完成后产出带说话人标记的文字记录与总结。Zoom、Meet、Telegram 这类通话都支持。

## 为什么用它 / 适合什么场景

- 不想让 Bot 加入会议被对方察觉。
- 想免去手动开 / 停录音的仪式感，自动捕获整段对话。
- 对隐私 / 系统洁净度敏感，不愿装驱动或内核扩展。
- 需要后续把会议内容整理成可检索的文字纪要。

## 关键能力

| 能力 | 说明 |
|------|------|
| 麦克风占用触发 | 通话开始自动录，挂断自动停 |
| 无 Bot 参会 | 仅录本机麦克风，对方无感 |
| 多客户端兼容 | Zoom / Meet / Telegram 等通话通用 |
| 无虚拟声卡 / 内核扩展 | 系统洁净，无副作用风险 |
| 说话人分离 | 输出文字记录带说话人标记 |
| 自动总结 | 会议结束后产出可阅读总结 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTq2YUbYAAFX1P.png)

## 相关概念

- [Toolknit Desktop](./tool-toolknit-desktop.md) — 同类 macOS 本机自动化思路