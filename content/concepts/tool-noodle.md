---
type: "Tool"
title: "noodle（终端里的 REST 客户端）"
description: "终端里的 REST 客户端，像 Postman 但跑在 TUI 里；请求存为 YAML，方便 Git 版本管理与团队协作。"
tags: "[cli, tui, rest, api, postman, yaml]"
timestamp: "2026-07-06T12:36:00.000Z"
resource: "https://github.com/wilfredinni/noodle"
---

# noodle（终端里的 REST 客户端）

## 它是什么

[`noodle`](https://github.com/wilfredinni/noodle) 是一个 **TUI（终端 UI）** 的 REST API 客户端，定位类似 Postman / Insomnia，但跑在终端里，**请求体存为 YAML**。

## 它解决什么

- **不想切窗口**：写代码时随手在终端里测个 API，不用打开 GUI
- **请求可版本化**：YAML 文件直接 `git diff`，团队共享同一份请求集合
- **纯文本友好**：YAML 比 Postman 的二进制 collection 更便于 review / merge

![noodle 界面](https://pbs.twimg.com/media/HMgTYB1aoAAb_jz.jpg)

## 关键特性

- 终端原生 UI（键鼠交互，无需离开 shell）
- 请求定义在 YAML 中，路径 = 文件名，结构清晰
- 支持变量、环境切换、headers、body、auth 等常规 REST 概念
- 适合喜欢键盘流、希望把 API 调用沉淀为可审计文本的开发者

## 适用场景

- 后端开发者日常写代码时随手测接口
- 团队需要把「常用 API 调试用例」作为代码资产共享与版本管理
- 远程 SSH / 无 GUI 环境下调试 API

## 参考链接

- [项目链接](https://github.com/wilfredinni/noodle)

## 相关概念

- [Kinetics](tool-kinetics.md) — 开源运动效果动画库，同时提供 CSS + React + Prompt 三种版本
- [Vesta Terminal](tool-vesta-terminal.md) — Swift/AppKit 写的 macOS 原生终端，Metal 渲染引擎
- [Plaza](tool-plaza.md) — 跨发行版 TUI 包管理器