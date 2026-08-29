---
type: Tool
title: "FFmpegFreeUI（Windows 免费 FFmpeg 图形外壳）"
description: "为 Windows 进阶用户做的免费 FFmpeg 交互外壳：不必手敲命令行也能灵活完成视频压制与格式转换，界面专业美观。"
resource: "https://github.com/Lake1059/FFmpegFreeUI"
tags: [windows, ffmpeg, video-transcoding, gui, free, media]
timestamp: "2026-08-29T21:30:00Z"
---

# FFmpegFreeUI（Windows 免费 FFmpeg 图形外壳）

## 它是什么

[Lake1059/FFmpegFreeUI](https://github.com/Lake1059/FFmpegFreeUI) 是面向 Windows 进阶用户的**FFmpeg 交互外壳**：把命令行 FFmpeg 包成一个**专业、美观、免费的 GUI**，用户不必手敲参数也能完成视频压制与格式转换。

定位：

- 比命令行 FFmpeg 友好（图形界面 + 模板）；
- 比付费转码工具（Hindenburg / Movavi / Adobe Encoder）轻量；
- 比同类免费 GUI 更「**进阶**」——保留对编码参数的细粒度控制。

## 为什么用它 / 适合什么场景

- 想用 FFmpeg 的能力但记不住 `-c:v libx264 -crf 18 -preset slow` 之类参数；
- 经常要把视频在 H.264 / H.265 / VP9 / AV1 之间转换；
- 不想为专业转码软件付订阅费，又对市面免费 GUI 的简陋界面 / 功能阉割不满意；
- 做短视频 / 自媒体 / 教学视频批量压制。

## 关键能力

| 能力 | 说明 |
|------|------|
| FFmpeg 引擎 | 直接调用系统安装的 FFmpeg / 静态版本 |
| 图形外壳 | 命令行参数可视化为选项 / 表单 |
| 视频压制 | 支持常见编码器（x264 / x265 / libsvtav1 等） |
| 格式转换 | MP4 / MKV / MOV / WEBM 等互转 |
| 免费 + 专业 | 无功能阉割、无水印、无订阅 |

## 相关概念

- [kiri](./tool-kiri.md) — 桌面截图 / 标注 / OCR / 录屏四合一，录屏之后常需 FFmpegFreeUI 二次压缩
- [article-tools](./tool-article-tools.md) — 浏览器内封面 / 二维码 / MD 转公众号工具，与 FFmpegFreeUI 互补于不同阶段

## 参考链接

- 项目链接：<https://github.com/Lake1059/FFmpegFreeUI>
- 原始推文：<https://x.com/QingQ77/status/2093600035195810102>
- 媒体：<https://pbs.twimg.com/media/HQ0MpTmb0AEu14r.jpg>