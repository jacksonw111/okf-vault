---
type: "Tool"
title: "sprite-maker（游戏精灵 AI 生成 + 动画化桌面工具）"
description: "JohnKinyanjui 出的 Tauri + Svelte + Rust + SQLite 桌面工具，靠本地装的 Codex CLI 调模型出 2D 精灵：聊天窗口描述素材贴参考图即可出静态精灵；说「Animate this」后 AI 先规划整个动作，再一帧一帧地生成 24–48 帧动画，身份参考与相邻帧保证角色不走形。"
tags: "[sprite, 2d-game, animation, tauri, codex, llm, character]"
timestamp: "2026-08-26T16:30:00Z"
resource: "https://github.com/JohnKinyanjui/sprite-maker"
---

# sprite-maker（游戏精灵 AI 生成 + 动画化桌面工具）

## 它是什么

[`sprite-maker`](https://github.com/JohnKinyanjui/sprite-maker) 是 JohnKinyanjui 出的开源**桌面工具**——专为「AI 出图到游戏生产级素材」最后一步打通的痛点设计：

| 阶段 | 能力 |
|------|------|
| 静态精灵 | 在聊天窗口描述素材 + 贴参考图 → 出静态 sprite |
| 动画化 | 对一张 sprite 说 **"Animate this"** → AI 先**规划整个动作**，再**一帧一帧**生成 **24–48 帧**动画 |

关键设计：
- **每帧都带「身份参考」+「相邻帧」** → 角色不会画着画着走形
- **稳定的角色形象 + 干净的透明通道 + 统一调色板 + 完整动画循环 + 规范文件结构**——AI 随手出图满足不了的生产级要求

技术栈：**Tauri + Svelte + Rust + SQLite**，调本地 **Codex CLI** 模型，三个平台都能用。

## 为什么用它 / 适合什么场景

- Indie 游戏 / 个人项目需要**生产级 2D 资源**（不是 demo 图）
- 想用 AI 加速但又怕角色走形 / 调色不统一 / 循环不完整
- 想保留对**调色板 / 帧数 / 文件命名**的硬性约束

## 关键能力

| 能力 | 说明 |
|------|------|
| 静态精灵 | 描述 + 参考图出图 |
| 24–48 帧动画 | 拆帧持续 |
| 身份参考 + 相邻帧 | 防走形 |
| Codex CLI 调用 | 本地模型 |
| 跨平台桌面 | Tauri 三平台 |
| 文件结构规范 | 满足生产管线 |

## 演示 / 媒体

- [Demo 视频](https://video.twimg.com/tweet_video/HQiPe_HaYAAcWPS.mp4)

## 参考链接

- [项目链接](https://github.com/JohnKinyanjui/sprite-maker)
