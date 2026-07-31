---
type: "Tool"
title: "知微（Lyrics-1/Finance_Management）"
description: "桌面财务管理应用：前端 Qt/QML、后端 Java Spring Boot，能注册登录、记流水明细、管理资产账户、看统计图表、做预算控制；中南大学学生作品。"
resource: "https://github.com/Lyrics-1/Finance_Management"
tags: "[finance, desktop-app, qt, spring-boot, java, student-project]"
timestamp: "2026-07-31T20:30:00Z"
---

# 知微（Lyrics-1/Finance_Management）

[知微](https://github.com/Lyrics-1/Finance_Management) 是一款**桌面财务管理应用**，前端用 **Qt/QML** 搭界面，后端用 **Java Spring Boot** 处理数据。学生作品（基于 Qt Creator）但功能覆盖完整：注册登录、流水明细、资产账户、统计图表、预算控制。

## 它是什么

- **跨平台桌面**：Qt 框架天生支持 Win / macOS / Linux
- **QML 写界面**：声明式 UI，比传统 Qt Widgets 更易写
- **Spring Boot 做业务层**：Java 生态熟悉的 REST / 事务 / 安全
- **核心场景**：流水（记账）、账户（资产）、统计（报表）、预算（控制）

## 为什么用它 / 适合什么场景

| 场景 | 知微的契合度 |
|------|--------------|
| 想本地管钱而不愿把数据上云 | 桌面应用 + 自托管后端 |
| 学习 Qt / QML 跨平台开发 | 学生项目的可参考工程 |
| 想做自己的记账工具并扩展 | 模块分明：账户、流水、统计、预算 |
| Java 后端 + Qt 前端混合架构 | 罕见的搭配，可作参考 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 注册登录 | 用户体系 |
| 流水明细 | 每笔收支记账 |
| 资产账户 | 多账户管理 |
| 统计图表 | 报表视图 |
| 预算控制 | 设置预算并追踪 |
| Qt/QML 界面 | Qt Creator 编写，跨平台原生 |

## 相关概念

- [Pi Exa](./tool-pi-exa.md) — Pi 终端 AI 助理的 Exa 搜索扩展，与本工具组合可做「在终端记账 / 问账目」场景
- [grayslate](./tool-grayslate.md) — 桌面便签本，本地保存思路与知微同源
- [zsui](./tool-zsui.md) — Rust 轻量原生 UI 框架，与 Qt/QML 同属「桌面跨平台 UI」栈选型
- [aether-android-agent](./tool-aether-android-agent.md) — Android 上的 AI Agent，可与桌面记账客户端做同步
- [phone-record-manager](./tool-phone-record-manager.md) — Windows 桌面工具（Python + PySide6 + SQLite），同属「桌面端小工具」组
