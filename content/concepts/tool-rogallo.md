---
type: "Tool"
title: "Rogallo（终端版 Gemini 客户端）"
description: "Python 写的终端 Gemini 客户端：能搜书签和历史、前后翻页、设主页；自动识别用户输入中的敏感内容做掩码，自带自签名证书并按站点记住——纯 CLI 形态的浏览器。"
resource: "https://github.com/davep/rogallo"
tags: "[gemini, terminal, tui, browser, privacy]"
timestamp: "2026-07-20T20:20:00Z"
---

# Rogallo（终端版 Gemini 客户端）

## 它是什么

[davep/rogallo](https://github.com/davep/rogallo) 是用 **Python** 写的命令行 Gemini 客户端（运行在 [Gemini 协议](https://geminiprotocol.net/) 上，类似 Gopher 的现代复刻）。和主流 Web 浏览器不同，Rogallo 完全跑在终端里，主打低带宽 / 隐私保护。

## 关键能力

| 能力 | 说明 |
|------|------|
| 终端形态 | 纯 CLI / TUI，无图形界面 |
| 书签 / 历史搜索 | 可搜本地书签和历史前后翻页 |
| 主页自定义 | 自定义 `~/.config/rogallo/gmi.ini` 主页 |
| 敏感内容掩码 | 自动识别用户输入中的 token / 密码 / 手机号等敏感内容并打码 |
| 按站点记忆证书 | 自动生成自签名证书并按 host 记住，免每次都 `-y` |

![Rogallo 截图](https://pbs.twimg.com/media/HNg6HDkbQAAVnWW.jpg)

## 相关概念

- [wlocks](./tool-wlocks.md) — 终端进程 ↔ 文件描述符 TUI 工具，同为「极简终端互联网工具」方向
- [NaviTui](./tool-navitui.md) — 终端 Navidrome 音乐播放器
- [tmux-spotlight](./tool-tmux-spotlight.md) — fzf 版 tmux 切换器

## 参考链接

- 项目链接: <https://github.com/davep/rogallo>
