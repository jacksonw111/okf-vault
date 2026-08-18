---
type: Tool
title: "dsh-desktop (dataelement/dsh-desktop)"
description: "用 Electron 把 DeepSeek Harness web 界面封装为桌面应用的另一个变体：启动时自动拉 Harness 子进程、随机回环端口、存好 profiles / plugins / sessions"
resource: "https://github.com/dataelement/dsh-desktop"
tags: [deepseek, harness, dsh, electron, desktop, cross-platform]
timestamp: "2026-08-18T12:00:00Z"
---

# dsh-desktop (dataelement/dsh-desktop)

## 它是什么
`dataelement/dsh-desktop` 是 DeepSeek Harness (DSH) 的又一款桌面封装：Electron 把官方 Web 界面打包进原生窗口，支持 macOS（Apple Silicon / Intel）与 Windows x64。区别于另两款 dsh-desktop 变体，它**自动管理 Harness 子进程 + 端口**：启动时拉一个 Harness 子进程、随机挑一个回环端口、存好 profiles / plugins / sessions，UI 就绪后自动开窗，**省去用户先敲 CLI 的麻烦**。

## 为什么用它 / 适合什么场景
- 想用 DSH 又不想每次手动起命令行 + 记端口。
- profiles / plugins / sessions 需要在「桌面常驻」之间复用，桌面壳自己管更省心。
- 已经在 macOS / Windows 桌面环境，希望「装上就能用」而非手动配 Node / CLI。

## 关键能力
| 能力 | 说明 |
|------|------|
| Electron 桌面壳 | macOS / Windows 双平台原生窗口 |
| 自动启子进程 | 启动时拉起 Harness 子进程 |
| 随机回环端口 | 自动挑端口，避开本地冲突 |
| 配置持久化 | profiles / plugins / sessions 自动落地 |
| 自动开窗 | UI 就绪后自动弹出，不用手动 `localhost:xxxx` |

## 媒体
- ![](https://pbs.twimg.com/media/HP5FhakbAAAO2gG.jpg)

## 相关概念
- [项目链接](https://github.com/dataelement/dsh-desktop) — 仓库地址
- [dsh-desktop (bruc3van)](./tool-dsh-desktop.md) — 另一款「把官方 Web UI 原样装进窗口」的 dsh-desktop 变体
- [DeepSeek-Harness-Desktop (sleep2agi)](./tool-deepseek-harness-desktop-shell.md) — 同类桌面壳变体，关注 macOS / Windows 跨平台
- [deepseek-harness-desktop (steven-kid)](./tool-deepseek-harness-desktop.md) — 同类桌面壳变体，定位「免配置」
