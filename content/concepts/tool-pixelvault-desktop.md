---
type: "Tool"
title: "PixelVault Desktop"
description: "pixelvault-dev 开源的 macOS / Linux 菜单栏小工具：复制一张图片，剪贴板立刻换成托管 URL，方便 Codex cloud / 网页 Claude Code / Cursor 后台 agent 这类「只收文本」的云端编程 agent 直接看到图。"
resource: "https://github.com/pixelvault-dev/desktop"
tags: [clipboard, image-hosting, cloud-agent, macos, linux, menu-bar]
timestamp: "2026-08-10T10:46:00Z"
---

# PixelVault Desktop

## 它是什么

[PixelVault Desktop](https://github.com/pixelvault-dev/desktop) 是个跨 macOS / Linux 的菜单栏小工具：只要你**复制一张图片**，剪贴板里的内容立刻被替换成这张图的**托管 URL**。下游只要是个能读文本的云端编程 agent——Codex cloud、网页版 Claude Code、Cursor 后台 agent——把剪贴板内容粘过去，**对方不需要装任何东西就能看到图**。

## 为什么用它 / 适合什么场景

- 用云端 Codex / Claude / Cursor 这类「只收文本」的 agent，但又想丢图进去（截图报错 / 设计稿 / OCR 校对）。
- 不想为「让 agent 看到一张图」折腾图床账号或上传步骤——直接在桌面复制即用。
- 私有 / 受控的图像托管（避免把工作截图丢到公网图床）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 复制即托管 | 复制图片 → 剪贴板变成托管 URL |
| 对端零安装 | cloud agent 收到 URL 直接访问 |
| macOS / Linux | 菜单栏小工具形态 |
| 截图友好 | 截屏 → 复制 → 粘贴给 agent 一气呵成 |

## 媒体

- 视频：<https://video.twimg.com/tweet_video/HPRlDyHbwAAkGMk.mp4>

## 参考链接

- [项目仓库](https://github.com/pixelvault-dev/desktop)
- [原始链接](https://x.com/QingQ77/status/2086766004034830518)

## 相关概念

- [claude-real-video](./tool-claude-real-video.md) — 同样解决「让 AI 真正看懂视觉内容」，但走「按场景抽帧 + 字幕」路线处理视频
