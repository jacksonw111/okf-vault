---
type: Tool
title: "dsh-visualize"
description: "DeepSeek Harness 插件：让 DSH 在对话里直接渲染模型生成的交互式可视化卡片，不再只是回一段文字"
resource: "https://github.com/Nagi-ovo/dsh-visualize"
tags: [deepseek, harness, dsh, visualization, ui]
timestamp: 2026-08-16T16:00:00Z
---

# dsh-visualize

## 它是什么
`Nagi-ovo/dsh-visualize` 是一个 **DeepSeek Harness (DSH)** 插件，把模型在对话里生成的「应该被画出来」的内容（图表、卡片、对比表、表单等）**就地渲染成交互式可视化组件**，而不是只回一段纯文本。

## 为什么用它 / 适合什么场景
- AI 给的「饼图 + 摘要」直接是图，能点能 hover，不用来回切窗口。
- 数据分析 / 报表场景：让 DSH 充当 BI 助手的可视化层。
- 想给用户**演示可交互原型**：AI 一句话 → 一个能拖的组件。
- 模型上下文里附带的结构化信息（schema、字典、表格）想直接渲染成 UI。

## 关键能力
| 能力 | 说明 |
|------|------|
| 卡片式渲染 | 模型输出 JSON 描述 → 卡片组件（图表 / 表单 / 列表 / 折叠面板） |
| 即时交互 | 卡片可点 / 可输入 / 可折叠，回写对话上下文 |
| 跟 DSH 对话同窗 | 渲染区跟文本消息同一会话区，不需要切外部应用 |
| 插件形态 | 不改 DSH 内核，作为官方工具协议接入 |

## 媒体
- ![](https://pbs.twimg.com/media/HPvKQ8TbUAApWQk.jpg)

## 相关概念
- [项目链接](https://github.com/Nagi-ovo/dsh-visualize)