---
type: "Tool"
title: "Dfetch（David17c/Dfetch）"
description: "Go 写的轻量系统信息小工具，neofetch 风格但启动更快、显示更干净；12 种 Linux 发行版 ASCII 标志，无外部依赖。"
resource: "https://github.com/David17c/Dfetch"
tags: [cli, linux, system-info, go, dotfiles]
timestamp: "2026-06-23T15:30:00Z"
---

# Dfetch（David17c/Dfetch）

## 它是什么

一个 Go 写的命令行小工具，定位类似 neofetch 但更轻：显示用户、系统、内核、Shell、桌面环境、CPU、内存、磁盘等基本信息，输出干净、启动飞快，配置项简单到不需要文档也能看懂。

## 为什么用它 / 适合什么场景

- **追求极简的终端美学**：neofetch 的 ASCII 艺术看着有点过时，Dfetch 字体更细更克制；
- **远程机器自检**：SSH 进去第一件事想看机器信息，又不想启动图形栈；
- **点文件 (dotfiles) 收藏**：单一可执行文件 + 一个配置文件 `~/.config/Dfetch/Dfetch.conf`，方便版本管理。

## 关键能力

| 能力 | 说明 |
|------|------|
| Go 单二进制 | 无运行时依赖，编译即跑 |
| 显示项可调 | 配置里改顺序 / 删字段 |
| 12 种发行版 ASCII | Ubuntu / Arch / Debian / Fedora 等 |
| 自定义图像 | 也能塞自己的 ASCII 作品 |
| 配置文件 | `~/.config/Dfetch/Dfetch.conf` |

## 媒体 / 原始链接

![界面截图](https://pbs.twimg.com/media/HLev1h2aEAAr4Yo.jpg)

- 项目链接：<https://github.com/David17c/Dfetch>

## 相关概念

- [Nefoin](concepts/tool-nefoin-nerdfont.md) — 同样属于「一行命令省心」的 CLI 工具（Nefoin 装字体）