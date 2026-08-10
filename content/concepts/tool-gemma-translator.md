---
type: "Tool"
title: "Gemma Translator"
description: "google-gemma 开源、跑在树莓派等本地设备上的离线实时语音翻译器，使用 Gemma 4 模型 + LiteRT-LM 推理引擎，480x320 小屏复古终端 UI，附带 3D 打印外壳文件。"
resource: "https://github.com/google-gemma/gemma-translator"
tags: [offline, voice-translation, raspberry-pi, gemma, liter-tm, edge-ai]
timestamp: "2026-08-10T00:33:00Z"
---

# Gemma Translator

## 它是什么

[Gemma Translator](https://github.com/google-gemma/gemma-translator) 是 google-gemma 团队出的一款**完全离线**的实时语音翻译器，目标硬件是树莓派一类的本地边缘设备。模型侧用 Gemma 4，推理引擎用 LiteRT-LM，整套部署下来**无需联网**也能工作。两个人各说自己的母语，机器实时把每句话译成对方的语言并朗读出来。

## 为什么用它 / 适合什么场景

- 离线 / 隐私敏感场景：不希望把对话内容上云做翻译（医疗 / 律师面谈 / 远程采访）。
- 边缘 / 无网环境：展会、野外、灾区、跨境活动现场的临时翻译。
- 极简终端风格硬件：480×320 的小屏幕设备和复古终端 UI 配合，整体像一台「会翻译的对讲机」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 完全离线 | 装好后断网也照常工作 |
| Gemma 4 模型 | google-gemma 系列最新语言模型 |
| LiteRT-LM 推理 | 轻量化本地推理引擎 |
| 实时双向翻译 | 双方各说母语，机器互译并朗读 |
| 480×320 UI | 复古终端界面，适配小尺寸屏幕 |
| 3D 打印外壳 | 仓库附外壳 3D 文件，可自行整成一台独立设备 |

## 媒体

![](https://pbs.twimg.com/media/HPPmo7KaEAEMOE4.jpg)

## 参考链接

- [项目仓库](https://github.com/google-gemma/gemma-translator)
- [原始链接](https://x.com/QingQ77/status/2086611737718210748)

## 相关概念

- [Freely](./tool-freely.md) — 同属「本地跑实时语音 / 转写」另一套（基于 Whisper），但偏会议场景的纯转写 + LLM 提示
