---
type: "Tool"
title: "doubao-say"
description: "为 Linux / Wayland 桌面提供豆包云识别驱动的全局语音输入，GTK4 + Python 写的，按触发键说话松手即把识别文本粘贴到当前应用；支持 System / English / 简体中文三档语言切换，Omarchy 用户装插件版。"
resource: "https://github.com/quanru/doubao-say"
tags: "[linux, wayland, voice-input, gtk4, python, doubao, omarchy]"
timestamp: "2026-09-16T16:03:00Z"
---

# doubao-say

## 它是什么

[quanru/doubao-say](https://github.com/quanru/doubao-say) 是跑在 **Linux / Wayland 桌面**上的全局语音输入工具，**GTK4 + Python** 实现，识别后端调用豆包云端。默认界面是英文，可切 System / English / 简体中文三档，选完自动记住。Omarchy 用户可直接装插件版，底层是同一个程序。

## 工作方式

按触发键开始说话，松手或再按一次触发键就把识别出来的文字直接粘贴到当前焦点应用，无需手动复制。

## 关键能力

| 能力 | 说明 |
|------|------|
| Linux / Wayland 原生 | GTK4 适配 Wayland 全局快捷键与会话 |
| 豆包云识别 | 国内低延迟、识别中文友好 |
| 多档语言 | System / English / 简体中文可切，记忆选择 |
| Omarchy 插件版 | 在 Omarchy 桌面上一键安装 |
| 跨语言混输 | 切换 System 模式后跟系统输入语言走 |

## 相关概念

- [OmniStudio](./tool-omnistudio.md) — 本地大模型一站式桌面工作台，与 doubao-say 一起补齐 Linux 输入体验