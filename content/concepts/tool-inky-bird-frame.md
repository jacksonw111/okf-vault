---
type: "Tool"
title: "inky-bird-frame（veteranbv/inky-bird-frame）"
description: "把附近近期观测或检测到的鸟类, 以插画式田野日志图版的形式展示在 Pimoroni Inky 彩色电子纸显示屏上的项目, 由「控制器」发现鸟情并用 Codex 生成/审核图版, 「显示节点」在树莓派上轮播已审核图版。"
resource: "https://github.com/veteranbv/inky-bird-frame"
tags: "[e-ink, raspberry-pi, birding, illustration, hardware, agent-creative]"
timestamp: "2026-07-17T04:40:00Z"
---

# inky-bird-frame

[inky-bird-frame](https://github.com/veteranbv/inky-bird-frame) 是一个「**给观鸟者看的数字画框**」：把附近近期观测或检测到的鸟类, 以**插画式田野日志**图版的形式, 推到 [Pimoroni Inky](https://shop.pimoroni.com/) 这类**彩色电子纸显示屏**上挂着。整套系统由两个角色协调：

| 角色 | 职责 |
|------|------|
| **控制器 (controller)** | 抓观测数据 (eBird / 摄像头) → 用 Codex 生成插画图版 → 自己审核后再发布 |
| **显示节点 (display)** | 一台树莓派接 Inky 屏, 定时拉已审核图版轮播 |

## 为什么不用 LCD 屏

LCD 常亮常换电; **电子纸耗电极低** + 没有背光, 适合做「挂在墙上画框, 偶尔更换画作」的场景。代价是**刷屏慢 (几秒一帧)**, 所以图像由 Codex 一次性生成 + 审核后才推送, 而不是实时。

## 关键能力

| 能力 | 说明 |
|------|------|
| 图版生成 | Codex 按鸟种 / 时间 / 地点生成插画式田野日志图版 |
| 自动审核 | 控制器自己审图, 通过的才下发 |
| 多节点轮播 | 一台「画框」接 Inky 屏, 可拉多张图版 |
| 离线友好 | 电子纸 + 本地缓存, 完全离线依旧能展示 |

## 媒体

![](https://pbs.twimg.com/media/HNRPed6bgAEDffw.jpg)
![](https://pbs.twimg.com/media/HNRPfdFa0AAXBnl.jpg)

## 参考链接

- [项目仓库](https://github.com/veteranbv/inky-bird-frame)
