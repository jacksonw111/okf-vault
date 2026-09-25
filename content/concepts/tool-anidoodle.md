---
type: "Tool"
title: "anidoodle（把插画 / 动画 / 短片写进代码）"
description: "anidoodle 把插画、动画和短片写进代码——同一份源码在不同机器上能重复生成相同结果，也能继续导出 GIF / MP4 / APNG 或离线 HTML。"
resource: "https://github.com/alexgreensh/anidoodle"
tags: "[illustration, animation, code-as-art, deterministic, gif-export, mp4-export, apng, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# anidoodle（把插画 / 动画 / 短片写进代码）

## 它是什么

[anidoodle](https://github.com/alexgreensh/anidoodle) 是一个「**插画 / 动画 / 短片 = 代码**」的项目——把视觉作品用代码描述出来：

- **同一份源码**在不同机器、不同时间能**重复生成相同结果**（确定性）
- 渲染完之后可以**继续导出**为 **GIF / MP4 / APNG**，或者**离线 HTML**（自包含单文件）

## 为什么用它 / 适合什么场景

- 想要**版本化的视觉资产**——插画、加载动画、片头短片用代码写，能 diff、能 review、能回滚，不会再丢 PSD 源文件。
- 团队里**没人会用 After Effects / Blender**，但有人会写 Python / JS——直接把动效当成代码资产管。
- 想做**可重复的实验素材**（论文 / 报告 / 网站插图），需要「同一份代码 = 同一份成片」的稳定性。
- 想交付**离线 HTML 单文件**（如品牌动效、宣传页、内嵌插画），不依赖 CDN / 在线工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 源码即产物（code-as-art） |
| 一致性 | 同一份代码跨机器 / 跨时间结果一致 |
| 导出 | GIF / MP4 / APNG / 离线 HTML |
| 适用 | 插画 / 动画 / 短片 |
| 协作 | 像代码一样 diff / review / 版本管理 |

## 媒体

![](https://pbs.twimg.com/media/HTBnq7GbMAA8tTI.jpg)

## 相关概念

- [Toolcraft](./tool-toolcraft.md) — pixel-point 出的创意类应用 starter kit（canvas + 工具栏 + 拾色器），anidoodle 偏向「静态 / 动效资产」一侧
- [anidoodle 同类项目](./tool-printfilm.md) — 剧本 → 分镜 → 生图 → 生视频 → 成片一体化平台
