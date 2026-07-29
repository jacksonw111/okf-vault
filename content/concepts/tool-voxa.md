---
type: Tool
title: "Voxa（手机语音远程指挥 AI 编程代理）"
description: "开源 Python 服务端，让你随时随地通过 iPhone 语音与 AI 编程代理（Claude Code 等）对话。对着手机说话下达任务，AI 代理在笔记本执行代码，完成后自动回拨电话告诉你结果。"
resource: "https://github.com/voxa-code/voxa"
tags: [voice, phone, ai-coding, remote, agent, python]
timestamp: "2026-07-28T01:20:00.000Z"
---

# Voxa

## 它是什么

**iPhone 语音 → AI 编程代理**的远程指挥系统——你不在电脑前也能派活给 Claude Code：

1. 你对 iPhone 说话下达任务
2. AI 代理在笔记本上执行代码
3. 完成后**自动回拨电话**告诉你结果

视频示例：
- <https://video.twimg.com/amplify_video/2081383734390247424/vid/avc1/1280x720/LLg4KHQYr7wfOV4U.mp4?tag=29>

## 工作流

```
[iPhone 语音] → [Voxa 服务端 Python] → [AI 编程代理（Claude Code）] → [回拨电话]
```

## 关键能力

| 能力 | 说明 |
|------|------|
| 手机语音入口 | 不必坐在电脑前 |
| 远程执行 | AI 在笔记本跑 |
| 回拨通知 | 完成后电话告知 |
| 编程代理对接 | Claude Code / 类似工具 |
| 开源 Python 服务 | 可自部署 |

## 适用场景

- 通勤 / 路上派活
- 远程服务器房间跑长任务
- 任何"AI 跑了几小时才回来"的场景

## 原始链接

- [项目仓库](https://github.com/voxa-code/voxa)
- [推文剪藏](https://x.com/QingQ77/status/2081912523100438861)

## 相关概念

- [Harness Remote](./tool-harness-remote.md) — 手机端遥控 OpenCode / Oh My Pi 等 AI 编程助手
- [HappyFigure / Hermes 桌面 (Hermes Mobile)](./tool-hermes-desktop.md) — Hermes Agent 的桌面 + 远程 GUI
- [Hermex](./tool-hermex.md) — SwiftUI iOS 应用，远程操控自托管 Hermes AI 代理
- [happier](./tool-happier.md) — 开源端到端加密跨设备 AI 编码客户端