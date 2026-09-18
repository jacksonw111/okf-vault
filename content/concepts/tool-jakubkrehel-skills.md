---
type: Tool
title: "jakubkrehel Skills（含 /explain-interface）"
description: "jakubkrehel 维护的 Agent Skills 仓库，首发 `/explain-interface`：用 DevTools 风格的手段拆解任意网页交互与渐变等视觉技术如何被实现，Agent 跑一遍给出拆解。"
resource: "https://github.com/jakubkrehel/skills"
tags: [agent, skills, devtools, web, explain, design, interface, design-engineering]
timestamp: 2026-09-18T15:30:00Z
---

# jakubkrehel Skills（含 /explain-interface）

## 它是什么
jakubkrehel 在 GitHub 开源的个人 Agent Skills 仓库，按 Claude Code / Codex 等支持「斜杠命令 Skill」的 agent 通用格式发布，主打「用 DevTools 风格工具拆解别人网页是怎么搭的」。首发命令 `/explain-interface`，回答类似「`https://interfere.com` 的渐变是用什么技术实现的？」

## 为什么用它 / 适合什么场景
- 想搞清楚一个具体网页交互 / 视觉细节（CSS 渐变、滚动联动、动画曲线、WebGL shader 等）是怎么搭的，但不想装浏览器扩展自己扒。
- 想在评审里引用「xx 网站用了 xx 技术」佐证设计决策，又不想手敲一长串 DevTools 操作。
- 教学 / 写作场景：让 agent 把别人页面的工程做法读出来再给你复盘一遍。

## 关键能力
| 能力 | 说明 |
|------|------|
| `/explain-interface <url>` | 给定网址，agent 像用 DevTools 一样逐元素拆解交互与渐变等视觉技术实现 |
| Skill 格式开放 | 命令作为 Skill 单元分发，可挂到 Claude Code / Codex 等支持的 agent |
| DevTools 风格抓取 | 复用 agent 自身的网页抓取能力，把"按 F12 看 elements / computed"翻译成自然语言 |
| 个人轻量仓库 | jakubkrehel 个人发布，按 Issue / PR 持续补充新 Skill 命令 |

## 一句话总结
**「别人网站是怎么搭的」用一条 `/explain-interface` 让 AI 自己开 DevTools 拆给你看。**

## Jakub 的「界面 6 块拆分」设计工程框架

Jakub Krehel 把界面拆成 **6 块**，每块一个 Skill：

| 块 | 关注点 |
|----|--------|
| UI 细节 | 圆角、按钮按下缩放、图标过渡的具体数值 |
| 排版 | 字号、行高、字重 |
| 配色 | 主题色、对比度、语义色 |
| 无障碍 | ARIA、键盘可达、对比度合规 |
| 布局 | 间距、栅格、嵌套 |
| 文案 | 标签、CTA、错误文案 |

配套一本设计工程杂志 **Interfaces**，让 agent 照着跑就能落地。

### 关键数值规则（可直接被 Skill 调用）

- 嵌套圆角：**外圈 = 内圈 + 内边距**
- 按钮按下缩到 **0.96**
- 图标切换：**透明度 + 缩放 + 4px 模糊** 三段过渡
- 与 Emil Kowalski（按下 0.97）只差 0.01，但风格立刻不一样

### 两个特别有用的 Skill

| Skill | 作用 |
|-------|------|
| `break` | 挑一个组件，临时拉起一个页面把所有状态 / 边界场景一次性渲染出来，一屏看出哪里会崩 |
| `reverse-engineer UI / 动画` | 反查别人网页上某段动画 / 某块 UI 到底怎么实现的 |

### 接入

Claude Code 有插件市场入口，其他 Agent 也能一条命令装。前端写完总觉得「差一口气、又说不清差在哪」的，让它过一遍基本能补上。

## 原始链接
- [jakubkrehel/skills 仓库](https://github.com/jakubkrehel/skills) — 原始仓库

## 相关概念
- [Jakub 设计 Skills](./note-jakub-design-skills.md) — Jakub 早期发布的设计 Skill 合集（同名不同项目）
- [Agent Skills 是什么](./term-agent-skills.md) — Skill 文件的通用约定