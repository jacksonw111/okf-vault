---
type: "Tool"
title: "Dopbase（自托管密钥管理：单文件二进制 + 加密存储 + 历史审计）"
description: "dopbase/dopbase：开源自托管密钥管理工具，Rust 后端 + 内嵌 Vue 管理界面，打包成单文件二进制；支持 macOS / Linux 的 AMD64 + ARM64；密钥按「项目 / 环境 / 单条记录」三层组织，SQLite 数据库 + 配置 + 主密钥默认落在 ~/.dopbase。"
resource: "https://github.com/dopbase/dopbase"
tags: "[self-hosted, secrets, key-management, rust, vue, single-binary]"
timestamp: "2026-09-20T18:00:00Z"
---

# Dopbase

## 它是什么

[dopbase/dopbase](https://github.com/dopbase/dopbase) 是开源自托管的**密钥管理工具**，解决「多人多环境下 `.env` 文件存密钥难管」的问题。

## 它怎么工作

| 维度 | 说明 |
|------|------|
| 后端 | Rust |
| 管理界面 | 内嵌 Vue |
| 打包 | 单文件二进制 |
| 平台 | macOS / Linux 的 **AMD64 + ARM64** |
| 三层组织 | 项目 / 环境 / 单条记录 |
| 存储 | SQLite + 配置 + 主密钥默认落在 `~/.dopbase` |
| 与可执行文件分离 | 数据库、配置、主密钥都和外置 exe / binary 分开 |

## 为什么用它 / 适合什么场景

- 团队里 `.env` 文件在每个开发者机器上**长得都不一样**，追责 / 同步 / 审计做不下去。
- 想用 1Password / Vault 这类专业工具，**又不想把密钥交给第三方**。
- 想要**自托管 + 单文件二进制**——丢到服务器就能跑。

## 关键能力

| 能力 | 说明 |
|------|------|
| 单文件二进制 | 一个 exe/binary 搞定后端 + 管理界面 |
| 三层组织 | 项目 / 环境 / 单条记录 |
| 加密存储 | 主密钥 + 加密字段 |
| 历史 | 每条密钥的修改历史可追 |
| 审计 | 谁改了什么有据可查 |
| 跨平台 | macOS / Linux × AMD64 / ARM64 |

## 项目链接

- 仓库：<https://github.com/dopbase/dopbase>

## 媒体

![](https://pbs.twimg.com/media/HSkrc23acAASEzc.jpg)

## 相关概念

- [Self-Hosted（自托管）](./term-self-hosted.md) — Dopbase 是面向密钥管理的自托管代表
- [Vaultty](./tool-vaultty.md) — 同为「让密钥可被管理」的工具思路
