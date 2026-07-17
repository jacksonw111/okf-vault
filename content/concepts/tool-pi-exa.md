---
type: "Tool"
title: "Pi Exa（junnjiee/pi-exa）"
description: "为 Pi Agent 打造的扩展包, 把 Exa 的网页搜索、内容抓取和深度研究能力接入智能体; 基础的网页搜索和抓取无需 API key 即可使用, 安装扩展后开箱即用; 深度搜索 (deep-lite / deep / deep-reasoning) 才需要 Exa API key。"
resource: "https://github.com/junnjiee/pi-exa"
tags: "[pi-agent, exa, web-search, extension, agent-tools]"
timestamp: "2026-07-17T10:10:00Z"
---

# Pi Exa

[Pi Exa](https://github.com/junnjiee/pi-exa) 是专为 [Pi Agent](https://github.com/badlogic/pi) 设计的**扩展包**, 把 [Exa](https://exa.ai/) 的**网页搜索 / 内容抓取 / 深度研究**三项能力接进 Pi 的工具系统。

## 它和 Pi 默认 search 的差别

Pi 原生自带一个**基础网页搜索** (抓 + 摘要), 但：

- 速度一般
- 缺「深度研究」分层 (摘要 / 完整 / 推理) 选项
- 想用强搜索只能外部接 Exa

**Pi Exa 的分层策略**很务实:

| 模式 | 是否需要 Exa API key | 用途 |
|------|------|------|
| 基础网页搜索 / 抓取 | **不需要**, 开箱即用 | 应付 80% 日常 |
| `deep-lite` / `deep` / `deep-reasoning` | 需要 | 复杂调研与推理链搜索 |

这样降低了「试用门槛」(无 key 也能跑), 又把能力天花板留给愿意付费的用户。

## 关键能力

| 能力 | 说明 |
|------|------|
| 即装即用基础搜索 | 无 API key 即可做基础搜索 / 抓取 |
| 分层深度搜索 | deep-lite / deep / deep-reasoning 三档 |
| Exa 全能力接入 | 搜索 + 内容抓取 + 深度研究 |
| Pi 扩展兼容 | 作为 Pi extension 安装, 不改动核心 |

## 参考链接

- [项目仓库](https://github.com/junnjiee/pi-exa)
- [Pi Agent 主页](https://github.com/badlogic/pi)

## 相关概念

- [pi-web-agent](./tool-pi-web-agent.md) — Pi 编码代理的网页工具包 (单一 web_explore 接口), Pi Exa 偏「搜索 / 抓取 / 研究」, pi-web-agent 偏「通用上网」
- [pi-task](./tool-pi-task-delegation.md) — Pi 子任务委派扩展, 可与 Pi Exa 配合做「搜索子任务」委派
- [Agent-Reach](./tool-agent-reach.md) — 一行命令给编码 agent 装互联网能力, Pi Exa 偏 Pi-only 的同类能力补充
