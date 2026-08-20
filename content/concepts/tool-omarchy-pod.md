---
type: Tool
title: "omarchy-pod (thisisgm/omarchy-pod)"
description: "在 Linux 桌面（Omarchy）状态栏里挂上 AirPods 的每只耳机 + 充电盒电量、聆听模式、自适应 ANC、对话感知、单耳 ANC、入耳检测等数据"
resource: "https://github.com/thisisgm/omarchy-pod"
tags: [linux, omarchy, airpods, waybar, bluetooth, anc]
timestamp: 2026-08-20T07:20:00Z
---

# omarchy-pod (thisisgm/omarchy-pod)

## 它是什么
[`thisisgm/omarchy-pod`](https://github.com/thisisgm/omarchy-pod) 是一个面向 **Omarchy 桌面**的 **Waybar** 状态栏扩展：把 **AirPods** 的细粒度状态——左右耳 + 充电盒电量、聆听模式、自适应 ANC 等级、对话感知、单耳 ANC、入耳检测——**实时挂到顶栏**里。

## 为什么用它 / 适合什么场景
- 在 Linux 桌面（Omarchy）上用 AirPods，不想每次都进手机蓝牙界面看电量。
- 需要一目了然判断 ANC 模式、是否被对话感知临时关闭、谁在耳。
- 想统一管理耳机状态而不打开 macOS / iOS。

## 关键能力
| 能力 | 说明 |
|------|------|
| 完整电量 | 左耳 + 右耳 + 充电盒分别显示 |
| 聆听模式 | 普通 / 通透 / 降噪模式实时显示 |
| 自适应 ANC | 显示自适应等级 |
| 对话感知 | 当临时切到通透时也能看到 |
| 单耳 ANC | 区分左右耳独立降噪 |
| 入耳检测 | 是否在耳中即时报 |
| Waybar 集成 | 直接挂到状态栏面板 |

## 媒体
- ![omarchy-pod 截图](https://pbs.twimg.com/media/HQDNGqLakAAz1P4.png)

## 相关概念
- [项目仓库](https://github.com/thisisgm/omarchy-pod) — 仓库主页
- [omawhoop](./tool-omawhoop.md) — 同为 Omarchy 状态栏扩展，把 WHOOP 健康指标挂在顶栏
