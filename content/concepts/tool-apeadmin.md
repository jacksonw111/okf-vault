---
type: Tool
title: "ApeAdmin"
description: "FastAPI + Vue3 的 MIT 中后台管理框架，原生为 AI Agent 调用做适配，底座提供 RBAC 权限 / 审计日志 / 菜单部门管理等企业级基础能力。"
resource: "https://github.com/KevinLiss/ApeAdmin"
tags: "[admin, fastapi, vue3, rbac, agent, mit]"
timestamp: "2026-09-07T13:14:00Z"
---

# ApeAdmin

## 它是什么
100% 开源（MIT）的中后台管理框架，FastAPI + Vue3，原生为 AI Agent 调用做适配。除了常见 admin 框架必备的 RBAC 权限管控、审计日志、菜单部门管理，还针对 AI Agent 场景做了接口适配，让 Agent 可以稳定调用后台数据与操作。

## 关键能力
| 能力 | 说明 |
|------|------|
| FastAPI + Vue3 | 现代前后端分离 |
| MIT 协议 | 商用免费 |
| RBAC | 角色权限 |
| 审计日志 | 操作可追溯 |
| 菜单 / 部门 | 经典企业后台模型 |
| Agent 适配 | 接口层对 AI 调用友好 |

## 与传统 admin 框架的差异
传统 admin 框架假设"操作者是带浏览器的用户"，ApeAdmin 多加一层假设："操作者也可能是一个 LLM Agent"——这影响接口设计（明确语义、可机器解析）和错误处理（缺字段给机器可读的诊断）。

## 适用场景
- 内部 SaaS / 工具管理后台
- 需要 Agent 直接调用的运营系统
- 想避开 Antd Pro / vue-element-admin 等收费栈的小团队

## 参考
- 项目链接：<https://github.com/KevinLiss/ApeAdmin>

## 相关概念
- [CopilotKit](tool-copilotkit.md) — 让 AI 直接读写后台的另一种路径（前端 UI 侧）
- [DataFoundry](tool-datafoundry-data-agent.md) — 企业级私有部署的数据 Agent 工作台