---
type: "Term"
title: "MapLibre GL"
description: "开源的矢量地图渲染引擎——fork 自 Mapbox GL JS v1.13（Mapbox 闭源前的最后一个开源版本），支持 WebGL 加速矢量瓦片 / 3D 建筑 / 自定义样式（MapLibre Style）；是当下自托管 / 隐私友好地图的事实渲染底座。"
resource: "https://maplibre.org"
tags: "[maplibre, map, webgl, vector-tiles, open-source]"
timestamp: "2026-10-06T22:51:00Z"
---

# MapLibre GL

## 定义

**MapLibre GL** 是开源的矢量地图渲染引擎——**fork 自 Mapbox GL JS v1.13**（Mapbox 切换到非开源许可前的最后一个开源 commit），由 MapLibre 社区维护。支持 WebGL 加速矢量瓦片渲染、3D 建筑 / 等距线框 / 自定义样式（MapLibre Style Spec），与 Mapbox GL JS API 高度兼容。是当下自托管 / 隐私友好 / 不锁定 Mapbox 场景下地图渲染的事实底座。

## 要点

- **官网**：[maplibre.org](https://maplibre.org)
- **底层**：WebGL；渲染瓦片为矢量而非栅格
- **数据源**：可消费 OpenStreetMap、Protomaps、自托管 PMTiles、自定义 GeoJSON
- **生态**：
  - **MapLibre GL JS**：浏览器 SDK
  - **MapLibre Native**：iOS / Android / Qt 嵌入
  - **MapLibre Style Spec**：与 Mapbox 兼容的样式规范
- **典型项目**：[`tool-hk-traffic-intelligence`](tool-hk-traffic-intelligence.md)（香港智慧城市交通看板）

## 相关概念

- [Cloudflare Workers](./term-cloudflare-workers.md) — 常作为 MapLibre 服务的部署底座
