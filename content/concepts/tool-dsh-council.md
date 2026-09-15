---
type: "Tool"
title: "DSH Council（多模型合议插件）"
description: "DeepSeek Harness 的插件，在 DSH Web 对话里通过 /council 命令启动多模型合议：作答模型并行回答、评审模型匿名对比、仲裁模型给出最终推荐。"
resource: "https://github.com/a1exsun/dsh-council"
tags: "[deepseek-harness, multi-model, consensus, council, plugin]"
timestamp: "2026-09-15T14:00:00Z"
---

# DSH Council（多模型合议插件）

## 它是什么

[DSH Council](https://github.com/a1exsun/dsh-council) 是 **DeepSeek Harness（DSH）** 的一个插件。在 DSH Web 对话窗口里敲 `/council` 即可触发「多模型合议」流程：让多家模型在同一题上各自作答、互相评审、最后由仲裁者综合给出推荐。

## 工作流

1. **作答阶段**：选 2–8 个模型，并行独立回答同一道题，互不参考。
2. **评审阶段**：选 1–8 个评审模型，匿名对比所有作答，按质量排序并指出差距。
3. **仲裁阶段**：选 1 个仲裁模型，把作答与评审一起读进去，输出最终推荐（并标注来自哪几位 / 哪几条）。

## 为什么用它

- 单一模型的盲区被多视角覆盖；评审环节显式产出差距清单，减少「AI 瞎写」的概率。
- 把 LLM-as-judge 流水线**前置到对话窗口**而不是写代码，复用门槛低。
- 适合对答案可靠性要求高、又不想自己写 orchestration 的场景（架构选型、代码评审、争议问题调研）。

## 关键能力

| 能力 | 说明 |
|------|------|
| `/council` 命令 | 在 DSH Web 对话里直接触发 |
| 角色分层 | 作答 / 评审 / 仲裁 三类角色可独立选模型 |
| 匿名评审 | 评审者看不到作答者身份，避免 brand bias |
| 可配置规模 | 作答 2–8、评审 1–8，按成本与精度灵活组合 |
| 仲裁综合 | 仲裁者显式引用作答与评审条目，可追溯 |

## 项目链接

- 仓库：<https://github.com/a1exsun/dsh-council>