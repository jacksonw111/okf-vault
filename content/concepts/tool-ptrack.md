---
type: Tool
title: "ptrack（DevEnchantments）"
description: "用现代 Web 栈（React 19 + NestJS 11 + Supabase）重写的一套项目组合管理（PPM）系统，替代原 Oracle APEX 版本，对九类记录做完整增删改查 + 历史审计。"
resource: "https://github.com/DevEnchantments/ptrack"
tags: "[project-management, react, nestjs, supabase, ppm, oracle-replacement]"
timestamp: "2026-07-19T00:07:00Z"
---

# ptrack（DevEnchantments）

## 它是什么

DevEnchantments/ptrack 是一个**用现代 Web 栈重写的项目组合管理（PPM）系统**，原作者用它替代了团队既有的 Oracle APEX 老旧应用。新版用 React 19 + NestJS 11 + Supabase 重新搭，对**九类核心记录**做完整 CRUD，并加上**字段级历史审计**与**删除审计**。

## 关键能力

| 能力 | 说明 |
|------|------|
| 九类记录 | 里程碑 / 行动项 / 问题 / 链接 / 资源 / 更新 / 状态报告 / 附件 / 人员 |
| 完整 CRUD | 每一类记录都支持增删改查与字段级校验 |
| 历史审计 | 按字段记录变更，可回放任意字段的历史值 |
| 删除审计 | 删除操作不直接抹除，保留审计轨迹 |
| 四步向导 | 新建项目时引导逐步填关键字段 |

## 适合谁

- 仍在使用 Oracle APEX / 老旧 PPM 工具的团队，想平滑迁移到现代 Web 栈
- 中小企业自建项目组合管理，不想被 Monday / Asana / Jira 的定价 / 锁定绑死
- 需要**审计级可追溯**的合规场景（金融 / 政企）

## 技术栈

| 层 | 选型 |
|----|------|
| 前端 | React 19 |
| 后端 | NestJS 11 |
| 数据库 / Auth | Supabase（Postgres + RLS） |

## 媒体预览

![](https://pbs.twimg.com/media/HNUV7ClasAAFNah.jpg)

## 相关概念

- [Seeder](./tool-seeder.md) — 小团队自托管项目管理 + MCP
- [annotai](./tool-annotai.md) — Phoenix / LiveView 元素级 AI 编码注释工具

## 参考链接

- 项目链接: <https://github.com/DevEnchantments/ptrack>