---
type: Tool
title: "blockout"
description: "用灰盒场景、走位标记与真实镜头参数做 AI 视频生成用的 previs，并导出视频生成器可跟随的运动参考包。"
resource: "https://github.com/wassermanproductions/blockout"
tags: [tool, ai-video, previs, cinematography, motion-reference, animation]
timestamp: 2026-07-10T03:31:00.000Z
---

# blockout

## 它是什么
面向 AI 视频生成的 previs（预可视化）工具：搭一个灰盒（blockout）场景、摆上走位标记、设定真实镜头参数，最后导出视频生成器可以直接跟随的"运动参考包"。

## 为什么用它 / 适合什么场景
- 用 AI 视频模型（可灵 / Sora / Veo 等）出片时，镜头运动 / 角色走位靠 prompt 难精确控制，需要"先拍一份视频版分镜"。
- 想用真实电影级镜头参数（焦段 / 机位 / 运动曲线）而不是空泛描述去驱动生成。
- 把传统影视 previs 工作流移植到 AI 视频流水线。

## 关键能力
| 能力 | 说明 |
|------|------|
| 灰盒场景 | 快速搭 3D 空间，专注构图与镜头而非细节建模 |
| 走位标记 | 角色 / 物体的运动路径与关键节点 |
| 真实镜头参数 | 焦段 / 机位 / 运镜曲线等电影级参数 |
| 运动参考包 | 导出可被视频生成器直接跟随的参考文件 |

## 媒体
![blockout 预览](https://pbs.twimg.com/media/HMv8o9ub0AAH6Z5.jpg)

## 相关概念
- [Kling 3.0（可灵 3）](note-kling-3-cinematic.md) — blockout 输出的运动参考包是给这类视频生成模型做镜头控制的