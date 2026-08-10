---
type: "Tool"
title: "ComfyUI Cable Management"
description: "vtokic 写的 ComfyUI 扩展，把节点连线当作电路板来自动布线：自动绕开节点、互相避让，支持菊花链串联、reroute 叠成排线、补全从右往左的折线支持，复杂工作流视觉变清爽。"
resource: "https://github.com/vtokic/comfyui-cable-management"
tags: [comfyui, node-editor, ui, ux, extension, ai-art]
timestamp: "2026-08-10T03:44:00Z"
---

# ComfyUI Cable Management

## 它是什么

[ComfyUI Cable Management](https://github.com/vtokic/comfyui-cable-management) 是一个 ComfyUI 扩展，把节点之间的**连线布线**当电路板走线来处理：自动绕开节点矩形、连线之间互相避让、支持菊花链串联、多个 reroute 堆叠变成整齐的「排线」，还补全了从右往左的折线支持。复杂工作流（几十甚至上百节点）从「意大利面」变成接近电路图的样子。

## 为什么用它 / 适合什么场景

- 复杂 ComfyUI 工作流可视化整理：节点一多连线就乱，自动布线让拓扑清晰。
- 教学 / 分享场景：把工作流截图发给别人看时不至于「分不清哪根线是干嘛的」。
- 大型 pipeline 维护：方便后续增删节点时看清上下游数据依赖。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自动绕节点 | 连线自动绕过节点矩形 |
| 连线避让 | 多根线互相不交叉重叠 |
| 菊花链串联 | 多节点顺序串成干净一根总线 |
| Reroute 排线 | 多个 reroute 叠成整齐的排线 |
| 右向左折线 | 补全反向方向布线的折线模式 |
| 拓扑整理 | 大型 pipeline 自动看上去清爽 |

## 媒体

![](https://pbs.twimg.com/media/HPPo0uVbcAAf8df.jpg)

## 参考链接

- [项目仓库](https://github.com/vtokic/comfyui-cable-management)
- [原始链接](https://x.com/QingQ77/status/2086659804123029549)
