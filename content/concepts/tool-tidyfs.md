---
type: "Tool"
title: "TidyFS（Linux 智能文件整理工具）"
description: "Go + Python 混编的 Linux 智能文件整理工具，能扫描文件夹按内容与文件名自动归类，TUI 展示或直接整理到分类目录。"
tags: "[linux, file-management, tui, go, python]"
timestamp: "2026-06-28T08:24:00Z"
resource: "https://github.com/xSarumo/TidyFS"
---

# TidyFS（Linux 智能文件整理工具）

## 它是什么

TidyFS 是面向 Linux 的**智能文件整理工具**，核心扫描引擎用 Go 写、分类逻辑用 Python 写。它会扫指定文件夹里的文档，按内容与文件名特征自动归类，在 TUI 里展示分类结果，或一键整理到分类目录。

## 关键能力

| 能力 | 说明 |
|------|------|
| 内容感知 | 读文档正文判定主题（不只按后缀） |
| 文件名辅助 | 结合命名约定做粗分类 |
| TUI 预览 | 终端界面浏览分类结果再决定是否整理 |
| 一键整理 | 确认后按分类目录移动文件 |
| Go + Python 混合 | Go 负责 I/O 密集扫描，Python 负责灵活分类规则 |

## 适用场景

- Downloads 文件夹长期积累的 PDF / Markdown 整理
- 学术笔记批量归类
- NAS 上「散落各处的发票 / 合同 / 学习资料」自动入档

## 界面预览

![TidyFS 整理视图](https://pbs.twimg.com/media/HL3fUQjbEAAyf9D.jpg)

## 参考链接

- [项目仓库](https://github.com/xSarumo/TidyFS)
- [原始链接](https://x.com/QingQ77/status/2071147590088114296)

## 相关概念

- [Forel（macOS 文件夹自动化）](tool-forel-macos.md) — 同类思路的 macOS 实现，用 FSEvents 实时监控
- [DeskBox](tool-deskbox.md) — Windows 上的文件收集与文件夹映射工具
- [Targie](tool-targie-similar-finder.md) — 重复 / 相似文件扫描，与 TidyFS 互补做整理前的去重