---
type: Tool
title: "tuistore（终端应用市场）"
description: "终端里的应用市场：搜索、浏览几百款终端 / GUI 应用，一键安装；自动识别操作系统与可用包管理器，给出最适合的安装命令。"
resource: "https://github.com/Gheat1/tuistore"
tags: [tui, terminal, package-manager, app-store, rust]
timestamp: "2026-07-21T02:36:00Z"
---

# tuistore（终端应用市场）

## 它是什么
[tuistore](https://github.com/Gheat1/tuistore) 是一款终端里的 **应用市场**：找终端工具得在 GitHub 上翻来翻去，装的时候还得猜是 `cargo install` / `brew` / `pipx`——README 里一半的命令在你机器上根本跑不了。tuistore 让你 **在终端里直接搜索、浏览几百款应用，一键安装**，它会自动识别你的操作系统和已有包管理器，给出最合适的命令。

## 为什么用它 / 适合什么场景
- 频繁在新机器上配环境，想用一个工具替代「查 GitHub + 装包管理器 + 敲命令」。
- 想发现新的终端工具，但不想在 awesome 列表里翻。
- 不希望一个工具只支持一种包管理器——希望按你机器的现状智能选。

## 关键能力
| 能力 | 说明 |
|------|------|
| 终端应用市场 | 搜索 + 浏览 + 一键安装 |
| 自动识别环境 | 操作系统 + 已有包管理器 |
| 智能选命令 | 给出当前环境最合适的安装方式 |
| 覆盖广 | 几百款终端 / GUI 应用 |
| TUI 形态 | 全终端可用 |

## 相关概念
- [NaviTui](tool-navitui.md) — 终端里的 Subsonic / Navidrome 音乐播放器（同类终端工具的兄弟项目）
- [tmux-spotlight](tool-tmux-spotlight.md) — 终端 Spotlight 风格应用切换器

## 参考链接
- 项目链接: <https://github.com/Gheat1/tuistore>
- 视频演示: <https://video.twimg.com/tweet_video/HNk9-ycaYAEBYMc.mp4>
