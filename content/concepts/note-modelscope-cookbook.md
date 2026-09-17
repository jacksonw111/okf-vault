---
type: "Note"
title: "ModelScope Cookbook（魔搭紫皮书）"
description: "魔搭社区开源的模型应用实战教程，8 部分 34 章覆盖模型认知 / 数据准备 / 推理部署 / 微调评测 / RAG-Agent / AIGC。"
resource: "https://github.com/modelscope/ms-cookbook"
tags: "[modelscope, cookbook, llm, rag, agent, aigc, lora, ms-swift, evalscope, ollama, 紫皮书, 教程]"
timestamp: "2026-09-17T15:43:00Z"
---

# ModelScope Cookbook（魔搭紫皮书）

## 是什么

[modelscope/ms-cookbook](https://github.com/modelscope/ms-cookbook) 是魔搭社区（ModelScope）开源的**模型应用实战教程**，合 8 个部分、34 章（截至 2026-09-17 已可读 33 章）。教程以「拿到一个开源模型后，下一步能做什么」为线索，把模型应用链路上每个环节的最小可行路径都写成可跑示例。

## 章节地图

| 部分 | 主题 |
|------|------|
| 1 | 模型认知与下载 |
| 2 | 数据准备 |
| 3 | 推理部署（Ollama 本地、Cloud Notebook、量化） |
| 4 | 用 ms-swift 微调 |
| 5 | 用 EvalScope 评测 |
| 6 | RAG 应用 |
| 7 | Agent 应用 |
| 8 | DiffSynth 图像 LoRA 等 AIGC 内容 |

## 适合谁

- 想系统性了解「开源模型从下载到应用」全链路的开发者。
- 需要在「本地 / 云端 / 量化」之间选型的团队——教程同时给 Ollama 本地跑、Cloud Notebook 跑、量化压缩三种方案。
- 想动手做 RAG / Agent 的工程师——第六、七部分覆盖了「模型 + 外部知识 + 工具调用」的典型组合。
- 想做 AIGC 的创作者——DiffSynth 图像 LoRA 等章节覆盖 LoRA 微调做特定画风/角色生成的工程细节。

## 与相关概念的关系

- [RAG（检索增强生成）](./term-rag.md) — Cookbook 第 6 部分是该概念的开源实践样板。
- [Multi-Agent（多智能体协作）](./term-multi-agent.md) — 第 7 部分 Agent 应用章节是该概念的具体落地。
- [AIGC / LoRA 微调] — DiffSynth 章节是图像 LoRA 微调的工程示范。

## 参考

- 项目链接：<https://github.com/modelscope/ms-cookbook>
