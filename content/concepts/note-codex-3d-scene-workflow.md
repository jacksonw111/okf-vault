---
type: Note
title: "Codex 做 3D 场景的正确打开方式"
description: "用 Codex + Tripo + Nanobanana 生成 3D 资产，配合 three.js / Web3D 在浏览器里跑起来的端到端流程。"
resource: "https://x.com/ring_hyacinth/status/2096704996381266424"
tags: "[codex, 3d, threejs, tripo, nanobanana, web3d]"
timestamp: "2026-09-07T13:17:00Z"
---

# Codex 做 3D 场景的正确打开方式

## 是什么
一段公开分享的 3D 场景制作工作流：用 Codex 作为 AI 编程助手，配合 Tripo（3D 资产生成）和 Nanobanana（图片生成）做资产层，再用 three.js / Web3D 在浏览器端渲染。整套流程是为了"网页端能跑"这个目标设计，避免重模型 / 大贴图 / 服务端依赖。

## 工作流
1. **文案 / 概念**：Codex 拆解场景需求
2. **图片参考**：Nanobanana 出场景概念图
3. **3D 资产**：Tripo 把概念图转成可在 three.js 里加载的模型
4. **代码集成**：Codex 写 three.js / Web3D 加载、灯光、相机代码
5. **浏览器内运行**：产物直接通过 URL 分享

## 关键能力
| 能力 | 说明 |
|------|------|
| 端到端 | 文案 → 资产 → 代码 → 浏览器 |
| 浏览器可跑 | 模型轻量化，无需服务端 |
| 工具可替换 | Codex / Cursor / Claude Code 都能套 |

## 适用场景
- 营销页 / Landing Page 的 3D Hero
- 互动故事 / 儿童教育 Web App
- 个人作品集中需要快速 3D 化的项目

## 参考
- 原帖：<https://x.com/ring_hyacinth/status/2096704996381266424>

## 相关概念
- [Codex](https://openai.com/index/codex/) — 流程中的 AI 编程助手
- [Tripo](https://www.tripo3d.ai/) — 3D 资产生成服务
- [three.js](https://threejs.org/) — 浏览器端 3D 渲染库
- [Fable 5 World Demo](tool-fable5-world-demo.md) — 浏览器内 4×4km 完全程序化开放世界