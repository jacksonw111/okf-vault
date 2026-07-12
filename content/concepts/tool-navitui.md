---
type: Tool
title: "NaviTui（终端 Subsonic / Navidrome 音乐播放器）"
description: "给 Navidrome / 任意 Subsonic 服务器用的终端音乐播放器（NaviTui）：在终端里显示真实封面、用 mpv 播放，支持离线下载、卡拉 OK 歌词、无限电台，并暴露控制 API 与 MCP 服务器给脚本与 AI 智能体使唤。"
resource: "https://github.com/Gheat1/NaviTui"
tags: [tool, terminal, tui, music, navidrome, subsonic, mcp]
timestamp: 2026-07-12T16:30:00Z
---

# NaviTui（终端 Subsonic / Navidrome 音乐播放器）

## 它是什么
终端里的 Subsonic 协议音乐播放器，专为 Navidrome / 任何 Subsonic 兼容服务器设计。在 TUI 中显示真实专辑封面、用 mpv 后端播放，支持离线下载、卡拉 OK 歌词、无限电台等高级功能，还把控制能力通过 API 与 MCP 服务器暴露给脚本和 AI 智能体调用。

## 为什么用它 / 适合什么场景
- 已自建 Navidrome 作为私人音乐库，希望在终端里直接播放、不切窗口。
- 想让 AI 编码 agent / 工作流脚本通过 MCP 直接控制播放器（"播放下一首""把当前曲目加入 XX 歌单"）。
- 偏好极简、键盘操作、SSH 远程仍可用的播放体验。

## 关键能力
| 能力 | 说明 |
|------|------|
| 终端原生 TUI | 在终端里渲染专辑封面、播放队列、歌词 |
| mpv 后端 | 用 mpv 播放，跨平台、格式全 |
| 离线下载 | 把歌曲 / 歌单下载到本地，无网也能听 |
| 卡拉 OK 歌词 | 同步卡拉 OK 风格滚动歌词 |
| 无限电台 | 内置无限电台模式，按规则自动连播 |
| 控制 API | 暴露 REST / API 控制接口 |
| MCP 服务器 | 内置 MCP server，让 Claude Code / Codex 等 agent 直接调用 |

## 参考链接
- [项目链接](https://github.com/Gheat1/NaviTui)
- [原始链接](https://x.com/QingQ77/status/2076280663339311208)

![NaviTui 终端播放器界面](https://pbs.twimg.com/media/HM-74sCbYAAzR4x.jpg)

## 相关概念
- [Orca Music Player（Svelte 5 + Tauri 2 本地音乐播放器）](tool-orca-music-player.md) — 同样是本地优先音乐播放器，但走 GUI 路线