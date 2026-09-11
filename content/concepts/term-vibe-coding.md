---
type: "Term"
title: "vibe coding"
description: "Andrej Karpathy 在 2025 年提出的 AI 编程范式：完全顺从 LLM 输出、不细读代码、把「感觉对」当成验收标准；与工程化的 AI 编码流程形成鲜明对照。"
resource: "https://x.com/karpathy/status/1886192184808149383"
tags: [ai-coding, term, vibe-coding, llm]
timestamp: "2026-09-11T21:40:00Z"
---

# vibe coding

## 定义

**Vibe coding** 是 Andrej Karpathy 于 2025 年 2 月提出的术语，指一种**完全把代码交给 LLM、程序员只看「感觉对不对」**的 AI 编程方式：你描述意图、模型生成代码、你不细读、甚至不调试，直接看运行效果；遇到 bug 就再丢一句 prompt 让它改。

> "There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists."  
> —— Andrej Karpathy

## 要点

- **顺从输出**：不再一行一行审代码，靠肉眼试运行 + 体感判断。
- **意图驱动**：用自然语言描述需求，prompt 是主要「代码」。
- **快速原型**：适合 demo、个人小工具、想法验证。
- **代价**：无法维护、无法审查、不懂原理、bug 难定位。
- **对照工程化**：与 [vibe-coding-rules](./tool-vibe-coding-rules.md) 这类「纪律流水线」是反面：vibe coding 不要纪律，工程化 vibe coding 把纪律装进 Skill。

## 适用场景

| 适合 | 不适合 |
|------|--------|
| 个人 hack / 一次性脚本 | 生产环境长期维护代码 |
| 想法快速验证 | 多人协作、需要 Code Review 的项目 |
| 教学 / 探索 | 安全敏感、金融 / 医疗等高风险领域 |
| 玩具 / Demo | 复杂业务逻辑、性能敏感的底层系统 |

## 与「AI 辅助编程」的区别

| 维度 | 传统 AI 辅助编程 | vibe coding | 工程化 vibe coding |
|------|------------------|-------------|-------------------|
| 代码审查 | 必读、必审 | 不读、只跑 | Skill 流水线自检 + 自动回归 |
| 测试 | 开发者写 | 没有 | 自动回归测试 Skill |
| 变更记录 | git commit 规范 | 无所谓 | 自动 changelog Skill |
| 适用边界 | 全部 | 玩具 / 一次性 | 长期项目可用 |

## 参考链接

- 原始来源：<https://x.com/karpathy/status/1886192184808149383>

## 相关概念

- [vibe-coding-rules](./tool-vibe-coding-rules.md) — 给 vibe coding 装上 6 个 Skill 纪律流水线
- [Claude Vibe Squad](./tool-claude-vibe-squad.md) — vibe coding 思路的多模型编排工具
- [playbook-vibe-coding-design-system](./playbook-vibe-coding-design-system.md) — vibe coding 设计系统的实践剧本
</content>
</invoke>