---
type: "Tool"
title: "Dotkeep（bash 写的 dotfiles 同步工具）"
description: "纯 bash 的 dotfiles 同步小工具，把工具本体和备份仓库分离，备份按 home/ root/ 两棵目录树存放，换机 clone 即可还原。"
resource: "https://github.com/metaory/dotkeep"
tags: "[dotfiles, bash, sync, backup, restore, cross-machine, nvim, zsh]"
timestamp: "2026-09-17T06:10:00Z"
---

# Dotkeep（bash 写的 dotfiles 同步工具）

## 它是什么

[metaory/dotkeep](https://github.com/metaory/dotkeep) 是 **metaory** 用纯 bash 写的 dotfiles 同步小工具。它解决「家里 / 公司 / VPS 几台机器的 `.zshrc`、nvim 配置、hosts 等散文件怎么统一管理」这个老问题：

- **工具本体**和**备份仓库彻底分离**——dotkeep 本身只负责「按清单同步」，备份仓库只负责「存文件」，互不污染。
- 备份内容按 **`home/`** 和 **`root/`** 两棵目录树分开存放，路径即结构。

## 关键能力

| 能力 | 说明 |
|------|------|
| 纯 bash | 零依赖 / 不需要 Python / Node / Go 运行时 |
| 工具与数据分离 | 升级 dotkeep 不会影响备份内容 |
| 双树结构 | home/ 普通用户配置 + root/ 系统级配置分别存档 |
| 一键还原 | 换机 clone 备份仓库、跑一次 dotkeep 即恢复全部配置 |

## 适合什么场景

- 同时维护 2 台以上机器（个人 PC / 工作机 / VPS / 树莓派），想把 dotfiles 集中管理的开发者。
- 不想引入 `chezmoi` / `yadm` / `stow` 等较大工具，只想要一个「能跑就行」的轻量替代的极简派。
- 喜欢研究「单一职责 + 工具与数据解耦」设计模式的工程师。

## 参考

- 项目链接：<https://github.com/metaory/dotkeep>

![preview](https://pbs.twimg.com/media/HSYlA6Ea8AE2mUz.jpg)
