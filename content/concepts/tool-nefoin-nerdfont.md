---
type: "Tool"
title: "Nefoin（一键安装 Nerd Font 的 CLI）"
description: "Nefoin = 轻量 Nerd Font 安装器：传一个字体名字就自动下载、解压、装好；依赖只有 fontconfig + curl + unzip，macOS / Linux 都能跑，免手动 clone 仓库 / 解 .zip。"
resource: "https://github.com/monoira/nefoin"
tags: "[nerd-font, cli, font, terminal, dev-tools, install]"
timestamp: "2026-06-21T16:11:00Z"
---

# Nefoin（一键安装 Nerd Font 的 CLI）

## 它是什么

**Nefoin**：一个轻量的 **Nerd Font 安装命令行工具**。传一个字体名字就自动下载、解压、装好。**免手动下载或克隆仓库**、免手动解压 .zip、免手动 `cp` 到 `~/.local/share/fonts/`。

## 为什么用它 / 适合什么场景

- 终端 / Vim / Neovim / tmux 状态栏想用 Nerd Font 图标，但不想每次手动装。
- 写 setup 脚本想「一键把开发字体装齐」，需要可编程方式。
- 只想装特定字体（不是全套 ~80 个 Nerd Font），不想浪费磁盘。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | 字体名（如 `JetBrainsMono`、`FiraCode`、`Hack`） |
| 操作 | 自动下载 → 解压 → 装到系统字体目录 |
| 依赖 | 仅 fontconfig + curl + unzip |
| 平台 | macOS + Linux |

## 与手动安装对比

| 步骤 | 手动 | Nefoin |
|------|------|--------|
| clone nerd-fonts 仓库 | ✓ | ✗ |
| 找字体 zip | ✓ | ✗ |
| 解压到 fonts 目录 | ✓ | ✗ |
| fc-cache 刷新 | ✓ | 内置 |
| 选字体 | 编辑文件名 | 传一个名字 |

## 媒体

- 视频演示：<https://video.twimg.com/tweet_video/HLQiBtRbgAEOELO.mp4>

## 相关概念

- [Biome](tool-biome.md) — 同为「少配置、能跑就行」的轻量 CLI 工具哲学
- [Lefthook](tool-lefthook.md) — 同为「开发体验中必备的轻量 CLI」