---
type: "Tool"
title: "Fable 5 World Demo（Braffolk/fable5-world-demo）"
description: "浏览器内 4×4 km 完全程序化生成的开放世界：地形 / 树木 / 云 / 水 / 光全部由代码在启动时算出，21,000 行代码 99% 由 Claude Fable 5 写就。"
resource: "https://github.com/Braffolk/fable5-world-demo"
tags: [demo, webgpu, fable, procedural, browser-game]
timestamp: "2026-06-23T15:30:00Z"
---

# Fable 5 World Demo（Braffolk/fable5-world-demo）

## 它是什么

一个跑在浏览器里的「完全程序化」开放世界 demo：4×4 km 的地形、19 万棵各不相同的树、45 万株灌木、上百万根草，全部在启动时由代码计算出来，不依赖任何美术资产。整个仓库 21,000 行代码，其中 99% 由 Claude Fable 5 直接生成，人只写了一纸需求文档。

## 为什么用它 / 适合什么场景

- **演示 LLM 编码能力上限**：用一份需求文档让模型自己写完整个项目；
- **WebGPU 渲染范本**：含水力侵蚀地形、体素云、探针全局光照；
- **零资产原型**：做新游戏 / 仿真项目的「最小可行世界」快速验证。

## 关键能力

| 维度 | 实现 |
|------|------|
| 地形 | 水力侵蚀模拟 |
| 植被 | 6 种树 × 19 万棵 + 45 万灌木 + 数百万草 |
| 大气 | 体素云 + 探针全局光照 |
| 水体 | 程序化水面 |
| 光照 | 探针（probe）GI |
| 渲染目标 | Chrome 113+ + WebGPU |

## 媒体 / 原始链接

![世界截图](https://pbs.twimg.com/media/HLdgyKYacAA920Q.jpg)

- 项目链接：<https://github.com/Braffolk/fable5-world-demo>

## 相关概念

- [Heartmorrow](tool-heartmorrow.md) — 同样在浏览器里跑 LLM 驱动的可玩世界
- [Pi Fusion](tool-pi-fusion.md) — 同样以「Fable 模型驱动 LLM 工作流」为核心