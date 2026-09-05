---
type: Tool
title: "Logic"
description: "全栈日志分析应用，注册本地文件 / 目录 / SFTP / HTTP(S) / 浏览器上传文件作为日志源，实时查看内容"
resource: "https://github.com/markdamics/Logic"
tags: [log, observability, fullstack, sftp, http]
timestamp: 2026-09-05T15:00:00Z
---

# Logic

## 它是什么
`markdamics/Logic` 是一个**全栈日志分析应用**，把各类日志源统一注册并实时检视内容，避免在不同日志查看器之间来回切换。

## 为什么用它 / 适合什么场景
- 需要同时看本地文件、远程 SFTP、HTTP(S) 接口、浏览器上传的混合日志时，不想为每种源各装一个工具。
- 调试 / 排障场景，希望所有日志集中到一个 Web 界面里实时滚动。
- 不想把日志推到 SaaS，希望自托管整套工具链。

## 关键能力
| 能力 | 说明 |
|------|------|
| 多源注册 | 本地文件、本地目录、SFTP、HTTP(S) 地址、浏览器上传文件均可作为日志源 |
| 实时检视 | 源内容更新即在 UI 中即时呈现 |
| 浏览器上传 | 用户可直接从前端拖拽上传文件作为临时日志源 |
| 全栈一体化 | 后端 + 前端在同一仓库，开箱即用 |

## 媒体
- ![](https://pbs.twimg.com/media/HRSzzaPbsAA5N8G.jpg)
- ![](https://pbs.twimg.com/media/HRSz0J7bcAAWTlF.jpg)

## 相关概念
- [原始链接](https://github.com/markdamics/Logic)