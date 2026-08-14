---
type: "Tool"
title: "gfty"
description: "rkana-org 开源的 CLI 工具：用代码定义并批量生成可自定义的 Gridfinity 收纳盒 / 底板 / 可拆标签 / 边框模型，并对接 Onshape API 自动导出 STEP 文件，省去逐个手搓 3D 打印标签。"
resource: "https://github.com/rkana-org/gfty"
tags: ["3d-printing", "gridfinity", "cli", "onshape", "step", "open-source"]
timestamp: "2026-08-14T19:50:00Z"
---

# gfty

## 它是什么
gfty 是给 Gridfinity 收纳系统爱好者的批量生成 CLI。用户用代码定义收纳盒 / 底板 / 可拆标签 / 边框模型的几何与尺寸，gfty 一次性生成大量变体；并对接 Onshape API，自动把模型导出为 STEP 文件，供下游 CAD / CAM 流程使用。

## 为什么用它 / 适合什么场景
- Gridfinity 收纳盒常用在工位 / 工具间整理，大量相同尺寸不同用途的盒子 / 标签手工画非常耗时。
- 适合「上百个格子、上千个标签」规模的工位整理项目。
- 已有 Onshape 账号的工程团队 / 创客空间可用 gfty 直接把模型导出到工程 CAD 流程。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入 | 代码定义（CLI） |
| 产物 | 收纳盒 / 底板 / 可拆标签 / 边框 |
| 导出 | 对接 Onshape API 输出 STEP |
| 适合 | Gridfinity 大规模批量整理 |
| 形态 | CLI |

## 媒体

效果示例：![效果示例](https://pbs.twimg.com/media/HPkbMJlaYAA7tLY.jpg)

## 相关概念
- [3DPrint Asset Manager](./tool-3dprint-asset-manager.md) — 3D 打印资产管理工具，与 gfty 同样面向 3D 打印工作流
