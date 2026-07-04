---
type: Tool
title: "SkillSpec"
description: "SkillSpec 是把 AI Agent 的 Skills 当作「可遵循、可测试、可验证」契约的工具:一条命令跑完整风险评估,把 Skill 文件输出成结构化报告。"
resource: "https://github.com/modigo/skillspec"
tags: [skillspec, skill, ai-agent, testing, validation, contract]
timestamp: "2026-07-04T15:00:00Z"
---

# SkillSpec

## 它是什么

`modigo/skillspec` 是一个让 AI Agent 的「Skill 文件」**可遵守、可测试、可验证**的工具 — 把 Skill 文件从「自然语言描述」升级成「Agent 必须遵守的契约」,一条命令跑完整审计并输出风险报告。

![配图](https://pbs.twimg.com/media/HMWr0Y4aUAA8rzV.jpg)

项目链接：<https://github.com/modigo/skillspec>

## 为什么用它 / 适合什么场景

- **Skill 文件如今多是 Markdown**,AI 是否真的按要求执行、会不会做不该做的事,没第三方审计。SkillSpec 给个合同视图。
- **企业内控**:Agent Skill 在公司里用,要通过安全 / 合规 / 工具白名单审查 — 这正是 SkillSpec 输出的报告。
- **Skill 作者质量自检**:写完一个 Skill 后跑一遍,看看是否有歧义 / 缺前置 / 缺边界。

## 关键能力

| 能力 | 说明 |
|------|------|
| 风险报告 | 一条命令跑完整 Skill 评估,输出结构化报告 |
| 契约化 | 把 Skill 文件解析成可机器校验的契约(spec) |
| 可测试 | 一组验证用例;CI 也能跑 |
| 可验证 | 在 Agent 实际调用 Skill 时核对契约遵守情况 |

## 它做了什么

1. 读 `SKILL.md`(或 Agent Skills 协议规定的元数据文件)
2. 解析能力描述、约束、工具调用范围
3. 对照一组安全 / 语法 / 行为规则生成检查报告
4. 输出风险等级与建议清单

## 适用团队

| 团队 | 用法 |
|------|------|
| Skill 作者 | 写完先跑一遍自检 |
| Agent 平台运营 | 上架前必跑,风险超阈值则拒绝 |
| 安全团队 | 审计内部门店里所有 Skill |
| AI 应用开发者 | CI 里加 skillspec,生成报告归档 |

## 相关概念

- [Agent Skills(代理技能包)](term-agent-skills.md) — Skill 规范本身
- [Skill_MAS](tool-skill-mas.md) — 元技能进化的多智能体系统编排
- [AgentStalker](tool-agent-stalker.md) — 把 LLM Agent 当系统而非模型来审计(污点图 / 攻击链 / 沙箱重放)
- [agent-lock](tool-agent-lock.md) — eBPF LSM 把 AI 代理限制在指定目录
- [SkillSpec 仓库](https://github.com/modigo/skillspec) — 项目链接
