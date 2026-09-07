---
type: Tool
title: "Open Steps"
description: "Claude Code 插件（7 个 Skill + 2 个 Hook），让 Agent 干完活用大白话汇报：做完没、要你干啥、欠没欠新债、能不能关；附 evals 目录可重跑 21 句触发测试。"
resource: "https://github.com/kharmanskyi/open-steps"
tags: "[claude-code, skill, plugin, evaluation, dev-experience]"
timestamp: "2026-09-07T13:08:00Z"
---

# Open Steps

## 它是什么
给 Claude Code 装的一组技能包（含 7 个 Skill + 2 个 Hook），把"干完活"这个环节从工程黑话改成大白话汇报。作者把整套打包成一个 Claude Code 插件安装。

## 解决的痛点
不懂工程术语的人用 AI 写代码，结束时面对一堆 commit hash、PR 链接、CI 状态、TODO，根本不知道"它到底做完没、我下一步要干啥"。

## 七个 Skill 的角色
| 角色 | 说明 |
|------|------|
| 挑活 | 从用户描述里抽出可执行任务 |
| 带你操作 | 把执行步骤转成"接下来你要做什么"清单 |
| 替你提问 | 在不确定时向用户发问而非硬猜 |
| 拦高风险 | 检测到删文件 / 改生产配置等动作要求二次确认 |
| 收尾汇报 | 一屏大白话汇报"做完没 / 要你干啥 / 欠没欠新债 / 能不能关" |
| 验别的会话 | 跨会话核验另一个 Agent 的产出 |
| 收口 | 把所有 Skill 串成一个完整闭环 |

## 两个 Hook
- 进入新任务前自动装载相关 Skill
- 收尾汇报前强制走"拦高风险" + "收口"两个 Skill

## Eval 体系
- 仓库自带 `evals/` 目录
- 21 句话在三个模型上测过触发情况
- Opus 100% / Sonnet 95% 触发率
- 用户可重跑验证

## 关键能力
| 能力 | 说明 |
|------|------|
| 大白话收尾 | 一屏讲清"做完没" |
| 7 技能闭环 | 挑活 / 操作 / 提问 / 拦截 / 汇报 / 验证 / 收口 |
| 自带 evals | 可重跑的触发率评测 |
| Claude Code 插件 | 一行命令安装 |

## 参考
- 项目链接：<https://github.com/kharmanskyi/open-steps>

## 相关概念
- [Agent Skills](term-agent-skills.md) — Open Steps 是一组打包好的 Skills
- [Claude Code](tool-claude-code.md) — Open Steps 的运行宿主
- [SkillSpec](tool-skillspec.md) — 另一套把 Skills 当契约测试的工具