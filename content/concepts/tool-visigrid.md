---
type: Tool
title: "VisiGrid（Rust 写的本地表格 / GPU 加速 Excel 平替）"
description: "Rust + GPUI 写的轻量本地表格程序：macOS / Windows / Linux 三端，冷启动约 300ms、安装包 < 30MB；所有操作走命令面板、条件格式用 =A1>100 -> warning 这类规则直接敲、134 个内置函数 + Excel 快捷键兼容。定位「为 Agent 准备的开源 Excel 平替」。"
resource: "https://github.com/VisiGrid/VisiGrid"
tags: [spreadsheet, rust, gpui, gpu, excel-alternative, local-first, agent-friendly]
timestamp: 2026-09-30T12:31:00Z
---

# VisiGrid

## 它是什么

**VisiGrid** 是 [VisiGrid](https://github.com/VisiGrid) 维护的本地表格软件：Rust 写、内核用 **GPUI** 做 GPU 渲染，三端覆盖（macOS、Windows、Linux）。安装包 < 30MB、冷启动约 300ms，形态属于「**原生 Excel 平替**」。

它做了几件和 Excel 不同的事：

- **所有操作走命令面板**：没有层层菜单，输入即执行。
- **条件格式用规则直接敲**：例如 `=A1>100 -> warning`，把规则写进单元格区域即可生效。
- **134 个内置函数 + 自动补全**。
- **Excel 快捷键兼容**：习惯 Excel 的键位可以无缝切过来。

整体定位被作者概括为「**为 Agent 准备的开源 Excel 平替**」——把表格当作可被程序化调用的本地数据引擎，而不是图形化的工作簿。

## 为什么用它 / 适合什么场景

- 想要一款**冷启动快、占用小**的本地表格软件，不想被 Excel 的体积和启动时间拖累。
- 希望表格操作可被脚本 / Agent 驱动——命令面板 + 规则直接敲降低了"程序化使用"的门槛。
- Excel 快捷键习惯想保留，但愿意放弃 Excel 的部分重量。
- 在多平台（macOS / Windows / Linux）都希望有一致的表格体验。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实现 | Rust + GPUI |
| 渲染 | GPU |
| 平台 | macOS / Windows / Linux |
| 安装包 | < 30MB |
| 冷启动 | ~300ms |
| 操作方式 | 命令面板驱动 |
| 条件格式 | 规则直接写在单元格（`=A1>100 -> warning`） |
| 内置函数 | 134 个，带补全 |
| 快捷键 | 兼容 Excel |
| 定位 | 为 Agent 设计的开源 Excel 平替 |

## 参考链接

- 仓库：<https://github.com/VisiGrid/VisiGrid>

## 媒体

- 视频：<https://video.twimg.com/amplify_video/2105153504440700928/vid/avc1/1200x720/MSKPxDcjEk6eMIAq.mp4?tag=29>

## 相关概念

- [GPUI](./term-ratatui.md) — Rust 终端 UI 框架；VisiGrid 把这种"GPU 加速 Rust UI"思路用到桌面应用