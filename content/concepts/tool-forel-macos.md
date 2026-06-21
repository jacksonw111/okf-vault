---
type: "Tool"
title: "Forel（macOS 文件夹自动化工具）"
description: "开源 macOS 菜单栏应用，自动整理指定文件夹里的文件：基于 FSEvents 实时监控，按文件名 / 后缀 / 类型 / 大小 / 日期 / 标签 / 颜色匹配规则，自动执行移动 / 复制 / 重命名 / 标记 / 删除 / 跑脚本 —— 号称 Hazel 平替，全本地运行无需订阅。"
resource: "https://github.com/qingq77/forel"
tags: "[macos, automation, file-management, hazel-alternative]"
timestamp: "2026-06-21T00:00:00Z"
---

# Forel（macOS 文件夹自动化工具）

## 它是什么

macOS 工具：**Forel** —— 菜单栏应用，专门做「自动整理文件夹」。号称 Hazel 的开源平替，全本地运行、无需订阅。

## 关键能力

| 能力 | 说明 |
|------|------|
| 规则维度 | 文件名 / 后缀 / 类型 / 大小 / 日期 / 标签 / 颜色 |
| 触发机制 | 原生 FSEvents 实时监控（不是轮询） |
| 自动操作 | 移动 / 复制 / 重命名 / 标记 / 删除 / 跑脚本 |
| 部署 | macOS 菜单栏 App，开源 |

## 与 Hazel 的差异

| 维度 | Forel | Hazel |
|------|-------|-------|
| 价格 | 免费开源 | 付费（约 $50） |
| 运行 | 全本地 | 全本地 |
| 功能深度 | 基本覆盖 | 更深（带 OCR / 自动标签 / iCloud 集成） |
| 触发 | FSEvents | FSEvents |

## 适用场景

- 桌面 / 下载 / 截图文件夹每天爆满 —— 设规则自动分类归档。
- 不想给 Hazel 付费 —— Forel 是开源替身。
- 自动化任务可以接受「文件名 / 后缀」级别的规则，不强求 Hazel 的高级 OCR。

## 媒体

![Forel 截图](https://pbs.twimg.com/media/HLJUkt9a4AAaNS3.jpg)

## 相关概念

- [OmniWM（macOS 水平滚动平铺 WM）](tool-omniwm-macos.md) — 同为「macOS 本地优先小工具」
- [Biome](tool-biome.md) — 同为「工具碎片化 → 一体化」思路的对照参考