---
type: "Tool"
title: "tourcn（通过 shadcn 注册表安装的 Tour 引导组件）"
description: "shadcn 项目里的 Tour 引导组件：作者厌倦了在不同 Tour 库的 CSS 里斗智斗勇，于是做了一个通过 shadcn 注册表安装的 Tour 组件，绕过 npm 直接拷进项目。"
resource: "https://github.com/bundui/tourcn"
tags: [shadcn, ui-component, tour, onboarding, react, registry]
timestamp: "2026-09-31T23:05:00Z"
---

# tourcn

## 它是什么
[tourcn](https://github.com/bundui/tourcn) 是一个为 **shadcn 项目**专门打造的 **Tour 引导组件**。它的出现是因为作者受够了在不同 Tour 库（react-joyride / shepherd / driver.js 等）的 CSS 里斗智斗勇——shadcn 项目有自己的 Tailwind 配置、设计语言，第三方库的 CSS 经常打架。

设计哲学：**通过 shadcn 注册表（registry）直接拷进项目**——而不是装 npm 包。组件代码落在你自己的仓库里，**样式与项目天然一致**，不需要「让库适配我」的反向适配。

## 为什么用它 / 适合什么场景
- 用 shadcn 做了产品，**需要新手引导 Tour**，但不想引入第三方库打架样式；
- 喜欢「**代码在我仓库里**」的工程美学（与 shadcn 一脉相承）；
- 想用 shadcn CLI 的 **registry 安装**模式加新组件；
- 想要一个**最小、可控**的 Tour 引导组件，而不是「全家桶」。

## 关键能力

| 能力 | 说明 |
|------|------|
| shadcn 注册表安装 | 通过 `shadcn add` 一行命令装到项目 |
| 自托管组件 | 代码落在你自己仓库里 |
| 无 CSS 冲突 | 用项目自身的 Tailwind，告别样式打架 |
| Tour 引导 | 高亮目标元素 + 文字说明 |
| 多步流程 | 多个步骤串联成完整 Tour |
| 演示 + 文档 | tourcn.vercel.app 看效果 |
| 开源 | GitHub 公开，可自由改 |

## 媒体
![](https://pbs.twimg.com/media/HREc6liXMAAscYt.jpg)

## 相关概念
- [Ark UI](tool-ark-ui.md) — Zag.js 团队的 headless 行为层；tourcn 是 Tour 组件成品，Ark UI 提供底层 headless 原语
- [shadcn/improve](tool-shadcn-improve.md) — 同样是 shadcn 生态；improve 是审计工具，tourcn 是组件成品

## 参考链接
- 项目链接：<https://github.com/bundui/tourcn>
- 演示与文档：<https://tourcn.vercel.app>