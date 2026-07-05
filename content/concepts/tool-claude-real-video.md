---
type: "Tool"
title: "claude-real-video（让 AI 真正看懂视频）"
description: "本地运行的 Python 工具，给 Claude 等 AI 助手提供「真正看懂视频」的能力——按场景变化与字幕智能抽取关键帧而不是按固定时间抽帧，输出可被多模态 LLM 直接消费的精简上下文。"
tags: "[video, multimodal, ai, claude, python, frame-extraction]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/HUANGCHIHHUNGLeo/claude-real-video"
---

# claude-real-video（让 AI 真正看懂视频）

## 它是什么

[`claude-real-video`](https://github.com/HUANGCHIHHUNGLeo/claude-real-video) 是一个**本地运行的 Python 工具**，让 Claude 等多模态 LLM 能「真正看懂」视频内容，而不是按固定时间间隔机械抽帧。

它通过**场景变化检测 + 字幕定位**智能抽取关键画面与对应字幕，把视频压缩成 LLM 一次能消化的精简上下文。

## 关键能力

| 能力 | 说明 |
|------|------|
| 场景变化检测 | 用图像差异算法识别镜头切换，只在切镜头处抽帧 |
| 字幕对齐 | 把字幕文本与对应时间戳绑定输出 |
| 本地运行 | 不上传视频到云端，隐私可控 |
| LLM 友好输出 | 输出结构化 markdown / JSON，可直接喂给 Claude / GPT |
| 多格式支持 | 常见 mp4 / mov / mkv 等视频格式 |
| Token 节省 | 相比「每秒一帧」抽样方式，能减少 80%+ 视觉 token 消耗 |

## 视频演示

视频：
- <https://video.twimg.com/tweet_video/HMbcCowasAAJDUv.mp4>

## 适用场景

- 用 Claude 分析长会议录像、产品 demo、教程视频
- 在本地把视频转成「图 + 字幕」形式的笔记，方便 RAG 系统索引
- 给短视频内容创作工作流加「AI 看片」步骤（自动写脚本 / 找高潮）
- 节省多模态 token：传统「每秒一帧」很容易烧光上下文窗口

## 参考链接

- [项目链接](https://github.com/HUANGCHIHHUNGLeo/claude-real-video)

## 相关概念

- [sim-use](tool-sim-use.md) — CLI 让 AI Agent 实时观察与操作 iOS 模拟器 / Android 设备屏幕，与本工具互补做「AI 看动态界面」
- [MemGUI-Agent](tool-memgui-agent.md) — 移动端 GUI Agent，ConAct 机制管理长任务上下文