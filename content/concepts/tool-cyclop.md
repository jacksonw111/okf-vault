---
type: "Tool"
title: "Cyclop"
description: "把 MacBook 刘海变成悬停即用的工具面板：媒体控制、文件暂存架、剪贴板历史、片段、日历、离线翻译、提词器全装在里面，原生 SwiftUI 实现、不向系统申请权限。"
resource: "https://github.com/akalikbergenov/cyclop"
tags: ["macos", "swiftui", "macbook-notch", "productivity", "menu-bar", "clipboard", "translation"]
timestamp: "2026-08-12T09:22:00Z"
---

# Cyclop

[Cyclop](https://github.com/akalikbergenov/cyclop) 把 MacBook 的**刘海**从"屏幕上的缺口"变成**悬停即用的工具面板**——媒体控制、文件暂存架、剪贴板历史、片段、日历、离线翻译、提词器一应俱全，全装在刘海那块小空间里。

## 它是什么

一个 macOS 原生（SwiftUI）小工具，把刘海区域当作"动态面板"用：鼠标悬停 / 点击刘海，它在原地展开成一个工具集合，不弹独立窗口。

## 为什么用它 / 适合什么场景

- **刘海利用**：把屏幕上的"废空间"变成生产力面板。
- **常驻随手用**：媒体控制、剪贴板、片段这类高频小操作不必切应用。
- **不打扰**：悬停展开、收起回到正常屏幕，不抢注意力。
- **离线翻译**：内置离线翻译，断网也能用。
- **不申请系统权限**：隐私优先。

## 关键能力

| 能力 | 说明 |
|------|------|
| 刘海面板 | MacBook 刘海处悬停展开 |
| 媒体控制 | 播放 / 暂停 / 切歌 |
| 文件暂存架 | 临时存放拖进来的文件 |
| 剪贴板历史 | 多条历史回看 / 重粘贴 |
| 片段 | 自定义快捷文本片段 |
| 日历 | 月视图 / 事件提醒 |
| 离线翻译 | 断网可用 |
| 提词器 | 演讲 / 录制时显示台词 |
| SwiftUI 原生 | macOS 原生体验 |
| 零系统权限 | 不向系统申请额外权限 |

## 参考链接

- [项目仓库](https://github.com/akalikbergenov/cyclop)

## 相关概念

- [LaunchCorner](./tool-launchcorner.md) — macOS SwiftUI 屏幕四角启动开关，与 Cyclop 同属"屏幕边缘空间利用"思路
- [CXGPU](./tool-cxgpu.md) — 终端 GPU 监控，也属于"系统级实时仪表盘"小工具