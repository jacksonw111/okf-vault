---
type: Tool
title: "OKF Static HTML Visualizer"
description: "Google Cloud 发布的 OKF 参考实现：将任意 OKF bundle 转化为单文件交互式图谱视图，纯前端，无需后端，数据不离开页面。"
resource: "https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf"
tags: "[okf, google-cloud, visualizer, html, reference-implementation]"
timestamp: 2026-06-17T00:00:00Z
---

# OKF Static HTML Visualizer

## 是什么

OKF Static HTML Visualizer 是 Google Cloud 随 OKF v0.1 一起发布的**参考消费者实现**（reference consumer）。它将任意符合 OKF 规范的 bundle 目录转化为一个独立的、交互式的图谱可视化页面。

## 核心特性

- **单文件**：所有 HTML/CSS/JS 内联到一个文件，双击即可在浏览器打开
- **零依赖**：不需要 Node.js、不需要后端服务、不需要安装
- **数据不离开页面**：纯前端处理，OKF bundle 的内容不会被上传到任何服务器
- **交互式图谱**：以节点-边图展示概念之间的 Markdown 链接关系

## 使用场景

当你有一个 OKF bundle 目录（本地文件夹或压缩包）时：

1. 把 bundle 喂给 visualizer
2. 在浏览器里以图谱方式探索概念之间的关联
3. 点击节点跳转到具体概念文件

这是 OKF 作为「可移植格式」的体现——同一个 bundle，既可以被 agent 消费做推理，也可以被人通过可视化器浏览。

## 设计意图

同样是一个**证明概念**：

- 展示了一种可能的 OKF 可视化路径
- 不要求使用 HTML 或图谱视图，bundle 可以被任意消费者解析
- 格式本身 vs 工具生态：OKF 只定义格式，生态由社区贡献

## 相关概念

- [Open Knowledge Format (OKF)](./term-okf.md) —— 本 visualizer 的消费目标格式
- [OKF Enrichment Agent](./tool-okf-enrichment-agent.md) —— 配套的参考生产者实现
