---
type: "Tool"
title: "Bendable（MacBook 盖子角度驱动折叠动画）"
description: "把 MacBook 开合盖板的物理动作变成屏幕上的实时折叠动画，由盖子角度传感器逐帧驱动。"
resource: "https://github.com/opensourcevillain/Bendable"
tags: "[macos, animation, sensor, macbook, playful]"
timestamp: "2026-09-13T00:02:00Z"
---

# Bendable（MacBook 盖子角度驱动折叠动画）

## 它是什么

[opensourcevillain/Bendable](https://github.com/opensourcevillain/Bendable) 是一个 macOS 小工具：**读取 MacBook 盖子角度传感器的数据**，把开合盖板的物理动作映射成屏幕上**实时折叠动画**——盖子开合多大，屏幕内容就折多少。

## 为什么用它 / 适合什么场景

- 想做有趣的桌面动效演示 / 屏幕装饰。
- 调试或演示**柔性屏/折叠屏 UI** 概念，借助真实物理输入驱动。
- 单纯觉得「笔记本盖子像翻书一样翻屏」好玩。

## 关键能力

| 能力 | 说明 |
|------|------|
| 传感器读取 | 调用 MacBook 盖子角度传感器 |
| 实时折叠动画 | 屏幕内容随开合角度变形 |
| 逐帧驱动 | 不抽样，连续平滑 |

## 媒体

- ![](https://pbs.twimg.com/media/HR-zJOJbkAAmNfR.jpg)

## 项目链接

- 仓库：<https://github.com/opensourcevillain/Bendable>