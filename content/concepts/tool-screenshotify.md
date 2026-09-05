---
type: Tool
title: "Screenshotify"
description: "常驻 Windows 托盘 / macOS 菜单栏的截图监控工具，调用用户自选视觉模型生成描述性文件名，建议先入待审、确认后才重命名"
resource: "https://github.com/shaqkao/screenshotify"
tags: [screenshot, ai, vision, rename, tray, desktop]
timestamp: 2026-09-05T15:00:00Z
---

# Screenshotify

## 它是什么
`shaqkao/screenshotify` 是一款**自动截图文件重命名工具**：常驻 Windows 系统托盘或 macOS 菜单栏，监控截图文件夹，发现新截图后调用用户**自选的视觉模型**生成描述性文件名，所有建议先入**待审列表**，人工逐条确认 / 编辑 / 跳过才真正改名，撤销一直可用；也支持批量扫描已有的旧截图文件夹。

## 为什么用它 / 适合什么场景
- 截图文件夹长期堆积 `Screenshot 2026-09-05 at 12.34.56.png`，事后想搜回根本找不到。
- 想把截图直接以「内容描述」作为文件名（如「chart-Q3-revenue.png」），便于检索与归档。
- 希望 AI 只是「建议」，**最终决定权留给人**，且可一键撤销。

## 关键能力
| 能力 | 说明 |
|------|------|
| 截图文件夹监控 | 自动发现新增截图 |
| 用户自选视觉模型 | 任意接入 OpenAI 兼容视觉模型 |
| 待审列表 | AI 建议先入队，人工确认 / 编辑 / 跳过 |
| 撤销机制 | 改名历史可回滚 |
| 旧文件夹批量扫描 | 对存量截图一次性补名 |
| 跨平台常驻 | Windows 托盘 + macOS 菜单栏 |

## 媒体
- ![](https://pbs.twimg.com/media/HRYYgMka4AASM4E.jpg)
- ![](https://pbs.twimg.com/media/HRYYg5YbsAElx3K.jpg)

## 相关概念
- [原始链接](https://github.com/shaqkao/screenshotify)