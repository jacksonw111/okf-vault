---
type: "Tool"
title: "vibe-coding-rules（AI 编码 6-Skill 编程纪律流水线）"
description: "给 AI 编码 Agent 配上一套由 6 个 Skill 组成的「编程纪律」流水线：改前自查、安全执行命令、改后跑 28 条规则、自动回归测试、生成变更日志——专门解决 AI 改代码时「失忆、重复踩坑、无回归、无变更记录」的问题。"
resource: "https://github.com/Ron-dali/vibe-coding-rules"
tags: "[ai-coding, skills, discipline, regression-test, changelog, engineering-practice]"
timestamp: "2026-07-08T02:30:00Z"
---

# vibe-coding-rules

## 它是什么

[vibe-coding-rules](https://github.com/Ron-dali/vibe-coding-rules) 是一套**由 6 个 Skill 组成的「编程纪律」流水线**，专门给 AI 编码 Agent 装上「改代码前 / 中 / 后」的多道关卡。

定位：AI 改代码常见的「**改完不跑测试、改前不查上下文、改完不写 changelog**」一次性打包解决。

## 6 大 Skill

| 阶段 | Skill | 干什么 |
|------|-------|--------|
| 改前 | 改前自查 | 检查是否读过相关文件、是否了解影响面 |
| 改中 | 安全执行命令 | 限制危险操作、确认 destructive 命令 |
| 改后 | 跑 28 条规则 | 自检代码风格 / 安全 / 性能 等 28 条 |
| 改后 | 自动回归测试 | 自动跑测试套件，验证改动有效 |
| 收尾 | 生成变更日志 | 改完自动写 CHANGELOG |
| 持久 | 记忆 / 复盘 | 让 AI「记住」下次别再踩同样的坑 |

## 解决的痛点

| 痛点 | 解决方式 |
|------|---------|
| AI 改代码失忆 | 改前自查 + 记忆 Skill |
| AI 重复踩坑 | 经验沉淀到 Skill 库 |
| AI 改完不跑测试 | 自动回归测试 Skill |
| AI 改完无 changelog | 自动生成变更日志 |
| AI 跑危险命令 | 安全执行命令 Skill |

## 适合谁

- 大量用 AI 改代码、但被「AI 太随便」困扰的团队。
- 个人开发者，希望给 Claude Code / Cursor 等加工程纪律。
- 任何想用「Skill」方式工程化 AI 编码流程的人。

## 参考链接

- [项目仓库](https://github.com/Ron-dali/vibe-coding-rules)

## 相关概念

- [fable-harness](./tool-fable-harness.md) — 同为「Claude Code 行为纪律」工具，fable-harness 偏 hooks，vibe-coding-rules 偏 skills
- [12-Factor Agents](./tool-12-factor-agents.md) — 同为 AI agent 工程化原则