---
type: "Tool"
title: "clawk（clawkwork/clawk）"
description: "本地 Agent 沙箱工具：每次执行给 Agent 开一台一次性 Linux 虚拟机，把本机的文件、密钥、配置挡在门外——「给 Agent 一台自己的机器，而不是用你的」。"
tags: "[agent, sandbox, vm, isolation, linux, security, cli]"
timestamp: "2026-07-18T20:00:00Z"
resource: "https://github.com/clawkwork/clawk"
---

# clawk（clawkwork/clawk）

## 它是什么

[`clawk`](https://github.com/clawkwork/clawk) 是 clawkwork 开源的本地 Agent 沙箱工具，**核心思路是「给 Agent 一台自己的机器，而不是共享用户的机器」**。

- Agent 通常需要装包、跑命令、访问网络；
- 在用户本机直接跑风险太大：污染环境、泄漏密钥、误删文件；
- clawk 直接给 Agent **开一台一次性的 Linux 虚拟机**；
- 跑完即销毁，本机文件、密钥、其余工作完全隔离。

## 关键能力

| 能力 | 说明 |
|------|------|
| 一次性 VM | 每次任务启动全新的 Linux 虚拟机 |
| 本地运行 | 不依赖远端服务，数据不出本机 |
| 完全隔离 | 本机文件系统 / 凭据对 Agent 不可见 |
| 自动销毁 | 任务结束 / 中断即回收资源 |
| CLI 优先 | 一条命令即可启动沙箱 |

## 与「容器 / Docker」沙箱的对比

| 维度 | Docker 容器 | clawk 一次性 VM |
|------|-------------|-----------------|
| 隔离强度 | 共享内核 | 独立内核 |
| 网络隔离 | 需手动配置 | 默认隔离 |
| 文件系统 | 共享挂载点 | 完全独立 |
| 启动开销 | 较小（百毫秒级） | 较大（秒级），但换来强隔离 |

## 适合什么场景

- 用本地 Agent 跑不可信代码 / 第三方脚本；
- 想在个人机器上跑 Claude Code / Codex 等 Coding Agent，又担心污染环境；
- 评测、调试 Agent 时需要「干净环境 / 干净复现」；
- 个人安全敏感工作（密钥、隐私数据）下的 Agent 使用。

## 演示视频

- [原始视频](https://video.twimg.com/tweet_video/HNUKrW1bEAAv1qm.mp4)

## 参考链接

- [原始链接](https://github.com/clawkwork/clawk)

## 相关概念

- [forkd](tool-forkd.md) — 同样为 Agent 提供隔离运行环境；forkd 追求「microVM 批量毫秒级 fork」，clawk 追求「CLI 一键开一次性 VM」，路线不同但目标领域重叠
- [云端 Agent 基础设施的设计教训](note-cloud-agent-infrastructure.md) — 反复强调「Agent 跑在哪」「隔离边界怎么划」，clawk 是这条原则在个人桌面层的落地
- [matterloop](tool-matterloop.md) — matterloop 解决「Agent 流程怎么不跑飞」，clawk 解决「Agent 在哪跑才安全」