---
type: Tool
title: "Smart Remarkable"
description: "基于 Rust 实现的 reMarkable 电子墨水平板视觉-语言 agent，是 awwaiid/ghostwriter 的派生项目：截屏手写页发给视觉大模型，把回答以真实笔迹 / 文字绘回屏幕。"
resource: "https://github.com/yangg1224/smart_remarkable"
tags: [tool, remarkable, e-ink, handwriting, vision-agent, rust]
timestamp: 2026-07-10T15:27:00.000Z
---

# Smart Remarkable

## 它是什么
reMarkable 电子墨水平板上的"视觉-语言智能体"，Rust 写就，作为 awwaiid/ghostwriter 的派生项目扩展了 Select Mode：把当前手写页面截屏发给视觉大模型，再把回答以真实笔迹或文字绘回到屏幕上。

## 为什么用它 / 适合什么场景
- 在 reMarkable 上做手写笔记 / 数学 / 草图时，希望 AI 像真人一样"看你写的东西并回应"。
- 想在墨水屏这种低功耗 / 无干扰设备上获得 AI 辅助，又不愿放弃手写体验。
- 研究 Rust 嵌入式 / 平板 agent 的参考实现。

## 关键能力
| 能力 | 说明 |
|------|------|
| 手写截屏 | 截取当前墨水页面发视觉模型 |
| 笔迹回写 | 把 AI 回答以真实笔迹或文字绘回屏幕 |
| Select Mode | 扩展自 ghostwriter，支持选区级交互 |
| Rust 实现 | 系统级性能与可控性 |

## 媒体
![Smart Remarkable 预览](https://pbs.twimg.com/media/HM1FPYXb0AAWods.png)

## 相关概念