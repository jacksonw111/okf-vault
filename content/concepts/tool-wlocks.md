---
type: "Tool"
title: "wlocks（programmersd21/wlocks）"
description: "用 Go 写的 TUI 工具, 通过轮询 /proc 实时展示进程与文件描述符的关系; 内置模糊搜索、多维度排序、主题切换和进程管理功能, 支持查看进程详情 (PID、cmdline、cwd、打开的所有 fd 及锁定时长)。"
resource: "https://github.com/programmersd21/wlocks"
tags: "[tui, golang, proc-fs, sysadmin, lock-debugging]"
timestamp: "2026-07-17T08:27:00Z"
---

# wlocks

[wlocks](https://github.com/programmersd21/wlocks) 是一个用 **Go 写的 TUI 工具**, 通过**轮询 `/proc`** 来实时展示**进程 ↔ 文件描述符**的关系。它特别适合回答「这个 fd 谁占着 / 锁了多久 / 何时释放」这类运维 / 开发常见疑问。

## 它解决的问题

「为什么这个文件删不掉」、「哪个进程拿着这个 socket」、「这个日志文件谁一直锁着」——答案都在 `/proc/<pid>/fd/*` 里, 但手动 ls 每个进程实在繁琐。wlocks 把这块体验封装为 TUI:

- 实时刷新 (轮询 `/proc`)
- 模糊搜索某进程 / 某 fd
- 多维度排序 (fd 数量 / 占用时长 / PID 等)
- 看每个进程详情 (cmdline / cwd / 所有打开的 fd)

## 关键能力

| 能力 | 说明 |
|------|------|
| /proc 轮询 | 实时刷新, 不依赖 lsof 等工具 |
| 模糊搜索 | 输入 PID / cmdline / fd 关键字快速定位 |
| 多维排序 | 按 fd 数量 / 锁定时长 / PID 等排序 |
| 主题切换 | 内置多套配色, 不影响长时间盯屏 |
| 进程管理 | 可终止 / 暂停 / 详情查看 |

## 媒体

视频：

- <https://video.twimg.com/tweet_video/HNRaGRgbcAAxze5.mp4>

## 参考链接

- [项目仓库](https://github.com/programmersd21/wlocks)

## 相关概念

- [lsof / fuser / flock 系列传统工具] — wlocks 的「/proc + TUI」现代版
- [Dfetch](./tool-dfetch.md) — Go 写的轻量系统信息 neofetch 风格替代, 同属「Go + TUI + 系统侧」一类小型工具
