---
type: Tool
title: "kitter"
description: "Rust 写的本地 Skill 管理工具，桌面应用和 CLI 共用一个核心；Skill 只留一份正本，装进项目时用链接而不是拷贝，更新一次全项目生效。"
resource: "https://github.com/what1f/kitter"
tags: [skill-management, rust, cli, desktop, local-only]
timestamp: "2026-09-06T00:00:00Z"
---

# kitter

## 它是什么

[kitter](https://github.com/what1f/kitter) 是一款 Rust 写的本地 Skill 管理工具，**桌面应用和 CLI 共用一个核心**。设计哲学是「Skill 只存一份正本，装到项目时用链接而不是拷贝」——不同项目可以组合不同 Skill，但永远不会出现"项目 A 改了一版、项目 B 没改"的漂移。

定位：

- **零账号、零服务器**：所有 Skill / 项目链接关系都存在本地。
- **跨形态**：同一套核心同时驱动 GUI 和 CLI，习惯命令行的人与习惯图形界面的人共享同一份逻辑。

## 为什么用它 / 适合什么场景

- AI Agent Skills 越攒越多，靠 Git 子模块或 `cp -r` 复制粘贴维护痛苦。
- 想让多个项目共享 Skill 的最新版本，又不想用子模块的复杂度。
- 团队里有人用 GUI、有人用 CLI，希望入口统一。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单正本 + 链接 | Skill 库只存一份，项目以链接形式挂载 |
| 桌面 + CLI 共核 | 同一 Rust 核心驱动两种前端 |
| 本地优先 | 不注册账号、无云端依赖 |
| Rust 实现 | 单二进制易分发，跨平台 |

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — kitter 管理的对象
- [kajisho5/ffmpeg-skill](./tool-ffmpeg-skill.md) — kitter 可管理的典型 Skill 例子

## 项目链接

- 项目主页：<https://github.com/what1f/kitter>
