---
type: Term
title: "auth.md（把身份验证说明写进 README）"
description: "WorkOS 提出的把鉴权说明写进服务仓库根目录 `auth.md` 的实践，让 LLM / agent 能直接读 README 就获知该服务如何接入认证，配合 x402 等付费协议可形成「自动鉴权 + 自动付费」组合。"
resource: "https://github.com/workos/auth.md"
tags: "[auth, llm, agent, workos, auth.md, x402, ai]"
timestamp: "2026-07-09T20:50:00Z"
---

# auth.md（把身份验证说明写进 README）

## 定义
`auth.md` 是 WorkOS 推动的一项**面向 LLM / agent 的服务发现约定**：每个需要在前面接入鉴权的服务，在仓库根目录放一个标准格式的 `auth.md`，声明该服务接受哪种鉴权方式（OAuth / API key / JWT / 设备码 / 等）以及如何获取。这样 agent 拉一个仓库就能直接读 `auth.md` 自动接入，不再需要人工写文档。

> 配合 **x402**（HTTP 402 状态码驱动的小额付费协议），可形成「自动鉴权 + 自动付费」组合，被视为是 agent 经济落地的关键基础设施之一。

## 要点

- **问题**：当前 OAuth / API key 文档普遍面向人类写，给 LLM / agent 看要么啰嗦要么残缺，agent 接入需要反复试错。
- **解法**：`auth.md` 用统一 schema 把鉴权方式、端点、scope、刷新策略写成机器可读 + 人类可读双友好的 Markdown。
- **生态位置**：与 `llms.txt`（让 LLM 读懂你的站点）、`mcp.json`（服务暴露哪些 MCP 工具）、`agents.md`/`AGENTS.md`（给 agent 的工作流指令）共同构成 **「agent-friendly repo」** 四件套。
- **x402 协同**：x402 让 agent 按请求次数付费结算，与 auth.md 搭配后 agent 可**自己判断要鉴权 + 自己决定要不要付费**，全程无需人类介入。
- **被推为「endgame」**：在原贴里被形容为与 x402 一起做成"agent 经济终局"的基建。

## 关键能力
| 能力 | 说明 |
|------|------|
| 标准 Markdown 鉴权说明书 | 与 `README.md` 同级，机器可读 |
| 多鉴权方案 | OAuth / API key / JWT / 设备码等多种方式 |
| LLM / agent 友好 | agent clone 仓库即可自助接入 |
| x402 联动 | 与 HTTP 402 付费协议配合形成"鉴权 + 付费"闭环 |
| 社区驱动 | WorkOS 在 GitHub 公开维护 schema 与示例 |

## 相关概念
- [x402](term-x402.md) — HTTP 402 状态码驱动的小额付费协议，本概念的最佳搭档（**注：本条目为关联命名空间占位，暂无独立条目**）
- [LLM Wiki 模式](term-llm-wiki.md) — 让 LLM 消费知识库的语义化约定
- [Agent Skills（代理技能包）](term-agent-skills.md) — Claude / Codex 等 agent 的技能包协议
- [MCP WebSearch](tool-deepseek-mcp-websearch.md) — 基于 DeepSeek API 的 MCP 联网搜索

## 参考链接
- 项目链接：<https://github.com/workos/auth.md>
