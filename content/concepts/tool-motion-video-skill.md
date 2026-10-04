---
type: "Tool"
title: "unclejobs-ai/motion-video-skill（30~90 秒动效视频制作 Skill）"
description: "unclejobs-ai 维护的 Claude Code Skill：把 AI 制作 30~90 秒动效视频的流程拆成 6 个阶段，每个阶段用脚本 + 退出码判定产出物是否通过——把角色形象、镜头时长、音画对位等不可控点变成可检验关卡。"
resource: "https://github.com/unclejobs-ai/motion-video-skill"
tags: "[ai-video, agent-skill, claude-code, motion, quality-gate]"
timestamp: "2026-10-04T08:00:00Z"
---

# motion-video-skill

## 它是什么

[unclejobs-ai/motion-video-skill](https://github.com/unclejobs-ai/motion-video-skill) 是 **unclejobs-ai** 维护的 Claude Code Skill——AI 制作 30~90 秒动效视频时，角色形象 / 镜头时长 / 音画对位等环节缺乏可检验把关手段，这套 Skill 把制作流程拆成 **6 个阶段**，每阶段用脚本 + 退出码判定产出物是否通过。

## 解决什么问题

| 问题 | Skill 解法 |
|------|-----------|
| 角色形象漂移 | 第 1 阶段用脚本锁定形象一致性，不通过就退出 |
| 镜头时长不可控 | 单独阶段验证时长 |
| 音画对位 | 单独阶段做音画同步验证 |
| 整体质量 | 6 个阶段 = 6 道关卡 |

## 与同方向 Skill 的差异

| Skill | 侧重 |
|-------|------|
| `tool-axichuhai-motion-video.md` | 16 个具体动效类型（K 线 / 黑胶 / 鱼群 等）模板 |
| `motion-video-skill` | 6 阶段通用质量门禁 + 退出码机制 |

## 适合场景

- AI 自动生成短视频想保证「每条都达标」
- 批量生产动效内容（广告 / 运营 / 教学）
- 把「AI 出视频」流程工程化、纳入 CI

## 参考链接

- 项目链接：<https://github.com/unclejobs-ai/motion-video-skill>

## 相关概念

- [axichuhai-motion-video-skills](./tool-axichuhai-motion-video.md) — 同方向的具体模板型 Skill（侧重内容）
- [motion-video-skill](#) — 同方向的流程质量门禁型 Skill（侧重把关）