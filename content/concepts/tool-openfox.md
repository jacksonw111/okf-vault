---
type: "Tool"
title: "OpenFox（quentin452/openfox）"
description: "把验收标准当成不可变契约,让本地 LLM 代理自己拆解计划、执行多步流水线、反复跑验证直到标准全过;跑在 vLLM / Ollama 这类本地后端,免去"本地模型只能开聊天窗,拆任务、验结果都得人肉盯"的痛点。"
resource: "https://github.com/quentin452/openfox"
tags: "[agent, local-llm, vllm, ollama, contract-driven, acceptance-criteria, multi-step]"
timestamp: "2026-08-11T16:00:00Z"
---

# OpenFox

[OpenFox](https://github.com/quentin452/openfox) 把**验收标准当成不可变的契约**,让本地 LLM 代理自己拆解计划、执行多步流水线、反复跑验证直到标准全过。跑在 vLLM / Ollama 这类本地后端上。

项目链接：<https://github.com/quentin452/openfox>

## 它是什么

一个**契约驱动的本地 agent 框架**:用户给"什么算成功"的判定标准,OpenFox 让本地模型把任务拆解成多步流水线,反复执行并跑验证,直到所有判定通过才放手。

## 为什么用它 / 适合什么场景

- **本地 LLM 也能干活**:不只聊天,而是真正跑多步任务并自验。
- **验收契约化**:把"什么算完成"显式写出来,避免 agent 跑偏。
- **后端可换**:vLLM / Ollama / 其他 OpenAI 兼容后端都行。

## 关键能力

| 能力 | 说明 |
|------|------|
| 契约式验收 | 验收标准作为不可变输入,代理不可绕过 |
| 多步流水线 | 拆解任务为有序步骤,逐步执行 |
| 自动重试 | 未通过的步骤反复跑直到通过 |
| 本地后端 | vLLM / Ollama 等 OpenAI 兼容服务 |
| 任务自拆解 | 模型自己决定任务结构 |
| 自验证 | 跑验收脚本 / 测试套直到全过 |

## 媒体

![](https://pbs.twimg.com/media/HPUzrzmaIAAfKdi.jpg)

## 参考链接

- [项目仓库](https://github.com/quentin452/openfox)

## 相关概念

- [12-Factor Agents](./tool-12-factor-agents.md) — 把 agent 当工程产物设计的原则集,OpenFox 是"契约驱动 + 本地后端"的具体落地
- [Ollama](./tool-ollama.md) — 本项目常见的本地后端选项
- [Better Harness](./tool-better-harness.md) — 五维审计 AI 编码工作流,与 OpenFox 的"验收标准"思路互补