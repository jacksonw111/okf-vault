---
type: Tool
title: "backend-agent-resume-scout（牛肉项目雷达，Codex 简历 Skill）"
description: "Codex 用的简历项目发现 Skill：先联网找一批候选项目，按业务价值过滤，让用户确认后再拉源码到本地验证，最后生成 Markdown + PDF 简历项目包，专门面向后端 / AI Agent 方向。"
resource: "https://github.com/lishuangqiang/backend-agent-resume-scout"
tags: [codex, skill, resume, career, github, agent, scout]
timestamp: 2026-06-26T16:50:00Z
---

# backend-agent-resume-scout（牛肉项目雷达）

## 它是什么

backend-agent-resume-scout（外号"牛肉项目雷达"）是一个 **Codex 用的 Skill**，专门帮**后端 / AI Agent 方向的求职者**从 GitHub 上筛出**真正能写进简历、经得起面试追问的项目**，并基于源码证据自动生成简历项目包。

它不只"扔一堆链接"，而是走完整流程：

1. **联网搜索**：先找一批候选项目（按后端 / Agent 关键词）
2. **业务价值过滤**：剔除纯玩具 / 教程级项目
3. **用户确认**：让你勾选要深挖哪些项目
4. **拉源码验证**：把目标仓库拉到本地，肉眼验证（不是 star 数刷的）
5. **生成项目包**：输出 Markdown + PDF 两种格式的简历项目包

## 为什么用它

| 痛点 | 解法 |
|------|------|
| 不知道简历该放什么项目 | 按后端 / Agent 方向精筛 |
| 担心项目太简单被面试官挑刺 | 业务价值过滤 + 源码验证 |
| 写项目描述太累 | 自动生成 Markdown + PDF 简历包 |
| 担心 star 多但代码烂 | 拉到本地看源码，不只看 star |

## 关键能力

| 能力 | 说明 |
|------|------|
| 联网搜候选 | 按关键词（后端 / Agent）找项目 |
| 业务价值过滤 | 剔除纯教程 / 玩具 |
| 人工确认 | 用户决定深挖哪些 |
| 源码验证 | 拉到本地审视实现质量 |
| 双格式输出 | Markdown + PDF 简历包 |
| Codex Skill | 走 Codex skill 体系，CLI / IDE 即用 |

## 原始链接

- [项目仓库](https://github.com/lishuangqiang/backend-agent-resume-scout)
- [原始推文剪藏](https://x.com/QingQ77/status/2070421304470048961)

## 相关概念

- [resume-jd-optimizer-cn](./tool-resume-jd-optimizer-cn.md) — 配套的另一段：基于目标 JD 解析差距 + 追问遗漏素材，生成定制简历
- [后端面试开放式问题清单](./tool-backend-interview-questions.md) — 同一求职场景的另一面：拿到 offer 后怎么准备面试
- [claude-code-best-practice](./tool-claude-code-best-practice.md) — 同为"用 Agent 武装自己"思路（这里是求职，CC-BP 是工程实践）
