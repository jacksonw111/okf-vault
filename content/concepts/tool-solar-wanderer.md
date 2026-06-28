---
type: "Tool"
title: "Solar Wanderer（浏览器内实时太阳系 3D 模拟器）"
description: "基于 Three.js + WebGL2 的浏览器实时太阳系 3D 模拟器，所有行星位置按 NASA JPL 星历计算（精度 ≤0.074°），从太阳表面到 10 万 AU 外的奥尔特云无缝缩放，gzip 后仅约 200 KB。"
tags: "[three-js, webgl2, solar-system, browser, nasa-jpl]"
timestamp: "2026-06-28T12:31:00Z"
resource: "https://github.com/hyqzz/Solar-Wanderer"
---

# Solar Wanderer（浏览器内实时太阳系 3D 模拟器）

## 它是什么

Solar Wanderer 是个**纯浏览器**运行的实时太阳系 3D 模拟器，基于 **Three.js + WebGL2**。所有行星位置按 **NASA JPL 星历**计算（精度 ≤0.074°），从太阳表面一路缩放到 10 万 AU 外的奥尔特云——你可以「飞」过每颗行星、卫星、小行星带、柯伊伯带、彗星，以及旅行者号的当前位置。

## 关键能力

| 能力 | 说明 |
|------|------|
| 纯浏览器 | 不用装任何东西，桌面/手机都能用 |
| NASA JPL 星历精度 | 行星位置误差 ≤0.074° |
| 无缝缩放 | 从轨道到大气层、地表、水下连续缩放 |
| 21 颗卫星 | 含月球、火卫一/二、木卫一~四、土卫六等 |
| 小行星带 + 柯伊伯带 + 彗星 | 不止八大行星 |
| 旅行者号当前位置 | 实时显示 NASA 深空网络数据 |
| gzip 后仅 ~200 KB | 极致轻量，纯前端即可加载 |

## 适用场景

- 教学场景：老师打开浏览器即给全班看实时太阳系
- 业余天文爱好者：缩到行星大气层看云层纹理
- 网页 demo / 可视化项目模板：Three.js + WebGL2 的高质量参考实现

## 参考链接

- [项目仓库](https://github.com/hyqzz/Solar-Wanderer)
- [原始链接](https://x.com/QingQ77/status/2071209750323155026)

## 相关概念

- [Fable 5 World Demo](tool-fable5-world-demo.md) — 浏览器内 4×4km 完全程序化开放世界，与 Solar Wanderer 同属「AI 生成可视化」家族
- [liquid-glass](tool-liquid-glass.md) — React 零依赖镜头组件，可与 Solar Wanderer 的 UI 叠加做出玻璃质感 HUD