---
type: Tool
title: "macos-sysdata"
description: "macOS 菜单栏小工具，逐条展开「系统设置 → 系统数据」里最大的那块存储占用，能识别能删的直接给清理入口。"
resource: "https://github.com/Jarvis322/macos-sysdata"
tags: "[macos, storage, cleanup, menu-bar, swiftui]"
timestamp: "2026-09-07T13:05:00Z"
---

# macos-sysdata

## 它是什么
macOS 菜单栏小工具，专门对付「系统设置 → 通用 → 储存空间」里那块最神秘、最占空间、又叫不出名字的"系统数据"。逐条展开里面的内容（缓存、临时文件、可清除快照、本地 Time Machine 等），可清理的项直接给清理入口。

## 痛点
macOS 自带的「系统数据」分类把太多东西糅在一起，普通用户根本看不到里面是什么、能删什么。

## 关键能力
| 能力 | 说明 |
|------|------|
| 逐条展开 | 把"系统数据"分类拆解为具体条目 |
| 容量可视化 | 每条占用多少一目了然 |
| 清理入口 | 可删项直接给操作按钮 |
| 菜单栏驻留 | 不占 Dock，按需点开 |

## 参考
- 项目链接：<https://github.com/Jarvis322/macos-sysdata>

## 相关概念
- [MacTools](tool-mac-tools.md) — 另一个 macOS 菜单栏工具集合
- [Uninstally](tool-uninstally.md) — macOS 卸载工具，配合清理残留
- [WinTrash](tool-wintrash.md) — Windows 版的"残留扫描"思路同源