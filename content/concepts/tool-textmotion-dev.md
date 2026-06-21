---
type: "Tool"
title: "textmotion.dev"
description: "Daniel White 维护的「文字动效」精选集合；专注文本层面的过渡（逐字、逐行、字符拆分、打字机、变形），是 transitions.dev 在文字粒度上的互补。"
tags: "[web, animation, text, typography, design-resources]"
timestamp: "2026-06-18T00:00:00Z"
resource: "https://textmotion.dev"
---

# textmotion.dev

## 它是什么

[`textmotion.dev`](https://textmotion.dev) 是「**文字动效**」精选集合——和 [transitions.dev](tool-transitions-dev.md) 是同一个生态（一个管页面级、一个管文字级）。

> "为什么这感觉这么好？"

——指的是**把文字本身的过渡做好**，可以让整页观感从「能用」瞬间升级到「舒服」。

## 适合场景

- Hero 区的逐字入场 / 错位入场；
- 列表的字符级 stagger；
- 标题在路由切换时做「字形 morph」；
- 数字 / 价格的滚动递增；
- 「正在输入」反馈（比纯 spinner 高级）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 字符级动画 | 逐字 stagger、随机进入 |
| 打字机效果 | 比传统 `setInterval` 那种更自然 |
| 文本 morph | 字符级从一个词变形到另一个（FLIP / SVG path） |
| 行级 stagger | 段落、列表项错位 |
| 数字滚动 | 计数器、累计、股价等 |
| 代码片段可复制 | 同 [transitions.dev](tool-transitions-dev.md) 的形式 |

## 与本知识库的关系

- 用 [tool-okf-static-html-visualizer](tool-okf-static-html-visualizer.md) 生成静态页面时，hero 区直接套一个 textmotion 效果，能让「平淡的概念卡片墙」立刻有「产品」感。
- 配合 [Hyperagent 设计网格 Skill](tool-hyperagent-design-skill.md)：排版规则 + 字符级动效 = 高级感翻倍。

- [演示视频 (1920×1080)](https://video.twimg.com/amplify_video/2065190091757101056/vid/avc1/1920x1080/lP3PCQKFuHGF9eJd.mp4?tag=27) — 作者本人发起的「Why does this feel so good?」短演示。

## 参考链接

- [原始链接 1](https://x.com/DanielWhit21874/status/2065190155460231678)
- [原始链接 2](https://x.com/Wen_Zw/status/2065200441164787722)

## 相关概念

- [transitions.dev](tool-transitions-dev.md)
- [JSON-Render / 生成式 UI](tool-json-render.md)
- [Hyperagent 设计网格 Skill](tool-hyperagent-design-skill.md)
- [index.how/to/articulate](tool-index-how-articulate.md) — 描述动效的术语词典
