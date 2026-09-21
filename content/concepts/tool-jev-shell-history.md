---
type: "Tool"
title: "jev-shell-history（zsh 鱼式 shell 历史自动补全）"
description: "给 zsh 补上 fish 风格的命令历史自动补全：用 TypeSafe 的 Jev 模型从最近 100 条去重历史中挑出最可能的一条，灰显在光标后供一键接受。"
resource: "https://github.com/mrnugget/jev-shell-history"
tags: "[zsh, fish, shell-history, autocomplete, jev, prediction]"
timestamp: "2026-09-21T22:00:00Z"
---

# jev-shell-history

## 它是什么

[mrnugget/jev-shell-history](https://github.com/mrnugget/jev-shell-history) 给 zsh 加上 fish shell 那种**「按下一条历史自动出现在光标后面」**的体验——区别在于它用 **TypeSafe 的 Jev 模型**做预测。

## 关键流程

1. 收集 zsh 最近 **100 条去重历史**。
2. 用 **Jev 模型**推断「最可能接下来要敲哪一条」。
3. 把候选**灰显在光标后**，用户一键（通常是 `→` 或 `Tab`）即接受。

## 为什么用它 / 适合什么场景

- 喜欢 fish shell 的体验但又想留在 zsh 生态（oh-my-zsh / p10k / 自定义补全）。
- 跑在重复性高的开发场景（CI 脚本、固定部署命令），历史补全明显提速。
- 已经在用 TypeSafe Jev 做其他判断的，可以复用同一套**类型化决策**能力。

## 关键能力

| 能力 | 说明 |
|------|------|
| Fish 风格 UX | 光标后灰显候选，一键接受 |
| Jev 驱动预测 | 类型化决策模型挑历史而不是字符串前缀匹配 |
| 局部训练数据 | 直接用本机最近 100 条历史，无需云端 |
| 不动 shell 配置 | 仅在光标后追加提示，不破坏既有补全 |

## 项目链接

- 仓库：<https://github.com/mrnugget/jev-shell-history>

## 媒体

视频：<https://video.twimg.com/tweet_video/HSodfWVb0AEgwpf.mp4>

## 相关概念

- [Laya（编码器式决策引擎）](./tool-laya-decision-engine.md) — 同为编码器式决策引擎
- [kev（Qwen 底座本地决策模型）](./tool-kev-decision-model.md) — 同样复刻 Jev 类架构的开源实现
