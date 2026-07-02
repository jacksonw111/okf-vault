---
type: Tool
title: "brain2qwerty"
description: "Meta + BCBL 的开源研究项目，用卷积编码器 + Transformer + 字符级语言模型，从非侵入式 MEG/EEG 脑电信号里解码出受试者正在打的句子。"
resource: "https://github.com/facebookresearch/brain2qwerty"
tags: "[research, neuroscience, brain-computer-interface, meg, eeg, transformer, meta]"
timestamp: "2026-07-02T14:30:00Z"
---

# brain2qwerty

## 它是什么
Meta（facebookresearch）与巴斯克认知大脑与语言中心（BCBL）联合发布的开源研究项目：从非侵入式的脑磁图（MEG）/ 脑电图（EEG）信号里，把受试者**正在打的字**还原出来。

## 为什么用它 / 适合什么场景
- 脑机接口（BCI）研究：非侵入式信号的端到端解码范式参考。
- 无障碍交互：未来 ALS 等运动障碍患者的辅助输入手段探索。
- 神经科学 + AI 跨学科工程：把 EEG/MEG 这种高噪声、低信噪比的时序信号丢给现代序列模型。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入信号 | 非侵入式 MEG（脑磁图）/ EEG（脑电图） |
| 模型结构 | 卷积编码器 + Transformer + 字符级语言模型 |
| 任务 | 把受试者正在键入的句子从脑信号里还原 |
| 数据来源 | Meta + BCBL 联合实验 |
| 形态 | 开源研究项目（GitHub 仓库 + 配套视频） |

## 相关概念
- [Cognee](tool-cognee.md) — 开源长期记忆框架，与脑机接口思路不同但都涉及「非文本信号的语义化」
- [memgui-agent](tool-memgui-agent.md) — GUI Agent 把用户操作当信号；brain2qwerty 把脑信号当操作

## 演示 / 参考
- 原始链接：<https://github.com/facebookresearch/brain2qwerty>
- 演示视频：<https://video.twimg.com/amplify_video/2072492791972982784/vid/avc1/2810x1576/Vh0xJ2mxe3VcBjlY.mp4?tag=28>