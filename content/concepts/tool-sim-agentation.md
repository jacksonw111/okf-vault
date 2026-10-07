---
type: "Tool"
title: "SimAgentation（iOS 模拟器浏览器标注 + Agent）"
description: "lcandy2 开源：把正在运行的 iOS 模拟器画面搬到浏览器里做标注，再把元素信息和截图交给编码 Agent 去改代码——点元素或拖框选中，写下要改什么。"
resource: "https://github.com/lcandy2/sim-agentation"
tags: "[ios-simulator, annotation, coding-agent, element-selection, screenshot]"
timestamp: "2026-10-07T11:27:00Z"
---

# SimAgentation

## 它是什么

[SimAgentation](https://github.com/lcandy2/sim-agentation) 是 **lcandy2** 开源的 **iOS 模拟器浏览器标注 + Agent 协作工具**——把正在运行的 **iOS 模拟器画面搬到浏览器** 里做标注，再把元素信息和截图交给编码 Agent 去改代码。

具体做法：
- 冻结模拟器画面到浏览器
- **点元素** 或 **拖框选中**
- 写下「要改什么」
- Agent 收到的是：**元素**、**所在界面**、**能在源码里搜到的字符串**、**加红框的全屏图 + 特写图** 两张截图

## 为什么用它 / 适合什么场景

- **iOS App 开发**：手画红框写反馈比写 issue 文字描述快
- **Coding Agent 协作**：结构化的标注 + 元素信息让 Agent 直接定位代码
- **设计 / 开发沟通**：截图上画框比文字描述准确
- **替代人工贴图 + 文字反馈**：直接出可机读的标注结构

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | 浏览器标注界面 |
| 数据源 | 正在运行的 iOS 模拟器 |
| 标注方式 | 点元素 / 拖框选中 |
| 反馈 | 文字评论 |
| Agent 输入 | 元素 + 界面 + 可搜字符串 + 红框图 + 特写图 |
| 输出 | 模拟器源码里直接定位 |

## 参考链接

- 项目仓库：<https://github.com/lcandy2/sim-agentation>

## 媒体

- ![](https://pbs.twimg.com/media/HUAEAkmaUAA2zDl.jpg)

## 相关概念

- [EditHere](./tool-edithere.md) — 桌面端截图标注的同类思路
