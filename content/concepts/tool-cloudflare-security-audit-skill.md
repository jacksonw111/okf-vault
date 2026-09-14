---
type: "Tool"
title: "Cloudflare security-audit-skill（多阶段安全审计 Skill）"
description: "Cloudflare 出的 coding agent Skill（3,288 stars）：多阶段安全审计，输出机器可读的、经过验证的 finding；适配 Cursor / Codex 等 agent。"
resource: "https://github.com/cloudflare/security-audit-skill"
tags: "[security, audit, skill, cloudflare, codex, cursor]"
timestamp: "2026-09-14T22:30:00Z"
---

# Cloudflare security-audit-skill（多阶段安全审计 Skill）

## 它是什么

[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) 是 **Cloudflare 出品的 coding agent Skill**：做**多阶段安全审计**，输出**机器可读、经过验证**的 finding。

> security-audit-skill is a Cloudflare coding agent skill for multi phase security audits. It outputs verified, machine readable findings for Cursor and Codex. 3,288 stars.

## 关键能力

| 能力 | 说明 |
|------|------|
| 多阶段审计 | 不止静态扫描，分阶段跑 |
| 验证后输出 | finding 经过验证，不是噪音 |
| 机器可读 | JSON / 结构化结果 |
| Cursor / Codex 适配 | 主流通用 coding agent |
| Cloudflare 出品 | 大厂背书 |

## Skill 的工作流（推断）

1. **静态分析** —— 先扫代码
2. **依赖审计** —— 检查依赖漏洞
3. **动态验证** —— PoC 验证 finding
4. **结构化输出** —— 机器可读报告
5. **修复建议** —— 给出 fix diff 或位置

## 适合谁

- 想给 coding agent 加一层安全审计
- 想找到的不只是 SAST 工具的 false positive
- 团队在用 Cursor / Codex 写大量 AI 代码

## 项目链接

- 仓库：<https://github.com/cloudflare/security-audit-skill>

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — 类似的「agent ↔ 工具」协议
