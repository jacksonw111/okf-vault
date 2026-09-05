---
type: Tool
title: "qq-farm-server"
description: "QQ 农场 Bot 服务器快照导出与一键部署工具，把整套挂机机器人 + 四个配套服务打包成可在新机器直接复刻的可部署包"
resource: "https://github.com/shichenovo/qq-farm-server"
tags: [qq, bot, farm, snapshot, deploy, self-hosted]
timestamp: 2026-09-05T15:00:00Z
---

# qq-farm-server

## 它是什么
`shichenovo/qq-farm-server` 是一款**QQ 农场挂机机器人快照导出工具**：从一台正在运行的 QQ 农场 Bot 服务器导出完整可部署快照（含主机器人 + 四个配套服务），在新服务器上一键复刻整套挂机环境，避免重复配置。

## 为什么用它 / 适合什么场景
- 已经在跑 QQ 农场 Bot，想迁移到新服务器 / VPS 时，不想从头配置机器人与配套服务。
- 想在多台机器上克隆同一份农场挂机环境做对比 / 备份 / 灾备。
- 运维场景：把整套运行时状态打包成可版本管理 / 可重放的快照。

## 关键能力
| 能力 | 说明 |
|------|------|
| 完整快照导出 | 把 Bot 主进程 + 四个配套服务（含配置、数据、依赖）一次性导出 |
| 一键部署 | 在新机器上跑同一条命令即可复刻整套挂机机器人 |
| 可重复性 | 相同快照 → 相同运行状态，便于跨机迁移与备份 |
| 配套服务打包 | 不只打包机器人本身，还打包与之耦合的四个附属服务 |

## 相关概念
- [原始链接](https://github.com/shichenovo/qq-farm-server)