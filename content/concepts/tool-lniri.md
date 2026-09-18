---
type: Tool
title: "Lniri（Niri 液态玻璃窗口效果）"
description: "为 Niri 滚动平铺 Wayland 合成器的窗口加可配置的液态玻璃折射与背景效果，Rust + GLSL 实现，可在 liquid 水滴与 kwin-glass 玻璃两套模式间切换。"
resource: "https://github.com/TattvaOrg/Lniri"
tags: [niri, wayland, compositor, linux, ricing, shader, glsl, rust]
timestamp: 2026-09-18T01:25:00Z"
---

# Lniri（Niri 液态玻璃窗口效果）

## 它是什么

[TattvaOrg/Lniri](https://github.com/TattvaOrg/Lniri) 是给 [Niri](https://github.com/YaLTeR/niri)（一款**滚动平铺 Wayland 合成器**）做的窗口背景效果插件。它把 Rust 和 GLSL 钩进 Niri 的窗口渲染管线，给窗口加上**液态玻璃**式的折射、模糊、背景扰动效果。

## 关键能力

| 能力 | 说明 |
|------|------|
| 液态玻璃效果 | 模拟水滴 / 玻璃的折射与背景模糊 |
| 两种内置模式 | `liquid`（水滴）与 `kwin-glass`（KDE 风格的玻璃） |
| 可配置 | 折射强度、模糊半径等参数可调 |
| Rust + GLSL | 核心逻辑用 Rust，着色器用 GLSL |

## 适合什么场景

- 已经在用 [Niri](https://github.com/YaLTeR/niri) 滚动平铺 Wayland 桌面、想要「视窗后面能看到淡淡折射背景」的视觉效果。
- 喜欢 ricing、想把 Wayland 桌面调到 macOS / KDE 那种玻璃质感、但又不肯切换合成器的用户。
- 想研究「如何给 Wayland 合成器做窗口级 shader 渲染」的开发者。

## 参考

- 项目链接：<https://github.com/TattvaOrg/Lniri>

![液态玻璃效果演示](https://pbs.twimg.com/media/HSa_XjGbIAAhoiz.jpg)
