---
type: "Tool"
title: "threejs-particle-fluids（GPU 粒子流体模拟库）"
description: "在 three.js 里做液体 / 软体 / 布料 / 烟雾 GPU 粒子模拟的库，PBF 求解器与渲染封装好，调用 API 即可。dgreenheck 出品。"
resource: "https://github.com/dgreenheck/threejs-particle-fluids"
tags: "[threejs, gpu, particle, fluid, pbf, simulation, webgl, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# threejs-particle-fluids（GPU 粒子流体模拟库）

## 它是什么

[threejs-particle-fluids](https://github.com/dgreenheck/threejs-particle-fluids) 是 dgreenheck 开源的 three.js 扩展库：在 three.js 场景里做液体、软体、布料、烟雾的 GPU 粒子模拟。PBF（Position Based Fluids）求解器和渲染都已封装好，无需自己写求解算法，调用 API 即可。

## 关键能力

| 能力 | 说明 |
|------|------|
| 流体模拟 | PBF 求解器封装好，支持液体模拟 |
| 多形态 | 液体 / 软体 / 布料 / 烟雾 |
| GPU 加速 | 在 GPU 上跑粒子模拟，性能可控 |
| three.js 集成 | 作为 three.js 库直接调用 |
| API 简洁 | 不需要懂流体动力学就能用 |

## 适合谁

- three.js 场景里想要液体 / 软体 / 布料 / 烟雾效果
- 不想自己写 PBF 求解器
- 想要可控的 GPU 粒子模拟

## 媒体预览

![](https://pbs.twimg.com/media/HTWR35kbwAAFqkk.jpg)

## 原始链接

- 项目主页：<https://github.com/dgreenheck/threejs-particle-fluids>

## 相关概念

- [BeeftV](./tool-beeftv.md) — 本地自由画布，文本 / 图 / 视频 / 音频模型生成 + Agent 摆节点