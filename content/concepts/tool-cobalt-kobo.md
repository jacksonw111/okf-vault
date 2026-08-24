---
type: Tool
title: "Cobalt（BandarLabs Kobo 应用平台）"
description: "BandarLabs 用 Rust 写的 Kobo 电子书应用平台：启动器 + 应用商店 + Rust SDK + 运行时 + 浏览器内 Clara BW 模拟器。"
resource: "https://github.com/BandarLabs/Cobalt"
tags: [kobo, e-ink, rust, sdk, simulator, embedded]
timestamp: "2026-08-24T00:16:00Z"
---

# Cobalt（BandarLabs Kobo 应用平台）

## 它是什么

[BandarLabs/Cobalt](https://github.com/BandarLabs/Cobalt) 是 BandarLabs 用 Rust 写的 Kobo 电子书（E-Ink 设备）应用平台。组成包括：

- **启动器（Launcher）**：替换 Kobo 原生主屏
- **应用商店**：在设备内分发第三方 App
- **Rust SDK**：开发 Kobo 应用的 Rust 工具链
- **运行时（Runtime）**：App 在 Kobo 上的执行环境
- **浏览器内模拟器**：在网页里模拟 Clara BW（N365）设备，无需真机即可开发调试

实测支持的机型为 Kobo Clara BW（N365）和 Elipsa 2E（N605）。

## 为什么用它 / 适合什么场景

- 想给 Kobo 设备开发第三方应用（读书器 / 笔记 / 工具），但不愿用 C/C++ 与原生 SDK。
- 想在桌面浏览器里用模拟器调试，省去每次刷真机的麻烦。
- 想参与 Kobo「类第三方生态」的早期建设。

## 关键能力

| 能力 | 说明 |
|------|------|
| Rust SDK | 用 Rust 而非 C 写 Kobo App |
| 浏览器模拟器 | 在网页里跑 Clara BW 模拟器做开发调试 |
| 应用商店 | 设备内分发第三方 App |
| 运行时 | 负责内存 / 资源 / 事件循环管理 |
| 启动器 | 替换默认主屏作为 App 入口 |

## 相关概念

- [InkBoard](./tool-inkboard.md) — 墨水屏专用桌面 HOME，配套软件
- [Apollo ESP32 Voice](./tool-apollo-esp32-voice.md) — 同类嵌入式 Rust 平台思路

## 参考链接

- [项目链接](https://github.com/BandarLabs/Cobalt)
- ![](https://pbs.twimg.com/media/HQYEXxGb0AAAe0p.jpg)