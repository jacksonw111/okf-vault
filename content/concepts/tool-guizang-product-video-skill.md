---
type: "Tool"
title: "Guizang Product Video Skill（代码提交一键产出产品更新宣传片）"
description: "op7418/guizang-product-video-skill：给定代码仓库 + 一堆提交，Agent 自动整理卖点、写白话文案、接原组件、做动画、配乐配音效、导出视频和可继续改的工程文件，一趟走完。"
resource: "https://github.com/op7418/guizang-product-video-skill"
tags: "[agent-skill, video, marketing, product-update, automation]"
timestamp: "2026-09-20T18:00:00Z"
---

# Guizang Product Video Skill

## 它是什么

[op7418/guizang-product-video-skill](https://github.com/op7418/guizang-product-video-skill) 是给 Agent 的「产品更新宣传片」Skill——给定一个**代码仓库 + 一堆提交**，自动跑完下面这一长串工序：

1. 整理**卖点**
2. 写**白话文案**
3. 接**原组件**（沿用项目里已有的 UI 部件）
4. 做**动画**
5. **配乐 + 配音效**
6. 导出**成片视频** + 一份**可继续改的工程**（不是黑盒渲染）

## 为什么用它 / 适合什么场景

- 每次发版都要做「**更新日志视频**」又懒得人工剪。
- 想让 AI 把仓库里干巴巴的 commit message 转成**人类能看完的产品故事**。
- 想要**可二次编辑的工程文件**——AI 出完片后还想改文案 / 配乐 / 镜头。

## 关键能力

| 能力 | 说明 |
|------|------|
| 输入即产物 | 输入：代码库 + commits；输出：成片 + 可改工程 |
| 卖点提炼 | 自动从提交记录里抽「这次更新值得讲什么」 |
| 白话文案 | 不堆术语，用户能听懂 |
| 原组件复用 | 沿用项目里既有 UI 部件，不会出现「视频里和实际产品长得不一样」 |
| 动效 + 配乐 + 音效 | 一站式视觉听觉素材生成 |
| 工程化输出 | 不是闭源渲染结果，可以接着改 |

## 项目链接

- 仓库：<https://github.com/op7418/guizang-product-video-skill>

## 媒体

![](https://pbs.twimg.com/media/HSnzobna8AAJZQK.jpg)

## 相关概念

- [Agent Skills（代理技能包）](./term-agent-skills.md) — Skill 协议层
- [Cloud Agent 基础设施（CREAO）](./note-cloud-agent-infrastructure.md) — 同样是「让 Agent 跑完一长串工序」的工程模式
