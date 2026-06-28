---
type: "Tool"
title: "beUI Animated Select"
description: "beUI 的动效 Select 组件，shadcn 风格 registry；面板从 trigger 处长出后「捏合」成独立 pill 形容器并回弹，gooey 弹簧动效，通过 `npx shadcn add @beui/select` 一键安装。"
tags: "[ui, animation, shadcn, react, select]"
timestamp: "2026-06-28T14:42:00Z"
resource: "https://beui.dev/components/motion/select"
---

# beUI Animated Select

## 它是什么

beUI Animated Select 是 beUI（一个 shadcn 风格 UI registry）推出的**动效 Select 组件**。最具辨识度的细节是「触发→面板」过渡：

> 面板从 trigger 处长出 → **捏合**成自己的 pill 形状容器 → 弹簧回弹。

动效关键词：**gooey（黏液态）** + **springy（弹簧）**。

## 安装

beUI 用 shadcn 风格的 CLI 安装：

```bash
npx shadcn add @beui/select
```

无需手改配置文件。

## 关键能力

| 能力 | 说明 |
|------|------|
| 捏合过渡（pinch-off） | 面板从 trigger 处「捏」出来成独立容器 |
| 弹簧动效 | gooey + springy 手感 |
| shadcn 兼容 | 直接 `npx shadcn add @beui/select` 装入项目 |
| 组件化 | 只引入 Select，不带无关组件 |
| Registry 生态 | 同 repo 预计会有更多动效组件 |

## 适用场景

- 想要给后台 / 工具站增加「会呼吸」的交互感
- 已有 shadcn 项目想局部升级某个组件
- 设计参考：研究 gooey + spring 的过渡细节

## 演示视频

- [演示视频](https://video.twimg.com/amplify_video/2070959118438014976/vid/avc1/2268x1472/t1DwvCVBa-uOZa9S.mp4?tag=28)
- [组件文档](https://beui.dev/components/motion/select)

## 参考链接

- [原始链接](https://x.com/Wen_Zw/status/2071242889494196237)

## 相关概念

- [transitions.dev](tool-transitions-dev.md) — 网页过渡效果精选合集，与 beUI 的「动效 Select」同源思路
- [textmotion.dev](tool-textmotion-dev.md) — 文字动效精选，与 beUI 动效语言互补
- [motion-skills](tool-motion-skills.md) — iart 发布的 50 个运动图形 Skill，UI 动效编排更系统
- [animations.dev/vocabulary](tool-animations-dev-vocabulary.md) — Emil Kowalski 的动画动作词汇表，定义「springy」「gooey」一类术语