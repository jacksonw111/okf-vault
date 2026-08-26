---
type: "Tool"
title: "Paperlab"
description: "在网页上模拟「真实纸张」的交互画布：可输入、可折叠、可抓角掀起；纸张不可伸缩，文字随页面弯折而非折痕处断裂；基于 three.js + greensock 实现。"
tags: "[paper, web, threejs, greensock, canvas, animation]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://paperlab.nawwara.studio"
---

# Paperlab

## 它是什么

[`Paperlab`](https://paperlab.nawwara.studio) 是一个浏览器内的「网页版纸张」交互画布，作者 NourMtir 把内部项目的工具花了六周沉淀成单独的库开源：纸张可输入、可折叠、可用鼠标抓住边角掀起，**纸张本身不可伸缩**，所以文字随页面弯折而不是在折痕处断裂。

技术栈使用 [`three.js`](https://threejs.org) + [`greensock`](https://greensock.com/gsap/)。

## 为什么用它

- 不像传统 HTML 文本流那样「平的」——纸张是真实的几何体
- 文字随纸张形状形变（mesh 跟随纸张顶点），所以折叠、起角时内容是跟着变形的
- 「撕页 / 折页」等物理直观交互替代滚动 / 切换按钮的常见范式
- 用 two month 的内部工具沉淀成库，作者表示内部项目对其反应强烈

## 关键能力

| 能力 | 说明 |
|------|------|
| 真纸张交互 | 折叠、抓角掀起、撕页 |
| 文字跟随纸张形变 | 文字随网格弯曲，不在折痕处断裂 |
| three.js + greensock | 3D 网格 + 时间轴动效双栈 |
| 浏览器原生运行 | 免安装，开页即用 |
| MIT 开源 | 可嵌入自有产品 |

## 演示 / 媒体

- [演示视频](https://video.twimg.com/amplify_video/2092298919661441024/vid/avc1/3024x1900/sFgDKd4JyzzzPQk4.mp4?tag=29) — 作者录的纸张交互示例
- [线上体验](https://paperlab.nawwara.studio)

## 参考链接

- [项目链接](https://paperlab.nawwara.studio)
- [源码仓库](https://github.com/NourMtir0722/Paperlab)
