---
type: Tool
title: "oh-story-dsh（worldwonderer/oh-story-dsh）"
description: "DSH 插件：把 AI 写长篇 / 短剧的整套创作方法做成三栏工作台，左侧文件树 / 中间编辑器 / 右侧 Agent 对话"
resource: "https://github.com/worldwonderer/oh-story-dsh"
tags: "[dsh, deepseek-harness, novel-writing, plugin, agent-workbench, short-drama]"
timestamp: "2026-08-22T13:13:00Z"
---

# oh-story-dsh

## 它是什么
[`worldwonderer/oh-story-dsh`](https://github.com/worldwonderer/oh-story-dsh) 是一个 **DeepSeek Harness (DSH)** 插件，把「用 AI 写长篇小说或短剧」的整套创作方法做成 DSH 内的三栏工作台：左边是文件树、中间是编辑器、右边是跟 Agent 的对话——**写什么、改什么都看得见**，不再只是聊天窗口里飘来飘去的段落。

## 为什么用它 / 适合什么场景
- 想写长篇（10 万字+）或短剧脚本，但 chat-only 工具用起来丢失项目结构。
- 想把「剧情大纲 / 角色档案 / 章节稿 / 场景描写」当作可被 Agent 操作的真实文件，而非聊天历史。
- 已经用 DSH 写作，想把它升级为「带文件视图 + 角色管理」的 IDE 式创作台。

## 关键能力
| 能力 | 说明 |
|------|------|
| 三栏工作台 | 文件树 + 编辑器 + Agent 对话三区同屏 |
| 文件即稿 | 章节、角色、世界观全是磁盘上的真实文件，可 git |
| Agent 协作 | 改稿 / 续写 / 校对直接对真实文件操作 |
| 适用长内容 | 长篇 / 短剧 / 多角色场景皆可 |
| 插件形态 | 不改 DSH 内核，作为官方工具协议接入 |

## 媒体
- 视频：<https://video.twimg.com/tweet_video/HQT-5J8aoAAhOW6.mp4>

## 相关概念
- [dsh-visualize](./tool-dsh-visualize.md) — DSH 内的可视化卡片插件，让模型输出就地渲染
- [dsh-plugin-dir-tree](./tool-dsh-plugin-dir-tree.md) — DSH 文件树插件，oh-story-dsh 在它基础上提供创作三栏布局
- [Story Engine](./term-story-engine.md) — 用结构化文件驱动 AI 创作的方法论
