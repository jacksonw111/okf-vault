---
type: Playbook
title: "Fact-Anchored Discovery Learning（先锁无条件事实、再走发现式推导）"
description: "把「先锁定无条件事实，再走发现式推导」的教学法编码成 Pi 配置，让 AI 教人时真的教会、而不是让人背下来。"
resource: "https://github.com/amosblomqvist/learn"
tags: [learning, pedagogy, pi-config, ai-tutor, scaffolding]
timestamp: "2026-08-27T12:43:00Z"
---

# Fact-Anchored Discovery Learning

## 它是什么
[amosblomqvist/learn](https://github.com/amosblomqvist/learn) 把一套教学法**编码成 Pi 配置**，目标：让 AI 教人时真的教会，而不是让人背下来。

**核心两步**：

1. **先锁定无条件事实（fact-anchored）** —— 把"必然成立"的前提、定义、约束先夯实；
2. **再走发现式推导（discovery learning）** —— 在这些事实之上，引导学习者自己推导、试错、归纳。

这两步顺序颠倒就会出现典型 AI 教学问题：直接抛结论、让人"听懂了"但不会做；或者让学习者"自由探索"却连基本事实都没掌握。

## 适用场景
- 用 AI tutor（ChatGPT / Claude 等）教学生或新人时，想避免"光说不练 / 光练不说"；
- 想给团队培训 / Onboarding 沉淀一套"AI 教学 prompt 模板"；
- 任何"用 AI 当老师"的场景，希望学习者真掌握知识而不是死记对话。

## 前置条件
- 已经选定要教的概念 / 技能；
- 把概念拆成「无条件事实」与「可推导结论」两类；
- 准备好引导性问题（scaffolding questions）。

## 步骤
1. **列出无条件事实**——定义、定理、约束、必须记住的前提。AI 在对话开头先把这些抛出来，让学习者确认掌握。
2. **设发现式任务**——在已锁定事实之上，设计需要学习者**自己尝试 / 推导**的子任务（如改条件看结论变化、补全推导步骤、对比两个例子的差异）。
3. **过程引导而非结论直给**——AI 在每一步只问"为什么 / 还差什么 / 哪里不对"，**不直接给答案**；等学习者真的卡住再提示一点点。
4. **回检事实**——每完成一段推导，回过头让学习者重述相关事实，加深锚定。
5. **沉淀为可复用 prompt 模板**——把上面这套流程编码成 Pi 配置（system prompt / 模板字符串），下次教同样的概念直接复用。

## 验证 / 自检
- [ ] 学习者能否在没有 AI 提示的情况下复述「无条件事实」？
- [ ] 学习者能否在新情境下应用发现式推导的结论（迁移能力）？
- [ ] AI 是否在「直接给答案」上克制住了？
- [ ] 教学流程是否沉淀成了可复用的 Pi 配置 / prompt 模板？

## 相关概念
- [Agent Skills（代理技能包）](term-agent-skills.md) — 把"做法"封装成 Skill 的思路；本 playbook 是把"教学法"封装成 Skill
- [taste-skill / redesign-existing-projects](tool-taste-skill-redesign.md) — 同样是把"做事方法"编码成 Skill，让 Coding Agent 按部就班执行
- [Pi Agent 核心手册](note-pi-agent-core-book.md) — Pi 配置 / Skill 体系的入门资料

## 参考链接
- 项目链接：<https://github.com/amosblomqvist/learn>
