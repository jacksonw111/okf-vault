---
type: Tool
title: "barehands (jaredrhod/barehands)"
description: "把网络摄像头变成手势界面，笔记/图片/3D 模型以玻璃卡片浮在画面上，用裸手捏、甩、拉伸、隔空抓取操控，可接给 AI 当手和眼睛"
resource: "https://github.com/jaredrhod/barehands"
tags: [gesture, computer-vision, webcam, ui, spatial, ai-input]
timestamp: 2026-08-20T10:18:00Z
---

# barehands (jaredrhod/barehands)

## 它是什么
[`jaredrhod/barehands`](https://github.com/jaredrhod/barehands) 把一个普通的**网络摄像头**变成**手势交互界面**：屏幕上浮出笔记、图片、3D 模型的"玻璃卡片"，用户用**裸手**做捏、甩、拉伸、隔空抓取等动作来操作。摄像头输出的手势数据还能**接给 AI 当"手和眼睛"**——让 agent 直接控制或浏览空间化内容。

## 为什么用它 / 适合什么场景
- 演示 / 教学场景：演讲者用双手操控卡片，比传统遥控笔更具表现力。
- 空间计算 / VR 替代：用摄像头 + 普通屏幕做出 Apple Vision Pro / Meta Quest 那样的空间感。
- 给 AI agent 提供"图形界面"的视觉 + 操作接口：agent 看得到浮窗在哪里、点哪里。
- 无障碍：身体活动受限的人群用大动作代替精确鼠标。

## 关键能力
| 能力 | 说明 |
|------|------|
| 裸手追踪 | 仅靠 RGB 摄像头，不需要深度摄像头 / 标记手套 |
| 玻璃浮卡 | 内容以毛玻璃卡片叠加在摄像头实景之上 |
| 多手势 | 捏、甩、拉伸、隔空抓取等 |
| AI 可接管 | 视觉 + 操作接口可对接 agent，让 AI 直接"看见并动手" |

## 媒体
- ![barehands 演示](https://pbs.twimg.com/media/HQD2RvAaEAABsRH.jpg)

## 相关概念
- [项目仓库](https://github.com/jaredrhod/barehands) — 仓库主页
- [term-webrtc](./term-webrtc.md) — 摄像头流媒体相关底层技术
