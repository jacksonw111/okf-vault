---
type: "Tool"
title: "laya-server（Laya System One 模型的 Docker 化 HTTP API）"
description: "1Panel 出品的 Laya System One 模型 Docker 化部署项目——对外暴露兼容 TypeSafe Jev 的 HTTP API（/v1/systemone），并提供可直接测试请求的网页，可做分类 / 评分 / 是否判断，返回含答案 / 模型名 / token 用量。"
resource: "https://github.com/1Panel-dev/laya-server"
tags: "[laya, system-one, docker, http-api, typesafe, jev-compatible, classifier, 1panel, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# laya-server（Laya System One 模型的 Docker 化 HTTP API）

## 它是什么

[laya-server](https://github.com/1Panel-dev/laya-server) 是 [1Panel](https://1panel.cn/) 开源的 Laya 模型服务化项目——把 [Laya](./term-laya.md) 的结构化判定能力装进 Docker，对外提供 **兼容 TypeSafe Jev 的 HTTP API**。

- 接口：`POST /v1/systemone`，提交状态 + 问题
- 任务类型：分类 / 评分 / 是否判断（多选 / 打分 / 0-1）
- 返回：答案 / 模型名称 / token 用量
- 内置：**可直接测试请求的网页**

## 为什么用它 / 适合什么场景

- 想在本地或服务器上**快速拉起一个 Laya 判定服务**，又不想自己写 FastAPI / 鉴权 / 模型加载逻辑。
- 已经在用 Jev 系列工具做 TypeSafe 判定，laya-server 协议兼容，可以**直接当 Jev 后端**接入现有调用栈。
- 想要「**带 UI 的 API 试用台**」——给非工程同事一个网页就能调。
- 适合作为 LLM agent 的**外部判定闸**：每轮 LLM 输出后再过一道 Laya 打分 / 分类，挡住胡说八道。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Docker 镜像 |
| API 路径 | `POST /v1/systemone` |
| 输入 | state + question（可指定分类 / 评分 / 是否任务） |
| 输出 | answer / model_name / token_usage |
| 协议 | TypeSafe Jev 兼容 |
| 自带 UI | 可直接测试请求的网页 |
| 适用 | LLM 外部判定闸、agent 评分 / 路由、批量分类 |

## 媒体

![](https://pbs.twimg.com/media/HTBnghoagAAjirt.jpg)

## 相关概念

- [Laya](./term-laya.md) — 本项目托管的 System One 模型
- [Jev](./term-jev.md) — TypeSafe 判定模型系列，laya-server 接口与其兼容
- [laya-mlx](./tool-laya-mlx.md) — Laya 在 Apple Silicon MLX 上的实现（端侧方案）
- [djev-run](./tool-djev-run.md) — 同为「Jev / TypeSafe + Docker 化部署」思路的另一个项目
