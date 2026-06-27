---
type: "Tool"
title: "Plaza（跨发行版 TUI 包管理器）"
description: "跨发行版的终端 TUI 包管理器浏览器，能同时搜 Arch 官方源和 AUR，同名包自动合并；管理视图能看到已装和能升级的包，升级 / 卸载在后台终端面板跑。"
tags: "[cli, tui, package-manager, arch, aur]"
timestamp: "2026-06-27T10:27:00.000Z"
resource: "https://github.com/StaszeKrk/plaza"
---

# Plaza（跨发行版 TUI 包管理器）

## 它是什么

[`Plaza`](https://github.com/StaszeKrk/plaza) 是一个**跨发行版的终端 TUI 包管理器浏览器**，让你在命令行里搜索、安装、管理包。它的特点是**同时搜 Arch 官方源和 AUR**，同名包自动合并成一条；管理视图能直接看到已装 / 待升级的包，升级 / 卸载在后台终端面板跑，不挡你继续干活。

[演示视频](https://video.twimg.com/amplify_video/2070483944685076480/vid/avc1/1280x720/sFuOslBeT2gljpPZ.mp4?tag=28)

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨发行版 | Arch 官方源 + AUR 同时搜 |
| 同名合并 | 多个源同名包自动合并为一条 |
| 管理视图 | 一眼看已装 / 可升级的包 |
| 后台运行 | 升级 / 卸载在后台终端面板跑 |
| 不阻塞 | 后台执行时主界面还能继续用 |

## 适用场景

- Arch / Manjaro / EndeavourOS 用户嫌 yay / pacman 单独切换麻烦
- 想用 TUI 图形界面找包、装包而不是敲命令行
- 想批量升级并实时看后台日志

## 参考链接

- [项目链接](https://github.com/StaszeKrk/plaza)
- [演示视频](https://video.twimg.com/amplify_video/2070483944685076480/vid/avc1/1280x720/sFuOslBeT2gljpPZ.mp4?tag=28)

## 相关概念

- [lazycron](tool-lazycron.md) — 同样是 Go 写的 TUI 工具，面向 cron 任务管理
- [tabiew](tool-tabiew.md) — 同样是 TUI 工具，面向表格数据查看