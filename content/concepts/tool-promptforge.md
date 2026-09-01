---
type: "Tool"
title: "PromptForge（本地 LLM 提示词打分与改写工具）"
description: "本地优先的提示词质量评分与优化工具（PyPI 包名 tuneprompt）：用约 1.5B 参数的 ModernBERT 从清晰度 / 具体性 / 上下文等 7 个维度打分，用 Qwen2.5 + LoRA 在保留原意的同时重写弱提示词，支持 Python API / CLI / Gradio 界面。"
resource: "https://github.com/arjun988/promptModel"
tags: [prompt-engineering, llm-tools, local-first, modernbert, qwen, lora, gradio, pypi]
timestamp: "2026-09-01T13:50:00Z"
---

# PromptForge

## 它是什么
[promptModel / PromptForge](https://github.com/arjun988/promptModel) 是一个**本地优先**的提示词质量评分与优化工具，已发布到 PyPI（包名 `tuneprompt`）。它把「含糊的人话」改写成「清晰、可执行的 LLM 指令」，同时保证不漂移原意。

实现上分两条流：

- **打分**：约 **1.5B 参数的 ModernBERT** 从**清晰度、具体性、上下文、目标性、约束性、示例完整性、结构性**等 7 个维度给出量化分数；
- **改写**：约 **1.5B 参数的 Qwen2.5 + LoRA** 微调后做忠实重写，目标是「保留原意 + 改得可执行」，不是「改得更花哨」。

入口支持三件套：**Python API**（嵌入既有 pipeline）、**CLI**（CI / pre-commit 可调）、**Gradio 界面**（本地浏览器调试）。

## 为什么用它 / 适合什么场景
- 想在**本地**评估提示词质量——数据不出网，不上传任何 prompt；
- 想给提示词工程建立**可量化**的评估流程（7 维分数可以接 CI 阈值门禁）；
- 想用 LoRA 微调的小模型做改写，避免每次都调 GPT-4 级别大模型；
- 想在写提示词时获得**结构化反馈**（哪个维度扣分），而不是 LLM 风格的「我觉得不错」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 7 维评分 | 清晰度 / 具体性 / 上下文 / 目标性 / 约束性 / 示例完整性 / 结构性 |
| 忠实重写 | Qwen2.5 + LoRA 微调，保留原意前提下改写 |
| 三种入口 | Python API / CLI / Gradio 浏览器界面 |
| 本地优先 | ModernBERT + Qwen 都在本地跑，prompt 不出网 |
| PyPI 发布 | 包名 `tuneprompt`，可直接 `pip install` |
| LoRA 可换 | 重写模块基于 LoRA，可换适配自己的领域 |
| 小模型路线 | 1.5B 级别，跑在消费级 GPU / Apple Silicon 上 |

## 相关概念
- [Prompt Self Tuning](tool-prompt-self-tuning.md) — 同样是本地提示词优化思路；PromptForge 偏评分 + 改写，Prompt Self Tuning 偏自我迭代

## 参考链接
- 项目链接：<https://github.com/arjun988/promptModel>
- PyPI：<https://pypi.org/project/tuneprompt/>（包名 `tuneprompt`）