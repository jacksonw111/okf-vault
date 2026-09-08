---
type: Tool
title: "design-os-3d-blender"
description: "面向 3D 打印的 AI agent 工作流：让 AI agent 在 Blender 5.2 里按规范建出尺寸正确、可直接打印的真实零件，对接打印生产环节。"
resource: "https://github.com/jangtrinh/design-os-3d-blender"
tags: [blender, 3d-printing, ai-agent, cad]
timestamp: "2026-09-08T00:00:00Z"
---

# design-os-3d-blender

## 它是什么
design-os-3d-blender 是 jangtrinh 开源的**面向 3D 打印的 AI agent 工作流**：让 AI agent 在 Blender 5.2 里按规范建出尺寸正确、可直接打印的真实零件，与打印生产环节对接。

## 为什么用它 / 适合什么场景
- 想让 LLM 帮自己设计可打印零件，而非只能看不能造的"视觉模型"。
- 想用 Blender 当 CAD 后端，借 AI agent 提速概念→可制造文件的链路。
- DIY / 创客场景：批量生成连接件、外壳、夹具。

## 关键能力
| 能力 | 说明 |
|------|------|
| Blender 5.2 集成 | 复用 Blender 作为 3D 内核 |
| 打印规范 | 输出满足尺寸/壁厚等打印约束 |
| AI agent 驱动 | 由 LLM agent 生成几何 |
| 生产对接 | 直通打印环节 |

## 参考
- 原始链接：<https://github.com/jangtrinh/design-os-3d-blender>

## 媒体
- ![](https://pbs.twimg.com/media/HRqICzUbkAAjugL.jpg)

## 相关概念
- [Blender](https://www.blender.org/) — 3D 内容创作套件
- [FreeCAD](https://www.freecad.org/) — 开源参数化 CAD
