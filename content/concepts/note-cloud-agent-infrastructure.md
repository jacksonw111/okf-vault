---
type: "Note"
title: "云端 Agent 基础设施的设计教训（CREAO）"
description: "CREAO 团队总结的「把桌面 agent 搬到云上时什么会变」：状态 vs 代码按所有权节奏解耦、凭据永不下沉到沙箱、所有触发器共享同一条执行管道；本质是把「agent = 自然语言接口的函数」这件事做成可被平台调用的基础设施。"
tags: "[ai, agent, cloud, infrastructure, sandbox, security]"
timestamp: "2026-06-17T00:00:00Z"
resource: "https://x.com/intuitiveml/status/2062699747224568212"
---

# 云端 Agent 基础设施的设计教训（CREAO）

> 来源：[@intuitiveml on X 2026-06-05](https://x.com/intuitiveml/status/2062699747224568212) —— CREAO 团队把桌面 agent 搬到云上几个月后总结的两条硬教训。

## 为什么桌面框架不能直接搬到云上

桌面 agent 默认拥有一堆云上没有的「免费午餐」：

- 持久化：文件系统一直都在；
- 身份：API key 在 `os.environ`，用户在终端前；
- 网络信任：本地回环、私有网段；
- 重试：用户盯着，崩了就再来；
- 生命周期：终端关掉，agent 死，不需要清理。

云上 agent **全部要重新搭**：沙箱每次启动都是新的、跑在别人共享的硬件上、被调度器 / HTTP / 别的 agent 触发、用户可能睡着了、代码本身可能是 LLM 从对抗性 prompt 生成的、文件系统必须扛过部署。

## 教训一：按「变化的节奏」切分状态 vs 代码

桌面环境里「用户环境和 agent runtime 是同一个东西、同一个人、同一个节奏更新」。云上不是。

**CREAO 的做法**（类比 OS 内核 vs 家目录）：

1. 用户的 Python / 依赖 / 数据 → 冻结成 sandbox snapshot，用户改一次才重新拍一次；任何一次运行都从同一张镜像启动，**保证可复现**。
2. 平台自己写的 runner 代码 → 高频部署，一天多次。
3. 这两件事**绝对不能绑在一个 artifact 里**——否则每次部署要么丢掉用户的冻结环境，要么强忍 runner 是旧版本。
4. 部署时只 hot-swap runner：`temp dir 暂存 → node --check 校验语法 → chattr +i 原子覆盖 → 清 V8 compile cache → 失败就杀沙箱重来`，整段 300ms。**只有 runner 真的换了才重拍 snapshot**。

**诊断问题**：你持久化的任何一个 artifact，问「这个 artifact 谁控制变化的节奏？」如果两边都控，迟早付出耦合代价。沿所有权边界切。

## 教训二：凭据永不下沉到执行边界

云 agent 的安全模型必须假设**沙箱里的代码已经被攻破**，而不是赌它没被攻破。

**硬规则**：任何长期凭据**绝不**进沙箱。

| 部件 | 位置 | 作用 |
|------|------|------|
| 沙箱内 | 仅持有 run-scoped 短令牌 | 调用外部 API |
| API Bridge | 沙箱外（host 侧） | 收到请求后挂上 OAuth token，再转发 |
| 凭据存储 | Bridge 后面的数据库 | 沙箱永远拿不到明文 |
| Bridge 鉴权 | 双层：IP allowlist + 短 JWT | 沙箱启动时平台签发，run 结束即失效 |

为什么是双层：

- **IP allowlist** —— 把 Bridge 钉死在内部网段，外部连接在网络层就被 drop。
- **短 JWT** —— 每个 run 一个，scope 到 user + app + session + run window。沙箱被劫持时，攻击者继承的也只是个 run 结束就死的令牌，且只能用于那一个 session。

同一个 Bridge 也是 billing、log、metric 的唯一出站口。**沙箱与外界的所有跨边界流量都走这一个接口**。

## 隐藏在下面的统一模式

四条不可妥协的属性：

- 状态在沙箱里，冻结到用户改；
- 代码可热替换，与状态独立；
- 凭据在 host 侧，绝不进 agent；
- **一条执行管道服务所有调用方**（UI 点击、定时、API、别的 agent）。

最后一条是整套设计的点睛之笔：一个 `executeAgent` 函数同时处理 UI 按钮、cron 触发、HTTP 调用，billing / log / metric 全部一致。新增一个触发面只是改路由，不是改架构。**agent 自己根本不知道也不关心是谁点了 Run**。

## 一句话总结

> 一个 agent 就是一个**带自然语言接口的函数**：实现归用户，触发面 / 运行时 / 安全边界归平台。纪律是让各层按自己的节奏演化，并提前把层与层之间的裂缝找到——别人会替你找的。

## 与本知识库其他概念的关系

- [Claude Code](tool-claude-code.md) — 桌面形态的 agent；搬到云上时正好踩中本文描述的所有「桌面默认 / 云上要重搭」的痛点。
- [Agent Skills 是什么](term-agent-skills.md) — Skills 是「agent 行为」的封装；本文是「agent 运行环境」的封装，两层互补。
- [forkd](tool-forkd.md) — 直接解决文中提到的「冷启动 microVM 太慢」，把 fork 的开销套在 VM 身上。

## 相关概念

- [Claude Code](tool-claude-code.md) — 桌面形态 agent；搬到云上踩中本文所有痛点
- [Agent Skills 是什么](term-agent-skills.md) — 行为层封装 vs 本文的环境层封装
- [forkd](tool-forkd.md) — 100ms 起 100 个 KVM 隔离沙箱，正是文中「冻结 snapshot + 快速派生」的极致版
