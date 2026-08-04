---
type: "Tool"
title: "TermBoard (HeyShinde)"
description: "摆脱手写 Makefile 和 bash 脚本，用一个常驻的交互式终端界面管理 Python 项目、虚拟环境和任务；自动识别 uv / poetry / pipenv / .venv，直接在对应环境里跑任务。"
resource: "https://github.com/HeyShinde/TermBoard"
tags: "[python, makefile, terminal, tui, venv, uv, poetry, pipenv, task-runner]"
timestamp: "2026-08-04T20:30:00Z"
---

# TermBoard (HeyShinde)

## 它是什么

[TermBoard](https://github.com/HeyShinde/TermBoard) 是一个**常驻的交互式终端界面**，把散在 Makefile 和 bash 脚本里的 Python 项目流程收进一个仪表盘。它会**自动识别项目用 uv / poetry / pipenv / .venv**，直接在这个环境里跑任务，不用自己手动激活。

![TermBoard 截图](https://pbs.twimg.com/media/HOzTmCTboAAUxxy.jpg)

## 为什么用它 / 适合什么场景

- **告别手写脚本**：Makefile / bash 的零散流程收进一个面板。
- **环境自动识别**：uv / poetry / pipenv / .venv 都自动接管。
- **常驻交互**：不用每次手敲命令，点选即可。
- **新手友好**：不用学 Makefile / shell 也能跑项目任务。

## 关键能力

| 能力 | 说明 |
|------|------|
| 常驻交互界面 | 仪表盘式 TUI，常驻终端 |
| 虚拟环境自动识别 | uv / poetry / pipenv / .venv 自动接管 |
| 任务面板化 | 原来写在 Makefile / bash 里的任务点选即可 |
| 自动激活环境 | 跑任务时无需手动 `source venv/bin/activate` |

## 虚拟环境支持

| 环境 | 自动识别 |
|------|----------|
| uv | ✓ |
| poetry | ✓ |
| pipenv | ✓ |
| .venv | ✓ |

## 参考链接

- [项目仓库](https://github.com/HeyShinde/TermBoard)

## 相关概念

- [Pi TBox](./tool-pi-tbox.md) — Pi 扩展工具开关面板
- [Hop SSH TUI](./tool-hop-ssh-tui.md) — Go 写的终端 SSH 多服务器切换 TUI
- [DockSurf](./tool-docksurf.md) — 终端里用键盘操作 Docker 的 TUI
