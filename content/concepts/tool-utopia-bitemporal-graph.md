---
type: Tool
title: "Utopia（双时态知识图谱）"
description: "把时间维度做进图谱底层的知识与决策系统：用双时态结构同时记录「事实何时成立」与「系统何时知道」，让旧版本与变更理由不再丢失；可在企业自有硬件上离线运行，全程可审计。"
resource: "https://github.com/deeplethe/utopia"
tags: [knowledge-graph, bitemporal, audit, self-hosted, decision-system, provenance]
timestamp: 2026-09-04T12:00:00Z
---

# Utopia（双时态知识图谱）

## 它解决什么问题

知识图谱和向量库通常只存**「当前正确」**的知识：一旦理解变了，就地覆盖——**旧版本没了，改动的理由也没了**。事后既无法回答「三个月前我们据以决策的事实是什么」，也无法审计「这条结论为什么变了」。

## 它的做法：双时态

Utopia 把**时间维度做进图谱底层**，用双时态（bitemporal）结构把两条时间线一起记录：

| 时间线 | 含义 |
|--------|------|
| 有效时间 | 该事实**在现实中何时成立**（生效 / 失效） |
| 记录时间 | 系统**何时知道**这件事（写入 / 修订） |

两条时间线分开存，就能同时回答「当时的事实是什么」和「我们当时以为的事实是什么」——这正是审计与复盘所需要的区分。

## 部署形态

企业可在**自有硬件上离线运行**一整套可审计的知识与决策系统，数据不出机房。

视频：<https://video.twimg.com/amplify_video/2095708935433195520/vid/avc1/1920x1044/x1FQthoFKt-F9_HG.mp4?tag=29>

## 参考链接

- 项目链接：<https://github.com/deeplethe/utopia>
- 原始链接：<https://x.com/QingQ77/status/2095788958600810525>

## 相关概念

- 暂无强关联概念。
