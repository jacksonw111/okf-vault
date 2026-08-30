---
type: "Tool"
title: "polkadot.sh（极简 SVG 占位图生成器）"
description: "零依赖、纯客户端的 SVG 占位图生成器：拼 URL 参数即可指定尺寸、点阵图案、配色、文字，输出可直接用 `<img>` 引用的可缓存 SVG。"
resource: "https://polkadot.sh/"
tags: [placeholder, svg, image-generator, frontend, design]
timestamp: "2026-08-30T21:50:00Z"
---

# polkadot.sh

## 它是什么
[polkadot.sh](https://polkadot.sh/) 是一个**极简的 SVG 占位图生成器**——零依赖、纯客户端运行，把尺寸、点阵图案、配色、文字拼到 URL 参数里就返回一个可以直接放进 `<img src="...">` 的可缓存 SVG 文件。

典型用例：

- 唱片封面占位（点阵图案「波点」直接呼应名字 `polkadot`）；
- 设计稿里的占位卡片（指定宽高 + 配色，截图就够用）；
- 演示数据 / mock UI 不想用 `placeholder.com` 的同质化灰块；
- 任何需要「**比纯灰块多一点设计感**」的占位场景。

## 为什么用它 / 适合什么场景
- 比 `placeholder.com` / `placehold.co` 多一层视觉质感（点阵 / 自定义色）；
- 纯客户端、零依赖、可静态部署在自己域名下；
- URL 直接描述成品，方便 Figma / 设计稿里反向追溯；
- 想要「**没有品牌水印**」的开源占位方案。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零依赖 | 纯 SVG 输出，浏览器 / CDN 即可 |
| URL 参数化 | 尺寸 / 图案 / 配色 / 文字都在 URL 里 |
| 静态缓存 | 输出文件可被 CDN / 浏览器永久缓存 |
| 可自托管 | 开源、可放自己域名下（避免第三方域名污染） |

## 相关概念
- [Pigo](tool-pigo.md) — 另一种「把功能压进单一 URL」的极简工具思路

## 参考链接
- 项目链接：<https://polkadot.sh/>
