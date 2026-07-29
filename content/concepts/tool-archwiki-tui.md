---
type: Tool
title: "ArchWiki TUI（终端 Arch Wiki 浏览器）"
description: "Go 写的终端 Arch Wiki 浏览器。可以在 TTY 修引导参数时直接搜索和阅读 Arch Wiki 文章，不必启动 X11 开浏览器。"
resource: "https://github.com/Harshil-Anuwadia/archwiki-tui"
tags: [arch-linux, tui, go, wiki, terminal, recovery]
timestamp: "2026-07-29T13:07:00.000Z"
---

# ArchWiki TUI

## 它是什么

Go 写的 **终端里的 Arch Wiki 浏览器**。当你在 TTY 修引导参数 / 系统故障时，不用切到 X 打开浏览器，直接在终端里搜索 + 阅读 Arch Wiki 文章。

视频示例：
- <https://video.twimg.com/tweet_video/HOWbp-EbQAA1Uom.mp4>

## 解决的痛点

| 痛点 | ArchWiki TUI 解法 |
|------|------------------|
| 系统挂了，X 起不来 | TTY 直接读文档 |
| 引导参数不会改 | 边查 Arch Wiki 边改 |
| 没有图形界面 | 纯文本终端界面 |
| 翻手机查资料麻烦 | 本机终端随时查 |

## 关键能力

| 能力 | 说明 |
|------|------|
| TTY 原生运行 | 不依赖 X / Wayland |
| 搜索 + 阅读 | Arch Wiki 离线 / 在线皆可 |
| Go 编写 | 单二进制，复制就能跑 |
| 终端键位 | 致敬 vim / less 风格 |

## 适用场景

- Arch Linux 系统救援
- 服务器无 GUI
- 远程 SSH 调试
- 任何想"少开一个标签页"的场景

## 原始链接

- [项目仓库](https://github.com/Harshil-Anuwadia/archwiki-tui)
- [推文剪藏](https://x.com/QingQ77/status/2082452833379799448)

## 相关概念

- [Network Doctor（终端网络诊断链）](./tool-network-doctor.md) — 同样是 TUI 形态的"系统排障"工具
- [lazycron](./tool-lazycron.md) — Go 写的 Linux cron TUI 管理器
- [Plaza](./tool-plaza.md) — 跨发行版 TUI 包管理器
- [Lex Ghostty Shaders](./tool-lex-ghostty-shaders.md) — 给 Ghostty 终端加 shader 效果