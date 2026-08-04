---
type: "Playbook"
title: "AGENTS.md 八规则（Vercel Next.js 团队）"
description: "把一份 8 条规则的 AGENTS.md 放进项目根目录，强制 AI 编码 agent 不写兼容层、不预防性抽象、不重新发明轮子，从源头省 token；side project / 内部工具 / 原型适用，生产环境需自行去掉第 1 条。"
resource: "https://x.com/AYi_AInotes/status/2084522269745820010"
tags: "[agents-md, ai-coding, token-saving, coding-rules, engineering-practice, vercel]"
timestamp: "2026-08-04T20:30:00Z"
---

# AGENTS.md 八规则（Vercel Next.js 团队）

把以下 8 条规则放进项目根目录的 `AGENTS.md`，Cursor / Claude Code / Codex / Windsurf 会自动读取并遵守。**目标是让 AI 写代码前先停一下——能不写的不写、能复用的复用、能简单的别复杂**。

## 适用场景

- 个人 side project / 内部工具 / 原型 / 一次性 demo
- 团队项目里专门给「AI 写代码的部分」加约束
- 想给 Cursor / Claude Code / Codex / Windsurf 等工具加一个"AI 行为守则"文件

## 适用前警告

这套规则**只适合 side projects，生产环境慎用**。原规则第 1 条「不保留向后兼容」曾让 agent 差点删了生产数据库的表、差点丢 2000 美元数据。生产环境建议至少**把第 1 条删掉或改温和**。

## 步骤（八条规则）

### 1. 不保留向后兼容
过时的直接删。**别加兼容层、别写 migration、别留 fallback**。这条最危险，side project 适用，生产环境慎用。

### 2. 选能满足当前需求的最简单实现
**不要预防性抽象，不要多此一举的配置层**。

### 3. 系统分层长
**先跑通一个最小的端到端版本，再往上加东西**。绝不为了未完成的复杂度拆掉能跑的东西。

### 4. 组件保持模块化
**关注点分离**，每个模块做一件事并做好。

### 5. 优先用成熟的、有人维护的库
**没有明确理由别自己重写**。

### 6. 先翻项目里已有的依赖能做什么
再考虑加新包或自己写。**别上来就假设库里没有**。

### 7. 架构决策往长了做
**不接受"先这样以后再换"的临时方案**。

### 8. 先看成熟产品怎么解决同一个问题
**用已验证的模式，别从零发明**。

## 验证 / 自检

- [ ] 项目根目录有 `AGENTS.md` 文件
- [ ] 文件包含上述 8 条规则（生产环境至少去掉第 1 条）
- [ ] 当前用的 AI 编码工具（Cursor / Claude Code / Codex / Windsurf）会自动读取 AGENTS.md
- [ ] AI 写代码时不再做兼容层 / 预防性抽象 / 重复发明
- [ ] token 消耗对比之前有下降趋势

## 适用范围调整

| 环境 | 调整 |
|------|------|
| side project / 内部工具 / 原型 | 原样使用 8 条 |
| 生产环境 | 删除或改温和第 1 条（不保留向后兼容） |
| 长期项目 | 第 7 条（架构往长了做）的"度"自己把握 |

## 为什么能省 token

AI 写代码最大的浪费其实不是写错，是**重复写多**：

- 它引三个依赖写五个抽象层解决一个标准库十行就能搞定的事
- 你让它改，它再写两百行

这 8 条规则是在它动笔之前**先把它按住**：能不写的不写、能复用的复用、能简单的别复杂。代码短了、返工少了，token 自然就省了。

## 参考链接

- 原帖：<https://x.com/AYi_AInotes/status/2084522269745820010>

## 相关概念

- [vibe-coding-rules](./tool-vibe-coding-rules.md) — 同样为 AI 编码 Agent 装"工程纪律"，但用 6 个 Skill 流水线方式实现
- [Vibe Coding 设计系统八步法](./playbook-vibe-coding-design-system.md) — 解决 UI 风格散乱的 8 步，与本规则针对"代码层"互补
- [12-Factor Agents](./tool-12-factor-agents.md) — AI agent 工程化的另一种原则体系
