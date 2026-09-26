---
type: "Term"
title: "Laya System One（1Panel 出品的 TypeSafe 判定模型，与 Jev 协议兼容）"
description: "1Panel 开源的 System One 结构化判定模型，对外提供兼容 TypeSafe Jev 的 HTTP API（/v1/systemone），可做分类 / 评分 / 是否判断，返回含答案 / 模型名 / token 用量；与 NandhaKishorM/laya 是不同的项目。"
resource: "https://github.com/1Panel-dev/laya-server"
tags: "[laya, system-one, typesafe, jev-compatible, 1panel, decision-model, open-source]"
timestamp: "2026-09-26T21:50:00Z"
---

# Laya System One（1Panel 出品的 TypeSafe 判定模型，与 Jev 协议兼容）

## 定义

[Laya System One](https://github.com/1Panel-dev/laya-server) 是 [1Panel](https://1panel.cn/) 开源的 **System One 结构化判定模型**——给 Agent 当快思考层用，**协议兼容 TypeSafe Jev**。

- 接口：`POST /v1/systemone`，提交 state + question
- 任务类型：**分类 / 评分 / 是否**判断（多选 / 打分 / 0-1）
- 返回：answer / model_name / token_usage
- 输出符合 TypeSafe schema，无需解析与 retry

> ⚠️ **同名异项目**：本条目特指 **1Panel 出的 Laya System One**；与 [NandhaKishorM/laya（编码器式决策引擎，choice / score / noul 三原语）](./tool-laya-decision-engine.md) 是两个不同的开源项目，定位有重合但实现与命名都分开。

## 要点

- **System One 定位**：给 Agent 做快思考 / 路由 / 闸门，不替代 LLM 慢思考。
- **TypeSafe 输出**：结构化判定结果，强类型 schema，无需解析。
- **协议兼容 Jev**：可以直接当 Jev 后端接入现有调用栈。
- **内置 UI**：自带可直接测试请求的网页，方便非工程同事上手。
- **典型用途**：LLM 输出后的外部判定闸、agent 评分 / 路由、批量分类、风险分级。

## 相关概念

- [Jev](./term-jev.md) — 同为 System One 决策模型，接口兼容
- [laya-server](./tool-laya-server.md) — Laya System One 的 Docker 化 HTTP API 部署项目
- [laya-mlx](./tool-laya-mlx.md) — Laya 在 Apple Silicon MLX 上的端侧实现
- [laya-decision-engine](./tool-laya-decision-engine.md) — 同名但不同的项目（编码器式决策引擎）
- [djev-run](./tool-djev-run.md) — 同为「Jev / TypeSafe + Docker 化部署」思路的另一个项目