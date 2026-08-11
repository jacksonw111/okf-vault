---
type: "Tool"
title: "DeepSeek SSD（yanun0323/deepseek_ssd）"
description: "把 284B 参数的 DeepSeek-V4-Flash-0731 MoE 模型跑在 Apple Silicon Mac 上,通过把按需路由的专家权重从 SSD 流式加载弥补统一内存不足,让约 30 GB 内存的 M 系列 Mac 本地跑得动超大规模 MoE。"
resource: "https://github.com/yanun0323/deepseek_ssd"
tags: "[deepseek, moe, ssd-offloading, apple-silicon, local-llm, inference]"
timestamp: "2026-08-11T16:00:00Z"
---

# DeepSeek SSD

[DeepSeek SSD](https://github.com/yanun0323/deepseek_ssd) 让 284B 参数的 DeepSeek-V4-Flash-0731 **MoE 模型**在 Apple Silicon Mac 的约 30 GB 统一内存里本地运行。MoE 推理时只有部分专家被路由激活,本项目通过把**按需路由的专家权重从 SSD 流式加载**,补足统一内存装不下全量权重的缺口。

项目链接：<https://github.com/yanun0323/deepseek_ssd>

## 它是什么

一个**MoE 专家权重 SSD 流式加载器**:保留少量常驻专家在内存,把剩余大量非活跃专家存放在 SSD,按路由信号动态取回;同时把统一内存当成 KV cache 与激活缓冲。给"买不起几百 GB 内存的 Mac 也能本地跑超大 MoE"提供了路径。

## 为什么用它 / 适合什么场景

- **消费级 Apple Silicon 跑超大 MoE**:不需买 Mac Studio / Mac Pro / 服务器 GPU。
- **统一内存不足补足**:MoE 稀疏激活特性 → SSD 流式权重天然契合。
- **本地 + 离线**:敏感数据不出本机,适合科研 / 个人场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| MoE 专家 SSD 流式加载 | 路由层在内存,被激活的专家按需从 SSD 拉取 |
| Apple Silicon 优化 | Metal / 统一内存模型适配 |
| 目标 284B 模型 | DeepSeek-V4-Flash-0731 全量参数规模 |
| 显存替代方案 | ~30 GB 统一内存即可启用 |
| 推理时仅活跃专家 | MoE 稀疏激活让 SSD 带宽压力可控 |
| 本地 / 离线运行 | 无需外网 / API Key |

## 媒体

![](https://pbs.twimg.com/media/HPV6eDubQAAK00E.jpg)

## 参考链接

- [项目仓库](https://github.com/yanun0323/deepseek_ssd)

## 相关概念

- [Ollama](./tool-ollama.md) — 基于 llama.cpp 的本地 LLM 一键启动器,与本项目属于同一「本地跑大模型」路线
- [Swiftlet](./tool-swiftlet.md) — Apple 设备流式运行 35B/80B Qwen MoE 的另一条路线