---
type: Tool
title: "OpenMontage（开源 Agentic 视频制作系统）"
description: "把 AI 编码助手变成完整视频制作工作室的开源工具——用自然语言描述需求，自动调研、写脚本、生成素材、剪辑、出成片，支持图片视频双模式与预算控制。"
resource: "https://github.com/calesthio/OpenMontage"
tags: "[video, agent, ai, media, remotion, open-source]"
timestamp: "2026-06-30T15:30:00Z"
---

# OpenMontage（开源 Agentic 视频制作系统）

## 它是什么

OpenMontage 是首个开源的 agentic 视频制作系统：用户和 AI 说「我想要一个什么样的视频」，AI 自动完成调研 → 写脚本 → 生成素材 → 剪辑 → 出成片全流程，最终通过 Remotion 用 React 组件编程式生成视频。

## 关键能力

| 能力 | 说明 |
|------|------|
| 双模式素材 | 支持「用图片做视频」和「从免费素材库找真实视频片段来剪」两种路径 |
| 全链路自动化 | 调研 → 脚本 → 素材 → 剪辑 → 成片全自动 |
| 质量评分器 | 每个环节都有质量评分器盯着，做得不好自动重做 |
| 预算控制 | 默认最多 10 美元，先看花多少再花 |
| 多代理兼容 | Claude Code / Cursor / Copilot / Codex / Windsurf 都能用 |
| 编程式渲染 | 最终通过 Remotion（React 组件）生成视频 |

## 适用场景

- 短视频内容批量生产（口播、解说、教程、营销）。
- 没有专业剪辑技能、但能用自然语言描述需求的人。
- 想用 AI 代理替代「素材网站 + 剪映 / PR」组合的场景。

## 演示参考

视频：<https://video.twimg.com/amplify_video/2071761737536434176/vid/avc1/1920x1080/-WfYsweTfPPv7xC9.mp4?tag=28>

## 相关概念

- [AI Media Assistant](./tool-ai-media-assistant.md) — 同样面向中文创作者的本地短视频生成 Web 工具
- [autoshorts](./tool-autoshorts.md) — 长视频 / 音频转竖屏短视频
- [Casting-Workflow](./tool-casting-workflow.md) — 番茄小说短篇生成
- [12-Factor Agents](./tool-12-factor-agents.md) — 让 Agent 从 demo 到实盘的工程原则

## 参考链接

- 项目链接：<https://github.com/calesthio/OpenMontage>