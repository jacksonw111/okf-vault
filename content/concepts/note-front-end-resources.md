---
type: "Note"
title: "前端 / 创客 资源合集（csaba_kissi 整理）"
description: "「程序员和创客的超棒网站和应用」列表：动画加载器、AI 复刻设计、React 加速 70%、GPU 终端、给编码代理的程序化视频——一次性五个高密度资源。"
tags: "[resources, frontend, tools, ai, react, terminal]"
timestamp: "2026-06-17T00:00:00Z"
---

# 前端 / 创客 资源合集

## 五件套

### 1. [css-loaders.colorion.co](https://css-loaders.colorion.co) — 99 个动画 CSS 加载器

纯 CSS 实现的加载动画集合——无 JS、无图片。**99 个变体**覆盖常见场景（圆环、进度条、骨架、脉冲…）。做「loading 状态没灵感」时直接来挑一个。

### 2. [21st.dev](https://21st.dev) — 用现成 prompt 复刻设计

**「看到喜欢的网站 → 喂 prompt → AI 复刻出代码」**。定位类似 v0 / Galileo，但更聚焦「把别人的设计学到手」。适合：做竞品研究 / 学习设计模式 / 快速出原型。

### 3. [Million (aidenybai/million)](https://github.com/aidenybai/million) — 让 React 快 70%

React 替代编译器：编译时把组件编译成细粒度 DOM 操作，**官方数据比 React 自身快 70%**。适合：性能敏感的 React 项目（dashboard、大列表、动画密集场景）。

### 4. [Alacritty](https://alacritty.org) — 开源、跨平台、OpenGL 终端仿真器

「**快到极致**」的 GPU 渲染终端。配置文件是纯 YAML，简洁、跨平台（macOS / Linux / Windows）。与 [kitty](https://sw.kovidgoyal.net/kitty/)、[WezTerm](https://wezfurlong.org/wezterm/) 同类。

### 5. [open-design.ai/html-video](https://open-design.ai/html-video) — 给编码代理的程序化视频

让 LLM 用 HTML + Canvas / WebGL **程序化生成视频**（非传统视频生成模型），用 prompt 控制动画 / 形状 / 时间线。类似 [Archify](tool-archify.md) 的视频版。

## 为什么这一条值得收录

- **密度高**——一条推文五个项目，每个都是「立刻能用 / 值得研究」。
- **覆盖三层**：CSS 层（css-loaders）/ 框架层（Million）/ 工具层（Alacritty）/ AI 层（21st.dev, open-design.ai）。
- 与本知识库现有工具的呼应：
  - css-loaders ↔ [transitions.dev](tool-transitions-dev.md) / [textmotion.dev](tool-textmotion-dev.md)
  - 21st.dev ↔ [JSON-Render](tool-json-render.md) / [Hyperagent 设计网格](tool-hyperagent-design-skill.md)
  - Million ↔ [Turborepo](tool-turbo.md) 之外的「前端性能」单点
  - Alacritty ↔ 终端 / DevContainer 主题
  - open-design.ai ↔ [Archify](tool-archify.md)

## 参考链接

- [原始链接 1](https://x.com/csaba_kissi/status/2066417489194483858)

## 相关概念

- [Archify](tool-archify.md)
- [JSON-Render / 生成式 UI](tool-json-render.md)
- [transitions.dev](tool-transitions-dev.md)
- [textmotion.dev](tool-textmotion-dev.md)
- [Hyperagent 设计网格 Skill](tool-hyperagent-design-skill.md)
- [Turborepo](tool-turbo.md)
