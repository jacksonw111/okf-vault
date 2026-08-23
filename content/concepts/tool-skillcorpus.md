---
type: Tool
title: "SkillCorpus（公开 SKILL.md 的可信技能库）"
description: "EverMind-AI/SkillCorpus：把散落各处的公开 SKILL.md 收拢、审一遍安全 / 许可证，再做成按任务检索的技能库，回答前直接塞进上下文"
resource: "https://github.com/EverMind-AI/SkillCorpus"
tags: [agent-skills, skill-corpus, curation, security, ai-agents]
timestamp: "2026-08-23T13:29:00Z"
---

# SkillCorpus（公开 SKILL.md 的可信技能库）

## 它是什么

[EverMind-AI/SkillCorpus](https://github.com/EverMind-AI/SkillCorpus) 把**公开仓库里的 SKILL.md** 文件**收拢、审一遍安全和许可证**，再做一份**按任务检索**的技能库：Agent 在回答前可以把**相关技能塞进上下文**，避免在用时临时搜到质量参差、来源不可信的版本。

## 为什么用它 / 适合什么场景

- 公开 SKILL.md 散落各处，Agent 需要时既找不到也信不过。
- 想统一团队 / 产品的 Agent 技能来源（避免随便抄一个老仓库的 SKILL.md）。
- 关注安全 / 许可证合规：使用前已经把每个 SKILL 审过一遍。

## 关键能力

| 能力 | 说明 |
|------|------|
| 收拢 | 把公开仓库里的 SKILL.md 集中索引 |
| 安全审核 | 每个 Skill 入库前过一遍安全检查 |
| 许可证合规 | 过滤掉许可证冲突的 Skill |
| 按任务检索 | Agent 描述任务 → 找匹配 Skill → 塞上下文 |
| 提升信任 | 统一来源比"网上随便搜"更可控 |

## 媒体

- ![](https://pbs.twimg.com/media/HQYDOAVbcAAi-cS.png)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — SkillCorpus 是「技能」的可信来源之一
- [SkillSpec](./tool-skillspec.md) — 给 Skills 做可遵守 / 可测试 / 可验证的契约评估
- [friskeval](./tool-friskeval.md) — 发布前对 agent 技能目录做路由检查

## 参考链接

- [项目链接](https://github.com/EverMind-AI/SkillCorpus)
