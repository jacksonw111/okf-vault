---
type: "Tool"
title: "CAPCOM REDox（下一代引擎数据层开源）"
description: "CAPCOM 把下一代引擎 REX 里的数据层单独拆出来开源——CAPCOM.REDox 是 .NET 侧比 System.Text.Json 更快的多格式解析器，支持直接改解析结果而非重建树。"
resource: "https://github.com/CAPCOM-TD-OSS/REDox"
tags: "[dotnet, json, game-engine, performance, serialization]"
timestamp: "2026-10-04T02:00:00Z"
---

# CAPCOM REDox

## 它是什么

[CAPCOM REDox](https://github.com/CAPCOM-TD-OSS/REDox) 是 **CAPCOM** 把下一代引擎 **REX** 里的数据层单独拆出来开源——CAPCOM.REDox 是 .NET 侧的多格式解析库。

## 关键能力

| 能力 | 说明 |
|------|------|
| 速度 | 比 `System.Text.Json` 更快 |
| 格式 | 多格式解析 |
| 可写性 | **直接改解析结果**而非重建树 |
| 出处 | CAPCOM 下一代引擎 REX 数据层 |

## 与 System.Text.Json 的差异

| 维度 | System.Text.Json | REDox |
|------|-----------------|-------|
| 速度 | 较慢（基线） | 更快 |
| 解析后修改 | 需重建对象树 | 直接改解析结果 |
| 多格式 | 单一 JSON 为主 | 多格式 |

## 适合场景

- .NET 项目需要高性能序列化 / 反序列化
- 解析后要做大量字段调整的场景（不必重建）
- 游戏 / 实时系统对解析延迟敏感
- 想用大厂生产验证过的解析库

## 参考链接

- 项目链接：<https://github.com/CAPCOM-TD-OSS/REDox>