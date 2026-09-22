---
type: Tool
title: "Axonel"
description: "把编码 Agent 关进独立 Git worktree 当后台进程——测试在磁盘上重跑，候选提交卡在人工审核关口等你批准才合并，避免 agent 留未跟踪文件 / 把跑不通的代码说成测试通过 / 往 main 推脏提交。"
resource: "https://github.com/axonel/axonel"
tags: "[ai-agent, git-worktree, sandbox, code-review, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# Axonel

## 它是什么
一个**编码 Agent 的隔离 + 审核 harness**：

> 把 agent 关进独立 Git worktree 当后台进程跑；测试由它在磁盘上重跑；候选提交卡在人工审核关口，等你批准才合并。

## 为什么用它 / 适合什么场景
- 编码 Agent 直接在仓库里干活会留下未跟踪文件、把跑不通的代码说成测试通过、还可能往 main 推脏提交——这些都靠 worktree + 审核关口挡掉。
- 想要对 Agent 输出做「二次独立测试验证」，而不是信任 Agent 自己的报告。
- 想要 PR 级别的「人类把关最后一道」工作流。

## 关键能力
| 能力 | 说明 |
|------|------|
| 隔离 | 独立 Git worktree 当后台进程 |
| 测试 | 磁盘上重跑 |
| 审核 | 候选提交卡人工审核关口 |
| 默认拒绝 | 改 main / 留未跟踪文件 / 假报告 都拦下 |

## 相关概念
- [Agent Gateway Isolation](playbook-agent-gateway-isolation.md) — 同为 Agent 安全 / 隔离模式
- [Cyberguard](tool-cyberguard.md) — 同为「目标级批准 → 执行 → 独立探针验证」的安全响应模型

## 项目链接
- 项目主页：<https://github.com/axonel/axonel>

## 媒体
- 截图：<https://pbs.twimg.com/media/HSyJaYVbQAAp2Ei.jpg>
