---
type: "Tool"
title: "dj-usb-tkit（haivala/dj-usb-tkit）"
description: "本地跑的 DJ 曲库管家:歌单整理 → 直接写入 Pioneer DJ USB 盘;同时能分析 / 诊断 / 修复坏掉的库,适合 DJ 与演出场景。"
resource: "https://github.com/haivala/dj-usb-tkit"
tags: "[dj, music, usb, pioneer, library-manager, local]"
timestamp: "2026-07-14T13:26:00Z"
---

# dj-usb-tkit

[dj-usb-tkit](https://github.com/haivala/dj-usb-tkit) 是本地跑的 **DJ 曲库管家**:把曲库整理成可演出格式后**直接写到 Pioneer DJ USB 盘**,同时能分析、诊断、修坏掉的库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 曲库整理 | 批量改名前缀 / 加流派 tag / 文件夹归类 |
| 写入 USB | 把整套曲库写到 Pioneer DJ 兼容的 USB 盘 |
| 坏库诊断 | 揪出断码 / 损坏 / 路径错误等问题 |
| 修复工具 | 改前缀 / 修 ID3 / 重命名 |
| 本地优先 | 不上传,数据全在本地 |

## 适合什么场景

- 演出 DJ 想**标准化 USB 库**(Pioneer CDJ / XDJ 系列)。
- 个人曲库从各处杂糅 → 想统一到 USB-ready 结构。
- 遇到 CDJ 报「track not found」等需要排查损坏文件。

## 与同类资源的差别

| 资源 | 特征 | dj-usb-tkit |
|------|------|-------------|
| NaviTui | TUI 音乐播放器(Navidrome) | 播放;dj-usb-tkit 是管理 / 写盘 |
| Orca Music Player | Svelte + Tauri 本地音乐播放器 | 播放 |
| MoChord | 和弦创作工作台 | 创作 |

## 参考链接

- [项目仓库](https://github.com/haivala/dj-usb-tkit)
