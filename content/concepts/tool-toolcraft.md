---
type: Tool
title: "Toolcraft"
description: "pixel-point 出的创意类应用 starter kit + UI 库:自带 canvas / 工具栏 / 滑块 / 曲线 / 拾色器,一行 npx 命令创建,配套 AI 指令让 agent 直接生成可视化工具。"
resource: "https://github.com/pixel-point/toolcraft"
tags: [toolcraft, pixel-point, ui-kit, creative, ai]
timestamp: "2026-07-04T15:00:00Z"
---

# Toolcraft

## 它是什么

Toolcraft(`@pixel-point/toolcraft`)是 pixel-point 团队出品的「创意类应用 starter kit」。它把所有「做画面 / 滤镜 / WebGL 着色器 / Three.js 场景 / 动效」这类应用都需要的前后端脚手架打包好 — 滑块、曲线编辑器、拾色器、动画时间线、画布、导出、工具栏全部预装。

安装方式:

```bash
npx @pixel-point/toolcraft create
```

## 为什么用它 / 适合什么场景

- **不重写 UI 框架就能做新工具**:不用每次都从 0 拼参数面板、导出、画布、撤销。
- **AI 原生**:自带 `AGENTS.md` / 指令文件,告诉 agent 怎么用这套 starter 出新视觉工具。给一句「我想做一个把照片转 80s VHS 风格」的描述,agent 能直接产出完整项目。
- **为创意 app 设计**:不偏向 SaaS 后台管理,纯偏创作方向(图像处理 / 着色器 / 动画 / 交互)。

## 关键能力

| 能力 | 说明 |
|------|------|
| Canvas / 画布 | 内置画布与基础渲染管线,可挂载任意 WebGL 效果 |
| UI 组件 | Slider / Picker / Timeline / Curve / Color / Number 等参数面板组件 |
| Export | 一键导出 PNG / JSON 配置 |
| Toolbar | 工具栏 + 历史栈 + 快捷键 |
| AI 指令 | 自带 AGENTS.md / SYSTEM prompt,告诉 agent 怎么用 starter 出新工具 |
| 模板可扩展 | 任何已经用 Toolcraft 写的应用本身都可以作为下一个项目的 template |

## 适用项目举例

- 图像滤镜与样式化(stylization)
- WebGL 着色器在线编辑器
- Three.js 场景搭建
- 动画 / motion graphics 工具
- 摄影后期 / 调色工具
- 任何需要画布 + 参数面板 + 导出的程序

## 相关概念

- [Cloudflare Kumo](tool-kumo.md) — 偏 dashboard / 后台管理的 UI 库
- [Componentry](tool-componentry.md) — 组件目录式组件库
- [Astryx](tool-astryx.md) — Meta 开源设计系统
- [Toolcraft 仓库](https://github.com/pixel-point/toolcraft) — 项目链接(参考链接)
