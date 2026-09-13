---
type: "Tool"
title: "svg-diagram（Bybit 团队的 Agent SVG 绘图规范 + Linter）"
description: "给 Agent 定一套手写 SVG 图的统一画法，配套零依赖 Linter 验证成品；架构图 / 流程图 / 时序图 / 数据流图 / 状态机图五类风格一致。"
resource: "https://github.com/bybit-exchange/svg-diagram"
tags: "[svg, diagram, agent-skill, lint, bybit, cjk]"
timestamp: "2026-09-13T00:12:00Z"
---

# svg-diagram（Bybit 团队的 Agent SVG 绘图规范 + Linter）

## 它是什么

[bybit-exchange/svg-diagram](https://github.com/bybit-exchange/svg-diagram) 是一套**给 Agent 手写 SVG 图的规范 + 零依赖 Linter**：架构图、流程图、时序图、数据流图、状态机图都按同一套规则画，Linter 负责校验产物是否符合规范，让多个 Agent / 多次产出的图风格一致。

## 为什么用它 / 适合什么场景

- 文档站 / 内部知识库依赖 Agent 产 SVG 图，但图与图之间风格漂移。
- 想给团队立一套「画图规范」，但希望机器可校验而不是靠 code review。
- 不希望引入额外构建 / 服务依赖。
- **中英文混排文档**：内置中文按「每字一个字号」算宽度的字符宽度表，避免落笔后溢出。

## 关键能力

| 能力 | 说明 |
|------|------|
| 五类图全覆盖 | 架构图、流程图、时序图、数据流图、状态机图 |
| 统一画法 | 框高跟字号走，拐弯只用曲线，箭头到目标框固定留白 11px |
| 零依赖 Linter | 读取最终 SVG 成品做 12 项硬核校验：转义、留白、字体、重叠、配色全覆盖 |
| 报错具体 | 例：「边距 11，应为 20 到 25」，直接点名问题 |
| 中英文字符宽度表 | 中英文各自一张表，落笔前先判定是否会溢出 |
| Noto Sans CJK SC 字体栈 | 中文图也能保字形 |
| 五组语义配色 | 不用每次自己挑色 |
| 白底底板 | 贴进 GitHub 暗色主题也清晰不脏 |
| 一条命令接入主流 Agent | Claude Code / Codex / Cursor / Gemini CLI 等几十个 Agent |
| 仓库附 10 张样图 | 直接参考抄样式 |
| 文字基线公式写死 | 避免「飘字」 |

## 集成方式

```
一条命令即可接入 Claude Code、Codex、Cursor、Gemini CLI 等几十个 Agent。
```

## 媒体

- ![](https://pbs.twimg.com/media/HSBYaUGawAE2Ha9.jpg)
- ![](https://pbs.twimg.com/media/HSBYaf5bkAAwhLI.jpg)

## 相关概念

- [Archify（LLM→JSON→SVG 架构图）](./tool-archify.md) — 同类「Agent 画架构图」思路，Archify 走 JSON→SVG 路径
- [Agent Skills（代理技能包）](./term-agent-skills.md) — svg-diagram 是一种典型的 Skill

## 项目链接

- 项目主页：<https://github.com/bybit-exchange/svg-diagram>