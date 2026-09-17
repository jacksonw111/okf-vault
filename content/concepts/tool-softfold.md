---
type: "Tool"
title: "Softfold（MacBook 合盖过渡动画）"
description: "ReffWu 开发的 macOS 工具，让屏幕内容跟着转轴角度实时折叠 / 模糊 / 变暗，给 MacBook 合盖加一段物理感过渡动画。"
resource: "https://github.com/ReffWu/softfold"
tags: "[macos, macbook, hinge-animation, transition, fold, ux-micro-detail]"
timestamp: "2026-09-17T14:41:00Z"
---

# Softfold（MacBook 合盖过渡动画）

## 它是什么

[ReffWu/softfold](https://github.com/ReffWu/softfold) 是 **ReffWu** 开发的 macOS 工具。它读取 MacBook 转轴角度传感器数据，**让屏幕内容跟着合盖动作实时折叠、模糊、变暗**——给原本生硬的「合盖 → 黑屏」加一段有物理感的过渡动画。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时折叠 | 屏幕内容随转轴角度变化做 3D 折叠变形 |
| 模糊 / 变暗 | 合盖过程中同步加模糊和亮度衰减，模拟离焦效果 |
| 转轴驱动 | 数据来自本机传感器，不需要手动触发 |
| 轻量常驻 | 后台运行但不耗电、不打扰工作 |

## 适合什么场景

- 想给 MacBook 加上「个性化开机仪式感」的桌面玩家。
- 研究 macOS 传感器接入 + Metal / CoreAnimation 做视觉过渡的开发者（项目是「读传感器 → 实时渲染」模式的样板）。
- 喜欢 micro-interaction / 动效细节的设计 / 工程从业者。

## 参考

- 项目链接：<https://github.com/ReffWu/softfold>

![preview](https://pbs.twimg.com/media/HSY56oAbkAAzxhx.jpg)
