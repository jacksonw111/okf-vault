---
type: Tool
title: "Falco (Rust browser engine)"
description: "从零用 Rust 写的微型浏览器引擎，不套 WebKit / Gecko / Chromium，能把 HTML / CSS / JS 渲染成 PNG，也能开个交互窗口；约 3.6 万行 Rust 自实现 HTML 解析 / CSS 级联 / 布局 / 绘制 / JS 虚拟机 / 字体栅格化 / PNG 编码。"
resource: "https://github.com/poxk/Falco"
tags: [rust, browser-engine, png, html, css, js, mini-browser]
timestamp: "2026-08-03T15:30:00Z"
---

# Falco (Rust browser engine)

## 它是什么
Falco（`poxk/Falco`）**从零用 Rust 写的一个微型浏览器引擎**，不套 WebKit / Gecko / Chromium，能把 HTML / CSS / JS 渲染成 PNG，也能开个交互窗口。

约 3.6 万行 Rust 从零实现：HTML 解析、CSS 级联、布局、绘制、JS 虚拟机、字体栅格化、PNG 编码全都自己写。编译后能把网页直接渲染成 PNG，或打开带地址栏的窗口浏览，滚动、点链接、填表单、前进后退都行。

## 为什么用它 / 适合什么场景
- **学习 / 教学价值**：整套浏览器栈 3.6 万行 Rust 能看清，是浏览器引擎教学极佳材料。
- **HTML → PNG 渲染**：把任意网页静态化为 PNG，用于截图 / 报告 / 卡片生成。
- **无浏览器依赖部署**：不需要系统装 Chromium / WebKit，单二进制即可。
- **嵌入式 UI**：可作为嵌入式 UI 引擎嵌入到 Rust 应用。

## 关键能力

| 能力 | 说明 |
|------|------|
| HTML / CSS / JS 渲染 | 完整浏览器栈：解析 → 级联 → 布局 → 绘制 |
| PNG 输出 | 整页渲染为 PNG，无需浏览器 |
| 交互窗口 | 带地址栏的浏览窗口：滚动 / 点击 / 表单 / 前进后退 |
| JS 引擎 | 自实现 JS 虚拟机 |
| 字体栅格化 | 自实现字体处理 |
| 零依赖 | 单 Rust 二进制，不依赖 WebKit / Gecko / Chromium |

## 项目链接
- <https://github.com/poxk/Falco>

## 相关概念
- [Obscura Headless Browser](./tool-obscura-headless-browser.md) — 另一类无头浏览器定位
- [HTML2PDF (Sanzar)](./tool-html2pdf-sanzar.md) — Rust 自建渲染管线的 HTML→PDF，与本工具同属「不依赖 Chromium 的渲染管线」
- [kumo](https://github.com/cloudflare/kumo) — Cloudflare 开源 React 组件库
