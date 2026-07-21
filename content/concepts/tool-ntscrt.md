---
type: Tool
title: "NTSCRT（Mac NTSC/VHS + CRT 模拟器）"
description: "macOS 原生工具：让图片或视频先经过真实模拟的 NTSC / VHS 信号退化（复合噪点、磁带噪声、磁头切换），再叠一层 RetroArch CRT 着色器，呈现老电视播放的质感。"
resource: "https://github.com/finnmckenty/NTSCRT"
tags: [macos, video, retro, ntsc, vhs, crt, shader]
timestamp: "2026-07-21T13:51:00Z"
---

# NTSCRT（Mac NTSC/VHS + CRT 模拟器）

## 它是什么
[NTSCRT](https://github.com/finnmckenty/NTSCRT) 是一款 macOS 原生工具：把现代图片 / 视频 **先经过真实模拟的 NTSC / VHS 信号退化**——复合噪点、磁带噪声、磁头切换——**再叠一层 RetroArch 的 CRT 着色器**，最终输出「老电视在放」的复古质感。不只是套滤镜，而是分两阶段做「信号损伤 + 显像管渲染」。

## 为什么用它 / 适合什么场景
- 给短视频 / MV / 演示做 80/90 年代美学的复古后处理。
- 想做出「不是单纯加噪点」的 NTSC / VHS 风格，而要信号级真实感。
- 在 Mac 上想要一个原生工具而非命令行 ffmpeg 拼滤镜。

## 关键能力
| 能力 | 说明 |
|------|------|
| NTSC 退化 | 复合编码层面的噪点、色度串扰、扫描线 |
| VHS 退化 | 磁带噪声、磁头切换、色彩偏移 |
| RetroArch CRT 着色器 | 模拟显像管成像（光晕 / 扫描线 / 边缘失真） |
| 两阶段叠加 | 信号损伤 + 显像管渲染分别独立调节 |
| macOS 原生 | 与系统相册 / 视频工作流衔接顺畅 |

## 相关概念
- [Kling 3 电影级画面](note-kling-3-cinematic.md) — 视频生成侧的画质讨论（与本工具形成「生成 + 后期」两侧对照）

## 参考链接
- 项目链接: <https://github.com/finnmckenty/NTSCRT>
- 预览截图: ![NTSCRT 截图](https://pbs.twimg.com/media/HNoq2wAa0AANl8J.jpg)
