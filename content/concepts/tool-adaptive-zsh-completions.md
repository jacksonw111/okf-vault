---
type: Tool
title: "Adaptive Zsh Completions"
description: "自适应 Zsh 补全引擎：跑 --help 摸清命令结构，再从你的 shell 历史里学用法，装的任何命令都能补。"
resource: "https://github.com/jacobpowaza/adaptive-zsh-completions"
tags: [zsh, shell, completion, ai-cli, terminal]
timestamp: "2026-08-25T19:30:00Z"
---

# Adaptive Zsh Completions

## 它是什么

[jacobpowaza/adaptive-zsh-completions](https://github.com/jacobpowaza/adaptive-zsh-completions) 是一个**自适应**的 Zsh 补全引擎。传统补全脚本得人工手写：「`git checkout --<tab>` 后出什么、什么顺序、什么描述」，维护成本高，跟不上 CLI 更新。

这个引擎的策略：

1. **跑 `--help` 摸清命令结构**——自动抽取子命令、参数、选项。
2. **从你 shell 历史里学用法**——你常用的参数 / 顺序会被优先推荐。
3. **装了什么命令，就能补什么命令**——零手写补全脚本。

视频：<https://video.twimg.com/tweet_video/HQeWLX3bMAA7CrO.mp4>

## 为什么用它 / 适合什么场景

- **CLI 工具装得多**：不想给每个新工具手写补全。
- **想补全贴合自己的习惯**：历史学到的顺序比静态脚本更顺手。
- **CLI 频繁更新**：工具改了参数结构，引擎再跑一次 `--help` 就跟上。
- **想偷懒不写 5 万行补全脚本**：这条项目描述里作者亲自吐槽的点。

## 关键能力

| 能力 | 说明 |
|------|------|
| `--help` 解析 | 自动抽取子命令 / 选项 / 描述 |
| 历史学习 | 从你过往 shell 历史里学常用顺序 |
| 零手写 | 装了任何命令就有补全候选 |
| 持续适配 | 命令升级后自动跟上 |
| 学习你的习惯 | 个性化排序，比静态脚本更顺手 |

## 相关概念

- [Kitty Sessionizer](./tool-kitty-sessionizer.md) — 终端侧的会话 / 项目管理
- [Agent Manager Tmux](./tool-agent-manager-tmux.md) — agent 与 tmux 的协同

## 参考链接

- 项目链接: <https://github.com/jacobpowaza/adaptive-zsh-completions>
- 原始链接: <https://x.com/QingQ77/status/2092213901957976153>