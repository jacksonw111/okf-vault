---
type: "Tool"
title: "mr-boxington（Rust 跨 worktree Cargo 编译缓存）"
description: "为 Rust 项目提供跨 worktree 共享的 Cargo 编译缓存，解决多检出重复编译和 target/ 目录膨胀问题。"
resource: "https://github.com/jdx/mr-boxington"
tags: "[rust, cargo, worktree, build-cache, dx, monorepo, jdx]"
timestamp: "2026-09-19T16:00:00Z"
---

# mr-boxington（Rust 跨 worktree Cargo 编译缓存）

## 它是什么

[jdx/mr-boxington](https://github.com/jdx/mr-boxington) 是 jdx 出品的 **Rust 编译缓存工具**——专门解决：

- **多 worktree**（同一 repo 多检出并行开发）时**重复编译**同一个依赖的问题。
- 每个 worktree 都有一份 `target/` 目录造成的**磁盘膨胀**。

## 为什么用它 / 适合什么场景

- 在大型 Rust 项目（特别是 monorepo / cargo workspace）里**同时开多个 worktree**做并行改动。
- 想把 `target/` 从「每 worktree 一份」改成「**全局共享一份**」，省磁盘省编译时间。
- 已经吃够「切个 worktree 就得重新拉一整套依赖编译」苦头的 Rust 开发者。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨 worktree 共享 | 多个 checkout 共用同一份编译产物 |
| 减少重复编译 | 同一 crate / proc-macro 不重复跑 rustc |
| target/ 去重 | 不再每个 worktree 都吃一份完整 target/ |
| jdx 工具链 | 与 jdx 的其它 Rust 开发工具（mise / rg 等）生态一致 |

## 与相关概念的关系

- [Rust for Kotlin Devs](./note-rust-for-kotlin-devs.md) — Rust 工程实践；mr-boxington 是其中「解决多 worktree 重复编译」的具体工具方案

## 参考

- 项目链接：<https://github.com/jdx/mr-boxington>
- 原始推文：<https://x.com/QingQ77/status/2101303797339603292>