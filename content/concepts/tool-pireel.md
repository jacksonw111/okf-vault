---
type: "Tool"
title: "Pireel（浏览器内视频剪辑 + MCP）"
description: "pireel/pireel，开源的浏览器内口播视频剪辑工具，无需注册 / 无需后端即可在浏览器里完成「剪 + 加字幕 + 套主题 + 导出」；暴露 MCP 接口让 AI Agent 直接调用。"
resource: "https://github.com/pireel/pireel"
tags: "[video-editor, browser, mcp, agent, subtitle, open-source]"
timestamp: "2026-07-23T12:23:00Z"
---

# Pireel（浏览器内视频剪辑 + MCP）

## 它是什么

[`pireel/pireel`](https://github.com/pireel/pireel) 是一款**完全跑在浏览器里**的视频剪辑工具，主打「口播视频（podcast-style）剪辑」：

- **零注册**：打开就用
- **零后端**：纯前端 / WebAssembly
- **零安装**：单页 Web 应用
- **开源**：可自部署 / 改源码
- **MCP 暴露**：暴露 MCP 接口，**AI Agent 可以直接调它干活**

## 关键能力

| 能力 | 说明 |
|------|------|
| 浏览器内剪辑 | 不依赖本地 FFmpeg / Premiere |
| 字幕 | 自动加字幕 / 改字幕 |
| 主题套用 | 一键切预设风格 |
| 导出 | 导出可直接发布成片 |
| MCP 接口 | Agent 可调用其内部工具 |
| 完全开源 | 可改可部署 |

## 为什么用它

- **「剪视频」变轻任务**：不需要学专业剪辑软件
- **AI 可调**：MCP 让 Agent 自动完成「剪掉口水段 + 套主题 + 加字幕」
- **隐私**：浏览器内本地处理，不上传云端
- **跨平台**：任何能跑浏览器的设备都行

## 适用场景

- 知识分享型口播视频博主
- 用 AI Agent 做内容生产流水线的团队
- 不愿装桌面剪辑软件的轻量用户

## 媒体

![](https://pbs.twimg.com/media/HN4VVstb0AAOwIJ.jpg)

## 相关概念

- [FableCut](./tool-fablecut.md) — 同为「浏览器内视频编辑器」，但强调 Agent 通过 MCP / REST 直接编辑时间线 JSON
- [Montara](./tool-montara.md) — 开源 AI 原生视频制作操作系统，Timeline IR 统一规划 / 编辑 / 渲染 / 质检
- [jzsub-skill](./tool-jzsub-skill.md) — Codex Skill：下载视频 + 封面 + 双语字幕 + 烧录 MP4
- [Freecut](./tool-freecut.md) — 把付费 ElevenLabs Scribe 换成免费可插拔本地转录后端
- [SkillHub / WorkBuddy-XHS](./tool-workbuddy-xhs-skills.md) — 同为「AI Skill + 内容生产」方向

## 原始链接

- [项目仓库](https://github.com/pireel/pireel)