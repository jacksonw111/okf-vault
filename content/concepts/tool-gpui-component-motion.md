---
type: Tool
title: "GPUI Component Motion（GPUI Component 的动画 / 过渡系统）"
description: "LongBridge 的 GPUI Component 在 motion 子模块上扩展的动画与过渡系统：把 GPUI 应用的入场 / 过渡 / 微交互动效做成可复用的声明式组件。"
resource: "https://longbridge.github.io/gpui-component/base/motion"
tags: [rust, gpui, animation, motion, ui, transition]
timestamp: "2026-08-29T21:30:00Z"
---

# GPUI Component Motion（GPUI Component 的动画 / 过渡系统）

## 它是什么

[longbridge/gpui-component](https://github.com/longbridge/gpui-component) 的 `motion` 子模块是给 GPUI Rust UI 应用加**动画 / 过渡**能力的子系统：把入场、退场、过渡、微交互做成可复用的声明式 API，开发者不必自己写缓动函数 / 时间曲线 / GPU 帧对齐。

定位：

- 不是「再做一个动画库」，而是把动画**作为 GPUI 应用的基本积木**；
- 与 [GPUI Component](./tool-gpui-component.md) 的设计语言一致——可直接对接现有 DataTable / 面板 / 弹层组件；
- 让 GPUI 应用的「微质感」不再输给 Web / iOS 的成熟动画体系。

## 为什么用它 / 适合什么场景

- 用 GPUI 写应用想加**交互动效**但又不想从零写缓动；
- 做金融终端 / 监控大屏，需要面板切换 / 抽屉 / Toast 的入场出动画；
- 想给 GPUI 应用一致的**动效语言**——不同面板遵循同一套缓动 / 时长；
- 设计 → 开发的动效规范传递——把动效作为组件 API 而不是散落的 magic number。

## 关键能力

| 能力 | 说明 |
|------|------|
| 声明式动画 | 把动效当作组件属性传入，不必手动算帧 |
| 入场 / 退场 | 面板、抽屉、Toast 的进入退出动画 |
| 微交互 | 按钮 / 选中 / 折叠 / 展开的微动效 |
| 与 GPUI Component 配套 | 与 DataTable / 面板 / 弹层一致的设计语言 |
| Rust 原生 | 不依赖 JS / Web，编译到 GPUI 桌面 / WASM 双端 |

## 相关概念

- [GPUI Component](./tool-gpui-component.md) — LongBridge 的 GPUI Rust UI 组件库整体；motion 是其动画子系统
- [Kinetics](./tool-kinetics.md) — 开源运动效果动画库（CSS + React + AI Prompt），是 Web 端的对应物；GPUI Component Motion 是 GPUI 端的对应物

## 参考链接

- 项目链接（文档）：<https://longbridge.github.io/gpui-component/base/motion>
- 原始推文：<https://x.com/Wen_Zw/status/2093729378773717034>
- 视频：<https://video.twimg.com/amplify_video/2093695169463980032/vid/avc1/1234x1364/K3g_gyL149UiHYLW.mp4?tag=29>