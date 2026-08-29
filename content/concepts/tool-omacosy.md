---
type: Tool
title: "omacosy（macOS 26 上的 omarchy 风格平铺桌面，五个自编译 Swift 小二进制）"
description: "macOS 26 上 AutoRaise、aerospace-swipe、JankyBorders 等工具相继失效或臃肿，omacosy 用五个自编译 Swift 小二进制把 omarchy 风格桌面环境装进一个仓库：Super 键平铺（dwindle 布局）、状态栏、焦点跟随鼠标、触控板滑动切工作区、实时工作区总览。"
resource: "https://github.com/paulsp94/omacosy"
tags: [macos, tiling, omarchy, swift, aerospace, window-management, super-key, dwindle]
timestamp: "2026-08-28T00:00:00Z"
---

# omacosy

## 它是什么
[paulsp94/omacosy](https://github.com/paulsp94/omacosy) 是**把 omarchy 风格平铺桌面装进 macOS 26** 的项目。背景：macOS 26（Apple 新一代桌面系统）让很多现成的平铺工具（AutoRaise、aerospace-swipe、JankyBorders 等）**失效或臃肿**，找不到合适的现成组合。

omacosy 用**五个自编译的 Swift 小二进制**重新实现所需能力——每个二进制职责单一，整个仓库是一个完整 omarchy 风格桌面环境：

| 二进制 | 职责 |
|--------|------|
| 平铺器 | Super 键触发 dwindle 布局 |
| 状态栏 | 屏幕顶部显示工作区、时钟、状态 |
| 焦点跟随 | 鼠标移到哪窗口就 focus 哪 |
| 工作区切换 | 触控板左右滑动切工作区 |
| 总览 | 实时显示所有工作区的窗口缩略图 |

## 为什么用它 / 适合什么场景
- macOS 26 用户想**找回 omarchy 风格**的平铺体验；
- 现成工具（AutoRaise / aerospace / JankyBorders）失效或臃肿，需要替代品；
- 喜欢**职责单一的小工具链**而非一个臃肿的 App；
- 想用 Swift 自编译整套——对 Apple 生态有掌控感。

## 关键能力
| 能力 | 说明 |
|------|------|
| 五个 Swift 二进制 | 每个职责单一，整套构成桌面环境 |
| Super 键平铺 | dwindle 布局 |
| 状态栏 | 工作区、时钟、状态显示 |
| 焦点跟随 | 鼠标移动自动 focus 窗口 |
| 触控板滑动切工作区 | 替代 aerospace-swipe |
| 工作区总览 | 实时窗口缩略图 |
| 适配 macOS 26 | 解决现成工具失效问题 |
| 极简组合 | 不依赖臃肿 App |

## 相关概念
- [Mouse Me](tool-mouse-me.md) — Linux 统一光标主题；omacosy 是 macOS 上**整套平铺桌面**的统一
- [Realmheart](tool-realmheart.md) — 同样为平铺桌面 Shell，但用 C++ + GTK 4 写给 Linux；omacosy 用 Swift 写给 macOS
- [Btop Quattro Plugin](tool-btop-quattro-plugin.md) — Omarchy 顶栏的 btop 摘要；omacosy 是**整套**而非单插件

## 参考链接
- 项目链接：<https://github.com/paulsp94/omacosy>
- 原始推文：<https://x.com/QingQ77/status/2093168692897144877>
- 媒体：<https://pbs.twimg.com/media/HQskSZGbIAAJ40e.jpg>、<https://pbs.twimg.com/media/HQskTegaAAApI_D.jpg>
