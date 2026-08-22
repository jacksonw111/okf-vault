---
type: "Tool"
title: "GPUI Component"
description: "Longbridge 开源的 GPUI Rust UI 组件库，配合 WASM 编译可在浏览器运行；DataTable 演示加载 100 万行仍保持流畅，是 GPUI 性能标杆之一。"
resource: "https://longbridge.github.io/gpui-component/"
tags: ["rust", "gpui", "ui", "wasm", "datatable", "open-source"]
timestamp: "2026-08-14T19:50:00Z"
---

# GPUI Component

## 它是什么
GPUI Component 是 Longbridge 开源的 Rust UI 组件库，基于 GPUI（Zed 编辑器同款 UI 框架）。除了桌面原生运行，它还可以编译到 WASM 跑在浏览器上，让 Rust UI 代码同时服务桌面与 Web 端。Demo 中 DataTable 一次性装入 100 万行仍能流畅滚动，是 GPUI 渲染性能的典型展示。

## 为什么用它 / 适合什么场景
- 想用 Rust 写高密度数据表格 / 复杂 UI，又希望能在浏览器里直接试运行。
- GPUI 本身偏 Zed 内部使用，包装成组件库后让外部项目可直接复用。
- 适合金融终端、监控大屏、表格密集型工具类应用。

## Design Guides（设计指引）
[longbridge.github.io/gpui-component/docs/design-guides](https://longbridge.github.io/gpui-component/docs/design-guides) 把 GPUI Component 的设计语言沉淀成一份给「人 + AI」共用的 Design Guides——不仅服务于 GPUI 应用本身，也可作为其他 Rust UI 项目在组件排布、色彩、交互一致性上的参考模板，让 AI 编码代理直接按规范生成合规界面。

## 关键能力
| 能力 | 说明 |
|------|------|
| 底层框架 | GPUI（Rust 原生 UI） |
| 运行目标 | 桌面原生 + 浏览器（WASM） |
| DataTable Demo | 100 万行流畅滚动 |
| 组件形态 | 长桥（Longbridge）开源组件库 |
| 适用 | 金融 / 监控 / 表格密集型工具 |

## 媒体

性能演示视频：[参考视频](https://video.twimg.com/amplify_video/2087930303365230592/vid/avc1/1072x720/HUlpxgSQR98HbwrC.mp4?tag=14)

## 相关概念
- [Toolcraft](./tool-toolcraft.md) — pixel-point 的创意类应用 starter kit，与 GPUI Component 都在「工具类 UI 模板」范畴
- [Pi-Livecraft](./tool-pi-livecraft.md) — 给 Pi 终端 AI 助手套一个随时能被模型改的 React 网页界面，另一种「AI 友好 UI」思路
