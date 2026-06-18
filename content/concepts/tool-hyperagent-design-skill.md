---
type: "Tool"
title: "Hyperagent 设计网格 Skill"
description: "Hyperagent 团队的 Claude Code skill：把 Müller-Brockmann《平面设计中的网格系统》（162 页）喂给代理，强制代理在代码中应用真网格、视觉层次、字体与排版规则——解决「AI 设计看起来很通用」的根问题。"
tags: "[ai, agent, skills, design, grid, typography, claude-code]"
timestamp: "2026-06-17T00:00:00Z"
---

# Hyperagent 设计网格 Skill

## 它是什么

`Hyperagent` 团队 (@hyperagentapp) 开源的 **Claude Code skill**：把 **Josef Müller-Brockmann** 的经典著作 *《平面设计中的网格系统》*（*Grid Systems in Graphic Design*，162 页）作为「教材」喂给编码代理，**强制**代理在写 UI 代码时遵循真实的网格系统、视觉层次、字体与排版规则。

目的：让「AI 设计的页面看起来很通用」不再是默认结果。

## 解决的根问题

> "AI 设计看起来很通用，因为它们不遵循任何真正的构图系统。"

具体痛点：

- 间距 8 / 12 / 16 / 24 满天飞，**没有**统一基准；
- 标题 / 正文 / 副标题视觉重量错配；
- 网格列数不固定，元素乱飘；
- 字体混用，hierarchy 不成立；
- 「凭感觉看起来好」而非「有据可依」。

## 工作方式

1. **把 Müller-Brockmann 162 页 PDF 作为系统提示的一部分**（或摘要 + 规则集）；
2. skill 被调用时，代理**先**用规则约束**输出**网格 / 字号 / 行高 / 列数 / 间距的 **设计令牌**；
3. **再**用这些令牌生成代码（Tailwind / CSS / 设计稿 JSON）；
4. 视觉层次、字体、间距**有据可依**，可以解释「为什么是 24px 不是 16px」。

## 关键能力

| 能力 | 说明 |
|------|------|
| 网格系统内化 | 列数 / 槽宽 / 边距按 Müller-Brockmann 公式推导 |
| 视觉层次 | 字号梯度、行高、字重基于经典 1.25 / 1.333 / 1.5 模块比例 |
| 字体与排版 | 中英文混排、衬线 / 无衬线对比、字符间距 |
| 适配代码生成 | 输出可直接落到 Tailwind / CSS / 设计 Token JSON |
| 可审计 | 「为什么用这个尺寸」可以引用原文页码 |

## 与 [mattpocock/skills](tool-mattpocock-skills.md) 的关系

matt 的 `/zoom-out`、`/grill-me` 是**通用** workflow；Hyperagent 设计网格是**专用领域** skill——把「参考书 → 规则 → 代码」的链路显式化。两者结合的范式：

```
matt 的 /zoom-out → 看大局
Hyperagent 设计网格 → 落到排版细节
shadcn/improve → 整体审计
```

## 使用方式

```bash
git clone <hyperagent-design-skill> .claude/skills/hyperagent-design
claude
# /hyperagent-design
# 描述需求：「做一个 SaaS landing page」
# 代理会先输出设计令牌，再出代码
```

## 相关概念

- [Agent Skills 是什么](term-agent-skills.md)
- [Claude Code](tool-claude-code.md)
- [mattpocock/skills](tool-mattpocock-skills.md)
- [shadcn/improve](tool-shadcn-improve.md)
- [Archify](tool-archify.md)
- [Müller-Brockmann 网格系统](https://www.amazon.com/Grid-Systems-Graphic-Design-Josef-Müller-Brockmann/dp/3721201450)
