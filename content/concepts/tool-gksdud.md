---
type: "Tool"
title: "gksdud（macOS 韩英键切换小工具）"
description: "把右 ⌘ 当韩英切换键用，过去得装 Karabiner 再手改一堆系统设置，快打时还常掉字；gksdud 装一个应用就把键映射和切换事件都办掉。"
resource: "https://github.com/codingnoye/gksdud"
tags: "[macos, korean, input-switch, hotkey, keyboard, ime]"
timestamp: "2026-09-21T22:00:00Z"
---

# gksdud

## 它是什么

[codingnoye/gksdud](https://github.com/codingnoye/gksdud) 是一个 **macOS 输入法切换小工具**：把**右 ⌘**直接绑成**韩英切换**键。

### 痛点

- 想用**右 ⌘**当韩英切换键，过去只能装 **Karabiner-Elements** 再手写复杂修改。
- 即使改完了，**快速打字时经常掉字**——Karabiner 的拦截逻辑与 IME 的事件有时序冲突。

### 它的做法

装一个**独立应用**，**键映射 + 切换事件**都自己处理，不依赖 Karabiner 这种通用键盘重映射层。

## 为什么用它 / 适合什么场景

- **韩英双语用户**想用右 ⌘ 切输入法。
- 不愿意装 Karabiner（或装过发现掉字）。
- 想要一个**轻量、专注**的解决方案，不附带通用键盘改键的功能。

## 关键能力

| 能力 | 说明 |
|------|------|
| 独立应用 | 不依赖 Karabiner-Elements |
| 右 ⌘ 切韩英 | 单键切换，覆盖最常用场景 |
| 不掉字 | 自管事件序列，避开 Karabiner 的 IME 时序坑 |
| 轻量 | 不附通用改键 |

## 项目链接

- 仓库：<https://github.com/codingnoye/gksdud>

## 媒体

视频：<https://video.twimg.com/tweet_video/HSodH6laMAARvkw.mp4>

## 相关概念
