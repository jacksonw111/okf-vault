---
type: Tool
title: "OmniVoice-Studio（3 秒样本开源语音克隆工具）"
description: "OmniVoice-Studio 是一个开源语音克隆工具：3 秒音频样本即可复刻任何人声，100% 本地运行，支持 646 种语言，可在 Claude / Cursor 等 agent 里直接调用。"
resource: "https://github.com/debpalash/OmniVoice-Studio"
tags: "[tts, voice-clone, local, open-source, speech-synthesis]"
timestamp: "2026-07-09T20:50:00Z"
---

# OmniVoice-Studio（3 秒样本开源语音克隆工具）

## 它是什么
`debpalash/OmniVoice-Studio` 是一个开源 TTS / 语音克隆工作台，号称「3 秒音频样本即可复刻任何人声，且 100% 本地运行」。宣称支持 **646 种语言**（远超 ElevenLabs 的 32 种）、可调性别/年龄/口音/情绪/方言、可粘贴 YouTube 链接自动转录翻译配音成 MP4；且已封装好给 Claude、Cursor 这类 agent 直接 MCP / function call 调起。

## 为什么用它 / 适合什么场景
- 想**完全本地跑语音克隆**，避免把声纹数据传到云端（隐私 / 合规考量）。
- 受够了 TTS SaaS 价格（个人 $5 起，Pro $99，企业 $1 320），本工具**白嫖到底**。
- 想给长视频/外语视频做**批量配音翻译**一条龙。
- 想给 agent 工具集加 TTS 能力。

## 关键能力
| 能力 | 说明 |
|------|------|
| 3 秒样本克隆 | 短样本即可生成稳定声纹 |
| 646 种语言 | 数量级领先主流商业方案 |
| 100% 本地 | 无需联网，隐私安全 |
| 性别 / 年龄 / 口音 / 情绪 / 方言 | 详细可控的声纹塑造 |
| YouTube → 转录 → 翻译 → 配音 → MP4 | 一条龙流水线 |
| Agent 集成 | 已封装给 Claude / Cursor 直接调起 |

## 媒体参考

预览截图：
- ![](https://pbs.twimg.com/media/HMrM5cVbgAAOQA2.png)

## 相关概念
- [purr](tool-purr.md) — macOS 14+ 菜单栏按住说话听写，全程本地推理
- [Verenu](tool-verenu.md) — 桌面听写工具：全局热键 + 可选转写 API + 可选清理模型
- [AI Media Assistant](tool-ai-media-assistant.md) — 中文创作者本地短视频生成 Web 工具

## 参考链接
- 项目链接：<https://github.com/debpalash/OmniVoice-Studio>
