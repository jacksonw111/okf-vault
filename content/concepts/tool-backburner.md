---
type: "Tool"
title: "backburner（USB-C 把 iPhone 变成 Mac 算力）"
description: "StayLameBro 出品的开源项目：用一根 USB-C 线把 iPhone 接成 Mac 的额外算力，跑 Qwen3.8-27B 时把 41-64 层交给手机 GPU 的矩阵单元，预填充提速 29%-44%，可用上下文从 64k 拉到 128k+。"
resource: "https://github.com/StayLameBro/backburner"
tags: "[mac, iphone, llm, inference, usb-c, qwen, gpu, edge-compute]"
timestamp: "2026-10-06T00:35:00Z"
---

# backburner

## 它是什么

[backburner](https://github.com/StayLameBro/backburner) 是 **StayLameBro** 出品的开源项目——用 **一根 USB-C 线** 把 iPhone 接成 Mac 的**额外算力**：跑 Qwen3.8-27B 时把 41-64 层交给手机 GPU 的矩阵单元。

## 关键能力

| 能力 | 说明 |
|------|------|
| 物理层 | 10Gb/s USB-C 线（iPhone + Mac 直连） |
| 模型拆分 | 1-40 层留 Mac，41-64 层给 iPhone GPU 矩阵单元 |
| 流水 | 256 token 一批错峰流水 |
| 提速 | 16k-48k 上下文预填充等待减少 **29% ~ 44%** |
| KV 卸载 | Mac 64k KV 到顶后，按每页 4,096 个 key 迁往手机 |
| 容量上限 | 启动时按 iPhone 剩余内存自动算；iPhone 17 Pro Max 8-bit 可到 196k-229k token |
| 实测 | 128k 上下文已可运行 |

## 适合场景

- 24GB 内存的 Mac 想跑更大上下文 LLM 但 KV 卡显存
- 不想花大钱买 M3 Ultra / 双机推理
- 有 Type-C 接口的旧 iPhone 闲置，可以拿出来当协处理器

## 参考链接

- 项目链接：<https://github.com/StayLameBro/backburner>

## 相关概念

- [Qwen3](./term-qwen3.md) — 演示所用基座模型
- [Apple Silicon](./term-apple-silicon.md) — Mac 与 iPhone GPU 的统一内存体系