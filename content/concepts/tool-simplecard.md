---
type: Tool
title: "SimpleCard（自托管数字商品发卡平台）"
description: "runtimepoet 开源的自托管数字商品发卡平台：卡密、激活码、账号自动发给付款成功的买家，买卖全程无人值守。后端 Spring Boot 3.4 + Java 22，前端 Next.js 16 + React 19，PostgreSQL 18+。"
resource: "https://github.com/runtimepoet/simplecard"
tags: [self-host, ecommerce, digital-goods, storefront, spring-boot, nextjs]
timestamp: 2026-08-21T03:15:00Z
---

# SimpleCard（自托管数字商品发卡平台）

## 它是什么
SimpleCard 是一个面向「卖卡密、卖激活码、卖账号」场景的自托管发卡平台：买家付款成功后系统自动把对应的卡密 / 激活码 / 账号信息发到买家手里，卖家不需要 7×24 在线。前后端分离 monorepo：后端 Spring Boot 3.4 + Java 22 写 API，前端 Next.js 16 + React 19 同时跑 storefront 与后台管理面板，数据库用 PostgreSQL 18+，统一用 pnpm 工作区管理。

## 为什么用它 / 适合什么场景
- 想自建一个独立站卖软件激活码 / 课程兑换码 / 游戏点卡 / 测试账号，不想依赖第三方平台抽成。
- 个人 / 小工作室不想被大平台政策左右，自己掌握数据与发货流程。
- 想要现代化（Spring Boot + Next.js 16）的发卡模板做二次开发。

## 关键能力
| 能力 | 说明 |
|------|------|
| 自托管 | 数据完全自己掌握，无第三方平台抽成 |
| 自动发货 | 付款成功立即发卡密 / 账号，无需人工 |
| Spring Boot 3.4 | 后端 Java 22 + 现代化响应式栈 |
| Next.js 16 storefront | 买家前端与卖家管理面板同仓库 |
| PostgreSQL 18+ | 主数据库，可水平扩展 |
| pnpm monorepo | 前后端统一工作区，单条命令构建 |

## 一句话总结
**Spring Boot + Next.js + Postgres 的现代发卡平台模板：把卡密自动发出去，买卖双方都不在线也能成交。**

## 原始链接
- [runtimepoet/simplecard](https://github.com/runtimepoet/simplecard) — 原始仓库

## 媒体
- ![SimpleCard 界面](https://pbs.twimg.com/media/HQIL4wwaEAA5vlM.jpg)

## 相关概念
- [xianyu-super-butler](./concepts/tool-xianyu-super-butler.md) — 同属「自动发货 / 自动回复」系，但平台是闲鱼
- [GanCook / 干饭厨子](./concepts/tool-gancook.md) — 同属自托管电商系