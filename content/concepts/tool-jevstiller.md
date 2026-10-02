---
type: "Tool"
title: "Jevstiller（tomerglick57：Jev 本地缓存 + 分歧上限）"
description: "tomerglick57/Jevstiller：反复调用 Jev 做分类时，每答一次都跑一趟网络很贵；Jevstiller 让本地小模型逐步接住这些请求，并配一条写死的分歧上限（disagreement cap）兜住答错比例——把云端决策模型变成「先本地、不确定再云端」的省钱版本。"
resource: "https://github.com/tomerglick57/Jevstiller"
tags: "[jev, local-llm, caching, classification, fallback, disagreement-cap, cost-saver]"
timestamp: "2026-10-02T11:30:00Z"
---

# Jevstiller（tomerglick57：Jev 本地缓存 + 分歧上限）

## 它是什么

[Jevstiller](https://github.com/tomerglick57/Jevstiller) 是 tomerglick57 出品的**Jev 调用省钱器**——

- 反复用 Jev 做分类时，每答一次都要调云端网络（贵）
- Jevstiller 让**本地小模型逐步接住**这些请求
- 配一条**写死的分歧上限（disagreement cap）**——本地答与云端答分歧超过阈值，才调云端；否则直接用本地答案

## 为什么用它 / 适合什么场景

| 场景 | Jevstiller 的好处 |
|------|-----------------|
| 大量调用 Jev | 省网络与 token 成本 |
| 想要低延迟 | 本地小模型亚毫秒返回 |
| 容忍小概率答错 | 分歧上限做兜底 |
| 边缘 / 离线场景 | 大部分请求本地就能搞定 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地小模型接管 | 训练一个本地 classifier 模仿 Jev |
| 分歧上限 | 本地答与云端答分歧超阈值才回源 |
| 渐进迁移 | 本地模型随调用数增加越来越准 |
| 成本可视化 | 显示「省了多少次云端调用」 |

## 工作原理

```
用户请求 → 本地小模型初答 → 答得自信？ → 是 → 直接用
                                    ↓ 否
                              → 调云端 Jev
                                    ↓
                              → 记录分歧，训练本地模型
```

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105982878685552879>
- 项目链接：<https://github.com/tomerglick57/Jevstiller>

## 相关概念

- [Jev WebMCP Extension](./tool-jev-webmcp-extension.md) — Jev 浏览器扩展版
- [Imajev](./tool-imajev.md) — 类似的「本地小模型 + 受约束输出」思路，但定位多模态决策
- [Local LLM](#) — 本仓库目前未收录
