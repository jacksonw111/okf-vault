---
type: "Term"
title: "3D Floor Plan（3D 户型图）"
description: "把传统 2D 平面户型图渲染成可在浏览器里旋转 / 缩放 / 漫游的 3D 场景——常用 three.js / Babylon.js + GLTF / IFC；用于自建房规划、家居摆放预览、智能家居集成可视化（如 Home Assistant 的 NeonPlan3D 集成）。"
resource: "https://en.wikipedia.org/wiki/Floor_plan"
tags: "[3d-floor-plan, home, architecture, threejs, webgl]"
timestamp: "2026-10-06T22:51:00Z"
---

# 3D Floor Plan（3D 户型图）

## 定义

**3D 户型图**是把传统 2D 平面户型图升级为**可在浏览器内旋转 / 缩放 / 漫游**的 3D 场景的形态——常用 `three.js` / `Babylon.js` + GLTF / IFC / OBJ 模型；用于自建房规划、家居摆放预览、装修方案对比，以及智能家居集成（如 Home Assistant 仪表盘里嵌入设备位置）。

## 要点

- **渲染栈**：`three.js` + WebGL / WebGPU，常见辅助库 `react-three-fiber` / `babylon.js`
- **数据源**：手画 SVG → 拉伸成墙体的 extrude 流程；或用 IFC / Revit / SketchUp 导出 GLTF
- **典型项目**：
  - [`tool-neonplan3d`](tool-neonplan3d.md) — Home Assistant 集成
  - [`tool-house-planner`](tool-house-planner.md) — 自建房规划
- **场景**：装修预览、设备位置可视化、户型分享

## 相关概念

- [Home Assistant](./term-home-assistant.md) — NeonPlan3D 集成宿主
- [House Planner](./tool-house-planner.md) — 同领域自建房工具
