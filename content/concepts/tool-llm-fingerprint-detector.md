---
type: "Tool"
title: "LLM Fingerprint Detector（OpenAI 兼容 API 行为指纹）"
description: "ToseaAI/llm-fingerprint-detector，给声称 OpenAI 兼容的 API 实际跑的 LLM 打行为指纹，识别模型替换 / 静态度量量化等代理欺骗行为；基于 arXiv 2607.10252 的「单词语题输出分布」方法，不看 logits 不碰权重，100-400 次补全就能出结果。"
resource: "https://github.com/ToseaAI/llm-fingerprint-detector"
tags: "[llm, api, fingerprint, benchmark, security, agent-evaluation]"
timestamp: "2026-07-23T11:30:01Z"
---

# LLM Fingerprint Detector（OpenAI 兼容 API 行为指纹）

## 它是什么

[`ToseaAI/llm-fingerprint-detector`](https://github.com/ToseaAI/llm-fingerprint-detector) 是个「**LLM 模型身份鉴别器**」——验证一个声称 OpenAI 兼容的 API 背后实际跑的 LLM 模型是否与宣称一致，专门对付：

- **模型替换**：宣传用 Sonnet 4.8，实际用 Sonnet 4.5-mini
- **静态度量量化**：宣传 fp16 全精度，实际偷偷跑 int4
- **代理欺骗**：转发商挂羊头卖狗肉

## 工作原理

不读 logits、不碰权重，纯靠「**行为指纹**」：

1. 发几百次「单词语题」prompt（如「输出 1 到 100 之间的随机数」「输出一个 JSON」）
2. 收集回答的输出分布（每个 token 的偏好、温度系数、随机性等）
3. 和已知模型的指纹库对比
4. 给出「是 / 不是 / 不确定」判定

基于 **arXiv 2607.10252** 的方法论，**100-400 次补全请求**就能出结论。

## 关键能力

| 能力 | 说明 |
|------|------|
| API 后端验证 | 验证「声称跑 Sonnet 4.8」的 API 是否真在跑 Sonnet 4.8 |
| 模型替换检测 | 发现偷偷换到更便宜 / 更弱的模型 |
| 静态度量检测 | 发现偷偷量化降精度 |
| 无侵入 | 不读 logits / 不碰权重，纯黑盒 |
| 快速 | 100-400 次补全请求可出结果 |

## 为什么用它

- **采购验收**：采购 LLM API 时验证服务商是否兑承诺
- **多供应商管理**：在多个 API 之间定期做体检
- **合规审计**：监管 / 风控场景下需要可追溯的模型身份证明
- **对抗代理欺骗**：识别转发商的「挂羊头卖狗肉」

## 适用场景

- LLM API 采购 / 评测团队
- 大模型供应商自证
- Agent 平台后端模型巡检
- 模型路由 / 配额调度时的二次确认

## 相关概念

- [AI Agent Guide](./tool-ai-agent-guide.md) — 21 章中文 AI Agent 教程，本工具属于其评测 / 安全防护章节可引用的工具
- [Fable Method](./tool-fable-method.md) — 把 Fable 5 的解题方式提炼成 Skill + 对抗式 eval
- [ReactBench](./tool-react-bench.md) — 同类「Agent 评测」理念，但聚焦 React 项目实战
- [Awesome Scientific LLM Benchmarks](./tool-awesome-scientific-llm-benchmarks.md) — 精选科学 LLM 基准清单

## 原始链接

- [项目仓库](https://github.com/ToseaAI/llm-fingerprint-detector)