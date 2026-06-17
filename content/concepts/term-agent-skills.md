---
type: "Term"
title: "Agent Skills（代理技能包）"
description: "为编码 / 通用 agent（Claude Code、Pi、Codex…）打包的「可复用提示词 + 工作流」模块；通过 slash command（如 /grill-me、/improve、/zoom-out）一键加载；本质是把团队里「老手怎么做」的隐性 SOP 显性化、可版本化、可分发的最小单元。"
tags: "[ai, agent, skills, prompt-engineering, claude-code]"
timestamp: 2026-06-17T00:00:00Z
---

# Agent Skills（代理技能包）

## 定义

**Agent Skills** 是为 AI agent（特别是 [Claude Code](./tool-claude-code.md)、Pi、Codex、Cursor 等终端 / IDE 编码 agent）打包的**可复用提示词 + 工具调用模板**。一个 skill 通常包含：

- **触发方式**：一个 slash command（如 `/improve`、`/grill-me`、`/zoom-out`）或自动匹配的场景。
- **系统提示 / 指令**：要 agent 扮演什么角色、按什么步骤执行、输出什么格式。
- **可选附件**：参考文件、模板、few-shot 例子、配套脚本。
- **元数据**：作者、版本、适用模型。

文件落地形式上，多为：

- `.claude/commands/<name>.md`（Claude Code 的 Commands）
- `.claude/skills/<name>/SKILL.md`（更结构化的 Skills 规范）
- 项目根的 `AGENTS.md` / `CLAUDE.md`（常驻系统提示）

## 要点

- **可分发、可版本化**：一个 skill 就是一个仓库 / 一个目录，`git clone` 就能用，PR 就能贡献。代表：[mattpocock/skills](./tool-mattpocock-skills.md)、[shadcn/improve](./tool-shadcn-improve.md)。
- **「老手 SOP」显性化的最小单元**：把「我每次接手老项目都先 grill 一遍接口」「我每次升级都先 zoom-out 一下」这种隐性习惯，写成谁都能 `/` 出来的命令。
- **不是 Prompt，是流程**：一个好的 skill 不会只是一段角色扮演提示，而是「输入什么 → 调用什么工具 → 输出什么产物」的一整套 SOP。
- **生态三件套**：
  1. **通用对话类** — `/grill-me` 逼问自己假设、`/zoom-out` 拉远视角、`/caveman` 极简表达、`/hand-off` 交接清单。
  2. **代码审计 / 改进类** — [shadcn/improve](./tool-shadcn-improve.md) 用最强模型审计仓库、出 backlog。
  3. **专用领域类** — [Hyperagent 设计网格 skill](./tool-hyperagent-design-skill.md) 教代理做排版、[Archify](./tool-archify.md) 把自然语言转成 SVG 架构图、[JSON-Render](./tool-json-render.md) 让代理渲染真实 UI。
- **跟 MCP 的关系**：Skills 是**软**的（提示词 + 工作流），MCP 是**硬**的（真接数据库 / 浏览器 / GitHub API）。两者互补：skill 里可以调用 MCP 工具。
- **对「前沿模型被撤下」的应对**：shadcn 提出的核心观点——**把智能当借来的，今天就榨取它来建 backlog**。skill 的本质就是「把模型的当下能力，编码进可复用的程序里」，模型明天变笨了 skill 还在。

## 为什么这个概念重要

它把 agent 的能力曲线从「今天模型能答什么」抬升到「团队积累了什么可复用资产」——是 AI 工作流从「玩具」走向「基础设施」的关键拐点。

## 怎么写一个 skill（最小骨架）

```markdown
<!-- .claude/commands/grill-me.md -->
你是一个极度挑剔的资深工程师。
当用户调用 /grill-me 时，对【用户当前任务的方案】做三轮反驳：
1. 假设层：哪些前提错了？
2. 边界层：哪些场景没考虑？
3. 失败层：最坏会发生什么？
输出「保留 / 修改 / 重做」三档结论。
```

放进项目 `.claude/commands/`，提交，团队所有人 `claude` 起手就能用。

## 代表性 skill 仓库

- [mattpocock/skills](./tool-mattpocock-skills.md) — Real Engineers 风格的合集
- [shadcn/improve](./tool-shadcn-improve.md) — 用最强模型做代码审计
- [Hyperagent 设计网格 skill](./tool-hyperagent-design-skill.md) — Müller-Brockmann 网格教 AI 做设计
- [Archify](./tool-archify.md) — 自然语言 → 架构图
- [JSON-Render / HarnessAgent](./tool-json-render.md) — agent 沙盒里渲染真实 UI

## 相关概念

- [Claude Code](./tool-claude-code.md)
- [mattpocock/skills](./tool-mattpocock-skills.md)
- [shadcn/improve](./tool-shadcn-improve.md)
- [OKF 是什么](./term-okf.md) — Agent Skill 与 OKF 都是「markdown + 约定」的 agent 可消费格式，理念同源
- `PRODUCER.md 协议` — 本身也是一个 skill
