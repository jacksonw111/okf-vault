---
type: "Note"
title: "awesome-ai-motion（把动效做成卡片给 agent 选）"
description: "gongnyang/awesome-ai-motion：把动效写成一张张卡片（每张含效果描述、参数、触发条件、适用场景），agent 读卡片就能挑选效果、生成参数、跑渲染——专为 AI 视频、信息图、滚动幻灯场景设计。"
resource: "https://github.com/gongnyang/awesome-ai-motion"
tags: "[motion, animation, ai-video, infographic, scroll-presentation, agent-readable, cards]"
timestamp: "2026-10-02T05:25:00Z"
---

# awesome-ai-motion（把动效做成卡片给 agent 选）

## 一句话

[gongnyang/awesome-ai-motion](https://github.com/gongnyang/awesome-ai-motion) 把「做 AI 视频、信息图、滚动幻灯」时需要的动效整理成**结构化卡片**，每张卡片含：

- 效果描述（动起来是什么样）
- 参数（时长 / 缓动 / 触发）
- 适用场景（hero / 列表 / 切换 / 高亮）
- 渲染提示词 / 模板代码

让 agent 直接读卡片挑效果、跑渲染，**避免在动效库前犹豫不决**。

## 为什么用它 / 适合什么场景

- **AI 视频生成**——Remotion / Runway / Kling / Veo 这些工具在「选哪种动效」上卡壳太久，用 awesome-ai-motion 直接给 agent 选项清单。
- **信息图 / 数据可视化**——柱图生长 / 数字滚动 / 折线绘制，给 agent 一组预制卡片就行。
- **滚动幻灯 / 文档演示**——「逐字逐行出现」、「卡片飞入」、「数字翻牌」等效果做成卡片，agent 一调一跑。
- **教学 / 教程视频**——把动效拆成步骤卡片，agent 按步骤拼装。

## 卡片结构（推荐格式）

```yaml
- name: "数字翻牌 (number-flip)"
  category: "data-counter"
  duration_ms: 800
  easing: "ease-out"
  trigger: "on-enter"
  description: "从旧数字逐位翻到新数字，带音效。"
  scene_tags: [dashboard, stat, hero]
  remix_hint: "适合 KPI、积分、倒计时。"
```

## 关键能力

| 能力 | 说明 |
|------|------|
| 结构化 | 每张动效一张卡，字段一致 |
| 分类 | 按 hero / 列表 / 切换 / 数据 / 强调分桶 |
| agent 友好 | 字段可直接进 prompt 或 JSON 调用 |
| 可扩展 | 自己加卡片即扩展动效库 |
| 跨工具 | 与 Remotion / Manim / CSS / Lottie 都可桥接 |

## 参考链接

- 原始链接：<https://x.com/QingQ77/status/2105891275077743075>
- 项目链接：<https://github.com/gongnyang/awesome-ai-motion>

## 相关概念

- [Kinetics](./tool-kinetics.md) — 99 个动画同时提供 CSS + React + AI Prompt 三种版本，动效库思路一致
- [Kobra](./tool-kobra-motion.md) — shadcn 风格的动效组件集
- [Remotion](#) — 程序化视频生成框架，本仓库目前未收录
