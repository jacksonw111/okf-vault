---
type: Tool
title: "nls"
description: "Go 写的现代化 ls 命令，把 Nushell 风格的表格化文件列表带到 bash / zsh / fish / PowerShell 等传统 shell：交互时显示美观表格，管道和脚本中保持快速纯文本。"
resource: "https://github.com/nolight132/nls"
tags: [tool, cli, go, ls, nushell, shell, terminal]
timestamp: 2026-07-10T00:48:00.000Z
---

# nls

## 它是什么
Go 编写的现代化 `ls` 命令复刻，把 Nushell 那种"结构化表格"输出带到 bash、zsh、fish、PowerShell 等传统 shell 里。交互时显示美观的表格，管道 / 脚本中自动退回纯文本以保持兼容与速度。

## 为什么用它 / 适合什么场景
- 喜欢 Nushell 的表格视图但又不想切到 Nushell 本身、保留现有 shell。
- 在管道里需要 `ls` 输出依然可被 `grep` / `awk` 处理，不想被 ANSI 颜色 / 表格边框破坏。
- 想给老 shell 来一次"零迁移成本"的现代化升级。

## 关键能力
| 能力 | 说明 |
|------|------|
| 表格化输出 | 交互模式显示对齐的列与表头 |
| 管道兼容 | 脚本 / 管道模式下输出纯文本 |
| 多 shell 适配 | bash / zsh / fish / PowerShell |
| Go 单二进制 | 部署简单，跨平台 |

## 媒体
![nls 预览](https://pbs.twimg.com/media/HMr70N7bkAAkIS-.png)

## 相关概念