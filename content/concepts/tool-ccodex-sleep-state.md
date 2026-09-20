---
type: "Tool"
title: "ccodex-sleep-state（Codex 本地配置接管 + 网页面板）"
description: "gylive/ccodex-sleep-state：Go 写的本地工具，跑一个本地服务 + 网页面板（默认 http://127.0.0.1:17841/admin/），自动备份并接管 Codex 的 config.toml，停止后恢复原状；面板集中展示接入状态、请求计数、模型切换、代理订阅、配置检查与修复。"
resource: "https://github.com/gylive/ccodex-sleep-state"
tags: "[codex, config, dashboard, local, dev-tool]"
timestamp: "2026-09-20T18:00:00Z"
---

# ccodex-sleep-state

## 它是什么

[gylive/ccodex-sleep-state](https://github.com/gylive/ccodex-sleep-state) 是给 **OpenAI Codex** 写的本地工具，用 Go 写。

启动后：

1. 跑一个本地服务 + 网页面板（**默认 http://127.0.0.1:17841/admin/**）。
2. **自动备份** Codex 的 `config.toml`，再**接管**它——把所有改动都集中到面板里。
3. 工具**停止后恢复原状**——`config.toml` 还原成最初的样子。

面板把下面这些事集中到一个网页里，**不用手改 JSON 或猜环境变量**：

- 接入状态
- 请求计数
- 模型切换
- 代理订阅
- 配置检查 + 修复

## 为什么用它 / 适合什么场景

- Codex 的 `config.toml` 配置项多、互相耦合、JSON 错一个字符就跑不起来。
- 想在一个网页里**集中切换模型 / 代理 / 配置**，反复 `vim config.toml` 太烦。
- 经常**临时切不同模型 / 代理**做对比——面板里点一下比改文件快。
- **担心改坏**——面板会先备份，停止后自动还原。

## 关键能力

| 能力 | 说明 |
|------|------|
| 本地服务 + 网页面板 | 默认 `http://127.0.0.1:17841/admin/` |
| 自动备份 | 启动时备份 `config.toml` |
| 停止恢复 | 工具关闭后 `config.toml` 还原 |
| 集中面板 | 接入状态 / 请求计数 / 模型切换 / 代理订阅 / 配置检查修复 |
| Go 单二进制 | 装好就能跑，无运行时依赖 |

## 项目链接

- 仓库：<https://github.com/gylive/ccodex-sleep-state>

## 相关概念

- [Codex Control Plane MCP](./tool-codex-control-plane-mcp.md) — 同为 Codex 的「管理面」工具，但走 MCP 协议而非本地服务
- [CodexPro](./tool-codexpro.md) — 同为打通 Codex 与外部配置的桥
- [Proxide](./tool-proxide.md) — 把 Codex 接 ChatGPT Pro 网页强模型的另一种桥接思路
