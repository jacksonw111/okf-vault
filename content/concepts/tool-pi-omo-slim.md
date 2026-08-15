---
type: "Tool"
title: "pi-omo-slim（Pi OMO-slim 风格多代理编排）"
description: "给 Pi 编码助手配一套 OMO-slim 风格的多代理编排：一个 Orchestrator 调度六个专精代理（Explorer / Librarian / Oracle / Designer / Fixer / Verifier）分工干活，不 fork 上游代码，靠 Pi 自身的扩展和子代理 API 实现。"
tags: "[pi, multi-agent, orchestrator, agent-roles, slim]"
timestamp: "2026-08-14T23:21:00Z"
resource: "https://github.com/joshua-zyy/pi-omo-slim"
---

# pi-omo-slim（Pi OMO-slim 风格多代理编排）

## 它是什么

`joshua-zyy/pi-omo-slim` 是给 [Pi Coding Agent](https://github.com/badlogic/pi-mono) 装的**多代理编排扩展**，模仿 OpenManus OMO 项目里 slim 版的角色分工，但**不 fork 上游代码**，整套实现只靠 Pi 自带的扩展点 + 子代理 API。

## 角色分工

| 角色 | 职责 |
|------|------|
| Orchestrator | 主调度，决定哪个子代理跑、下一步交给谁 |
| Explorer | 摸代码——扫仓库结构、读关键文件、给出概览 |
| Librarian | 查文档——找依赖文档、API 文档、issue 历史 |
| Oracle | 定架构 & 调试策略——做高层决策、决定怎么拆问题 |
| Designer | 做界面——前端 / 设计稿 / 交互 |
| Fixer | 落地实现——写代码、改文件、跑命令 |
| Verifier | 独立验收——检查改完是否过测试、是否符合需求 |

## 为什么用它 / 适合什么场景

- **大任务拆解**：单一 LLM 在面对大型仓库改动时容易「越界」「幻觉」；拆成专精代理后每一步更聚焦。
- **不污染上游**：与 fork 派不同，`pi-omo-slim` 纯靠 Pi 的扩展机制，Pi 升级时本扩展无缝跟随。
- **可替换角色**：六个角色按需启用 / 禁用 / 替换。

## 关键能力

| 能力 | 说明 |
|------|------|
| Orchestrator 模式 | 单一主代理调度，决定下一步派谁 |
| 6 个专精代理 | 每个角色专注一类任务 |
| 不 fork 上游 | 完全基于 Pi 扩展点 |
| 子代理 API | 用 Pi 的子代理机制做嵌套调用 |
| 角色可关 | 不需要哪个角色就关哪个 |
| 上游友好 | Pi 升级不影响本扩展 |

## 与相关工具的差异

| 工具 | 思路 | 差异 |
|------|------|------|
| OpenManus OMO（原始） | 上游 fork 改造 | 重、与上游同步成本高 |
| [pi-hive](tool-pi-hive.md) | Pi 层次化多智能体团队（YAML 拓扑） | 更通用，本项目是 OMO 风格专门版 |
| [Cotal](tool-cotal.md) | 多智能体开放协议框架 | 协议层抽象 |
| **pi-omo-slim** | **OMO 风格 + Pi 扩展** | **零 fork、角色预设** |

## 适用人群

- Pi Coding Agent 用户，跑中型以上任务。
- 喜欢 OpenManus OMO 角色分工、又不想 fork 的人。
- 想给编码代理加「验证环节」（Verifier）的人。

## 参考链接

- [项目链接](https://github.com/joshua-zyy/pi-omo-slim)

## 相关概念

- [pi-hive](tool-pi-hive.md) — Pi 的层次化多智能体团队协作工具
- [pi-task](tool-pi-task-delegation.md) — Pi Agent 子任务委派扩展
- [Cotal](tool-cotal.md) — 多智能体开放协议框架