---
type: "Tool"
title: "reelbench-skills（AI 视频拉片 Skill）"
description: "给写 AI 视频用的 Claude Code / Codex 装个「拉片」 skill，一条片子自动拆成镜头表加交互报告；核心 video-shots 切点时长由 ffmpeg 实测，模型只填四个关键字段，过 14 道质量门对账。"
resource: "https://github.com/eternityspring/reelbench-skills"
tags: "[ai-skill, video-analysis, ffmpeg, shot-list, claude-code, codex]"
timestamp: "2026-09-12T22:30:00Z"
---

# reelbench-skills

## 它是什么

[eternityspring/reelbench-skills](https://github.com/eternityspring/reelbench-skills) 是**给 AI 视频工具用的「拉片」Skill 集**：装到 Claude Code / Codex，一条片子自动拆成镜头表 + 交互报告；核心 `video-shots` 用 ffmpeg 实测切点时长，模型只填四个关键字段，最后过 14 道质量门对账。

## 核心特性

| 特性 | 说明 |
|------|------|
| 自动拉片 | 一条视频 → 镜头表 + 报告 |
| ffmpeg 切点 | 切点时长实测非估算 |
| 模型填字段 | 只需四个关键字段 |
| 14 道质量门 | 自动对账 |
| 多格式报告 | HTML / JSON / 关键帧 |
| 多语言示例 | 中英文示例齐全 |

## 为什么用它 / 适合什么场景
- 做 AI 视频评测 / benchmark。
- 复盘优秀作品的镜头节奏。
- 想标准化拉片流程避免漏看。

## 关键能力

| 能力 | 说明 |
|------|------|
| 镜头切点 | ffmpeg 实测 |
| 关键字段填写 | 模型自动填四个字段 |
| 质量门 | 14 道自动对账 |
| HTML / JSON | 多格式报告 |
| 关键帧 | 自动导出 |
| 53 镜示例 | 仓库自带 3 分钟完整示例 |

## 参考链接

- 项目仓库：<https://github.com/eternityspring/reelbench-skills>

## 媒体

- ![](https://pbs.twimg.com/media/HR-s7oAaUAAzfkq.jpg)

## 相关概念
