---
type: "Tool"
title: "geo-sleuth（用 OpenStreetMap 反推照片拍摄地点）"
description: "给 Agent 一张照片，靠 OpenStreetMap 几何、高程天际线、卫星影像与街景反推拍摄点，返回相机坐标、误差半径、朝向与卫星证据图。"
resource: "https://github.com/Oldcircle/geo-sleuth"
tags: "[geo, openstreetmap, image-geolocation, elevation, sky-line, agent-tool]"
timestamp: "2026-09-21T22:00:00Z"
---

# geo-sleuth

## 它是什么

[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth) 给 Agent 一张照片，**反推拍摄地点与角度**——不用联网调用商业地理位置 API，纯靠开源地理数据自行推理。

## 它怎么推

| 数据源 | 用途 |
|--------|------|
| OpenStreetMap 几何 | 街道走向、建筑轮廓、路口拓扑 |
| 高程天际线 | 由 DEM/DSM 推出画面中可见的山脊 / 天际剪影 |
| 卫星影像 | 与地面目标物（建筑、路口、地块形状）做视觉匹配 |
| 街景 | 当 OSM 信息不足时作为辅助证据 |

## 输出

- 相机坐标
- 误差半径
- 镜头朝向
- 卫星证据图（哪一块卫星图与画面匹配）

## 为什么用它 / 适合什么场景

- Agent 拿到一张照片，需要告诉用户「这大概在哪拍的」「朝向哪里」。
- 不想付商业 geolocation API（如 Google 的 find-face-in-photos）调用费。
- 想跑**离线 / 私有**场景，数据走 OSM 与公开影像。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多数据源融合 | OSM 几何 + 高程 + 卫星 + 街景互补 |
| 输出结构化 | 坐标 / 误差 / 朝向 / 证据图齐全 |
| Agent 可调用 | 接口面向 Agent，不是给人用的 GUI |
| 全开源 | 不依赖商业地理位置 API |

## 项目链接

- 仓库：<https://github.com/Oldcircle/geo-sleuth>

## 媒体

![](https://pbs.twimg.com/media/HStENg7aoAAiqeN.jpg)
![](https://pbs.twimg.com/media/HStEOSuasAA_1Hn.jpg)

## 相关概念
