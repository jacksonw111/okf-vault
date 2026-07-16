---
type: "Tool"
title: "codex-storyboard（Yuuhann1999/codex-storyboard）"
description: "给短视频/自媒体用的本地分镜台 Codex 插件,让 Codex 直接建视频项目、写分镜表,再用图片/视频生成能力把素材填回对应镜头。"
resource: "https://github.com/Yuuhann1999/codex-storyboard"
tags: "[codex, storyboard, plugin, short-video, agent-skill, web-ui]"
timestamp: "2026-07-16T12:15:00Z"
---

# codex-storyboard

[codex-storyboard](https://github.com/Yuuhann1999/codex-storyboard) 是**面向短视频/自媒体创作者的本地分镜台 Codex 插件**——以 Codex 插件形式分发,装好后说一声「打开分镜台」就拉起本地 Web 工作台(默认 `127.0.0.1:43218`),无需懂 MCP 或文件路径。

## 它解决了什么

做短视频的人最痛的是「分镜→素材→剪辑」之间来回切换:脑子里已有镜头设计,但要在剪映、Midjourney、Sora、ChatGPT 之间跳来跳去手动对齐每个镜头的画面。codex-storyboard 让 Codex 当总指挥,剧本一次写好就分发给图片/视频生成工具,自动回流到统一时间线。

## 关键能力

| 能力 | 说明 |
|------|------|
| Codex 插件分发 | 装好后用自然语言就能调起,无需 MCP / 路径知识 |
| 本地 Web 工作台 | 默认 `127.0.0.1:43218` 起前端,可视化分镜表 |
| 分镜项目创建 | Codex 直接建视频项目骨架,每个镜头一行配置 |
| 素材回填 | 接入图片/视频生成能力,生成的素材自动落到对应镜头 |
| 自媒体场景 | 默认面向抖音 / 快手 / B站短片节奏 |

## 媒体

![](https://pbs.twimg.com/media/HNRJurOa8AE8RAP.jpg)

## 参考链接

- [项目仓库](https://github.com/Yuuhann1999/codex-storyboard)

## 相关概念

- [OpenMontage](./tool-openmontage.md) — 通用 agentic 视频制作系统,与本工具面向相似场景(短视频自动化)
- [multi-design-ppt](./tool-multi-design-ppt.md) — 同样基于 Agent Skills 协议分发,本工具是其「视频分镜」方向的延伸
