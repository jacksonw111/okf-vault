---
type: "Tool"
title: "html2pdf（SanzarRehman/HTML2PDF）"
description: "Rust 自建渲染管线的 HTML→PDF 转换工具，不启动 Chromium；单进程并行转多份文档，替代「用 Chromium 转 PDF 占 800+ MB/次」的高内存方案。"
resource: "https://github.com/SanzarRehman/HTML2PDF"
tags: "[pdf, html-to-pdf, rust, rendering, memory-efficient, batch-conversion]"
timestamp: "2026-07-31T20:30:00Z"
---

# html2pdf（SanzarRehman/HTML2PDF）

[html2pdf](https://github.com/SanzarRehman/HTML2PDF) 是一款 **Rust 自建渲染管线的 HTML → PDF 转换器**：不像 Chromium/Puppeteer/Playwright 那样启动完整浏览器（单任务 800+ MB），它直接走自己的渲染栈——**单进程内并行处理多份文档**，把并发批转换从「内存撑不住」变成「常规能力」。

## 它是什么

- 不启动 Chromium / WebKit 引擎
- 用 Rust 重写的轻量 HTML 渲染管线
- 单进程可同时跑多个 HTML→PDF 转换任务
- 内存占用对应任务数量线性增长，不必担心 OOM

## 为什么用它 / 适合什么场景

| 痛点 | html2pdf 的对策 |
|------|------------------|
| Chromium 转换占 800+ MB | 不启动浏览器，内存占用大幅下降 |
| 并发跑几个撑不住 | Rust 任务并行，单进程内可同时转多份 |
| 部署到小内存服务器常被 OOM kill | 摆脱 Chromium，单任务内存通常远低 |
| 需要 CI / Worker 内做批量 PDF | 适合无头、低内存环境 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 自建渲染管线 | 无浏览器依赖，Rust 原生实现 |
| 并行转换 | 单进程多任务并行 |
| 小内存适配 | 适合 Serverless / CI / 容器 |
| 替代方案 | 用来替掉项目里 Puppeteer / Playwright 的 PDF 调用 |

## 局限（取舍）

- 兼容性：自建渲染管线对复杂 CSS / 现代 JS 渲染可能不如 Chromium 完整（动态渲染动画 / Web Font 复杂场景需评估）
- 调试：浏览器开发者工具不能直接复用

## 相关概念

- [Kling 3.0 Cinematic](./note-kling-3-cinematic.md) — 视频生成工具，与 html2pdf 都是「重 client 改轻 server」思路
- [Penpot](./tool-penpot.md) — 用 SVG / CSS / HTML 等开放标准输出，不依赖浏览器内置 PDF
- [playbook-spa-pdf-viewer](./playbook-spa-pdf-viewer.md) — 浏览器内 PDF 阅读器 SPA，与 html2pdf 上下游互补（转换 → 阅读）
- [bento-slides](./tool-bento-slides.md) — 把 markdown / HTML 转幻灯片，可借 html2pdf 思想扩展为「无浏览器 PDF / 幻灯片批转换」
