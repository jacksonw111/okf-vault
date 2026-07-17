---
type: "Tool"
title: "Codex Dream Skin"
description: "给 Codex 桌面端做外部主题换肤,不改官方安装包,通过本机 CDP 注入一张 16:9 壁纸来美化界面。"
resource: "https://github.com/Fei-Away/Codex-Dream-Skin"
tags: "[codex, theme, skinning, cdp, customization]"
timestamp: "2026-07-17T00:34:16Z"
---

# Codex Dream Skin

[Codex Dream Skin](https://github.com/Fei-Away/Codex-Dream-Skin) 是一个面向 ChatGPT Codex 桌面端的外部换肤方案——**不改官方安装包**, 通过本机 **CDP (Chrome DevTools Protocol)** 注入一张 16:9 壁纸, 让原生界面瞬间有种「作者定制感」。

## 它解决的问题

Codex 桌面端是封闭的 Electron 应用, 用户无法直接换主题。社区的换皮思路多是：

- 替换安装包里的静态资源 → 易被官方升级覆蓋
- 注入 CSS / JS → 需要长期挂一个进程

本工具走的是**CDP 注入壁纸**: 利用本地 CDP 端口临时接管窗口, 把一张图当背景铺上去即可, 无副作用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 零侵入 | 不改官方安装包, 不替换资源文件 |
| CDP 注入 | 利用 Codex 桌面端本地暴露的 Chrome DevTools Protocol 端口 |
| 16:9 自适配 | 壁纸自适应 16:9 窗口, 不用手动裁 |
| 可热替换 | 换图即换肤, 不需要重装 |

## 媒体

![](https://pbs.twimg.com/media/HNY8cLDbQAAN5Q6.jpg)

## 参考链接

- [项目仓库](https://github.com/Fei-Away/Codex-Dream-Skin)

## 相关概念

- [Codex-X](./tool-codex-x.md) — Tauri 2 跨平台 Codex 桌面端管理器, 主题是其中一环
- [AgentLock](./tool-agent-lock.md) — 用 eBPF 限制编码 Agent 的访问范围, 与本工具的「外部接管 Codex」思路可参考
