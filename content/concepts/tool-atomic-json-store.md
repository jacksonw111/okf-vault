---
type: "Tool"
title: "atomic-json-store（GreyforgeLabs，Python 原子 JSON 存储）"
description: "Python 小程序存 JSON 状态时，躲开三种常见问题：写一半崩掉、两个进程互相覆盖、旧格式文件加载失败。"
resource: "https://github.com/GreyforgeLabs/atomic-json-store"
tags: "[python, json, atomic-write, file-locking, tool]"
timestamp: "2026-09-29T16:00:00Z"
---

# atomic-json-store（GreyforgeLabs，Python 原子 JSON 存储）

## 它是什么

[atomic-json-store](https://github.com/GreyforgeLabs/atomic-json-store) 是 GreyforgeLabs 开源的 Python 小工具：给 Python 小程序存 JSON 状态时，提供原子写、文件锁、版本兼容等保障，躲开常见的「写一半崩掉 / 两个进程互相覆盖 / 旧格式文件加载失败」三类问题。

## 它解决的问题

Python 程序用 JSON 文件存状态很常见，但有三个常见坑：

| 问题 | 后果 |
|------|------|
| 写一半崩掉 | JSON 文件损坏，下次启动加载失败 |
| 两个进程同时写 | 后写覆盖先写，数据丢失 |
| 旧格式文件加载 | 新代码读老格式抛异常 |

atomic-json-store 给这三个问题都提供对策。

## 关键能力

| 能力 | 说明 |
|------|------|
| 原子写 | write-temp + rename 模式，崩溃也不会留半成品 |
| 文件锁 | 多进程并发写安全 |
| 旧格式兼容 | 加载失败时优雅降级 / 迁移 |
| 轻量 | 给 Python 小程序用，无重型依赖 |

## 媒体预览

![](https://pbs.twimg.com/media/HTWsRg6bYAA2PE5.jpg)

## 原始链接

- 项目主页：<https://github.com/GreyforgeLabs/atomic-json-store>

## 相关概念

- [InvoiceFlowAI](./tool-invoice-flow-ai.md) — 同为 Python 小工具场景，处理结构化本地存储