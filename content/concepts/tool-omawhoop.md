---
type: Tool
title: "omawhoop (NathanRGagnon/omawhoop)"
description: "把 WHOOP 健康数据（strain / recovery / 睡眠）挂到 Omarchy 桌面状态栏，直接顶栏看数据，省得掏手机"
resource: "https://github.com/NathanRGagnon/omawhoop"
tags: [linux, omarchy, whoop, health, waybar, status-bar]
timestamp: 2026-08-20T08:03:00Z
---

# omawhoop (NathanRGagnon/omawhoop)

## 它是什么
[`NathanRGagnon/omawhoop`](https://github.com/NathanRGagnon/omawhoop) 是 **Omarchy 桌面**的状态栏扩展，把 **WHOOP** 健身手环的关键指标挂到 **Waybar** 顶栏：扫一眼就看到当天的 **strain**（训练负荷），点开面板可看到更细分的 **recovery / 睡眠** 等指标，**不必再掏手机**。

## 为什么用它 / 适合什么场景
- 用 WHOOP 但日常在 Linux 工作，希望桌面也能直接看到健康曲线。
- 想把"训练 / 恢复 / 睡眠"作为顶栏里持续可见的提醒。
- 希望健康数据进入"可工作场景"而非锁在手机 App 里。

## 关键能力
| 能力 | 说明 |
|------|------|
| Strain 顶栏直显 | 不打开面板也知道今天训练多累 |
| Recovery 详情 | 点开看身体恢复评分 |
| 睡眠指标 | 点开看睡眠阶段、时长 |
| Waybar 集成 | 与 Omarchy 桌面顶栏无缝整合 |
| 不掏手机 | 所有读数都在桌面，避免频繁解锁手机 |

## 媒体
- ![omawhoop 截图](https://pbs.twimg.com/media/HQDNMC8b0AAXfEn.png)

## 相关概念
- [项目仓库](https://github.com/NathanRGagnon/omawhoop) — 仓库主页
- [omarchy-pod](./tool-omarchy-pod.md) — 同样挂在 Omarchy 状态栏的另一扩展（显示 AirPods 状态）
