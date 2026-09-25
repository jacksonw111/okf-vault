---
type: "Tool"
title: "golive-skill（把 AI 编码产物真正部署到用户自己账号的 Agent Skill）"
description: "让 AI 编码智能体搭出来的应用真正上线——域名、托管、数据库、登录、邮件、支付，全部跑在用户自己的账号上，之后可以整体交接或拆除。"
resource: "https://github.com/mikehasa/golive-skill"
tags: "[agent-skill, deployment, self-hosted, claude-code, codex, cursor, byok, open-source]"
timestamp: "2026-09-25T15:55:00Z"
---

# golive-skill（把 AI 编码产物真正部署到用户自己账号的 Agent Skill）

## 它是什么

[golive-skill](https://github.com/mikehasa/golive-skill) 是一个 **Agent Skill**——给 Claude Code / Codex / Cursor 这类编码智能体加一道「**把搭出来的应用真正部署上线**」的工序：

- **域名**
- **托管**
- **数据库**
- **登录鉴权**
- **邮件**
- **支付**

全部跑在**用户自己的账号**上（Cloudflare / Vercel / Supabase / Stripe 之类），不依赖 demo 平台、不绑死中介。

部署完成后，用户可以**整体交接**（转交给运营团队）或**整体拆除**（关账号、删资源）。

## 为什么用它 / 适合什么场景

- 用 AI 编码智能体快速搭出来一个 MVP / 内部门户，但不想再花一周研究「怎么把 Vercel preview 变成真域名 + 真数据库 + 真支付」。
- 强调「**用户掌控资源**」：基础设施挂在用户自己账号下，工具方不卡脖子。
- 想把「AI 搭出来 → 真实上线」做成可重复的工序，团队里任何人都能跑同一套 Skill 出活。
- 适合一人 / 小团队快速验证商业想法时缩短「搭完到收钱」的距离。

## 关键能力

| 能力 | 说明 |
|------|------|
| 形态 | Agent Skill（Claude Code / Codex / Cursor 可加载） |
| 部署范围 | 域名 / 托管 / 数据库 / 鉴权 / 邮件 / 支付 |
| 账号归属 | 用户自己（BYOK 思路：Cloudflare / Vercel / Supabase / Stripe 等） |
| 收尾 | 可整体交接、可整体拆除 |
| 适配场景 | AI 编码产物的「最后一公里上线」 |

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — golive-skill 所属的技能包生态
- [Self-Hosted](./term-self-hosted.md) — 把基础设施握在自己手里，是 golive-skill 的部署哲学
