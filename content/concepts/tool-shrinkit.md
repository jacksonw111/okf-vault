---
type: "Tool"
title: "Shrinkit（macOS 屏幕录制压缩 / 加速）"
description: "macOS 屏幕录制的 .mov 常有几百 MB，PR 或 Slack 根本塞不进去。Shrinkit 用 ffmpeg 把录制压缩再加速，丢进文件夹或右键一下，回来就是体积小、可直接粘贴的 .mp4。"
tags: "[macos, ffmpeg, video, screen-recording, automation]"
timestamp: "2026-08-15T08:19:00Z"
resource: "https://github.com/noxend/shrinkit"
---

# Shrinkit（macOS 屏幕录制压缩 / 加速）

## 它是什么

`noxend/shrinkit` 是 macOS 上一键压缩屏幕录制的小工具。它解决一个非常具体的痛点：macOS 自带录屏产出的 `.mov` 文件动辄几百 MB，PR / Slack / Discord 等都上传困难。Shrinkit 用 ffmpeg 把这些录制**重新编码 + 必要时加速**，丢进文件夹或右键一下，返回一个体积小、可直接粘贴的 `.mp4`。

> 视频演示：
> [原始链接](https://video.twimg.com/amplify_video/2088088124236972032/vid/avc1/2940x2030/9TiZxC9oNccn6x97.mp4)

## 为什么用它 / 适合什么场景

- **录屏分享**：要做 bug 复现 / 教程分享 / Slack 演示，但文件太大塞不进去。
- **批量压缩**：一批老录屏想瘦身归档。
- **可选加速**：1× 太啰嗦的视频，可以选 2× / 4× 加速节省时间。

## 关键能力

| 能力 | 说明 |
|------|------|
| ffmpeg 重新编码 | 选合适 codec（默认 H.264）压到 MB 级 |
| 加速选项 | 可设 1× / 2× / 4× 等倍数 |
| 触发方式 | 拖入文件夹 / 右键菜单均可触发 |
| 输出 `.mp4` | 兼容 PR / Slack / Discord / 各类 IM |
| 保留可读性 | 默认 CRF 在「画质 / 体积」之间取平衡 |
| 批量 | 多文件一次处理 |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| FFmpeg 命令行 | 手动跑命令 | 灵活但需记参数 |
| HandBrake | GUI 转码器 | 通用视频转码，非专门针对录屏 |
| **Shrinkit** | **录屏专用 + 自动化触发** | 拖一下就完成 |

## 适用人群

- 经常录屏分享 bug / 教程的 macOS 用户。
- 想给录屏瘦身的团队（PR review、Slack 沟通）。
- 不愿意记 ffmpeg 命令的人。

## 参考链接

- [项目链接](https://github.com/noxend/shrinkit)

## 相关概念

- [claude-real-video](tool-claude-real-video.md) — Python 工具，按场景变化 + 字幕智能抽帧让 AI 真正看懂视频
- [autoshorts](tool-autoshorts.md) — Tauri 2 长视频 / 音频转竖屏短视频 + AI 选爆款段