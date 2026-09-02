---
type: Tool
title: "Microduck Replica（机器鸭复刻研究）"
description: "对官方不开源硬件的 Microduck 做第三方复刻研究：靠公开的 MJCF 模型和 47 个 STL 网格反推整套装配图、CAD 装配体和电控方案。"
resource: "https://github.com/fanhao375/microduck-replica"
tags: [microduck, robotics, hardware-reverse-engineering, cad, openhardware]
timestamp: 2026-09-02T12:00:00Z
---

# Microduck Replica（机器鸭复刻研究）

## 它是什么

[Pollen Robotics 的 Microduck](./tool-microduck.md) 官方只开源软件，硬件 BOM / CAD / 装配文档全部缺失。`microduck-replica` 是第三方复刻研究：作者利用 `microduck_rl` 仓库里自带的 MJCF 模型与 47 个 STL 网格反推整机装配关系（精度 0.1mm），最终交付 7 张装配 / 爆炸图、15 个按刚体分组的 CAD 装配体——直接导入 FreeCAD / Fusion 360 即可看到装好的整机。电控方案也做了对应复刻。

## 关键能力

| 能力 | 说明 |
|------|------|
| 0.1mm 装配精度 | 基于 MJCF + STL 反推，整机装配关系可被 CAD 软件识别 |
| 7 张装配 / 爆炸图 | 直观展示整机结构 |
| 15 个刚体分组装配体 | 按刚体分组便于单独编辑单个零件 |
| FreeCAD / Fusion 360 直接打开 | 不需要专用 CAD 工具 |

## 项目链接

- [项目主页](https://github.com/fanhao375/microduck-replica)
- [Microduck 官方开源仓库](https://github.com/pollen-robotics/microduck)

## 相关概念

- [Microduck（开源机器鸭）](./tool-microduck.md) — 官方开源软件部分
