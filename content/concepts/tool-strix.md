---
type: "Tool"
title: "Strix（自主 AI 渗透测试 agent）"
description: "用自主 AI 渗透 agent 自动发现和验证应用漏洞，生成可直接利用的 PoC 而不是一堆误报；把渗透流程拆成可监督、可审计的多阶段任务。"
tags: "[security, pentest, agent, vulnerability, ai, poc]"
timestamp: "2026-07-05T00:00:00Z"
resource: "https://github.com/usestrix/strix"
---

# Strix（自主 AI 渗透测试 agent）

## 它是什么

[`Strix`](https://github.com/usestrix/strix) 是用 **自主 AI 渗透 agent** 自动发现与验证应用漏洞的开源项目，目标是替代「靠脚本扫出一堆 CVEs 误报」的传统工具，**输出能直接复现的 PoC（Proof of Concept）**。

![Strix 截图](https://pbs.twimg.com/media/HMXA7O-awAA5RR8.jpg)

## 关键能力

| 能力 | 说明 |
|------|------|
| 自主 agent | AI 自主规划攻击路径，无需人工逐步驱动 |
| 漏洞发现 | 扫描目标应用并识别可被利用的弱点 |
| 漏洞验证 | 在沙箱中验证漏洞是否真实可利用 |
| PoC 生成 | 输出可直接复现的漏洞利用代码 |
| 误报过滤 | 通过验证环节把可疑点降噪为高置信度结果 |
| 流程化任务 | 把渗透测试拆为多阶段：侦察 → 攻击面 → 利用 → 报告 |

## 工作流程

1. **侦察**：目标 URL / 域名输入，自动发现子域与暴露端口
2. **攻击面映射**：识别 Web 接口、API、认证机制
3. **漏洞利用**：让 agent 在隔离沙箱中尝试已知漏洞模式
4. **验证**：二次复现可疑点，过滤误报
5. **报告**：输出包含 PoC 的结构化报告

## 与同类工具的区别

- **vs Flounder**：Flounder 把现有编码 agent 包装为审计系统，更强调「复用 Codex / Claude Code」；Strix 是为渗透测试**专门设计**的 agent
- **vs AgentStalker**：AgentStalker 是把 LLM Agent 当审计**目标**（审计代理本身的安全性），Strix 是把 agent 当**渗透测试执行者**

## 适用场景

- 团队定期对自家 Web 应用做安全体检
- 红队演练：用 AI 替代初级渗透工程师完成大量重复劳动
- 在受控沙箱里跑真实攻击路径，验证防御是否到位
- 输出可读 PoC 直接交给开发团队复现修复

## 参考链接

- [项目链接](https://github.com/usestrix/strix)

## 相关概念

- [Flounder](tool-flounder.md) — 把现有编码 agent 包装为白帽安全审计系统
- [AgentStalker](tool-agent-stalker.md) — 把 LLM Agent 当审计目标，检查代理框架本身的安全性
- [agent-lock](tool-agent-lock.md) — eBPF 沙箱把 AI 代理限制在指定目录，避免 Strix 这类工具失控访问