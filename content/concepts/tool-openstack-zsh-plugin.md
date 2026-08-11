---
type: "Tool"
title: "OpenStack Zsh Plugin（whoami96/openstack-zsh-plugin）"
description: "Oh My Zsh 插件,把日常 OpenStack CLI 操作收成 fzf 交互选择:切云 / 激活虚拟环境 / 按名字模糊搜虚拟机再 SSH,免去手动敲一长串命令。"
resource: "https://github.com/whoami96/openstack-zsh-plugin"
tags: "[openstack, zsh, oh-my-zsh, fzf, ssh, devops]"
timestamp: "2026-08-11T16:00:00Z"
---

# OpenStack Zsh Plugin

[OpenStack Zsh Plugin](https://github.com/whoami96/openstack-zsh-plugin) 是 Oh My Zsh 的插件,把每天都要敲的 OpenStack CLI 操作收成**fzf 交互式选择**——切云账号、激活虚拟环境、按名字模糊搜虚拟机再 SSH,不用再手动拼长命令。

项目链接：<https://github.com/whoami96/openstack-zsh-plugin>

## 它是什么

一层针对 OpenStack CLI 的 zsh 快捷封装,把多账号、多虚拟环境、多目标主机的日常运维动作从"敲完整命令"变成"键盘选 + 回车"。

## 为什么用它 / 适合什么场景

- **多云账号 / 多 VM 切换**:开新会话不用切 rc 文件。
- **模糊搜索**:fzf 接管目标 VM 名称,长名字也记得住一半就能选。
- **直接 SSH**:选中即连,不需要额外手敲 ssh 命令。

## 关键能力

| 能力 | 说明 |
|------|------|
| fzf 交互选择 | 模糊搜索命令目标,免去记忆完整命令 |
| 多 OpenStack 云切换 | 一键在不同云账号 / 项目上下文间切 |
| 虚拟环境激活 | 把 OpenStack 虚拟环境做成可选项 |
| 模糊搜 VM | fzf 接管目标主机名 |
| 直接 SSH | 选中目标后直接发起 SSH,无需手敲 |
| Oh My Zsh 集成 | 与 zsh 生态无缝衔接 |

## 媒体

视频：<https://video.twimg.com/tweet_video/HPVK4CEbcAADqYs.mp4>

## 参考链接

- [项目仓库](https://github.com/whoami96/openstack-zsh-plugin)

## 相关概念

- [Cobalt Spark](./tool-cobalt-spark.md) — 极简 Oh My Zsh 主题,与本工具同一生态
- [Hop SSH TUI](./tool-hop-ssh-tui.md) — Go 写的终端 SSH 多服务器切换 TUI,与本工具功能相似但通用