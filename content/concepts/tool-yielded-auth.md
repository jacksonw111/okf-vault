---
type: "Tool"
title: "yielded-dev/auth（Effect Schema 驱动的全栈身份认证）"
description: "yielded-dev 出品的 Effect 框架身份认证方案：用一份 Schema 契约同时定义服务端认证路由和客户端查询，把账号、会话与身份流程收进同一套类型。"
resource: "https://github.com/yielded-dev/auth"
tags: "[typescript, effect, auth, full-stack, schema]"
timestamp: "2026-10-04T08:30:00Z"
---

# yielded-dev/auth

## 它是什么

[yielded-dev/auth](https://github.com/yielded-dev/auth) 是 **yielded-dev** 出品的 **Effect** 框架身份认证方案。

## 关键思路

- 用**一份 Schema 契约**同时定义：
  - 服务端认证路由（HTTP / RPC）
  - 客户端查询（请求参数 / 返回结构）
- 把账号、会话与身份流程收进**同一套类型**
- 避免「服务端字段改了客户端没改」的传统前后端类型漂移

## 适用场景

- 使用 Effect 框架（TypeScript 函数式 / 异步运行时）的项目
- 想从源头杜绝 auth 字段错位
- 全栈 TS 项目，希望服务端和客户端共享一套类型源头

## 优势

| 优势 | 说明 |
|------|------|
| 类型一致 | 改 schema 一处，前后端都跟着变 |
| 减少样板 | 不必重复定义 DTO / Request / Response |
| 静态校验 | 编译期就能抓到字段不匹配 |

## 参考链接

- 项目链接：<https://github.com/yielded-dev/auth>