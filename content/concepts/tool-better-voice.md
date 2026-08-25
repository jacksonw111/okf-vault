---
type: Tool
title: "BetterVoice"
description: "语音听写时用鼠标圈选屏幕区域，截图与转写文字一起进剪贴板，让「这个」「那个」指代有上下文。"
resource: "https://github.com/TarunTomar122/better-voice"
tags: [voice, dictation, ocr, clipboard, accessibility]
timestamp: "2026-08-25T19:30:00Z"
---

# BetterVoice

## 它是什么

[TarunTomar122/better-voice](https://github.com/TarunTomar122/better-voice) 是一个 Windows 桌面端的语音听写增强工具。普通语音听写最大的痛点是：用户嘴里的「这个」「那个」无法被转写引擎识别——它不知道你指的是屏幕上哪一块。

BetterVoice 的解法是：**录音过程中随时用鼠标圈选屏幕区域**，圈到的画面会被截图，转写出的文字会连同这张截图一起塞进剪贴板，让「这个」指向的内容不再是黑箱。

![](https://pbs.twimg.com/media/HQdBEtvbMAAgdHn.png)

## 为什么用它 / 适合什么场景

- **技术文档 / 代码注释口述**：一边讲「这里有个空指针」一边圈出对应行，截图随文字一起落到笔记。
- **Bug 复述**：口头描述 bug 时圈选 UI 元素，听写 + 截图同步进工单 / IM。
- **远程协作**：远程会议里口头描述对方看不到的画面，截图帮你兜底。
- **无障碍 / 行动不便场景**：用声音 + 鼠标圈选代替完整键盘输入。

## 关键能力

| 能力 | 说明 |
|------|------|
| 实时语音转写 | 录音 → 转写为文字（接 ASR 引擎） |
| 屏幕区域圈选 | 鼠标拖框截屏，截图随当前段落一起入剪贴板 |
| 上下文绑定 | 转写片段 + 截图一一对应，避免「这个」指代歧义 |
| 剪贴板集成 | 结果直送剪贴板，方便贴到 IM / 笔记 / 工单 |

## 相关概念

- [Toolcraft](./tool-toolcraft.md) — 创意类应用 starter kit，也强调「让 AI 直接产出视觉工具」的思路

## 参考链接

- 项目链接: <https://github.com/TarunTomar122/better-voice>
- 原始链接: <https://x.com/QingQ77/status/2092059383265988924>