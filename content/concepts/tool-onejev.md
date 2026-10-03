---
type: "Tool"
title: "OneJev（OmniJev：屏幕 / 照片 / 视频 / 文本判定的小型决策模型）"
description: "OmniJev 出品的 OneJev：屏幕、照片、视频和文本上的判定类问题，用一次前向传播直接返回「类型化答案 + 校准概率」，便宜快速给屏幕理解 / OCR 验证 / 内容守门场景。"
resource: "https://github.com/OmniJev/OneJev"
tags: "[decision-model, structured-output, typesafe, jev-family, agent]"
timestamp: "2026-10-03T00:00:00Z"
---

# OneJev

## 它是什么

[OneJev](https://github.com/OmniJev/OneJev) 是 **OmniJev** 出品的**小型决策模型**——专门解决「屏幕 / 照片 / 视频 / 文本上的判定类问题」：

- **一次前向传播**：不像 LLM 要生成 token 流，OneJev 一次推理直接给答案
- **类型化输出**：返回结构化结果，不必解析自由文本
- **便宜快速**：适合大批量、低延迟场景

## 为什么用它 / 适合什么场景

| 场景 | OneJev 的价值 |
|------|---------------|
| 屏幕内容守门 | 用户截图后立即判定是否包含敏感信息 |
| OCR 结果校验 | 验证 OCR 提取是否可信 |
| 内容合规 | 大量图片 / 视频批量判定 |
| Agent 工具调用前判定 | 先用 OneJev 过滤再调 LLM |
| GUI Agent | 截图后判定「这是按钮 / 输入框 / 文字」 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入 | 屏幕 / 照片 / 视频 / 文本 |
| 输出 | 类型化答案 + 校准概率 |
| 速度 | 一次前向传播 |
| 适用 | 大批量、低延迟判定 |
| 与 Jev 关系 | 属于 Jev 决策模型家族的「多模态」扩展 |

## 参考链接

- 项目链接：<https://github.com/OmniJev/OneJev>

## 相关概念

- [Jev（TypeSafe 结构化判定模型家族）](./term-jev.md) — OneJev 所属的决策模型家族
- [Abide（QuietGlass）](./tool-abide-rubric.md) — 同生态下用 Jev 做 agent 软规则检查的 Hook
