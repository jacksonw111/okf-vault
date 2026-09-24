---
type: "Tool"
title: "Better Night Light（Android 夜览分时段调度）"
description: "不少 ROM 的 Night Light 只有「日落开、日出关」一个开关，没有分时段强度和调度。Better Night Light 借 ADB / Shizuku / root 权限直接接管系统原生 Night Light，把夜间拆成多段分别调色温。"
resource: "https://github.com/paulsnuff/BetterNightLight"
tags: "[android, night-light, color-temperature, adb, shizuku, root, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# Better Night Light（Android 夜览分时段调度）

## 它是什么

[Better Night Light](https://github.com/paulsnuff/BetterNightLight) 是一个 Android 工具：原生 Night Light 通常只提供「日落开、日出关」一个开关，无法分时段调整强度。Better Night Light 借 ADB / Shizuku / root 权限直接接管系统原生 Night Light，**把夜间拆成多段分别调色温**（如「22:00 偏暖 / 02:00 更暖 / 05:00 渐亮」）。

## 它解决的问题

- 不少 ROM 自带的 Night Light 没有「分时段强度 / 调度」功能
- 想按时间段精细控制色温（比如深夜更深更暖 / 凌晨渐亮）
- 想接管而不是替换系统原生 Night Light（避免额外耗电）

## 权限要求

| 方式 | 说明 |
|------|------|
| ADB | 通过 USB / 无线 ADB 调试 |
| Shizuku | 在系统层授权，免 root |
| root | 直接写系统设置 |

## 适用场景

- 重度屏幕用户 / 程序员想按精细化曲线调色温
- 深夜写作 / 阅读想比「日落开关」更深的暖色
- 凌晨渐亮以避免被冷色屏幕「打激灵」醒来

## 原始链接
- 项目主页：<https://github.com/paulsnuff/BetterNightLight>

## 相关概念