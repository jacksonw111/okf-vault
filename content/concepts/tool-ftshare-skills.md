---
type: "Tool"
title: "FTShare-skills（FTShare-Lab/FTShare-skills）"
description: "把 FTShare 的金融数据 / 投研流程包成 Agent 可直接调用的 Skill,供 Claude Code / Codex 等 Agent runtime 使用,把金融工具接入 agent 工具链。"
resource: "https://github.com/FTShare-Lab/FTShare-skills"
tags: "[finance, agent-skills, claude-code, codex, finsearch, api]"
timestamp: "2026-07-15T14:30:00Z"
---

# FTShare-skills

[FTShare-skills](https://github.com/FTShare-Lab/FTShare-skills) 把 **FTShare 的金融数据和投研流程包成 Agent 能直接调的 Skill**,给 Claude Code、Codex 这类 runtime 用,把金融工具接入 agent 工具链。

## 它解决了什么

金融数据(行情 / 公告 / 研报 / 财务表)原 API 多半是 HTTP+专有 schema,Agent 调用要先学 API 文档、再做拼装、再解决认证。Skills 把这些**预先折叠好**,Agent 拿到的是一组「语义化动作」(拉日线 / 取公告 / 算估值),收到自然语言指令就能做。

## 关键能力

| 能力 | 说明 |
|------|------|
| Skill 化 API | 把散装 HTTP 包成命名清晰的动作 |
| Claude Code / Codex 兼容 | 直接放进 Agent runtime skill 仓 |
| 金融垂类覆盖 | 行情 / 公告 / 研报 / 财务 / 估值 |
| 可派生数字投研 | Agent 可在此基础上做组合诊断、行业对比 |

## 参考链接

- [项目仓库](https://github.com/FTShare-Lab/FTShare-skills)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — skill 协议本身的定义
- [Claude Code（终端原生 AI 编码 agent）](./tool-claude-code.md) — 这套 skill 优先兼容的 runtime
