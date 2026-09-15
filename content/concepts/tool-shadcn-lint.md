---
type: "Tool"
title: "shadcn-ui/lint（Tailwind 设计系统的 Agent 优先 Linter）"
description: "shadcn-ui/lint：给 Tailwind 设计系统用的 linter，让人写死哪些类名能用，Agent 撞线时报错直接告诉它错在哪、换成组件里已有的哪个写法。"
resource: "https://github.com/shadcn-ui/lint"
tags: "[tailwind, linter, design-system, agent, shadcn]"
timestamp: "2026-09-15T14:55:00Z"
---

# shadcn-ui/lint（Tailwind 设计系统的 Agent 优先 Linter）

## 它是什么

[shadcn-ui/lint](https://github.com/shadcn-ui/lint) 是 shadcn/ui 官方推出的 **Tailwind 设计系统 linter**。它的核心思路是：**让人在配置里写死「哪些类名能用」**——这相当于把设计 token 与组件约定编码成 lint 规则；当 Agent 或开发者写出不在白名单的类名时，linter **不仅报错，还直接告诉它替换成组件里已有的哪个写法**。

## 为什么用它

- 传统 ESLint / Stylelint 对 Tailwind 的覆盖偏弱，往往只查顺序不查「**这个类名项目到底允不允许**」。
- 「**Agent 撞线报错 + 给出可替换的写法**」是关键：普通 lint 只说「违规」，这个 linter 直接告诉 Agent「**改成 `bg-primary` 而不是 `bg-blue-500`**」，让 Agent 不靠人也能收敛到设计系统里。
- 对设计系统建设期最有用——约定还没变成肌肉记忆的阶段，让 lint 替你说话。

## 关键能力

| 能力 | 说明 |
|------|------|
| 类名白名单 | 配置只允许的 Tailwind 类，超出即报错 |
| 智能替换 | 报错时给出项目内已有的等价类名 |
| Agent 优先 | 报错信息面向 Agent 可读、可执行 |
| 设计系统护栏 | 让 design token 真正落到代码而非 PPT |
| Tailwind 专精 | 对 Tailwind 类名做精准匹配，不是模糊规则 |

## 适合谁

- 在用 Tailwind + shadcn 做 UI，正在建组件库 / 设计系统的团队
- 团队里大量引入 Agent 写 UI 代码，怕它乱写 className
- 想用 lint 而不是 review 把设计约束前置

## 媒体

![](https://pbs.twimg.com/media/HSOq2Q_bkAAB8Pw.jpg)

## 项目链接

- 仓库：<https://github.com/shadcn-ui/lint>

## 相关概念

- [Tailwind CSS](tool-tailwind-css.md) — shadcn-ui/lint 专为 Tailwind 类名体系设计
- [gap-trap](tool-gap-trap.md) — 同样面向「让 Agent 写代码守规矩」的护栏思路