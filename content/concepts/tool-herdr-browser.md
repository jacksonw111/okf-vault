---
type: "Tool"
title: "herdr-browser（ogulcancelik/herdr-browser）"
description: "在 Herdr 终端面板里渲染一个真实 Chromium 浏览器视图，并通过 CDP（Chrome DevTools Protocol）让自动化客户端驱动它——把浏览器塞进 TUI，让终端 agent 能直接驱动网页。"
resource: "https://github.com/ogulcancelik/herdr-browser"
tags: "[terminal, herdr, chromium, cdp, browser-automation, tui]"
timestamp: "2026-07-31T20:30:00Z"
---

# herdr-browser（ogulcancelik/herdr-browser）

[herdr-browser](https://github.com/ogulcancelik/herdr-browser) 在 **Herdr 终端面板（TUI）里嵌入一颗真正的 Chromium** 并暴露 **CDP（Chrome DevTools Protocol）** 给自动化客户端——**把浏览器塞进终端，让 agent 直接驱动网页**而不是切换窗口。

## 它是什么

- **TUI 内嵌实时 Chromium 视图**：你在终端里看网页长什么样，无需切到独立浏览器
- **CDP 暴露给客户端**：第三方自动化脚本 / agent 可通过 Chrome DevTools Protocol 驱动它
- **不走 headless 模式**：是真的 Chromium 渲染，CSS / 动画 / Web Font 与桌面浏览器一致
- **「浏览器在终端里」范式**：纯键盘流的人也可以看到画面

## 为什么用它 / 适合什么场景

| 痛点 | herdr-browser 怎么解 |
|------|----------------------|
| Terminal UI（TUI）通常只能跑 ASCII / 半图形 | 直接显示网页真实样貌 |
| headless 浏览器与真实渲染有差异 | 借用真正 Chromium 一致性 |
| Agent 切窗口去看网页很卡 | 终端内同框即可 |
| 自动化需要 CDP 但不想启整套 Chrome 服务 | 把它当 devtools-server 用 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 真实 Chromium 渲染 | 不走 headless，CSS / 动画与桌面一致 |
| TUI 嵌入视图 | 画面直接显示在终端面板里 |
| CDP 暴露 | 客户端可调用 Chrome DevTools Protocol 自动化 |
| 多端驱动 | 既可人看，也可让 agent / 脚本驱动 |

## 相关概念

- [herdr-reviewr](./tool-herdr-reviewr.md) — 也是 Herdr 生态内的工具，但聚焦在「让 agent 的代码改动落到 diff 面板供人审」
- [forkd](./tool-forkd.md) — microVM fork 化沙箱（100 个 100ms 启动），与 herdr-browser 在「让 agent 能跑长任务」互补
- [aether-android-agent](./tool-aether-android-agent.md) — Android 本地通用 AI Agent，可用 herdr-browser 思路把终端 UI 移植到 Android
- [Penpot](./tool-penpot.md) — 浏览器内设计工具，herdr-browser 也能用它
- [openbrowser](./tool-openbrowser.md) — 类似定位：浏览器自动化框架（与 herdr-browser 的 CDP 暴露组合可让 agent 在终端里驱动网页）
- [browser-search-agent](./tool-browser-search-agent.md) — 浏览器内 AI 搜索 agent
