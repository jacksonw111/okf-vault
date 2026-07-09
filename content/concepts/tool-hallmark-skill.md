---
type: Tool
title: "Hallmark（开源 AI 编码设计 Skill）"
description: "Hallmark 是一个开源 design skill，让 Claude Code / Cursor / Codex 一键加载「设计感」，避免 AI 生成 UI 出现「能跑但难看」的中等生成品。"
resource: "https://github.com/nutlope/hallmark"
tags: "[design, ui, ux, ai-coding, skill, claude-code, cursor, codex]"
timestamp: "2026-07-09T20:50:00Z"
---

# Hallmark（开源 AI 编码设计 Skill）

## 它是什么
`nutlope/hallmark` 是一个**面向 AI 编码 agent 的开源设计 Skill**（设计纪律文件包），目的是让 Claude Code / Cursor / Codex 等 agent 在写 UI、落地页、组件时，从一开始就具备「设计感」输出，而不是产出一个能用但视觉上很「AI 风」的中等品。

安装一行：

```bash
npx skills add nutlope/hallmark
```

## 为什么用它 / 适合什么场景
- 觉得自己用 AI 写的 UI 总「差那么一点设计感」的开发者。
- 不想**每写一个 UI 都手工打补丁**——直接让 agent 加载设计 Skill。
- 适合：前端工程师、产品经理、独立开发者、Vibecoder 团队。
- 与 [Kinetics](tool-kinetics.md)（CSS + React + Prompt 三版本动画库）和 [Vibecoded Design Tells](tool-vibecoded-design-tells.md)（AI 网站设计特征排行榜）形成「设计提升三件套」。

## 关键能力
| 能力 | 说明 |
|------|------|
| Agent Skills 协议打包 | 符合 [Agent Skills](term-agent-skills.md) 规范，npx 一键装 |
| 跨编辑器 | Claude Code / Cursor / Codex 通吃 |
| 设计纪律 | 内置排版 / 配色 / 间距 / 字体层级等设计规则 |
| 即装即用 | 一行命令加载，下一次 agent 调用就生效 |

## 媒体参考

演示视频：
- <https://video.twimg.com/amplify_video/2074794215465426944/vid/avc1/1920x1080/AjVhGWU0s3WdnXcO.mp4?tag=28>

## 相关概念
- [Kinetics](tool-kinetics.md) — 99 个开源运动效果动画库，三版本同步发
- [Vibecoded Design Tells](tool-vibecoded-design-tells.md) — 320 万 Reddit 帖子总结的「AI 网站视觉痕迹」排行榜
- [Agent Skills（代理技能包）](term-agent-skills.md) — 本概念遵循的协议
- [shadcn themes on 21st.dev](tool-shadcn-themes-21st.md) — 聚合社区所有 shadcn 主题的预览/复制站

## 参考链接
- 项目链接：<https://github.com/nutlope/hallmark>
- 原始介绍（x.com）：<https://x.com/L_go_mrk/status/2074799402888376556>
