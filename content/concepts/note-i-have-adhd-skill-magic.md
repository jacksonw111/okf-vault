---
type: "Note"
title: "Skill vs Prompt —— 为什么 Skill 更有「关注度」"
description: "liaocaoxuezhe 在讨论里点出的现象：规定输出风格的内容，用 Skill 包装比放进 AGENTS.md 更容易获得关注（44.4k star 的 i-have-adhd 例子）。但更短更轻的规则其实更适合直接放进 AGENTS.md。"
resource: "https://github.com/ayghri/i-have-adhd"
tags: "[skill, prompt, agents-md, attention, output-style]"
timestamp: "2026-09-14T22:30:00Z"
---

# Skill vs Prompt —— 为什么 Skill 更有「关注度」

## 它是什么

> Skill 就是有种魔力，比 prompt 更好获得关注。

原文讨论了一个值得反思的现象：

> 像这种简单的、规定输出风格的内容，因为 ADHD 这个热门词语，居然有 **44.4k stars**：[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

但同样的内容**其实应该放进 `AGENTS.md`，而不是打包成一个 Skill**：

> 你完全可以简单地在 AGENTS.md 里面加一句话就行：

例如输出风格规则：

```markdown
## 沟通与输出规范
默认采用低认知负担、便于行动的表达方式。
- 先给答案或下一步；不寒暄、不预告
- 拆解行动；多步任务使用编号
- 保持聚焦；只处理当前目标
- 持续交代状态；说明「已完成什么 / 当前在哪 / 下一步是什么」
- 表达具体直接；短段落 + 直白措辞
- 降低启动成本；结尾只给一个具体下一步
- 必要时覆盖默认规则；破坏性操作先确认
- 执行优先；不把 AI 应做的工作改写成教程
```

## 核心论点

| 维度 | Skill | AGENTS.md 一行规则 |
|------|-------|---------------------|
| 可见度 | 高（可 star / 命名） | 低（埋在被读文件里） |
| 复用性 | 高（可跨 repo 装） | 低（按 repo 写） |
| 适用 | 复杂、可命名、可版本化的能力 | 简短通用规则 |
| 注意力 | 强（带名字 / topic） | 弱（淹没在文本里） |

## 启示

- **Skill 不是越大越好**：当规则只有几句话，更适合放 `AGENTS.md`
- **Skill 的真正价值是「注意力 + 复用」**：能被记住、能被传播、能被复用
- 名字要选好——「ADHD 风格输出」有话题度，「低认知负担沟通」没有
- 长 prompt 不必都做成 Skill；短规则反而更该直接进 AGENTS.md

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 体系本身
- [Agents.md 八条规则](./playbook-agents-md-eight-rules.md) — AGENTS.md 的标准范式

## 参考链接

- 实例仓库：<https://github.com/ayghri/i-have-adhd>
