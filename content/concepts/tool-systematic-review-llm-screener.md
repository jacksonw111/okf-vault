---
type: "Tool"
title: "Systematic-Review-LLM-Screener（pythyn/Systematic-Review-LLM-Screener）"
description: "本地命令行工具，用本地大模型加速系统综述里的「标题 + 摘要筛选」环节——又快又保证数据不出本机，适合对隐私 / 数据合规敏感的学术研究。"
tags: "[systematic-review, research, local-llm, screening, cli, privacy]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/pythyn/Systematic-Review-LLM-Screener"
---

# Systematic-Review-LLM-Screener（pythyn/Systematic-Review-LLM-Screener）

## 它是什么

[`Systematic-Review-LLM-Screener`](https://github.com/pythyn/Systematic-Review-LLM-Screener) 是 pythyn 开源的本地 CLI，专门解决**系统综述（systematic review）里最痛苦的「标题 + 摘要筛选」环节**：

- 系统综述要按 PRISMA 流程筛几千上万篇文献；
- 人工筛极慢，用云端 LLM 又怕泄稿（未发表 / 保密研究）；
- 这个工具把 LLM 调用放到**本机**，配合本地模型（如 Ollama / llama.cpp / vLLM）跑筛选；
- 数据全程不出本机，**合规 + 隐私友好**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地推理 | 不发请求给任何云端 LLM |
| CLI 友好 | 命令行即可跑批处理、适合研究人员脚本化工作流 |
| 标题 + 摘要筛选 | 专攻系统综述「Level 1 筛选」阶段 |
| 数据不出本机 | 未发表 / 保密文献可放心过 |

## 适合什么场景

- 高校 / 实验室做系统综述（医学、教育、心理、AI 等领域）；
- 涉及未发表数据 / 保密协议的综述项目；
- 想把 LLM 筛文献嵌入现有 PRISMA 工作流的团队。

## 参考链接

- [原始链接](https://github.com/pythyn/Systematic-Review-LLM-Screener)

## 相关概念

- [Local LLM 硬件指南](note-local-llm-hardware-guide.md) — 选择本地模型、估算显存时可直接参考该笔记
- [antidoom](tool-antidoom.md) — 同样为「本地 LLM 体验」服务；antidoom 让本地模型别 doom-loop，这个工具让本地模型能干活