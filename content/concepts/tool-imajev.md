---
type: "Tool"
title: "Imajev（mohit67890/imajev：本地小模型多模态决策器）"
description: "mohit67890 出品的本地多模态决策框架：2B/4B/9B 小模型在本地同时读照片 / 业务记录 / 文本，按你给定的选项输出带概率与「说不了」的决策；程序只在置信时才动手，把不可信答案拒掉。"
resource: "https://github.com/mohit67890/imajev"
tags: "[local-llm, multimodal, classification, decision, confidence-calibration, small-model, calibration]"
timestamp: "2026-10-02T12:20:00Z"
---

# Imajev（mohit67890/imajev：本地小模型多模态决策器）

## 它是什么

[Imajev](https://github.com/mohit67890/imajev) 是 mohit67890 出品的**本地多模态决策框架**：让 2B / 4B / 9B 这种本地小模型**同时读照片、业务记录、文本**，按用户预定义的「选项」输出**带概率 + 「说不了（refuse）」** 的决策。**程序只在置信时动手**——把置信度不够的答案拒掉，由上层兜底。

## 为什么用它 / 适合什么场景

| 场景 | Imajev 的好处 |
|------|--------------|
| 本地分类 / 路由 | 不用上云，敏感数据不出端 |
| 多模态融合（图像 + 文字 + 结构化记录） | 同一框架统一处理 |
| 必须知道「不确定」 | refuse 选项是 first-class，模型答不出的会主动拒答 |
| 编排多 agent | 把不可信的答案挡在前置环节，省下游 token |
| 边缘 / 离线 | 2B / 4B 模型够用，普通笔记本就能跑 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 小模型优先 | 2B / 4B / 9B，本地可跑 |
| 多模态输入 | 图像 / 业务记录 / 文本三种模态同帧 |
| 受约束输出 | 用户给定的有限选项集合，避免自由发挥 |
| 概率 + refuse | 输出每选项概率 + 「说不了」置信区间 |
| 决策门控 | 程序层可设阈值，低于阈值拒执行 |
| 置信校准 | 模型答错的占比可被框架估算并写死上限 |

## 输出样例（伪代码）

```json
{
  "options": [
    { "label": "approve", "prob": 0.62 },
    { "label": "reject",  "prob": 0.21 },
    { "label": "review",  "prob": 0.13 }
  ],
  "refuse_prob": 0.04,
  "top": "approve",
  "confident": true
}
```

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105995965148828098>
- 项目链接：<https://github.com/mohit67890/imajev>

## 相关概念

- [Jevstiller](./tool-jevstiller.md) — 把云端 Jev 决策模型换成「本地逐步接管」的省钱版本
- [Cloudflare Clef & Clef-flash](./tool-cloudflare-clef.md) — 边缘托管的同类决策模型，托管而非本地
- [Harness Engineering](./term-harness-engineering.md) — 大伞概念，本工具是「受约束决策门控」的具体实现
