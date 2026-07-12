---
type: Tool
title: "jzsub（Codex 视频自动双语字幕与烧录 Skill）"
description: "一个 Codex Skill：自动下载视频、获取封面、生成翻译好的双语字幕，并烧录成 MP4 格式，一条命令完成「原始视频 → 双语字幕 MP4」全流程。"
resource: "https://github.com/pengchujin/jzsub"
tags: [tool, codex, skill, video, subtitle, bilingual]
timestamp: 2026-07-12T16:30:00Z
---

# jzsub（Codex 视频自动双语字幕与烧录 Skill）

## 它是什么
开源 Codex Skill，把「下载视频 → 获取封面 → 翻译成双语字幕 → 烧录成 MP4」串成一条命令。开发者或内容创作者把视频 URL（或本地路径）丢给它，出来的就是带双语字幕和封面的成品 MP4。

## 为什么用它 / 适合什么场景
- 想给搬运到海外 / 引流到中文站点的视频批量加中英双语字幕。
- 自媒体内容工作流里"双语字幕 MP4"是高频产物，但每条都手动做耗时严重。
- 已用 Codex 类 AI 编码 CLI 作为统一入口，不想再开 GUI 视频工具。

## 关键能力
| 能力 | 说明 |
|------|------|
| 一键下载 | 输入视频 URL，自动下载到本地 |
| 自动封面 | 抽取视频关键帧作为封面图 |
| 双语字幕 | 自动翻译并生成中 / 英（或其它目标语言）双语字幕轨 |
| 字幕烧录 | 把双语字幕内嵌到 MP4 文件，跨平台可播 |
| Codex Skill | 通过 Codex Skill 协议加载，作为 agent 工具调用 |

## 工作流（高层）
1. Codex 收到任务 → 调用 jzsub Skill
2. 下载原始视频 → 抽取封面帧
3. ASR + 翻译 → 生成双语字幕
4. ffmpeg 烧录字幕 + 写封面元数据 → 输出 MP4

## 参考链接
- [项目链接](https://github.com/pengchujin/jzsub)
- [原始链接](https://x.com/pengchujin/status/2076196945090281668)
- [转发来源](https://x.com/Wen_Zw/status/2076226028603924881)

![jzsub 流程示意](https://pbs.twimg.com/media/HNAiEabaEAAwGwt.jpg)

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — jzsub 是按 Agent Skills 协议打包的 Skill