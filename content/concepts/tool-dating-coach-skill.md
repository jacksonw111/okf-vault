---
type: Tool
title: "Dating Coach Skill（HowToGetAlongWithGirls）"
description: "Mayuqi-crypto 写的 Claude 用的 AI 恋爱教练技能包，放在 .claude/skills/ 即可用。覆盖聊天记录逐条分析、阶段诊断、知识问答、对象档案管理，从搭讪到长期相处全流程，作者内置道德底线拒绝欺骗与操控。"
tags: "[claude-skill, dating, life-coaching]"
timestamp: "2026-07-01T15:30:00Z"
resource: "https://github.com/Mayuqi-crypto/HowToGetAlongWithGirls"
---

# Dating Coach Skill（HowToGetAlongWithGirls）

## 它是什么
Mayuqi-crypto 写的 Claude 技能包，给 AI 助手装上「恋爱教练」能力。装到 `.claude/skills/` 目录下，Claude 即可像恋爱教练一样分析用户与对象的聊天记录、给建议、做阶段诊断。

## 为什么用它 / 适合什么场景
- 想让 Claude 帮忙复盘聊天记录（信号识别 + 用户错误 + 改进话术）
- 想从「吸引」到「长期关系」一站式学方法论
- 想给 Claude 装一个具体领域的垂直 Skill 做扩展

## 关键能力
| 能力 | 说明 |
|------|------|
| 聊天记录逐条分析 | 指出信号、用户错误、给话术 |
| 阶段诊断 | 识别当前关系阶段（陌生 / 吸引 / 暧昧 / 交往 / 长期） |
| 知识问答 | 恋爱方法论问答，覆盖吸引到长期关系 |
| 对象档案管理 | 记录每个人对象的性格 / 兴趣 / 雷区 |
| 道德底线 | 作者内置底线：拒绝欺骗 / 操控 / 套路 |

## 与「PUA 套路」工具的区别
作者明确强调：「这是教练不是套路」。
- **不是**：教用户背固定话术 / 制造虚假人设 / 操控情绪
- **是**：帮用户识别真实信号 / 改善沟通 / 自我成长
- 工具内置道德边界，使用者想滥用会被拒

## 安装
```bash
git clone https://github.com/Mayuqi-crypto/HowToGetAlongWithGirls ~/.claude/skills/dating-coach
```

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 的概念元定义
- [mattpocock/skills](tool-mattpocock-skills.md) — 另一套 Claude Skill 合集（编码向）
- [Claude Code 微醺创意 Skill](tool-claude-code-tipsy-skill.md) — 另一种「垂直场景 Skill」示例

## 原始链接
- [项目仓库](https://github.com/Mayuqi-crypto/HowToGetAlongWithGirls)