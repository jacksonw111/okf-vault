---
type: "Tool"
title: "rulesify（ydeng11/rulesify）"
description: "用 Rust 写的「AI 技能一键安装器」：从 Anthropic、OpenAI 等官方来源拉取 50+ 个预置技能（Agent Skills），支持按领域 / 标签筛选，一键安装到 Claude Code、Codex、Cursor 等 AI 编码工具，让代理直接获得相应能力。"
resource: "https://github.com/ydeng11/rulesify"
tags: [rust, cli, agent-skills, installer, claude-code, codex, cursor, anthropic, openai]
timestamp: "2026-07-27T20:30:00Z"
---

# rulesify（ydeng11/rulesify）

## 它是什么

`ydeng11/rulesify` 是一个用 **Rust** 写的 **AI 技能一键安装器**：它帮用户从 **Anthropic、OpenAI** 等官方来源安装 **50+ 个预置技能**（Agent Skills），支持**按领域和标签筛选**。装技能是一键的，目标工具覆盖 **Claude Code、Codex、Cursor** 等 AI 编码工具。彻底告别「手动搜 GitHub repo、复制 SKILL.md 文件、再贴进自己项目」的体力活。

## 为什么用它 / 适合什么场景

- 想给 **Claude Code / Codex / Cursor** 批量喂技能，但**不想一个个手动复制**；
- 希望**按场景筛选**技能（如 devops、测试、文档、code-review），不靠模糊关键词；
- 偏好 **Rust 写的单文件可执行**，无 Node / Python 环境依赖；
- 团队里多人想装同一套技能，需要**统一入口**保证一致。

## 关键能力

| 能力 | 说明 |
|------|------|
| 50+ 预置技能 | 内置收录 50+ 个主流 Agent Skills |
| 多源支持 | 从 Anthropic、OpenAI 等官方 / 社区源拉取 |
| 按域筛选 | 支持按领域和标签过滤技能 |
| 一键安装 | 装到 Claude Code / Codex / Cursor 等 |
| Rust CLI | 单二进制即可运行，跨平台 |

## 媒体 / 原始链接

视频：

- <https://video.twimg.com/tweet_video/HOItUYbakAANw7K.mp4>

- 项目链接：<https://github.com/ydeng11/rulesify>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — rulesify 解决的就是「如何方便地安装 Agent Skills」
