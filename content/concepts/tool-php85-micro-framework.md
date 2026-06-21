---
type: "Tool"
title: "PHP 8.5 零依赖微型框架（单条 PCRE 路由）"
description: "极简 PHP 8.5 框架，核心代码仅 850 行、不依赖任何第三方库：用一条 PCRE 正则搞定全部路由分发（一万条路由也只做一次 preg_match），JIT 编译后接近 O(1) 的请求开销，内置模板引擎 / 验证 / 数据库 / DI / 会话 / CLI。"
resource: "https://github.com/qingq77/php85-micro"
tags: "[php, micro-framework, regex-router, zero-dependency]"
timestamp: "2026-06-21T00:00:00Z"
---

# PHP 8.5 零依赖微型框架（单条 PCRE 路由）

## 它是什么

由 `@QingQ77` 在 2026-06 推荐的极简 **PHP 8.5 微型框架**：

- **零依赖**：850 行核心代码，不引入任何第三方库。
- **单条 PCRE 路由**：用一条正则搞定全部路由分发（一万条路由也只做一次 `preg_match`）。
- **JIT 编译后接近 O(1) 请求开销**。

## 内置能力

| 能力 | 说明 |
|------|------|
| 路由 | 单条 PCRE 正则分发 |
| 模板引擎 | 内置 |
| 验证 | 内置 |
| 数据库 | 内置 |
| DI | 内置 |
| 会话 | 内置 |
| CLI | 内置 |

## 适用场景

- 想在 PHP 上做 **极致轻量** 的微服务 / API。
- 不想被 Composer 生态绑架 —— 零依赖。
- 学习目的 —— 850 行核心代码就是一份「框架怎么写」的教材。

## 相关概念

- [Turborepo](tool-turbo.md) — 同为「少即是多」的工程哲学
- [Ultracite](tool-ultracite.md) — 同为「工具碎片化 → 一体化」思路