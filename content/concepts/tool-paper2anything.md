---
type: Tool
title: "paper2anything"
description: "Claude Code 技能包，给一篇学术论文 PDF，自动生成 5 种宣传物料：PPT 幻灯片、学术海报、项目主页、小红书笔记、公众号文章；解析靠 MinerU，每个技能独立文件夹可自动触发；浙江大学 AI4GC Lab 出品。"
resource: "https://github.com/QuZhan51496/paper2anything"
tags: "[claude-code, skill, academic, paper, ppt, poster, mineru]"
timestamp: "2026-07-03T00:38:00Z"
---

# paper2anything

## 它是什么
**Claude Code 技能包**，给一篇学术论文 PDF 自动产出 5 种宣传物料：PPT 幻灯片、学术海报、项目主页、小红书笔记、微信公众号文章。每个产出对应一个独立文件夹里的 Skill，可被自动触发。

由浙江大学 **AI4GC Lab**（QuZhan51496）开发。解析论文使用 [MinerU](https://github.com/opendatalab/MinerU)，把 PDF 转成结构化的文本与图表信息。

## 为什么用它 / 适合什么场景
- 写完论文要赶 poster 终稿、答辩幻灯片、公众号介绍等一堆衍生物料，时间紧。
- 想用单一工具链覆盖「学术到大众」的 5 种传播形态，而不是切 5 个网站手写。
- 已有 Claude Code 工作流，希望物料产出也是 Skill 形式（可被自动化触发）。
- 多模态实验室 / 团队，跨论文复用同一套模板。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入 | 论文 PDF |
| 解析 | [MinerU](https://github.com/opendatalab/MinerU) 抽取文本 + 图表 + 公式 |
| 产出 1 | PPT 幻灯片（答辩用） |
| 产出 2 | 学术海报（A0 / A1 等） |
| 产出 3 | 项目主页（GitHub Pages 风格） |
| 产出 4 | 小红书笔记（图文排版） |
| 产出 5 | 微信公众号文章（富文本） |
| 触发方式 | 每个 Skill 独立文件夹，可由 Claude Code 自动触发 |
| 出品方 | 浙江大学 AI4GC Lab（QuZhan51496） |

## 相关概念
- [Obsidian Knowledge Agent](tool-obsidian-knowledge-agent.md) — 也是「论文 → 结构化笔记」的 AI 管道；paper2anything 侧重「论文 → 宣传物料」
- [speaker（学术演讲 PPTX 备注 Skill）](tool-speaker-pptx-skill.md) — 学术演讲备注生成；paper2anything 是从论文直接生成 PPT 内容
- [paper-lifecycle](tool-paper-lifecycle.md) — 论文写作 Codex skills 套件（审稿 / Rebuttal）；paper2anything 侧重「论文发表后的宣传」

## 项目链接
- 项目主页：<https://github.com/QuZhan51496/paper2anything>

## 媒体
![](https://pbs.twimg.com/media/HML7O6cacAA_TYC.jpg)