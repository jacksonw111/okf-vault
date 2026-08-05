---
type: "Tool"
title: "open·kritt（Kritt-ai/open-kritt）"
description: "把安全研究拆成小任务、用多 AI 代理并行执行的安全扫描框架，结果合并为可验证、可排序的漏洞发现。"
resource: "https://github.com/Kritt-ai/open-kritt"
tags: [security, code-audit, vulnerability, ai-agents, parallel, multi-agent]
timestamp: "2026-08-05T14:15:00Z"
---

# open·kritt（Kritt-ai/open-kritt）

## 它是什么

**open·kritt** 是一款**多 AI 代理并行的安全扫描框架**：单个模型直接读整个代码库找漏洞的效果很差，open·kritt 把安全研究**拆成小任务**、**用多个 AI 代理并行执行**，再把结果合并成**可验证、可排序的漏洞发现**。

## 为什么用它 / 适合什么场景

- **大型代码库**：单次上下文塞不下整个仓库，多代理并行更高效。
- **AI 安全研究**：自动化初筛 → 人工复审的流水线。
- **可验证结果**：每个漏洞带 PoC / 复现路径，不是「模型说有问题就有问题」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 任务拆分 | 把大仓库 / 大扫描拆成多个可独立执行的子任务 |
| 多代理并行 | 多 AI 代理同时跑不同子任务 |
| 结果合并 | 各代理发现合并去重 / 排序 |
| 可验证 | 每条漏洞带可复现证据，不止「可能性」 |
| 可排序 | 按严重度 / 置信度 / 可利用性排序 |

## 参考链接

- [GitHub 仓库](https://github.com/Kritt-ai/open-kritt)

## 相关概念

- [Strix](./tool-strix.md) — 另一款自主 AI 渗透测试 agent，输出可直接复现的 PoC；可与 open·kritt 对照「并行 vs 自主」
- [Cliare](./tool-cliare.md) — Rust 写的 CLI 黑盒审计工具，给 CLI 打 Agent 就绪评分