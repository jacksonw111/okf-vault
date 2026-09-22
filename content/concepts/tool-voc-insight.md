---
type: Tool
title: "voc-insight"
description: "售后与产品团队的客户反馈 AI 助手——把工单、群聊、表格里的每条反馈喂给 DeepSeek，自动产出摘要 / 分类 / 严重程度 / 建议优先级，并把指向同一件事的反馈合并成单一 issue 跟踪到底。"
resource: "https://github.com/jinjian-liu/voc-insight"
tags: "[ai-agent, customer-feedback, deepseek, open-source]"
timestamp: "2026-09-22T00:00:00Z"
---

# voc-insight

## 它是什么
一个**客户反馈（Voice of Customer）的 AI 聚合工具**：

> 把散落在工单、群聊、表格里的每条客户反馈喂给 DeepSeek，自动吐出摘要 / 分类 / 严重程度 / 建议优先级；再把指向同一件事的反馈合并到同一个 issue 上，跟到处理完毕。

## 为什么用它 / 适合什么场景
- 售后与产品团队手上反馈散落在多个渠道，难以聚合。
- 需要把重复反馈归并成单一 issue，避免「同一件事被多人重复提」。
- 希望 AI 给每条反馈打严重程度 + 建议优先级，便于排期。
- 想用 DeepSeek 这类国产模型做轻量 LLM 推理。

## 关键能力
| 能力 | 说明 |
|------|------|
| 输入源 | 工单 / 群聊 / 表格等 |
| 模型 | DeepSeek |
| 单条处理 | 摘要 + 分类 + 严重程度 + 建议优先级 |
| 聚合 | 把指向同一件事的多条反馈合并到一个 issue |
| 跟踪 | 一跟到底，处理闭环 |

## 项目链接
- 项目主页：<https://github.com/jinjian-liu/voc-insight>

## 媒体
- 截图：<https://pbs.twimg.com/media/HSyIyobaIAADrYu.jpg>
