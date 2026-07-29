---
type: Tool
title: "Timecode-Agent（长视频带时间戳证据账本）"
description: "Python CLI 工具，帮 coding agent 从长视频中提取带时间戳的可复用证据，避免逐帧采样带来的遗漏和上下文丢失。采用「转录优先」策略——先提取时间轴转录文本 + 场景 / 音频 / OCR / 人脸等确定性信号，再按需视觉验证。"
resource: "https://github.com/mupozg823/timecode-agent"
tags: [video, agent, evidence, timestamp, transcript, python]
timestamp: "2026-07-28T09:21:00.000Z"
---

# Timecode-Agent

## 它是什么

Python 命令行工具，专门给 **coding agent** 设计——处理**长视频**生成**带时间戳的可复用证据账本**。

视频示例：
- <https://video.twimg.com/amplify_video/...>

## 核心策略：转录优先

不是"固定采样所有帧"那种暴力做法：

1. 先提取**时间轴转录文本**
2. 再提取**确定性信号**——场景 / 音频 / OCR / 人脸
3. 按需**视觉验证**（关键位置再瞄一眼）
4. 检测点（checkpoints）、捕获来源、编辑决策存进**仅追加账本**
5. 支持 EDL / FCPXML / OTIO 等后期导出格式

![示意图](https://pbs.twimg.com/media/HOSMNVMawAAOp4x.jpg)

## 与「固定帧采样」的差异

| 固定采样 | Timecode-Agent |
|----------|----------------|
| 所有帧都看 | 按需看 |
| 容易遗漏关键帧 | 转录优先锁定 |
| context 浪费 | 节省 token |
| 无证据链 | 账本可追溯 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 转录优先 | 先文本后视觉 |
| 多模态信号 | 场景 / 音频 / OCR / 人脸 |
| 仅追加账本 | 不可篡改的证据链 |
| 多种导出 | EDL / FCPXML / OTIO |
| 长视频友好 | 适合 coding agent 处理 |

## 原始链接

- [项目仓库](https://github.com/mupozg823/timecode-agent)
- [推文剪藏](https://x.com/QingQ77/status/2082033570772898104)

## 相关概念

- [Claude Real Video](./tool-claude-real-video.md) — Python 工具，按场景变化 + 字幕智能抽帧让 AI 真正看懂视频
- [OpenMontage](./tool-openmontage.md) — 首个开源 agentic 视频制作系统
- [Cinema Manager](./tool-cinema-manager.md) — 找片 Skill，多源搜索 + 质量评分
- [Timecode 思路与 Long Video Benchmark（VideoAgent）](./tool-video-shotcraft.md) — 视频导演 Skill，106 镜头卡 + 162 动效样式