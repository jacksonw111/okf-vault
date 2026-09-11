---
type: "Tool"
title: "YourDesk（Go 写的 Mac/Windows 远控）"
description: "Go 写的远控工具：管 Mac 和 Windows，远端 ID 或 IP 直连，常用机器存成站台分组；画面走硬编硬解谈不拢自动降级，FPS / 码率 / 编解码状态全挂工具栏上，4K 屏可开 FSR / Core ML 放大。"
resource: "https://github.com/VaderChen/YourDesk"
tags: "[remote-desktop, go, macos, windows, h264, fsr]"
timestamp: "2026-09-11T22:05:00Z"
---

# YourDesk

## 它是什么

[VaderChen/YourDesk](https://github.com/VaderChen/YourDesk) 是一个 **Go** 写的**远程桌面工具**：管 Mac 和 Windows，远端 ID 或 IP 直连，常用机器存成「站台」分组管理。

## 画面与性能

| 维度 | 说明 |
|------|------|
| 编解码 | 两边都支持的**硬编硬解**（优先硬件） |
| 降级 | 谈不拢自动回落到软编码 |
| 状态可见 | FPS / 码率 / 编解码格式**全挂工具栏** |
| 4K 放大 | FSR / Core ML 放大 |
| Apple Silicon | 实验性补帧 |

## 为什么用它 / 适合什么场景

- 自建远控替代 TeamViewer / AnyDesk。
- 家里 Mac + Windows 混合环境，需要统一工具管。
- 想看硬编硬解状态来排查性能问题。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台 | macOS + Windows |
| 直连 | 远端 ID 或 IP |
| 站台分组 | 常用机器列表 |
| 硬件优先 | H264 / HEVC 硬编硬解 |
| 自动降级 | 硬件谈不拢回软编码 |
| 性能可视 | 工具栏显示 FPS / 码率 |
| 4K 放大 | FSR / Core ML |
| 补帧 | Apple Silicon 实验性 |

## 参考链接

- 项目仓库：<https://github.com/VaderChen/YourDesk>

## 媒体

- ![](https://pbs.twimg.com/media/HR5fAdNbgAAj2my.jpg)

## 相关概念

- [mobilecode](./tool-mobilecode.md) — 移动端 AI 编码内嵌模拟器
- [mobile-harness](./tool-mobile-harness.md) — 安卓端原生 AI 编码套件
- [panelui](./tool-panelui.md) — React Native 128 组件 UI 库
</content>
</invoke>