---
type: "Tool"
title: "ObsidianArc（自托管多用户 AI 网关）"
description: "OnyxAxisOwO/ObsidianArc：自托管的多用户 AI 聊天服务与 API 网关，把多家模型的调用、用户权限、配额额度收进一个 Go 单文件服务里统一管理。"
resource: "https://github.com/OnyxAxisOwO/ObsidianArc"
tags: "[self-hosted, ai-gateway, multi-user, chat, go]"
timestamp: "2026-09-15T12:00:00Z"
---

# ObsidianArc（自托管多用户 AI 网关）

## 它是什么

[ObsidianArc](https://github.com/OnyxAxisOwO/ObsidianArc) 是一个**单文件 Go 服务**，把多家模型的调用、用户权限、配额额度收到同一个网关后面统一管理。既可以给团队当作内部 AI 聊天入口，也能直接当成 API 代理 / 网关来用。

## 为什么用它

- 「**多用户** + **多模型** + **统一网关**」是中型团队 / 自托管爱好者的常见组合拳——ObsidianArc 把这套范式压成一个 Go 单文件，部署成本极低。
- 不需要单独再为每家模型维护一个前端：所有模型走同一个网关，前端只关心鉴权 + 配额。
- 名字虽然叫 ObsidianArc，但**和 Obsidian 笔记软件没有关联**——只是个巧合命名。

## 关键能力

| 能力 | 说明 |
|------|------|
| 多用户 | 内置用户体系与权限 |
| 多模型 | 同一网关接入多家模型，按用户 / 角色路由 |
| 配额管理 | 每个用户的额度与限速可配 |
| 统一聊天入口 | 一个前端对所有模型 |
| 单文件部署 | Go 单二进制，跑在 VPS / 家用服务器 |
| 自托管 | 数据完全本地可控 |

## 适合谁

- 想给小团队 / 家庭部署一个「**统一 AI 入口**」又不想上云的人
- 想自托管多模型路由 + 配额系统，又不想自己拼 litellm + nginx + auth 的极简党
- 已经有反向代理 / SSO，需要把多家模型一并接进来

## 项目链接

- 仓库：<https://github.com/OnyxAxisOwO/ObsidianArc>