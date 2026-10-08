---
type: "Tool"
title: "CADCraft（纯 Rust 写的开源 CAD）"
description: "storytold 出品：用纯 Rust 从零写了一套开源 CAD 制图应用，命令行提示、对象捕捉、极轴、正交、grips、右键重复都按 AutoCAD 老规矩来；兼容 DXF / DWG，并让 Agent 通过 MCP 和 CLI 驱动它画图。"
resource: "https://github.com/storytold/cadcraft"
tags: "[cad, rust, open-source, autocad, dxf, dwg, mcp, agent]"
timestamp: "2026-10-08T23:50:00Z"
---

# CADCraft

## 它是什么

[CADCraft](https://github.com/storytold/cadcraft) 是 storytold 团队用**纯 Rust** 从零写的**开源 CAD 制图应用**：

- 命令行提示、对象捕捉、极轴、正交、grips、右键重复……都按 **AutoCAD 的老规矩**做
- 兼容 **DXF / DWG** 文件格式
- 让 **Agent 通过 MCP 和 CLI** 驱动它画图

定位是「为懂 AutoCAD 的工程师 + 让 Agent 能调用的开源 CAD」。

## 为什么用它 / 适合什么场景

- **AutoCAD 老用户**：习惯命令行 / 对象捕捉 / grips 的人
- **不想给 AutoCAD 月费**：开源 + 可商用
- **Agent 友好**：可由 AI 自动出工程图
- **DXF / DWG 兼容**：能读老工程图

## 关键能力

| 能力 | 说明 |
| ------ | ------ |
| 引擎 | Rust 写的纯本地引擎 |
| 命令行模式 | 沿用 AutoCAD 的命令行交互范式 |
| 对象捕捉 | endpoint / midpoint / intersection 等 |
| 极轴 / 正交 | 角度 / 垂直水平辅助 |
| Grips | 拖动对象夹点编辑 |
| DXF / DWG | 兼容主流 CAD 文件格式 |
| MCP / CLI | Agent 可调用出图 |
| 跨平台 | Rust 二进制，可移植 |

## 参考链接

- 项目链接：<https://github.com/storytold/cadcraft>

## 媒体

![](https://pbs.twimg.com/media/HUE_XgAa0AAMp7C.jpg)

## 相关概念

- [EffectCraft](./tool-effectcraft.md) — 同作者 storytold 的另一款 Rust 写的「AE 替代」
- [Lightcraft](./tool-lightcraft.md) — 同作者的「Lightroom 替代」
- [VectorCraft](./tool-vectorcraft.md) — 同作者的「Illustrator 替代」
- [WordCraft](./tool-wordcraft.md) — 同作者的「Word 替代」
- [SoundCraft](./tool-soundcraft.md) — 同作者的「Pro Tools 替代」