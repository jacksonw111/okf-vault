---
type: Tool
title: "xy (Reflex)"
description: "reflex-dev/xy，Python 图表库，用 Rust 算 + WebGL2 画，从 1 万到 1 亿点都能秒出图，同时兼容声明式 API 和 matplotlib 写法。"
resource: "https://github.com/reflex-dev/xy"
tags: "[python, chart, webgl2, rust, matplotlib, large-data, dataviz]"
timestamp: "2026-08-01T20:30:00Z"
---

# xy (Reflex)

## 它是什么

[`reflex-dev/xy`](https://github.com/reflex-dev/xy) 是一个**Python 图表库**——Rust 算坐标 + WebGL2 渲染，**从 1 万点到 1 亿点都能秒出图**。同时支持**声明式 API**（类似 Plotly）和 **matplotlib 风格**两种写法，开发者不需要为了大数据量放弃熟悉的接口。

## 解决什么痛点

- Matplotlib 小数据 OK，大数据（百万点）卡死浏览器 / 内存爆
- Plotly / Bokeh 等对 100w+ 点就开始卡
- 想用现代声明式 API 但又不想放弃 matplotlib 风格

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust 计算 | 坐标计算、聚合在 Rust 端，比纯 Python 快 10-100x |
| WebGL2 渲染 | GPU 端渲染，1 亿点也能 60fps |
| 双写法 | 声明式 API + matplotlib 风格 API，老用户无迁移成本 |
| 大数据 | 1 万 → 1 亿点平滑过渡，不需要换工具 |

## 适合什么场景

- 科学计算 / 金融时间序列 / IoT 数据等需要画百万+ 散点的场景
- 想用 Python 写图但不想每次都被 matplotlib 性能瓶颈卡住
- 想给 React / Web 前端输出交互式大数据图

## 与同类工具的差异

| 工具 | 写法 | 性能 |
|------|------|------|
| Matplotlib | 命令式 | 小数据快，大数据卡 |
| Plotly | 声明式 | 中大数据 |
| Datashader | 大数据 | 栅格化，交互性弱 |
| xy (Reflex) | 双写法 | 1 万 → 1 亿点全秒出 |

## 媒体

![xy 截图](https://pbs.twimg.com/media/HOhajKgbwAEE52-.jpg)

## 原始链接

- [项目仓库](https://github.com/reflex-dev/xy)
- [原始推文](https://x.com/QingQ77/status/2083497466629120171)