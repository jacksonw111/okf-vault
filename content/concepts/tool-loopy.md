---
type: Tool
title: "Loopy"
description: "Forward Future 出品的带反馈 AI 代理工作流模板：执行 → 自我验证 → 决定继续或停下，可装到 Codex / Cursor / Claude Code。"
resource: "https://github.com/Forward-Future/loopy"
tags: "[ai-agent, loop-engineering, skill, prompt-template, self-verification]"
timestamp: "2026-06-29T16:00:00Z"
---

# Loopy

## 它是什么
Loopy 是 Forward Future 出品的「带自我反馈机制的代理循环工作流」模板库。核心是一套带自我验证的提示词模式：代理执行任务后自己判断结果是否符合预期、决定继续或停下。项目分两部分：Loop Library 网站（公开目录，可浏览复制循环模板）+ Loopy 技能（装到 Codex / Cursor / Claude Code 等代理里使用）。

## 为什么用它 / 适合什么场景
- **干重复活时不想每次都从头指挥**：定义好「做 → 查 → 修 → 再做」的循环模板，代理自己跑。
- **结果质量不稳定**：在循环里嵌入「验证 + 决定下一步」的逻辑，代理不再单步盲目推进。
- **想把代码历史里的重复模式沉淀成循环**：Loopy 支持从 git 历史提炼、从目录查找匹配、对话式编写新循环。

## 关键能力
| 能力 | 说明 |
|------|------|
| Loop Library 网站 | 公开目录浏览 / 复制循环模板 |
| Loopy 技能 | 装到 Codex / Cursor / Claude Code 等代理 |
| 从代码历史提炼 | git diff 中识别重复工作转循环 |
| 目录查找匹配 | 在已有循环库中找最匹配的模板 |
| 审计 / 修复 | 检查现有循环的合理性并修复 |
| 对话式编写 | 用自然语言交互生成新循环 |
| 有限轮次执行 | 设定轮次上限，跑完出运行凭证 |
| 发布材料准备 | 把验证过的循环打包成可分发格式 |

## 参考链接
- [原始链接](https://x.com/QingQ77/status/2071596045541191833)
- [项目链接](https://github.com/Forward-Future/loopy)

## 相关概念
- [Loop Engineering](./tool-loop-engineering.md) — 同名概念的方法论 + 三个 CLI（loop-audit / loop-init / loop-cost），与 Loopy 互为补充
- [Loops（jwangkun/loops）](./tool-loops-jwangkun.md) — 100 个 AI 自动化循环模板，可直接参考循环结构
- [loops.elorm.xyz](./tool-loops-elorm-xyz.md) — 几十位大神的 loop engineering 思路集合