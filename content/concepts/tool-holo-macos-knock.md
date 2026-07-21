---
type: Tool
title: "Holo（macOS 桌面敲击识别）"
description: "实验性的 macOS 原生工具：把 MacBook 周围桌面划分成四个可分配的敲击区域，通过内置麦克风采集声音、本地识别敲击位置并触发对应动作。"
resource: "https://github.com/JustinGamer191/Holo"
tags: [macos, audio, knock-detection, ml, experimental]
timestamp: "2026-07-21T01:15:00Z"
---

# Holo（macOS 桌面敲击识别）

## 它是什么
[Holo](https://github.com/JustinGamer191/Holo) 是一款 **实验性的 macOS 原生工具**：把 MacBook 周围的物理桌面划分成 **四个可分配的敲击区域**，用内置麦克风采集声音、**本地识别**敲击位置，再触发对应动作（比如切歌 / 启动 App / 跑脚本）。属于「物理空间 + 声音信号 + 本地模型」三者结合的探索型交互。

## 为什么用它 / 适合什么场景
- 想给厨房 / 工作台 / 演讲场景找一个「不用摸键盘也能触发操作」的物理手势。
- 喜欢尝试「声音 → 位置 → 动作」这种非传统输入范式。
- 跑演示 / 做播客 / 做直播，需要物理空间里的「轻量开关」。

## 关键能力
| 能力 | 说明 |
|------|------|
| 四区识别 | 把桌面划分为四个敲击区域 |
| 麦克风采集 | 用内置麦，不需要额外硬件 |
| 本地识别 | 推断在哪个区域敲击 |
| 触发动作 | 每区绑定一项快捷操作 |
| macOS 原生 | 与系统集成顺畅 |

## 相关概念
- [StrokeMouse](tool-strokemouse.md) — macOS 鼠标手势自定义工具（同样是「物理动作触发动作」的 macOS 输入范式）

## 参考链接
- 项目链接: <https://github.com/JustinGamer191/Holo>
