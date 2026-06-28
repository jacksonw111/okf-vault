---
type: "Tool"
title: "Plex TUI"
description: "Python 写的终端 Plex 客户端，三栏布局（左库列表 / 中海报详情 / 右播放信息）全键盘浏览与播放视频，支持 Kitty/Ghostty 原生图片显示与 mpv 解码。"
tags: "[plex, tui, terminal, mpv, python]"
timestamp: "2026-06-28T06:23:00Z"
resource: "https://github.com/so1omon563/plex-tui"
---

# Plex TUI

## 它是什么

Plex TUI 是用 **Python** 写的 Plex 媒体服务器**终端客户端**，把 Plex Web 那套「翻海报、选电影、播放」的体验移植到 TTY 里。三栏布局：

- **左**：媒体库列表（电影 / 剧集 / 音乐）
- **中**：当前选中条目的海报 + 详情
- **右**：播放状态与进度

全键盘操作（vim 风格），海报与剧照通过 **Kitty / Ghostty 终端的原生图像协议**直接显示在 TUI 里。

## 关键能力

| 能力 | 说明 |
|------|------|
| 三栏 TUI 布局 | 库 / 详情 / 播放三栏可视 |
| mpv 播放 | 调用外部 mpv 解码视频，兼容几乎所有格式 |
| 原生图片显示 | 支持 Kitty / Ghostty 终端图像协议，海报直显 |
| Plex 浏览器登录 | 走标准 Plex 账号 OAuth，无需手填 token |
| 续播 / 搜索 / 诊断 | 三个常用操作内置快捷键 |
| 多渠道分发 | Homebrew / PyPI / AUR 三处可装 |

## 安装

```bash
brew install plex-tui        # macOS / Linuxbrew
pip install plex-tui         # PyPI
yay -S plex-tui              # Arch / AUR
```

## 界面预览

![Plex TUI 三栏布局](https://pbs.twimg.com/media/HL3fME4aQAA2Y7S.jpg)

## 参考链接

- [项目仓库](https://github.com/so1omon563/plex-tui)
- [原始链接](https://x.com/QingQ77/status/2071117139520495706)

## 相关概念

- [LX Music Desktop](tool-lx-music-electron.md) — 桌面音乐播放器，TUI 之外的另一类本地优先媒体工具
- [Ember（Hacker News 阅读器）](tool-ember-hackernews.md) — 同样追求「原生体验 + 零依赖」的本地优先客户端