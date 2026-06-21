---
type: "Tool"
title: "animations.dev/vocabulary（动作词汇表）"
description: "Emil Kowalski 维护的「描述动画动作的精准词汇表」——把「错开 / 方向感知 / 空间一致性 / 交叉淡入 / 布局动画」等动效沟通常用词结构化，让设计师、程序员、AI 用同一套词精准描述想要的动画。"
tags: "[animation, vocabulary, design, ui, ai-prompt]"
timestamp: "2026-06-17T00:00:00Z"
resource: "http://animations.dev/vocabulary"
---

# animations.dev/vocabulary（动作词汇表）

## 它是什么

[`animations.dev/vocabulary`](http://animations.dev/vocabulary) 是 **Emil Kowalski**（动画库 Motion 作者）维护的「**动作词汇表**（motion vocabulary）」——把日常描述 UI 动画时用得上的「精准动词 / 形容词 / 副词」按语义分组整理。

> 原话：「要从 AI 获取好的动画，你需要擅长告诉它你想要什么。」

## 解决的痛点

程序员 / 设计师 / AI 在描述动画时常常词穷：

| 模糊说法 | 精准说法 |
|----------|----------|
| 「让列表动起来」 | stagger each item by 60ms |
| 「动画自然点」 | ease-out, damping 0.8 |
| 「淡入淡出」 | cross-fade with shared layout |
| 「方向感」 | direction-aware (origin from cursor / scroll position) |
| 「空间一致」 | spatial consistency（layoutId） |

词汇表让三类角色（人 / 人 / AI）**用同一套词精确沟通**。

## 典型词汇（来源推文摘录）

| 类别 | 例词 |
|------|------|
| 时序 | stagger、delay、duration、choreography |
| 方向 | origin-aware、direction-aware、spatial consistency |
| 转场 | cross-fade、shared layout、layout animation |
| 节奏 | ease-out、spring、damping、bounce |
| 编排 | overlap、offset、cascade |

## 与 [index.how/to/articulate](tool-index-how-articulate.md) 的关系

Emil Kowalski 在「设计 / UI 词汇」领域出了**两份**资源：

| 资源 | 范围 |
|------|------|
| [animations.dev/vocabulary](http://animations.dev/vocabulary) | **专注动画 / 动作**词汇 |
| [index.how/to/articulate](tool-index-how-articulate.md) | **广义设计 / UI/UX** 12 大类词汇 |

两份互补：articulate 是大词典（颜色 / 排版 / 间距 / 形状 / 反馈等），animations.dev/vocabulary 是它的「动画子卷」深挖。

## 用法

- **设计师 → 程序员**：用同一份词写 brief / 提需求，不再「这个弹一下」。
- **AI prompt 写动画**：把「错开这个物品列表」改成 `stagger list items by 80ms with spring(damping: 0.7)`——效果稳定可复现。
- **跨团队 review**：review UI 稿时直接引用词汇表里的术语，不再用「感觉不对」当理由。

## 相关概念

- [index.how/to/articulate](tool-index-how-articulate.md) — 同一作者的大词典（12 类），animations.dev 是它的动画子卷
- [transitions.dev](tool-transitions-dev.md) — 词汇表管「怎么说」，transitions.dev 管「具体怎么实现」
- [textmotion.dev](tool-textmotion-dev.md) — 同一波「动效资源」生态；专注文本级动效
