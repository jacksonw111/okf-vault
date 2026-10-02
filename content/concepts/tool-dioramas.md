---
type: "Tool"
title: "Dioramas（blendi-remade：three.js 3D 落地页套件）"
description: "blendi-remade 出品的开源 3D 落地页套件：把 AI 生成的模型资产与 three.js 引擎拼起来，做滚动驱动、能交互的电影感 3D 落地页。20 个示例，MIT 协议，模型 CC BY 4.0，含 fal + Meshy 优化流水线。"
resource: "https://github.com/blendi-remade/dioramas"
tags: "[three-js, 3d, landing-page, scroll-driven, ai-asset, fal, meshy, webgl]"
timestamp: "2026-10-02T07:28:00Z"
---

# Dioramas（blendi-remade：three.js 3D 落地页套件）

## 它是什么

[Dioramas](https://github.com/blendi-remade/dioramas) 是 blendi-remade 出品的**开源 3D 落地页套件**——把 AI 生成的 3D 模型资产 + three.js 引擎 + 滚动驱动交互拼成一套可发布的电影感 3D 落地页。

- **20 个能直接跑的 3D 网站示例**
- 代码 **MIT** 协议；生成模型 + 图片 **CC BY 4.0**
- **不收费、不要求注册**

## 流水线

1. **fal** 上用 **Nano Banana 2** 出白底产品图
2. 交给 **Meshy 7.1** 图生 3D，得到 6 万–25 万三角面的 PBR 模型
3. `scripts/optimize.mjs` 做**焊接、meshopt 压缩、贴图转 WebP**，把 25 MB 压到 **3–8 MB**
4. 落地到 three.js 场景，加**滚动驱动 / 鼠标交互**
5. 发布上线

## 为什么用它 / 适合什么场景

| 场景 | Dioramas 的好处 |
|------|----------------|
| 想做电影感 3D 落地页 | 一套现成 three.js 模板 |
| 不会 3D 建模 | 拿产品图交给 fal + Meshy 自动出模型 |
| 关心模型体积 | 25 MB → 3-8 MB 的现成优化 |
| 想要交互感 | 滚动 / 鼠标 / 视角响应都有现成示例 |
| 商用可改 | MIT 协议 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 20 个示例 | 各种风格 3D 落地页参考 |
| 流水线完整 | fal → Meshy → 优化 → three.js → 部署 |
| 体积优化 | 25 MB → 3-8 MB |
| 滚动驱动 | 滚动位置驱动相机 / 模型变换 |
| 鼠标交互 | Hover / click / 拖拽 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105921977550590044>
- 项目链接：<https://github.com/blendi-remade/dioramas>

## 相关概念

- [three.js](#) — Dioramas 核心引擎，本仓库目前未收录
- [Solar Wanderer](./tool-solar-wanderer.md) — 另一个 three.js 优秀 demo
- [Kobra Grouped Table](./tool-kobra-grouped-table.md) — 不同形态的「落地页组件」库
