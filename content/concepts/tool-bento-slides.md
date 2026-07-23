---
type: "Tool"
title: "Bento（单 HTML 演示文稿 + Agent 编辑）"
description: "nyblnet/bento，一个单 HTML 文件的演示文稿工具：编辑 / 播放 / 查看三合一，接收方打开即可使用，文档数据以明文 JSON 存在文件头部，支持 Agent / AI 直接编辑。"
resource: "https://github.com/nyblnet/bento"
tags: "[slides, presentation, html, single-file, agent, json]"
timestamp: "2026-07-23T14:25:00Z"
---

# Bento（单 HTML 演示文稿 + Agent 编辑）

## 它是什么

[`nyblnet/bento`](https://github.com/nyblnet/bento) 是一款「**单 HTML 文件演示文稿工具**」——整份幻灯片就是**一个 .html 文件**，可以：

- 编辑（自带编辑器）
- 播放（自带演示模式）
- 查看（任何浏览器打开都能用）
- **被 Agent / AI 直接编辑**（数据以明文 JSON 存在文件头部）

## 关键能力

| 能力 | 说明 |
|------|------|
| 单 HTML 文件 | 整份幻灯片是一个 .html |
| 三合一 | 编辑 + 播放 + 查看 |
| 零安装 | 接收方不需要装任何软件 |
| 明文 JSON | 文档数据存在 HTML 文件头部，结构化、可解析 |
| Agent 友好 | AI Agent 可读 / 改这份 JSON |

## 为什么用它

- **传一份 .html 就行**：邮件 / IM / GitHub 都能分发
- **不会被版本格式淘汰**：纯 HTML 标准
- **Agent 可改**：让 Claude / Codex / GPT 直接帮你改幻灯片
- **离线可用**：打开就是离线状态

## 适用场景

- 极简分享场合（演讲资料 / 培训手册 / 客户提案）
- 想用 Agent 自动生成幻灯片的开发者
- 不想依赖 Keynote / Google Slides 的轻量用户
- 数据需要「版本化」管理的小型演示

## 相关概念

- [Presenter Mode](./tool-presenter-mode.md) — 给任意幻灯片加演示者视图（备注 + 计时 + 黑屏）
- [Bolt Slides](./tool-bolt-slides.md) — StackBlitz 出的 AI 编码 Agent 一句话生成 Web 应用底座幻灯片
- [Multi-Design PPT](./tool-multi-design-ppt.md) — 基于 Agent Skills 协议，按 62 种品牌设计语言出 HTML / PPTX / PDF
- [build-plan](./tool-build-plan-html.md) — 把技术方案 / Build Plan 文档一键变可打开的 HTML 页

## 原始链接

- [项目仓库](https://github.com/nyblnet/bento)