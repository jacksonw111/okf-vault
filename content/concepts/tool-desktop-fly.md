---
type: Tool
title: "desktop-fly（macOS 桌面上的真果蝇）"
description: "用 FlyWire 真实果蝇脑图谱的突触数据跑脉冲仿真，把一只 3D 果蝇放到 macOS 桌面上：走路、理毛、睡觉、躲光标等动作均由同一套真实神经元回路决定。"
resource: "https://github.com/DenisSergeevitch/desktop-fly"
tags: [neuroscience, simulation, desktop, fun, three-d, flywire]
timestamp: 2026-08-21T05:16:00Z
---

# desktop-fly（macOS 桌面上的真果蝇）

## 它是什么
desktop-fly 是一款桌面常驻应用，把 FlyWire 项目公开的真实果蝇全脑连接组（connectome）数据，用脉冲神经网络（spiking neural network）跑一遍仿真，得到一只完全由真实神经元回路驱动的桌面 3D 果蝇。它会走、会理毛、会睡觉，会主动躲开你的鼠标光标——行为不是脚本动画，而是连接组电活动外化后的结果。

## 为什么用它 / 适合什么场景
- 想在桌面上养一只「不费电、不拉屎、不会逃出屏幕」的电子宠物。
- 计算神经科学 / 神经形态计算爱好者想要的可视化 demo：连接组 → 行为 的最小可行示例。
- 想要一个「不联网、不写日志、只会按神经回路反应」的本地桌面常驻彩蛋。

## 关键能力
| 能力 | 说明 |
|------|------|
| FlyWire 真实连接组 | 数据源是真果蝇全脑突触图谱，不是随机生成的虚拟网络 |
| Spiking 仿真 | 神经元以脉冲形式相互作用，行为是电活动涌现结果 |
| macOS 桌面常驻 | 桌面级 3D 渲染，与鼠标 / 时钟 / 其他窗口共存 |
| 自发行为 | 走路 / 理毛 / 睡觉 / 避光标，无显式脚本 |
| 本地运行 | 不联网，数据与计算均在本机 |

## 一句话总结
**把真实果蝇全脑连接组跑成一只会自己走路理毛的桌面 3D 果蝇——神经回路就是它的行为程序。**

## 原始链接
- [DenisSergeevitch/desktop-fly](https://github.com/DenisSergeevitch/desktop-fly) — 原始仓库

## 媒体
- ![果蝇在桌面](https://pbs.twimg.com/media/HQIZsidboAABnnX.png)
- ![果蝇行为](https://pbs.twimg.com/media/HQIZtSmaMAAafF8.png)

## 相关概念
- [Heartmorrow](./concepts/tool-heartmorrow.md) — 同样把「神经 / 心智模型」做成桌面常驻应用