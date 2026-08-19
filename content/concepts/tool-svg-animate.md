---
type: Tool
title: "svg_animate（Treamz/svg_animate）"
description: "Flutter 库：直接用 flutter_svg 的渲染器把 SVG 自带的 SMIL / CSS 动画跑起来，不必再转 Lottie 或引入 JS 运行时"
resource: "https://github.com/Treamz/svg_animate"
tags: "[flutter, svg, animation, smil, lottie-alternative]"
timestamp: "2026-08-19T16:00:00Z"
---

# svg_animate（Treamz/svg_animate）

## 它是什么
[`Treamz/svg_animate`](https://github.com/Treamz/svg_animate) 是一个 Flutter 库：在 Flutter 里要播放**带动画的 SVG**，一般要么转 Lottie（重画动画），要么引 JS 运行时（成本高），而 svg_animate 直接复用 `flutter_svg` 的渲染器把 SVG 自带的 **SMIL / CSS 动画**跑起来——零额外转换、零 JS 运行时。

## 为什么用它 / 适合什么场景
- 设计师交付的是带 SMIL / CSS 动画的 SVG，不想为 Flutter 重画成 Lottie。
- 想要「SVG 一份 → 多端一致」（Web / Flutter 都用同一份素材）。
- 包体积敏感：不愿为了一套动画图引整套 Lottie 运行时。

## 关键能力
| 能力 | 说明 |
|------|------|
| 复用 flutter_svg 渲染器 | 无新渲染层，直接调用现有 SVG 渲染能力 |
| 支持 SMIL / CSS 动画 | SVG 自带的两类动画声明都识别 |
| 无 JS 运行时 | 纯 Dart 端实现，跨平台一致 |
| 不必再转 Lottie | 一份 SVG 即可在 Web / Flutter 复用 |

## 媒体
- ![svg_animate 截图](https://pbs.twimg.com/media/HP-pJFJa4AAlCsR.png)

## 相关概念
- [项目仓库](https://github.com/Treamz/svg_animate) — 仓库主页