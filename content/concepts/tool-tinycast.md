---
type: Tool
title: "Tinycast（macOS 原生轻量启动器 + 剪贴板历史）"
description: "macOS 上缺少一个轻量、原生、无 Electron 依赖的启动器与剪贴板历史工具。Tinycast 是纯原生 macOS 启动器（约 3 MB、<100 MB 内存），Swift + SwiftUI/AppKit 写，零第三方依赖。支持模糊搜索启动应用、内置计算器、可搜索的剪贴板历史、全局快捷键与按应用绑定快捷键。"
resource: "https://github.com/abue-ammar/tinycast"
tags: [macos, launcher, clipboard, swift, native, productivity]
timestamp: "2026-07-30T07:43:00.000Z"
---

# Tinycast

## 它是什么

**macOS 原生轻量启动器 + 剪贴板历史**——3 MB 二进制，<100 MB 内存，零 Electron 依赖：

- 模糊搜索启动应用（Alfred / Raycast 风格）
- 内置计算器（表达式即结果）
- 可搜索的剪贴板历史
- 全局快捷键
- 按应用绑定快捷键（每个 App 一组动作）

![截图](https://pbs.twimg.com/media/HOXardcb0AAjvIQ.jpg)

## 与 Raycast / Alfred 的差异

| 维度 | Alfred / Raycast | Tinycast |
|------|------------------|----------|
| 安装体积 | 大（几百 MB） | ~3 MB |
| 内存占用 | 几百 MB | <100 MB |
| 依赖 | Electron / 内置 Chromium | 纯原生 Swift |
| 启动速度 | 一般 | 极快 |
| 扩展生态 | 丰富 | 极简 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 模糊应用启动 | 打字即搜 |
| 计算器 | 表达式直接出结果 |
| 剪贴板历史 | 可搜索，可回贴 |
| 全局快捷键 | 自己定义 |
| 按应用快捷键 | 每个 App 一组动作 |
| 零依赖 | Swift + SwiftUI/AppKit |

## 适合谁

- 想替代 Alfred / Raycast 但更轻量的 Mac 用户
- 老款 Mac（内存紧张）的用户
- 喜欢「工具就该小而美」的极简派
- 不想装付费订阅 / 商店扩展的人

## 原始链接

- [项目仓库](https://github.com/abue-ammar/tinycast)
- [推文剪藏](https://x.com/QingQ77/status/2082733686014005408)

## 相关概念

- [CloseUp](./tool-closeup.md) — macOS 给 Mission Control 缩略图加关闭 / 最小化按钮
- [MacTools](./tool-mac-tools.md) — macOS 菜单栏工具集，30+ 小工具
- [Forel](./tool-forel-macos.md) — Hazel 开源平替，FSEvents 实时监控文件夹