---
type: "Tool"
title: "SiphonDB（跨平台桌面数据库管理工具）"
description: "Tauri v2 + React 19 + Rust 构建的跨平台桌面数据库 GUI 客户端，支持 PostgreSQL、MySQL/MariaDB 与 SQLite，内置交互式数据网格、行级 CRUD、SQL 编辑器与基于 Rust 多线程的 SSH 隧道（密码 / 私钥认证）。"
tags: "[database, gui, tauri, rust, react, postgres, mysql, sqlite, ssh]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/Premod1/SiphonDB"
---

# SiphonDB（跨平台桌面数据库管理工具）

## 它是什么

[`SiphonDB`](https://github.com/Premod1/SiphonDB) 是用 **Tauri v2 + React 19 + Rust** 写的跨平台桌面数据库 GUI 客户端，覆盖 PostgreSQL、MySQL/MariaDB、SQLite 三种主流引擎，目标是用同一个壳替代 Navicat / DBeaver / TablePlus 等多套工具。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跨平台桌面壳 | Tauri v2 单二进制，Windows / macOS / Linux 通吃 |
| 多引擎支持 | PostgreSQL、MySQL/MariaDB、SQLite |
| 交互式数据网格 | 浏览表数据时支持排序、筛选、分页 |
| 行级 CRUD | 直接在网格里增、删、改、查单行 |
| SQL 编辑器 | 高亮 + 自动补全 + 多语句执行 |
| SSH 隧道 | Rust 多线程实现的 SSH 转发，支持密码与私钥两种认证 |
| 现代前端 | React 19 + 现代化 UI 框架，体验更接近 Web 应用 |

![SiphonDB 截图](https://pbs.twimg.com/media/HMYVtrEaAAAikoQ.jpg)

## 适用场景

- 个人开发者需要一套轻量 GUI 同时管理本地 SQLite + 远端 Postgres
- 通过跳板机访问生产库，内置 SSH 隧道免去外部工具配置
- 想用 Tauri 体系做桌面工具，但不愿写原生 UI 的前端开发者
- 需要在 Windows / macOS / Linux 间无缝切换，不被厂商客户端的版本差异卡住

## 参考链接

- [项目链接](https://github.com/Premod1/SiphonDB)

## 相关概念

- [Dory](tool-dory.md) — macOS 上 Docker Desktop 的开源替代品，可在本地容器里跑 SiphonDB 要连的数据库