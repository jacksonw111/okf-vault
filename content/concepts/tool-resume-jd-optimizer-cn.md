---
type: Tool
title: "resume-jd-optimizer-cn（中文定制简历生成器）"
description: "基于目标 JD 和真实经历，解析岗位差距、追问遗漏素材，生成 ATS 可读、HR 易判断、面试可自洽的中文定制简历。"
resource: "https://github.com/coinluu/resume-jd-optimizer-cn"
tags: [resume, jd, ats, chinese, career, ai]
timestamp: 2026-06-26T16:50:00Z
---

# resume-jd-optimizer-cn

## 它是什么

resume-jd-optimizer-cn 是一个**基于目标 JD 与真实经历自动生成中文定制简历**的工具。它解决"通用简历海投 0 回复"的核心问题——把"我有什么"和"对方要什么"做精准对齐。

工作流：

1. **喂入 JD**：目标岗位描述
2. **喂入真实经历**：你做过的事（项目 / 实习 / 工作）
3. **解析岗位差距**：JD 关键词 vs 你的经历，找出**缺什么 / 弱什么**
4. **追问遗漏素材**：针对差距反向问你"你到底做没做过 X？"
5. **生成定制简历**：输出
   - ATS（简历自动筛选系统）能正确解析的格式
   - HR 一眼能判断的"对不对口"
   - **面试时能自圆其说**（这是底线，不编造）

## 为什么用它

| 痛点 | 解法 |
|------|------|
| 简历海投石沉大海 | 针对每个 JD 定制 |
| 编了项目面试被问穿 | "面试可自洽"是底线，工具会主动追问可疑素材 |
| 不懂 ATS 怎么筛 | 按 ATS 友好格式输出 |
| 不会写中文技术简历 | 内置中文表达模板 |
| 不知道 JD 真正要什么 | 关键词差距分析 |

## 关键能力

| 能力 | 说明 |
|------|------|
| JD 解析 | 关键词 / 必备技能 / 加分项拆解 |
| 经历差距分析 | 你的素材 vs JD 要求 |
| 主动追问 | 缺素材时反向问你 |
| ATS 友好输出 | 格式合规，ATS 不误判 |
| 面试自洽底线 | 不编造项目 / 经历 |
| 中文表达 | 内置技术简历中文模板 |

## 原始链接

- [项目仓库](https://github.com/coinluu/resume-jd-optimizer-cn)
- [原始推文剪藏](https://x.com/QingQ77/status/2070468364552786354)

## 相关概念

- [backend-agent-resume-scout](./tool-backend-agent-resume-scout.md) — 同一求职场景的"上游"：先帮你找简历该写什么项目
- [后端面试开放式问题清单](./tool-backend-interview-questions.md) — 配套的"下游"：简历过了之后准备面试
- [ExamPrep-AI](./tool-exam-prep-ai.md) — 同样把"主观产出"（简历 / 笔记）变结构化，但场景是备考
