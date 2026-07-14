---
type: "Tool"
title: "fable-commander（DennisWei9898/fable-commander）"
description: "Claude Code 编排 Skill:把任务交三类角色——最强模型只负责规划与审稿,便宜模型负责研究与写码,独立 agent 专门挑刺验收,用模型成本差换更高产出。"
resource: "https://github.com/DennisWei9898/fable-commander"
tags: "[claude-code, skill, orchestration, multi-agent, role-routing, model-router]"
timestamp: "2026-07-14T15:48:00Z"
---

# fable-commander

[fable-commander](https://github.com/DennisWei9898/fable-commander) 是一个 **Claude Code Skill**,把任务按角色切分:

| 角色 | 用什么模型 | 干什么 |
|------|-----------|--------|
| 规划 / 审稿 | 最强模型 | 拆任务、定方向、审最终产物 |
| 研究 / 写码 | 便宜模型 | 大量上下文检索与样板实现 |
| 验收 / 挑刺 | 独立 agent | 不信任 worker 自评,独立 agent 跑验证 |

## 关键设计

- **成本最优**:把「贵的模型」用在「便宜的判断」上,贵的判断留给贵的环节。
- **独立验收**:worker 不自我评估,由专门 agent 挑刺,降低「自评分通过」陷阱。
- **Skill 形态**:以 Claude Code Skill 形式存在,即装即用。

## 适合什么场景

- 中型任务(开发功能 / 写文档 / 提 PR),想用最贵模型前**先让便宜模型干苦活**。
- 团队里 Claude Code 用户希望**统一调用模式**(规划 + 写 + 验)。
- 想压低 API 账单,但不愿牺牲质量。

## 与同类资源的差别

| 资源 | 特征 | fable-commander |
|------|------|-----------------|
| loop.js | 目标 + 执行 + 验证三件事同 prompt | 平权式;fable-commander 三角色分明 |
| Agentic Mercy 10x | 路由 + 写入钩子强制规范 | 偏流程纪律;fable-commander 偏模型成本优化 |
| fable-harness | Hooks / Skill / 子代理纪律化 | 偏通用纪律;fable-commander 偏特定三角色编排 |

## 参考链接

- [项目仓库](https://github.com/DennisWei9898/fable-commander)

## 相关概念

- [fable-harness](./tool-fable-harness.md) — 通用 Claude Code 行为协议,偏纪律化流程
- [loop.js](./tool-loop-js.md) — 同 prompt 多角色编排工具
- [agentic-mercy-10x](./tool-agentic-mercy-10x.md) — Claude Code 路由 + 写入钩子发行版
