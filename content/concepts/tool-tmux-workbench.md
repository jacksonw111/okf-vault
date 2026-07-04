---
type: Tool
title: "tmux-workbench"
description: "tmux-workbench 是 Rust 写的「tmux 会话记忆管理器」:把本地和 SSH 上散落的 tmux 会话统一索引,记录项目路径 / 当前命令 / git 状态 / 备注 / 别名 / 标签 / 归档状态,CLI + TUI 一个入口管理。"
resource: "https://github.com/LeON-Nie-code/tmux-workbench"
tags: [tmux, workbench, rust, tui, ssh, session-manager]
timestamp: "2026-07-04T15:00:00Z"
---

# tmux-workbench

## 它是什么

`LeON-Nie-code/tmux-workbench` 是 Rust 写的 tmux 工作区记忆管理器。**问题**:开发者在多台机器(本地 + 跳板 + 服务器)、多个项目上开的 tmux 会话越来越多,要「找回昨天那个跑迁移的会话」很费劲;tmux 自带的 session list 不够看。**解法**:把所有本机 + SSH 上的 tmux 会话集中索引,记下每条会话的项目路径、当前命令、git 状态、备注、别名、标签、归档状态,CLI 和 TUI 一个入口统一操作。

<https://video.twimg.com/tweet_video/HMTcJrXaMAAmGvd.mp4>

项目链接：<https://github.com/LeON-Nie-code/tmux-workbench>

## 为什么用它 / 适合什么场景

- **多机器开发**:本地 + 两台跳板 + 一台线上服务器,以前要 `ssh → tmux ls → attach` 找半天。
- **会话分项目**:不仅看名字,还能直接告诉我「这窗口是在 `/home/me/project-x`、当前在跑 `cargo test`、git branch `feature/...`、备注 『等 review』」。
- **跨设备找会话**:从笔记本 SSH 到桌面上,不用重连,workbench 直接列出所有可达会话。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨主机索引 | 本机 + SSH 远端 tmux 会话统一进一个表 |
| 会话元数据 | 项目路径 / 当前命令 / git status / 备注 / 别名 / 标签 / 归档 |
| CLI | 可在脚本里直接用,如 `tw goto alias-name` |
| TUI | 终端下全键盘交互浏览,带 vim 风格快捷键 |
| 归档支持 | 「我暂时不处理」的会话标注归档,过滤时不再出现 |
| 单二进制 | Rust 出可执行文件,无需 runtime / npm / 大量依赖 |

## 工作流

1. `tw add` 注册一个新会话(自动抓到项目路径、当前命令、git 信息)
2. `tw ls` 列出全部(可按 tag / 主机过滤)
3. `tw attach <alias>` 跳进指定会话
4. `tw archive <alias>` 收进归档

## 相关概念

- [mux(Claude Code tmux 插件)](tool-mux-claude-tmux.md) — 浮动面板管理 Claude Code 多个会话;同样在「让 tmux 会话更好用」方向
- [Vaultty](tool-vesta-terminal.md) — macOS 原生终端,也是为 tmux / 多 agent 会话并行设计
- [tmux-workbench 仓库](https://github.com/LeON-Nie-code/tmux-workbench) — 项目链接
