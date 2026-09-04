---
type: Tool
title: "CraftBot（用可执行 Blender 代码做建筑设计的 AI Agent）"
description: "建筑师 AI Agent 研究项目：模型不直接画图或建网格，而是输出在 Blender 里程序化建楼的 Python 脚本，再由脚本派生平面图、剖面、立面、BIM 模型与工程量清单，并用自动渲染回看循环反复修正。"
resource: "https://github.com/lukapiskorec/craftbot"
tags: [architecture, blender, agent, code-generation, bim, grounded-reasoning, research]
timestamp: 2026-09-04T12:00:00Z
---

# CraftBot（用可执行 Blender 代码做建筑设计的 AI Agent）

## 核心思路

让大语言模型**不直接画图、也不直接建网格**，而是通过**可执行的 Blender Python 代码**参与建筑设计。设计意图落在代码里，几何由代码生成——于是设计是可复现、可 diff、可参数化调整的。

![](https://pbs.twimg.com/media/HRRZryPbkAALXXx.jpg)

## 工作流

1. 读取设计任务书，并摄入文档、图像等领域资料做 **grounded 推理**（结论有据可依，而非凭空生成）。
2. 输出在 Blender 里**程序化建楼**的 Python 脚本。
3. 由脚本派生：平面图、剖面、立面、BIM 模型、工程量清单。
4. **自动渲染 → 回看 → 修正**循环，反复迭代直至满足任务书。

## 为什么值得看

- 「模型产出代码、代码产出几何」这一层间接性，把不可控的生成变成可审阅的中间产物——这个模式在 CAD、数据可视化、报表生成等场景同样成立。
- 渲染回看闭环给了 Agent 一个视觉层面的自我校验信号。

## 参考链接

- 项目链接：<https://github.com/lukapiskorec/craftbot>
- 原始链接：<https://x.com/QingQ77/status/2095851371178188931>

## 相关概念

- 暂无强关联概念。
