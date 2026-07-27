---
type: "Tool"
title: "TeamPass（nilsteampassnet/TeamPass）"
description: "自托管的团队密码管理器：PHP + MySQL 写的开源 vault，可装在自家服务器上让团队共享凭据；要求 MySQL 5.7+（或 MariaDB 10.7+）与 PHP 8.2+，传统 LAMP 和 Docker 安装都可。"
resource: "https://github.com/nilsteampassnet/TeamPass"
tags: [password-manager, team, php, mysql, self-hosted, vault]
timestamp: "2026-07-27T20:30:00Z"
---

# TeamPass（nilsteampassnet/TeamPass）

## 它是什么

`nilsteampassnet/TeamPass` 是一款**自托管的团队密码管理器**：用 **PHP + MySQL** 写的开源 vault，让公司团队把密码、共享凭据**放在自己服务器上**，不必交给第三方。要求 **MySQL 5.7+**（或 **MariaDB 10.7+**）和 **PHP 8.2+**，传统 LAMP 安装和 **Docker** 部署都可以。

## 为什么用它 / 适合什么场景

- 公司 / 团队需要**共享凭据**，但不愿付费 / 上传密码到 1Password / LastPass 等 SaaS；
- 已有内网服务器 + DBA，倾向**自家维护一个密码 vault**；
- 已有 LAMP / Docker 运维栈，部署门槛低；
- 重视**审计 + 权限细分**（TeamPass 默认有角色 / 文件夹层级权限）。

## 关键能力

| 能力 | 说明 |
|------|------|
| 自托管 | 装在自己服务器上，不依赖任何第三方 |
| 共享凭据 | 团队成员按角色 / 文件夹读写权限访问 |
| PHP + MySQL | 经典 LAMP 技术栈，运维成本低 |
| Docker 支持 | 提供容器化部署 |
| 权限细分 | 文件夹 / 角色 / 用户粒度授权 |
| 历史审计 | 凭据的访问与修改日志可查 |

## 媒体 / 原始链接

![](https://pbs.twimg.com/media/HOIVVBwaIAAksqb.jpg)

- 项目链接：<https://github.com/nilsteampassnet/TeamPass>
