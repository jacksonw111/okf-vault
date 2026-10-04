---
type: "Tool"
title: "ClassCAD.ai（MCP 接入的 AI 参数化 CAD 系统）"
description: "AWV Informatik 出品的 MCP CAD 系统：通过 Model Context Protocol 让 Codex / Claude Code / Cursor / VS Code 等 Agent 直接调出参数化 CAD 几何模型，支持参数化建模 / 约束草图 / 装配 / 实体建模，可输出 STEP 等工程文件。"
resource: "https://classcad.ai"
tags: "[cad, mcp, agent, 3d-printing, parametric-modeling, engineering]"
timestamp: "2026-10-04T02:00:00Z"
---

# ClassCAD.ai

## 它是什么

[ClassCAD.ai](https://classcad.ai) 是瑞士 **AWV Informatik** 推出的 **AI 可调用的 CAD 系统**——通过 MCP（Model Context Protocol）让 Codex / Claude Code / Cursor / VS Code 等 AI Agent 直接调出参数化 CAD 几何模型。

## 与「文生 3D」的本质区别

| 维度 | 文生 3D | ClassCAD |
|------|---------|----------|
| 输入意图 | 「给我一个长得像这样的模型」 | 「外径 80mm、孔径 30mm、法兰衬套」 |
| 输出 | 3D 网格（仅外观） | 参数化几何模型（尺寸准确） |
| 可继续修改 | 一般不可 | 改参数即可 |
| 可进入工程流程 | 否 | 是（输出 STEP 等） |
| 可计算 | 否 | 体积 / 质量属性 / 几何检查 |

## 关键能力

| 能力 | 说明 |
|------|------|
| 接入方式 | MCP 协议，AI Agent 可直接调用 |
| 建模方式 | 参数化建模、约束草图、装配、实体建模 |
| 输出 | STEP 等工程格式 |
| 计算 | 体积 / 质量属性 / 几何检查 |
| 工作流 | Agent 接收自然语言描述 → 调用 CAD 建模 → 输出可继续修改的工程模型 |

## 典型场景

- PCB 出来后直接让 Agent 设计外壳（壁厚 2mm、Type-C 开孔、R5 圆角、预留安装柱）
- 机械零件尺寸沟通：直接用自然语言描述 + Agent 出参数化模型
- 3D 打印前快速迭代

## 参考链接

- 项目链接：<https://classcad.ai>

## 相关概念

- [MCP（Model Context Protocol）](./term-mcp.md) — 让 AI Agent ↔ 工具的开放协议，本工具的核心接入方式