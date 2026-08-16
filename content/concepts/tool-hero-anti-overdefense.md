---
type: Tool
title: "HERO-Anti-OverDefense"
description: "一段可直接贴进 AI 编码助手配置文件的规则块，专门治「过度防御」四个毛病：乱加哈希、死磕边界、清单代替判断、搭没用脚手架"
resource: "https://github.com/wanshuiyin/HERO-Anti-OverDefense"
tags: [ai-coding, prompt-rules, agent-config, claude-code, codex]
timestamp: 2026-08-16T16:00:00Z
---

# HERO-Anti-OverDefense

## 它是什么
`wanshuiyin/HERO-Anti-OverDefense` 是一个 **AI 编码 agent 的规则块（prompt rules）项目**：把「别过度防御」的若干条禁令写成一组可直接粘贴的指令文本，目标读者是 Claude Code / Codex 等在仓库根有规则文件的编码助手。

## 为什么用它 / 适合什么场景
- 写了几次让 AI「完善一下边界检查」，结果它开始到处加 hash、log、try/except，代码反而变臃肿。
- 评审时发现 AI 给的 PR 90% 是无意义的兜底，真正的功能只有 10%。
- 想统一一个团队 / 个人项目里 AI 编码助手的风格基线。
- 喜欢简单实现、不喜欢「防御性编程」堆叠。

## 关键能力 / 四个被治的毛病
| 毛病 | 表现 |
|------|------|
| 乱加哈希 / cache | 给纯函数加 `lru_cache`、给一次性 IO 加 MD5，理由只是「以防万一」 |
| 死磕边界情况 | 写主流程前先列 5 个 if/else 处理「理论上」的 null、负数、超长串 |
| 清单代替判断 | 评分卡 / checklist 取代真正的逻辑判断，写出一堆「自查通过」的代码 |
| 搭没用脚手架 | 上来先建 utils / helpers / decorators / interfaces 目录，实际只调一次 |

## 媒体
- ![](https://pbs.twimg.com/media/HPvGpJpasAA_z4f.jpg)

## 相关概念
- [项目链接](https://github.com/wanshuiyin/HERO-Anti-OverDefense)