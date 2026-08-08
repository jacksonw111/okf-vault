---
type: "Note"
title: "Single File Web Apps"
description: "「无构建 / 无框架 / 单 HTML 文件」风格的代表性项目集：把完整应用塞进一个 .html，下载即用，强调可移植与极简。"
tags: [single-file, no-build, web, demo, html]
timestamp: "2026-08-08T20:00:00Z"
---

# Single File Web Apps

## 什么是「单文件 Web App」

「单文件 Web App」指整站全部塞进一个 `.html` 文件（外加可能同目录的少量资源）、不依赖构建步骤、不依赖任何前端框架的项目风格。打开文件即跑，复制粘贴即可分发。

## 风格特征

- **零构建**：没有 webpack / vite / npm install。
- **零框架**：不依赖 React / Vue / Svelte，纯粹 vanilla JS 或最少量类库。
- **单文件**：HTML / CSS / JS 都内联在同一个 `.html`。
- **可移植**：用 U 盘、邮件附件、QR 码都能分发。
- **可审计**：一份文件就够看清全部实现。

## 代表项目

| 项目 | 复刻目标 |
|------|---------|
| [macOS Web](./tool-macos-web.md) | macOS 桌面 |
| [Win11 Web](./tool-win11-web.md) | Windows 11 桌面 |
| [Windows 98 in Browser](./tool-win98-browser.md) | Windows 98 怀旧 |

## 适用场景

- 产品演示 / hero image 落地页的交互演示。
- 教学示例与「设计参考」。
- 在受限环境（无 node、无网络）下交付一个可用工具。

## 相关概念

- [macOS Web](./tool-macos-web.md) — 复刻 macOS 桌面的单文件项目