---
type: "Tool"
title: "KeyboardWarrior"
description: "Rust 写的节奏打字游戏：把 Guitar Hero 的玩法改成「按节奏敲对音符对应的字母」，谱面直接兼容 Clone Hero / YARG 社区库（.sng 文件或歌曲文件夹），也支持在游戏里连 Chorus Encore 搜谱下载。"
resource: "https://github.com/elicoggins/keyboardwarrior"
tags: [game, rhythm, typing, rust, clone-hero, yarg]
timestamp: "2026-08-08T20:30:00Z"
---

# KeyboardWarrior

## 它是什么

KeyboardWarrior 是用 Rust 写的节奏打字游戏，把 Guitar Hero 那套「卡节拍命中音符」的玩法移植到键盘打字：每个音符对应一个字母 / 键位，卡着音乐节拍敲对就算命中。它直接读取 Clone Hero / YARG 的社区谱面库（`.sng` 文件或歌曲文件夹），也支持在游戏里连 Chorus Encore 搜谱下载。

## 为什么用它 / 适合什么场景

- 想把练打字和练节拍感结合，做「双手 + 耳朵」训练。
- 已有 Clone Hero / YARG 谱面库，想换一种玩法。
- 想做编程 / 写作 / 音乐之外的休闲活动。
- 想跑开源 / 本地的节奏游戏，不依赖 Steam。

## 关键能力

| 能力 | 说明 |
|------|------|
| 打字 + 节拍玩法 | 把 Guitar Hero 思路迁移到字母键位 |
| Clone Hero / YARG 谱面 | 直接读 `.sng` 文件或歌曲文件夹 |
| Chorus Encore 联机 | 游戏内可搜谱下载 |
| Rust 实现 | 单一可执行文件，跨平台 |
| 开源 | 自由修改、扩展玩法 |

## 相关概念

- [csakura](./tool-csakura.md) — 终端樱花树动画，同属「程序化视觉 + Rust」项目
- [Mochord](./tool-mochord.md) — 和弦创作工作台
- [Mineradio](./tool-mineradio.md) — Electron 沉浸式 Windows 音乐播放器