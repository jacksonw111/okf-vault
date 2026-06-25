---
type: Tool
title: "Seahi-Serial（多串口调试工具）"
description: "VS Code Serial Monitor 风格的多串口调试工具，可同时连多路串口、自定义配置，支持 ANSI 颜色显示。"
resource: "https://github.com/SeaHi-Mo/Seahi-Serial"
tags: [embedded, serial, debug, vscode]
timestamp: "2026-06-25T03:21:00Z"
---

# Seahi-Serial（多串口调试工具）

## 它是什么

一款仿照 VS Code Serial Monitor 风格的多串口调试工具。日常嵌入式调试时常常需要**同时盯着多路串口**（例如同时看 MCU 主日志 + 模组日志 + GPS 输出），而一般串口工具一次只开一个窗口——它解决这个问题。

## 为什么用它 / 适合什么场景

- **嵌入式开发**：MCU、ESP32、模组联调阶段。
- **多设备并行调试**：比如一份代码要跑在 N 个板子上同时观察。
- **自定义配置**：每路串口的波特率、数据位、停止位独立配置。
- **ANSI 颜色**：日志里靠 ANSI 颜色区分类别，比肉眼数 `[INFO]`/`[ERR]` 更省眼。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多串口并行 | 同时连多路 |
| 独立配置 | 每路串口可设波特率 / 数据位 / 停止位等 |
| ANSI 颜色 | 输出日志带颜色高亮 |
| VS Code 风格 | 界面仿照 Serial Monitor |

## 相关概念

- [ESPHome Guition 语音助手旋钮屏](./tool-esphome-guition-va.md) — 同属嵌入式 / 物联网开发场景，Seahi-Serial 是 PC 端调试，Guition 是设备端落地