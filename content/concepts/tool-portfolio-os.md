---
type: "Tool"
title: "portfolio-os"
description: "PHP + MySQL 写的「合伙运营多站点」自托管工作台：把站点 / 密码 / 任务 / 人员 / 账目都放一处，最便宜的共享主机就能跑。"
resource: "https://github.com/tnandla/portfolio-os"
tags: [php, mysql, self-hosted, multi-site, password-manager, team]
timestamp: "2026-08-08T20:30:00Z"
---

# portfolio-os

## 它是什么

portfolio-os 是一款用 PHP + MySQL 写的「合伙运营多站点」自托管工作台，专门为多人合伙运营多个站点的小团队设计：把站点清单、共享密码、任务分配、人员协作、账目结算都收进同一后台。部署只依赖 PHP + MySQL，最便宜的共享主机就能跑。

## 为什么用它 / 适合什么场景

- 多人合伙运营若干站点 / 域名，需要共享凭据 / 任务 / 财务。
- 想用极低成本（共享主机）的栈做团队协作工具。
- 不希望把团队凭据放在第三方 SaaS（1Password Teams / Notion）。
- 需要一个「内部 OS」来承载多个站的运营。

## 关键能力

| 能力 | 说明 |
|------|------|
| 站点管理 | 把多个站 / 域名统一登记 |
| 共享密码 | 团队凭据集中托管 |
| 任务协作 | 分配 / 跟踪 / 完成 |
| 人员管理 | 成员角色与权限 |
| 账目结算 | 收入 / 成本 / 分成 |
| 极轻部署 | 共享 PHP + MySQL 主机即可运行 |

## 相关概念

- [Seeder](./tool-seeder.md) — 看板 + 客户请求队列 + 内置 MCP，自托管
- [LawLink](./tool-lawlink.md) — 中小律所开源自部署案件管理系统
- [GanCook](./tool-gancook.md) — 自托管点菜系统