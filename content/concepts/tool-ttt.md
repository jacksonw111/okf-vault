---
type: Tool
title: "TTT"
description: "Go 写的终端原生 IDE，单二进制零配置，定位替代 VS Code 这类重型编辑器；含语法高亮 / 多光标 / 折叠 / LSP / Git / 终端 / Lua 插件"
resource: "https://github.com/eugenioenko/ttt"
tags: [ide, terminal, go, lua, lsp, git]
timestamp: 2026-09-05T15:00:00Z
---

# TTT

## 它是什么
`eugenioenko/ttt` 是一个**跑在终端里的 IDE**，用 Go 写成，单二进制分发，零配置启动，目标是对标 VS Code 这类「重型」图形编辑器，让人在 SSH / 服务器 / 远程开发机里也能享受现代 IDE 功能。

## 为什么用它 / 适合什么场景
- 想在远程服务器 / SSH / 低带宽环境获得完整 IDE 体验（语法高亮、LSP、Git、终端）。
- 不想为编辑器装 Node / Electron 运行时（VS Code 的隐性依赖）。
- 喜欢「单文件零配置」哲学：下载即跑，不写 settings.json 也能用。

## 关键能力
| 能力 | 说明 |
|------|------|
| 终端原生 | 完全跑在 TTY 内，无需 X / Wayland / 远程桌面 |
| 语法高亮 | 内置多语言高亮 |
| 多光标 | 类 VS Code 多光标编辑 |
| 折叠 | 代码折叠 |
| LSP 支持 | Language Server Protocol 补全 / 跳转 / 重构 |
| Git 集成 | 内置 Git 命令面板 |
| 全局搜索 | 跨文件快速搜索 |
| 自带终端 | IDE 内嵌 shell，无需切窗口 |
| 多目录工作区 | 一次管理多个项目根 |
| Lua 插件 / 主题 | 通过 Lua 写自定义插件和配色 |

## 媒体
- 视频：<https://video.twimg.com/tweet_video/HRSb-hEbgAApXEN.mp4>

## 相关概念
- [原始链接](https://github.com/eugenioenko/ttt)