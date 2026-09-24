---
type: "Tool"
title: "jevgpt（判定模型当生成模型用）"
description: "把 TypeSafe 的判定模型 jev-latest 当成生成模型来用——靠多选判定逐词拼出一段聊天回复。"
resource: "https://github.com/Bewinxed/jevgpt"
tags: "[jev, typesafe, classification, generation, chat, tool]"
timestamp: "2026-09-24T21:55:00Z"
---

# jevgpt（判定模型当生成模型用）

## 它是什么

[jevgpt](https://github.com/Bewinxed/jevgpt) 是一个实验性项目：把 TypeSafe 的判定模型 jev-latest（设计上做分类 / 多选判定）当成生成模型来用，靠多选判定逐词拼出一段聊天回复。

## 关键思路

- 判定模型：原本只用于多选 / 分类
- 当生成模型用：靠多选判定逐词拼出一段回复
- 视角：把「生成」看作「每步一次分类」

## 适用场景

- 想用便宜的判定模型做聊天回复（探索性实验）
- 想理解「判定模型 vs 生成模型」的边界
- 想在受限 / 受监管的环境下做受限输出

## 注意点

- 这是实验性项目，质量与体验取决于 jev-latest 的判定能力
- 不能替代真正的生成模型做开放式任务

## 原始链接
- 项目主页：<https://github.com/Bewinxed/jevgpt>

## 相关概念
- [Astra-Ares](./tool-astra-ares.md) — 同思路：在 Codex 旁用便宜模型做档位路由
- [jev-browser-use](./tool-jev-browser-use.md) — 同思路：用便宜模型做浏览器点击