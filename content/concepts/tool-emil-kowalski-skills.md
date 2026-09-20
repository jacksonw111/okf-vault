---
type: "Tool"
title: "emilkowalski/skills（设计工程 / 动画 / Apple 风格 10 件套 Skill 合集）"
description: "emilkowalski/skills：Linear 设计师 Emil Kowalski 维护的 Agent Skills 仓库，覆盖设计工程总则 / 动画设计 / 动画审查 / 动画改进 / 动画机会识别 / Apple 设计原则 / 原型多方案 / 移动端网页 / 现代 Swift / UI 组件库挑选十大 Skill，让 AI 做界面时更有设计品味。"
resource: "https://github.com/emilkowalski/skills"
tags: "[design, animation, skill, wwdc, apple, swift, motion, agent-skills, emil-kowalski]"
timestamp: "2026-09-20T18:00:00Z"
---

# emilkowalski/skills

## 它是什么

[emilkowalski/skills](https://github.com/emilkowalski/skills) 是 **Emil Kowalski**（前 Vercel、现 Linear 设计师）维护的 Agent Skills 仓库（GitHub Star 接近 4w）。目的是让 **AI 做界面时更有「设计品味」**——尤其是**动画选择、交互细节和视觉打磨**。

整套包含 **10 个 Skill**，每个 Skill 解决一类具体场景。

## 10 个 Skill 一览

| Skill | 作用 |
|-------|------|
| `/emil-design-eng` | 设计工程总则：关注 UI 整体质感 / 组件设计 / 动画选择 / 交互细节；适合开发新界面时作为总体设计指导 |
| `/animate` | 制作动画：先判断是否需要加，再决定动画目的 / 实现方式 / 属性 / 曲线 / 时长；适合弹窗 / 抽屉 / 按钮反馈等动效 |
| `/review-animations` | 审查动画：检查已有动画是否多余、速度是否拖沓、缓动是否合适、是否考虑减少动态效果；适合动画完成后的专项评审 |
| `/improve-animations` | 改进项目动画：检查整个项目的动画并整理出可执行的改进建议；适合接手已有项目、想系统提升动效质量时使用 |
| `/find-animation-opportunities` | 寻找动画机会：判断界面上哪些地方值得增加动画、哪些地方不应该动；重点不是「多加动画」，而是让动效真正帮助用户理解反馈或状态 |
| `/apple-design` | Apple 风格设计原则：将 Apple WWDC 设计分享中的界面与动效原则整理成指导，帮助改善界面层级、反馈和整体连贯性 |
| `/prototype` | 制作多个原型方案：针对一个 UI 需求生成多个不同方案，便于比较布局和组件形态；适合设计方向还不确定时使用 |
| `/mobile-native` | 优化移动端网页体验：帮助网页在手机上更像原生应用，关注安全区 / 触控反馈 / 输入框缩放和移动端视口等细节 |
| `/write-swift` | 编写现代 Swift：覆盖 Swift 值类型 / 并发 / 泛型 / 性能和测试等工程实践 |
| `/pick-ui-library` | 选择 UI 组件库：根据需求挑选合适的组件库，避免不必要地手写复杂组件、或引入维护状况不佳的依赖 |

## 为什么用它 / 适合什么场景

- 想给 **Claude Code / Codex / Cursor** 这类 agent 注入「**有品味的设计直觉**」，而不是让它默认产出 shadcn / Tailwind 默认样式。
- 做 **iOS / macOS / 跨端 UI** 时，希望「**动效与微交互**」一开始就在合格线以上。
- 团队里没有专职设计师，**把 Emil 的判断框架当 Skill 装上**，把 agent 当初级设计师用。

## 关键能力

| 能力 | 说明 |
|------|------|
| 10 个 Skill | 覆盖「设计总则 / 动画全流程 / Apple 风格 / 原型 / 移动端 / Swift / 选型」 |
| 来源权威 | Emil Kowalski 是 Linear / Vercel 出品的设计师 |
| Skill 协议 | `npx skills add emilkowalski/skills` 一行装 |
| 主题统一 | 整套围绕「让 AI 写出的 UI 更有设计品味」 |
| 单仓库 | 一个仓库装 10 个 Skill，按需调用 |

## 项目链接

- 仓库：<https://github.com/emilkowalski/skills>

## 媒体

![](https://pbs.twimg.com/media/HSpOz65bsAAYdVe.jpg)
![](https://pbs.twimg.com/media/HSpO3VAbAAE1h_Z.jpg)

## 相关概念

- [Apple Design Skill（/apple-design）](./tool-apple-design-skill.md) — 本仓库里的一个 Skill，单独抽出条目
- [Agent Skills（代理技能包）](./term-agent-skills.md) — 本概念遵循的协议
- [jakubkrehel Skills](./tool-jakubkrehel-skills.md) — 同为高质量个人维护的 Agent Skills 仓库
- [Jakub 设计 Skills](./note-jakub-design-skills.md) — 同样面向「让 AI 写 UI」的另一套 Skill
