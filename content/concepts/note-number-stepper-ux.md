---
type: Note
title: "Number Stepper UX：长按 + 滚动数字 + 渐变遮罩"
description: "「Design Engineering 101」提倡的 Number Stepper（数字步进器）动效设计原则：长按加速、滚动数字、过渡模糊、渐变遮罩，避免硬切。"
tags: "[ux, motion, design-engineering, micro-interaction]"
timestamp: "2026-06-30T15:30:00Z"
---

# Number Stepper UX：长按 + 滚动数字 + 渐变遮罩

## 它是什么

一段来自 alyx_so「Design Engineering 101」系列的 UI 工程经验：数字步进器（Number Stepper / +/- 输入框）若只点一下加一、点一下减一，用户在「调整到目标值」时会点二十次，体验很差。正确做法是**奖励长按（按住连续触发）**，并用滚动数字、过渡模糊、渐变遮罩把切换过程做得自然。

## 关键原则

- **奖励长按**：按下后快速连续步进，而不是逼用户反复点按。
- **滚动数字**：数字变化时使用滚动 / 位移动画过渡，让眼睛能跟踪到「加到几了」。
- **过渡模糊（blur on transitions）**：切换瞬间用模糊减弱，避免数字跳变刺眼。
- **渐变遮罩（gradient masks）**：在数字容器边缘加渐变遮罩，避免「数字突然出现 / 消失」的硬切感。

## 适用场景

- 数量 / 金额 / 时长等需要在大范围内调整的数值输入。
- 移动端尤其重要（手指可长按）。
- 任何把 `<input type="number">` 升级成「可控、有手感」控件的场景。

## 演示参考

视频：<https://video.twimg.com/amplify_video/2071656812668174336/vid/avc1/1916x1080/Yyr6nqBZrp0tCFaf.mp4?tag=28>

## 相关概念

- [transitions.dev](./tool-transitions-dev.md) — 网页过渡动效精选合集
- [textmotion.dev](./tool-textmotion-dev.md) — 文字动效精选合集
- [animations.dev/vocabulary](./tool-animations-dev-vocabulary.md) — Emil Kowalski 动画动作词汇表