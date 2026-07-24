---
type: Tool
title: "codex-slides（给 Codex 编程代理用的开源幻灯片工作室）"
description: "跑在 Codex 内置浏览器里的开源幻灯片工作室。一句话 / 一个 GitHub 仓库 / 一堆文件出发,自动走完调研→大纲→选风格→渲染→编辑→演示→导出 PPTX/PDF 全链路,内置 45 套模板与 73 套社区风格,6 组 24 种场景化工作流。"
resource: "https://github.com/nexu-io/codex-slides"
tags: [codex, slides, presentation, agent-skill, web-ui, pptx, pdf]
timestamp: "2026-07-24T00:00:00Z"
---

# codex-slides

[codex-slides](https://github.com/nexu-io/codex-slides) 是一款**给 Codex 编程代理用的开源幻灯片工作室**——直接跑在 Codex 的内置浏览器里，从一句话 / 一个 GitHub 仓库 / 一堆文件，自动跑完一整条幻灯片生产链。

## 它解决的问题

把资料转成幻灯片，传统路径要：先手动写大纲 → 选模板 → 套内容 → 调版式 → 导出 PPTX。每一步都要人盯。

codex-slides 把整条链交给 Codex 代理 + 内置浏览器完成：

| 阶段 | 谁做 |
|------|------|
| 调研 | Codex 读输入（仓库 / 文件 / 一句话）|
| 大纲 | Codex 自动生成 |
| 选风格 | 内置 45 套模板 + 73 套社区风格，代理按场景挑 |
| 渲染 | 浏览器内实时渲染 |
| 编辑 | 内嵌编辑器微调 |
| 演示 | 浏览器内直接放 |
| 导出 | PPTX / PDF |

10 页以上高质量幻灯片大约 4-5 分钟出。

## 关键能力

| 能力 | 说明 |
|------|------|
| 跑在 Codex 内置浏览器 | 装好就能用，无外部依赖 |
| 多输入起点 | 一句话 / GitHub 仓库 / 一堆文件 |
| 全流程自动化 | 调研→大纲→选风格→渲染→编辑→演示→导出 |
| 模板丰富 | 45 套内置模板 + 73 套社区风格 |
| 场景化工作流 | 6 组 24 种场景（新建 / 转文档 / 数据故事 / 深研 / 品牌重制 / 培训 等）|
| 双格式导出 | PPTX / PDF |
| 4-5 分钟 10+ 页 | 高质量幻灯片产出速度 |

## 适用场景

- 把 GitHub 仓库 / 项目代码转成演示材料
- 把一堆 PDF / 笔记转成培训幻灯片
- 用一句话描述一个想法，快速出第一版 deck
- 想给 Codex 加一个「汇报输出」通道

## 参考链接

- 项目仓库: <https://github.com/nexu-io/codex-slides>

## 媒体

![](https://pbs.twimg.com/media/HN9RENTbAAAfOCV.jpg)

## 相关概念

- [codex-storyboard](tool-codex-storyboard.md) — 同为 Codex 内运行的内容工作室，本工具做幻灯片，storyboard 做视频分镜
- [multi-design-ppt](tool-multi-design-ppt.md) — Agent Skills 协议幻灯片生成 Skill，62 种品牌设计语言，本工具走 Codex 内浏览器路径
- [bento-slides](tool-bento-slides.md) — 单 HTML 文件演示文稿，数据明文 JSON 存头部，本工具是 agent 驱动版本