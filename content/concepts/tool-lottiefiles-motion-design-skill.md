---
type: "Tool"
title: "LottieFiles Motion Design Skill（结构化动效设计领域知识）"
description: "LottieFiles 团队开源的 Motion Design Skill：把动画导演思维（情感意图 → 视觉叙事 → 动效工艺）编码为 Agent 可激活的领域知识，提供四层渐进式架构（SKILL.md / director / patterns / reference）+ 三条主线 + 三条硬规则。"
resource: "https://github.com/LottieFiles/motion-design-skill"
tags: "[agent-skills, lottie, motion-design, animation, design-system]"
timestamp: "2026-09-14T22:40:00Z"
---

# LottieFiles Motion Design Skill（结构化动效设计领域知识）

## 它是什么

[LottieFiles Motion Design Skill](https://github.com/LottieFiles/motion-design-skill) 是 [LottieFiles](https://lottiefiles.com/) 团队开源的**结构化动效设计领域知识**：Agent 处理 UI 动画、状态过渡、加载反馈等任务时，Skill 自动激活，为模型注入专业动效设计的判断力。

## 核心理念：理念优先，实现无关

Skill 让 Agent 在**写代码之前**先回答「**像动效导演一样思考**」的问题：
- 观众应该感受到什么？
- 哪个元素是主角？
- 运动路径是弧线还是直线？

具体实现（CSS / GSAP / Framer Motion / Lottie / Spring）只是最后的翻译步骤。

## 内容架构：渐进式加载的四层

| 层 | 文件 | 作用 |
|----|------|------|
| 1 | `SKILL.md` | 主指令（< 500 行，常驻上下文） |
| 2 | `director/` | 设计哲学（按需深读） |
| 3 | `patterns/` | 可复用配方（入场退场 / 状态反馈 / 氛围 / 编排） |
| 4 | `reference/` | 查询表（时长 / 缓动 / 质量清单 / 排错） |

## 三条主线

回答动效设计的三个递进问题：

### 1. 情感意图
观众应感受什么——信任 / 愉悦 / 紧迫 / 平静……情绪直接决定时长与缓动。

### 2. 视觉叙事
即使是 200ms 的提示淡入，也隐含「**设置 → 行动 → 收尾**」三段结构（约 20-30% / 30-40% / 30-40% 的时间分配）。

### 3. 动效工艺
弧线、次级运动、错峰，让运动「**可信**」。

### 工艺层面三层次

| 层 | 幅度 | 用途 |
|----|------|------|
| 主要动作 | 100% | 主角元素 |
| 次要动作 | 30-50%，延迟 50-100ms，缓动不同 | 跟随主角 |
| 氛围层 | 10-20%，持续 | 不抢注意力 |

> 缺了后两层，动画就会显得「**扁平廉价**」——这是对「**为什么我的动画看起来没有灵魂**」最直接的答案。

## 三条硬规则

1. **空间移动绝不用 linear 缓动**（旋转加载器 / 进度条除外）
2. **重要状态变化绝不只改透明度**，必须叠加位移或缩放
3. **1/3 规则**——移动不超过屏幕 1/3 不加关键帧，同时运动的元素不超过总数的 1/3

## 最大的亮点：把手艺「参数化」

把近百年的动画手艺（迪士尼 12 原则、Material Design、Apple HIG 的隐性知识）从**定性描述**变成**定量参数**：

| 参数 | 取值 |
|------|------|
| 时长表 | 提示 80-120ms / 按钮 120-180ms / 模态框 300-400ms / 页面过渡 400-600ms；入场比退场长 30-50% |
| 缓动方向 | 入场 ease-out、退场 ease-in、屏内 ease-in-out；直接给 Material 3 / Apple HIG 贝塞尔数值 |
| 动效人格 | Playful / Premium / Corporate / Energetic 四种，各自绑定时长区间、曲线、过冲百分比 |
| 品牌识别 | 一条签名曲线 + 三档时长 + 一个统一入场模式 |

## 为什么用它

- **动效设计**领域，AI 通常只会生成「能动」的代码——但**节奏、缓动、层次**全靠人手调。Skill 把隐性知识显性化。
- **硬规则 + 量化参数**意味着团队不需要再为「这个动画对不对」反复争论——查表就行。
- 适配 Lottie / GSAP / Framer Motion / CSS / Spring 等多种实现，**绑定平台但不绑实现**。

## 媒体

![](https://pbs.twimg.com/media/HSJ3xmzasAA9AVM.jpg)

## 项目链接

- 仓库：<https://github.com/LottieFiles/motion-design-skill>

## 相关概念

- [Agent Skills（代理技能包）](term-agent-skills.md) — Skill 把领域知识注入 Agent 的标准范式
- [Dunhuang Aura Skill](tool-dunhuang-aura-skill.md) — 同类「风格 → Skill」思路，专注视觉品牌