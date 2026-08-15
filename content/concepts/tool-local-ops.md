---
type: "Tool"
title: "local-ops（macOS 本地服务 / 命令指挥台）"
description: "在 macOS 上把常用服务、项目命令和一次性批处理任务收进一个本地网页指挥台：一键启停、重启、看日志、诊断，还能每 2 秒盯着本机端口和服务状态。"
tags: "[macos, devops, dashboard, local-server, ops]"
timestamp: "2026-08-15T05:14:00Z"
resource: "https://github.com/laogou717/local-ops"
---

# local-ops（macOS 本地服务 / 命令指挥台）

## 它是什么

`laogou717/local-ops` 是一个本地 Web 控制台，专门给 macOS 开发者管理「本地常驻服务 + 项目级命令 + 一次性批处理」。它把所有常用服务（如 PostgreSQL、Redis、自研后端、Mock 服务）和项目命令（启动、构建、重置数据库）收敛到一个网页面板，支持一键启停 / 重启 / 看日志 / 跑诊断，并自动每 2 秒轮询本机端口与服务存活状态。

> ![](https://pbs.twimg.com/media/HPpf6ljaYAAaMtK.jpg)

## 为什么用它 / 适合什么场景

- **本机服务太多**：日常开发常跑 N 个后台进程（DB、缓存、Mock、worker），手动 `brew services` + 终端切来切去很烦。
- **命令散落**：启动脚本在 shell alias / Makefile / package.json 都有，无法集中查阅。
- **端口被谁占了**：常碰到「3000 端口被谁占了」，自带端口扫描省事。
- **看日志麻烦**：不用每个服务都开一个终端窗口。

## 关键能力

| 能力 | 说明 |
|------|------|
| 服务面板 | 列出所有注册的本地服务，按状态着色（运行 / 停止 / 异常） |
| 一键启停 | 按钮触发启动 / 停止 / 重启，免去敲命令 |
| 日志查看 | 聚合多个服务的 stdout / stderr，一处看 |
| 项目命令 | 把每个项目的 `dev` / `build` / `db:reset` 等命令集中 |
| 端口监控 | 每 2 秒扫描本机端口，标出谁在监听 |
| 进程诊断 | 列出活跃进程、内存占用、CPU 占用 |
| 一次性任务 | 注册一次性批处理（如「清理 Docker 卷」） |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| [Vaultty](tool-vaultty.md) | 块式终端 + 自动注入 .env | 偏「单终端 UI」，不在面板层 |
| local-ops | Web 面板 + 集中调度 | 偏「运维仪表盘」，管多个服务 |
| [MacTools](tool-mac-tools.md) | 菜单栏小工具集 | 偏「macOS 系统级」开关，不管项目命令 |

## 适用人群

- macOS 上的全栈 / 后端工程师。
- 同时维护多个本地项目、需要频繁启停依赖服务的开发者。
- 想给本地开发做「统一面板」的人。

## 参考链接

- [项目链接](https://github.com/laogou717/local-ops)

## 相关概念

- [Vaultty](tool-vaultty.md) — 块式终端 + Keychain 自动注入 .env
- [MacTools](tool-mac-tools.md) — 免费开源 macOS 菜单栏工具集
- [md-wechat](tool-md-wechat.md) — 同一作者出品的公众号 Markdown 排版工具