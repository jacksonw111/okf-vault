---
type: Tool
title: "CCSwitch-operations"
description: "把 CC Switch 多处分散的配置（SQLite / settings.json / 9 个 agent live 配置）维护收拢成几条带校验的命令，避免手动改坏。"
resource: "https://github.com/RuriLothlorien/CCSwitch-operations"
tags: [ccswitch, claude-code, codex, ops, configuration, sync]
timestamp: "2026-08-24T05:35:00Z"
---

# CCSwitch-operations

## 它是什么

[RuriLothlorien/CCSwitch-operations](https://github.com/RuriLothlorien/CCSwitch-operations) 是给 CC Switch（Claude Code / Codex / 其它 AI agent 的多客户端切换器）做配置维护的一组操作脚本。CC Switch 的真实状态分散在三处：

- 一个 SQLite 数据库
- 一份 `settings.json`
- 9 个 agent 的 live 配置文件

手动在多个地方改、互相回写覆盖、甚至 CCS 自身编辑缺陷造成损坏，是常见的事故源。这套脚本把日常维护压成几条带校验的命令，照着跑就不会坏。

## 为什么用它 / 适合什么场景

- **同时跑多个 agent 客户端（CC + Codex + Hermes ...）的人**：每次想统一某个 model / API key / prompt 都要改很多份文件，容易漏。
- **担心「改完被回写覆盖」**：脚本的写入顺序固定，避免 CCS 在中间重新写一次覆盖你的改动。
- **想给配置维护做版本管理 / 自动化**：脚本输出是幂等的，可以塞进 cron 或 CI。

## 关键能力

| 能力 | 说明 |
|------|------|
| 集中读取 | 一条命令同时 dump SQLite + settings.json + 9 个 live 配置 |
| 校验 | 写回前对比三处是否一致 / 有冲突 |
| 幂等写入 | 多文件写回有固定顺序，避免互相回写 |
| 同步分发 | 一处改完 → 推到 SQLite / settings / 各 agent live 配置 |
| 安全回滚 | 写入前自动备份，失败时一键还原 |

## 相关概念

- [Harness Router](./tool-harness-router.md) — 类似定位：把多个 agent harness 收进同一界面与一套 API
- [CloudSync Workflow](./tool-cloudsync.md) — 云端 agent 记忆 / 配置同步

## 参考链接

- [项目链接](https://github.com/RuriLothlorien/CCSwitch-operations)