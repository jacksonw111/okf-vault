---
type: "Tool"
title: "Panel（研究工作台）"
description: "把聊天、文件、PDF、Markdown、Jupyter notebook 塞进同一套可拼的 Pane 工作台，Agent 在 workspace 目录里读写文件、动工具前先确认、后台命令可看可停，notebook 跑真 kernel 两边同时改。"
resource: "https://github.com/greentfrapp/panel"
tags: "[research, jupyter, markdown, pdf, agent-workspace, pane-ui]"
timestamp: "2026-09-16T16:02:00Z"
---

# Panel（研究工作台）

## 它是什么

[greentfrapp/panel](https://github.com/greentfrapp/panel) 是一个**研究场景下的多 Pane 桌面工作台**：把**聊天、文件、PDF、Markdown、Jupyter notebook** 等多种内容形式塞进同一套可拼的 Pane 界面，省掉来回切窗口的麻烦。Agent 就坐在 workspace 目录旁读写文件，**动工具前先向用户确认一次**，后台命令可看可停；notebook 跑的是真实 kernel，文件和 notebook 两边可以同时修改。

## 为什么用它 / 适合什么场景

- 做数据 / ML / 调研类工作时，不想反复切换 IDE、PDF 阅读器、聊天窗口。
- Agent 改文件时希望可视化确认改在哪一段、什么时间改的。
- notebook 与代码文件希望互相引用、同一 workspace 内联动。
- 想让 Agent 的工具调用变成可视、可中断的，不再是黑盒脚本。

## 关键能力

| 能力 | 说明 |
|------|------|
| 可拼 Pane 界面 | 聊天 / 文件 / PDF / Markdown / Jupyter 同一窗口并排 |
| Agent 旁路 | Agent 在 workspace 目录读写文件，可视可确认 |
| 工具调用前确认 | 危险操作前向用户提示，不黑盒执行 |
| 后台命令可视化 | 跑长任务时能看进度、能中途停 |
| 真 Jupyter kernel | notebook 跑真 kernel，与文件改动双向同步 |
| Agent 主动补展示 | 缺什么图表 / 视图，Agent 直接写一段代码补出来 |

## 媒体

- ![](https://pbs.twimg.com/media/HSTV1XBbgAAOUgS.jpg)

## 相关概念

- [Harness Engineering](./term-harness-engineering.md) — Panel 是「Agent 旁路 + 可视化」这一 harness 思路的具象实现