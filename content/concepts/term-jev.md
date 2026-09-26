---
type: "Term"
title: "Jev（TypeSafe 结构化判定模型家族）"
description: "Jev 系列是一类「System One」快速决策模型：不生成自然语言，而是直接输出符合 TypeSafe schema 的结构化判定（分类 / 评分 / 是否 / 路由），给 Agent 当快思考与外层判定层用。"
tags: "[jev, system-one, typesafe, decision-model, agent, classification, open-source]"
timestamp: "2026-09-26T21:50:00Z"
---

# Jev（TypeSafe 结构化判定模型家族）

## 定义

[Jev](https://github.com/) 是一类**结构化判定模型家族**——给 Agent 当 **System One（快思考）**层用。与传统生成式 LLM 不同，Jev 不输出自然语言，而是直接给出符合 **TypeSafe schema** 的判定结果（分类 / 评分 / 是否 / 路由），确定性高、低延迟、可解释（直接给概率 / 选项 / 打分）。

## 要点

- **不生成文本**：只做决策，返回结构化结果，**不需要解析 / retry**。
- **TypeSafe 输出**：结果直接落到强类型 schema，调用方不需要做格式清洗。
- **System One 定位**：给 Agent 做「快思考 / 路由 / 闸门」层，不替代 LLM 的慢思考与长文生成。
- **可解释**：判定依据直接是概率 / 选项 / 打分，便于审计与回放。
- **典型用途**：工具调用路由、动作选择、风险分级、意图识别、证据审计。

## 项目链接

- 仓库：<https://github.com/>

## 相关概念

- [Laya](./term-laya.md) — 同为 System One 决策模型，接口与 Jev 兼容
- [CLM](./term-clm.md) — 用对比学习做决策的另一类 System One 模型
- [CLM-8B](./term-clm-8b.md) — CLM 的 8B 版本
- [decider-2b](./term-decider-2b.md) — Jev 思路下的端侧 2B 小模型
- [JevRev](./tool-jevrev.md) — 把 Jev 当外脑给 LLM 加决策 / 证据审计回路
- [djev-run](./tool-djev-run.md) — Cloud Run 一键部署 Jev 兼容服务
- [laya-server](./tool-laya-server.md) — Laya System One 的 Docker 化 HTTP API（Jev 兼容）