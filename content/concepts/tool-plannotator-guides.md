---
type: Tool
title: "plannotator / guides（diff 评审 HTML 页生成）"
description: "把一份代码 diff 拆成有章节的阅读顺序，逐章讲清楚每组文件改了什么、为什么改；最后产出用浏览器就能直接打开的单文件 HTML 评审页。"
resource: "https://github.com/plannotator/guides"
tags: [agent, code-review, diff, html, plan, devtools]
timestamp: 2026-08-21T14:27:00Z
---

# plannotator / guides（diff 评审 HTML 页生成）

## 它是什么
plannotator/guides 把 AI 编码 agent 的「代码评审」体验做成有结构的产物：拿到一份 PR diff 后，先按文件 / 主题拆成章节，每个章节用自然语言讲清楚「这组文件改了什么 / 为什么这么改 / 风险点在哪」，最后把所有内容打包成一份浏览器可直接打开的单文件 HTML 评审页——不依赖任何服务、不上传代码、可在本地分享。

## 为什么用它 / 适合什么场景
- AI 编码 agent 跑完一轮后想给人类一份「人能读懂」的 PR 摘要，而不是一坨 patch。
- 团队 code review：想让 reviewer 先看 HTML 评审页里的章节化解释再看 raw diff。
- 安全 / 合规场景：希望 PR 评审产物可归档、可离线打开、可邮件外发。

## 关键能力
| 能力 | 说明 |
|------|------|
| 章节化阅读顺序 | 把 diff 拆成主题分组，非按文件平铺 |
| 自然语言解读 | 每组文件配「改了什么 / 为什么改」解释 |
| 单文件 HTML | 产出无依赖单文件，浏览器即开 |
| 本地优先 | 不上传代码、不连服务端 |
| 可分享 | HTML 文件可直接邮件 / IM 发给同事 |

## 一句话总结
**把 agent 改完代码后那坨 diff，变成一份「章节化、浏览器即开」的单文件 HTML 评审报告。**

## 原始链接
- [plannotator/guides](https://github.com/plannotator/guides) — 原始仓库

## 媒体
- ![plannotator 评审页示意](https://pbs.twimg.com/media/HQNmBLyasAAphA0.png)

## 相关概念
- [kcap-cli](./tool-kcap-cli.md) — 给 AI 编码助手做可观测性 CLI，含 PR / agent 行为分析
- [Codex Dream Skin](./tool-codex-dream-skin.md) — 同样把桌面 / Web 体验做成可分享的产物