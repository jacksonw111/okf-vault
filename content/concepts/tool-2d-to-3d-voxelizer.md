---
type: Tool
title: "2D-to-3D Voxelizer"
description: "把 2D 像素画转换成 3D 体素（voxel）艺术并导出 .obj 文件的桌面工具，支持单张精灵图或 4/6 面精灵图生成完整 3D 模型"
resource: "https://github.com/GazPrash/2d-to-3d-voxelizer"
tags: [voxel, 3d, pixel-art, obj, sprite, game-asset]
timestamp: 2026-08-17T16:00:00Z
---

# 2D-to-3D Voxelizer

## 它是什么

`GazPrash/2d-to-3d-voxelizer` 是一个**桌面工具**：把 2D 像素画（精灵图 / sprite sheet）**升维**为 3D 体素（voxel）模型并导出标准 `.obj` 文件。支持两种输入：
- **单张精灵图**：直接拉伸 / 挤出成 3D 体。
- **4 / 6 面精灵图**：根据多视角图（顶 / 底 / 前 / 后 / 左 / 右）还原更准确的 3D 形状。

输出可直接导入 Blender、Unity、Three.js 等 3D 工具继续编辑。

## 为什么用它 / 适合什么场景

- 像素美术师想快速把作品**立体化**做素材。
- 游戏开发者要做**复古体素风**关卡原型。
- 想用 .obj 通用格式把像素艺术塞进 3D 引擎。
- 想保留原像素「颗粒感」的体素效果，而不是平滑多边形。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单图输入 | 单张精灵图挤出 3D |
| 多视角输入 | 4 / 6 面精灵图还原更准的体素结构 |
| .obj 导出 | 通用 3D 格式，主流引擎 / 软件通用 |
| 保留颗粒感 | 体素化不抹平，像素艺术风格延续 |
| 桌面端运行 | 本地处理，无需上传 |

## 媒体

- ![](https://pbs.twimg.com/media/HPwhW2lboAAO8fL.jpg)

## 原始链接

- [项目仓库](https://github.com/GazPrash/2d-to-3d-voxelizer)

## 相关概念

- [Solar Wanderer](./tool-solar-wanderer.md) — 同样用体素 / 像素风做 3D 实时可视化（Three.js）