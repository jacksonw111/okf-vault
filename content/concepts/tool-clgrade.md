---
type: "Tool"
title: "clgrade（Rust 终端调色工具）"
description: "Rust 写的终端原生调色工具，界面用 Ratatui，图像显示靠 chafa；五页切换——曝光白平衡滑杆、色轮、Scopes 波形、Pipeline 调色顺序、Presets 预设。"
resource: "https://github.com/Cladamos/clgrade"
tags: "[rust, terminal, color-grading, ratatui, chafa, tui]"
timestamp: "2026-09-12T22:30:00Z"
---

# clgrade

## 它是什么

[Cladamos/clgrade](https://github.com/Cladamos/clgrade) 是一个**终端原生调色工具**：Rust + Ratatui 写 UI，图像显示靠 chafa 把图渲染到终端，五页可切换：

| 页面 | 用途 |
|------|------|
| 滑杆页 | 拉曝光 / 白平衡 |
| 色轮页 | 推偏色 |
| Scopes | 看波形 / 直方图 |
| Pipeline | 排调色节点顺序 |
| Presets | 存 / 调自己的预设 |

## 为什么用它 / 适合什么场景
- 喜欢全键盘操作、不想开 Lightroom / DaVinci。
- 服务器 / SSH 远程环境下没有 GUI，调色还是要做。
- 想把调色工作流接到脚本 / CI 里自动化。

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端 UI | Ratatui，全键盘 |
| 图像显示 | chafa 转 ANSI / 字符画 |
| 多页面 | 曝光 / 色轮 / Scopes / Pipeline / Presets |
| 预设管理 | 存 / 复用 |
| 跨平台 | Rust 写，到处跑 |

## 参考链接

- 项目仓库：<https://github.com/Cladamos/clgrade>

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HR5yMBda0AARS9e.mp4>

## 相关概念
