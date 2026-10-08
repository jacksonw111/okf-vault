---
type: "Term"
title: "Omarchy（Arch + Hyprland 一体化桌面发行版）"
description: "basecamp 推出的 Linux 桌面发行版：基于 Arch Linux + Hyprland 合成器，把美化主题、键盘流、默认应用、Web/AI 工作流打包成一个开箱即用、风格统一的桌面系统。"
resource: "https://omarchy.org/"
tags: "[omarchy, arch-linux, hyprland, linux-distro, desktop-environment, ricing]"
timestamp: "2026-10-08T23:40:00Z"
---

# Omarchy

## 定义

**Omarchy** 是 basecamp（DHH 团队）推出的一款 Linux 桌面发行版：基于 **Arch Linux + Hyprland 合成器**，把「美化主题、键盘优先流、默认应用、Web/AI 工作流」打包成一套开箱即用、视觉风格统一的桌面系统。

它的目标不是「让你自己折腾配置」，而是「一次性给你一套 DHH 风格的、有审美的、能立刻干活的桌面」。

## 要点

- **基座**：Arch Linux + Hyprland（平铺 Wayland 合成器）
- **形态**：iso / 镜像化发行版，安装即用，不要求用户从零 `pacman` 配置
- **默认美学**：Mac-like 圆角 + Hyprland 动画 + 统一配色主题（多套可选）
- **默认流**：键盘优先、Tiling、终端为王、Web/AI 工作流集成
- **生态**：围绕它诞生了一大批周边工具（[OmaControl](./tool-omacontrol.md) 顶栏任务管理器、[Omarchy Mac Starter](./tool-omarchy-mac-starter.md) macOS 触感套件、[omacvm](./tool-omacvm.md) Apple Silicon 虚拟机方案、[omashow](./tool-omashow.md) 等）
- **目标用户**：Linux 老手想要「省去自己 rice 的麻烦」、Mac 用户想平迁到 Linux 又不想从零配 Hyprland

## 项目链接

- 官网：<https://omarchy.org/>
- 源码：<https://github.com/basecamp/omarchy>

## 相关概念

- [OmaControl](./tool-omacontrol.md) — Omarchy 顶栏任务管理器
- [Omarchy Mac Starter](./tool-omarchy-mac-starter.md) — 给 Omarchy 套一层 macOS 操作手感
- [omacvm](./tool-omacvm.md) — 把 Omarchy 跑在 Apple Silicon Mac 上
- [Impasto](./tool-impasto-arch-hyprland.md) — 同生态（Arch + Hyprland）另一套开箱即用 Quickshell 桌面