---
type: "Tool"
title: "Fluid Functionalism（流体功能主义设计体系）"
description: "fluidfunctionalism.com 提出的设计系统：在 modal 里嵌入流体功能主义风格的 sidebar，强调层叠、连续、不打断的过渡体验；同时也是一个用 Spring physics 替代死板过渡的开源组件库，底层支持 Radix / Base UI，可用 shadcn 命令搬进项目。"
resource: "https://fluidfunctionalism.com/"
tags: "[design, design-system, sidebar, modal, ui, spring-physics, radix, base-ui, shadcn]"
timestamp: "2026-09-28T23:45:00Z"
---

# Fluid Functionalism（流体功能主义）

## 它是什么

[fluidfunctionalism.com](https://fluidfunctionalism.com/) 是设计师 micka_design 提出的**设计语言 / 设计体系 + 开源组件库**：

- **设计语言侧**：强调**层叠、连续、不打断**的过渡体验。常用于在 **modal 弹窗里嵌入 sidebar**——侧栏不是「弹完消失」的硬切换，而是 fluid 滑入并承接上下文。
- **组件库侧**：把组件库里所有**交互动效**全部换成**弹簧物理（Spring physics）**，而不是定死的过渡时间——连点、中途反悔都会自然回弹。

## 关键特征

### 1. 流体 / 弹簧过渡

- **悬停手感**：光标挪上去时背景像水流一样顺滑
- **文字响应**：文字会随光标靠近微微**增重变粗**
- **回弹自然**：连点或中途反悔都会自然回弹，不是「机械开关」

### 2. 覆盖 AI Agent 时代的交互组件

- 思考过程折叠面板
- 多步提问卡片
- 按钮 / 面板等常规组件

### 3. 底层兼容

- 支持 **Radix** 与 **Base UI**
- 一条 **shadcn** 命令即可搬进自己项目
- 每个组件详情页都能看到背后的想法与数学逻辑

## 为什么用它 / 适合什么场景

- 想给 modal / 弹窗 / 抽屉交互做更顺滑的过渡。
- 想研究「**流体功能主义**」这种设计语言的具体落地。
- 想让用户在 modal 中不丢失主上下文。
- 觉得现有组件库「点起来硬邦邦」——想换**弹簧物理**驱动的自然手感。
- 想给 AI Agent 应用的「思考过程 / 多步提问」UI 配一套已调好手感的组件。
- 已在用 Radix / Base UI / shadcn——无缝接入。

## 关键能力

| 能力 | 说明 |
|------|------|
| 设计语言 | 流体功能主义（modal 内 sidebar 嵌入、连续过渡） |
| 物理 | Spring physics 弹簧物理驱动所有交互 |
| 悬停 | 背景水流般顺滑 + 文字随光标增重 |
| 组件覆盖 | 常规组件 + Agent 思考过程折叠 + 多步提问卡片 |
| 底层 | Radix / Base UI |
| 安装 | 一条 shadcn 命令搬进项目 |
| 文档 | 每个组件都有想法 + 数学逻辑 |

## 媒体

- ![](https://pbs.twimg.com/media/HRvn1ZqaYAAyAke.jpg)
- 视频：<https://video.twimg.com/amplify_video/2104516927528083456/vid/avc1/2828x1962/ZupbtugQf5dZD_rg.mp4?tag=29>

## 相关概念

- [app-shell-sidebar](./playbook-app-shell-sidebar.md) — 应用外壳侧栏布局剧本
- [Sonaui AnimatedDropdown](./tool-sonaui-animated-dropdown.md) — 共享布局指示器的下拉过渡