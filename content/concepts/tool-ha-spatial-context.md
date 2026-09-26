---
type: "Tool"
title: "ha-spatial-context（Home Assistant 空间上下文：把楼层平面图变成设备地图）"
description: "Greminn 开源的 Home Assistant 自定义组件：把楼层平面图转换为带真实比例、设备位置和无线连接关系的空间地图，让 AI 助手与其他自动化程序获得「家庭物理位置」信息。"
resource: "https://github.com/Greminn/ha-spatial-context"
tags: "[home-assistant, spatial-context, floor-plan, smart-home, ai-context, open-source]"
timestamp: "2026-09-26T21:55:00Z"
---

# ha-spatial-context（Home Assistant 空间上下文：把楼层平面图变成设备地图）

## 它是什么

[ha-spatial-context](https://github.com/Greminn/ha-spatial-context) 是 Greminn 开源的 **Home Assistant 自定义组件**——把 **Home Assistant 里的楼层平面图**转换为**带真实比例 + 设备位置 + 无线连接关系**的「空间地图」，让 AI 助手和其他自动化程序获得「**家庭物理位置**」信息。

## 关键能力

- 每个楼层可放**背景图**
- **校准真实尺寸**
- 画**房间 / 墙体**
- 添加**门窗** + **设备**
- 标注**无线连接关系**（设备 ↔ 设备 / 设备 ↔ 网关）

## 为什么用它 / 适合什么场景

- 智能家居自动化只靠**设备名 / 房间名**不够——AI 助手需要**真实位置**才好做调度（例：「离窗户近的灯先关」「这个设备被这堵墙挡住了，信号弱」）。
- 装修 / 搬家后想**重建空间 + 设备拓扑**的可视化记录。
- 跑**室内定位 / 跟随人员**类自动化（设备在哪儿、人在哪儿）。
- 给 Agent 一个**「物理世界 + 数字世界」的统一上下文层**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Home Assistant 自定义组件 |
| 输入 | 楼层平面图 + 设备清单 |
| 输出 | 带真实比例 + 拓扑的「空间地图」 |
| 信息 | 比例 / 设备位置 / 门窗 / 无线连接 |
| 用途 | 给 AI 助手 / 自动化程序提供空间上下文 |

## 媒体

- ![](https://pbs.twimg.com/media/HTETcFuaUAAP8vj.jpg)

## 相关概念

- [Self-Hosted（自托管）](./term-self-hosted.md) — Home Assistant = 经典自托管场景
- [Home Assistant 平台相关工具](./tool-homeassistant.md) — 同生态工具参考