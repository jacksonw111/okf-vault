---
type: Tool
title: "dsh-harmonyos-pc（让 DeepSeek Harness 完整跑在鸿蒙 PC 上）"
description: "把 DeepSeek Harness（DSH）全套能力迁移到 HarmonyOS PC 平台，让鸿蒙笔记本用户无需绕道 Linux 虚拟机就能用 DSH 的 Agent / 插件生态。"
resource: "https://github.com/Entity-Him/dsh-harmonyos-pc"
tags: [deepseek-harness, dsh, harmonyos, hongmeng, cross-platform, agent, pc]
timestamp: "2026-08-28T00:00:00Z"
---

# dsh-harmonyos-pc

## 它是什么
[Entity-Him/dsh-harmonyos-pc](https://github.com/Entity-Him/dsh-harmonyos-pc) 是**让 DeepSeek Harness（DSH）原生跑在 HarmonyOS PC** 上的移植项目。背景：DSH 官方主要面向 Linux / macOS / Windows 三端，而鸿蒙 PC（HarmonyOS NEXT PC 端）走的是 ArkTS / 鸿蒙原生 API，DSH 的 Python 运行时、Node 插件、桌面壳生态没法直接复用。

dsh-harmonyos-pc 把 DSH 的核心运行时搬到鸿蒙 PC 上，使得：

- 鸿蒙 PC 用户**不用装 Linux 虚拟机**也能用 DSH；
- 现有 DSH 插件市场（800+ 社区插件）可继续发挥作用；
- 配合 DSH 桌面壳项目（[dsh-desktop](tool-dsh-desktop.md) / [dsh-desktop-dataelement](tool-dsh-desktop-dataelement.md)）可在鸿蒙 PC 上获得接近 Linux 的体验。

## 为什么用它 / 适合什么场景
- 鸿蒙 PC 主力开发 / 学习者想直接用 DSH 而不切系统；
- 鸿蒙 PC 生态想接住 DSH 的 800+ 插件 / Skills 资产；
- 跨平台团队里有人用鸿蒙 PC、有人用 macOS / Linux / Windows，希望**同一套 Agent Harness** 协作。

## 关键能力
| 能力 | 说明 |
|------|------|
| 鸿蒙 PC 移植 | DSH 核心运行时在 HarmonyOS PC 上跑通 |
| 插件兼容 | 800+ DSH 社区插件继续可用 |
| 跨端协作 | 与 Linux / macOS / Windows 上的 DSH 用户同一份工作流 |
| 零虚拟机 | 无需 Linux 虚拟机 / 远程服务器转发 |
| 原生集成 | 与鸿蒙 PC 的文件系统、应用生态原生对接 |

## 相关概念
- [DSH Desktop](tool-dsh-desktop.md) — DSH 官方 Web UI 装进原生桌面窗口；dsh-harmonyos-pc 是其**鸿蒙 PC** 版本
- [DSH Desktop Dataelement](tool-dsh-desktop-dataelement.md) — 另一款 Electron 封装的 DSH 桌面壳，与 dsh-harmonyos-pc 形成多端矩阵
- [DeepSeek Harness Desktop](tool-deepseek-harness-desktop.md) — 把官方 Web 界面打包成跨平台桌面应用

## 参考链接
- 项目链接：<https://github.com/Entity-Him/dsh-harmonyos-pc>
- 原始推文：<https://x.com/QingQ77/status/2093320191241527419>
- 媒体：<https://pbs.twimg.com/media/HQtOFOXbQAAnpuX.jpg>
