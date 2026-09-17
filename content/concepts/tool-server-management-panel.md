---
type: "Tool"
title: "ServerManagementPanel"
description: "coraspirin 出的 Docker Linux 小主机一体化面板：状态查看、容器启停、备份、端口转发全包。"
resource: "https://github.com/coraspirin/ServerManagementPanel"
tags: "[docker, linux, server-panel, homelab, container-management, backup, port-forwarding]"
timestamp: "2026-09-17T04:56:00Z"
---

# ServerManagementPanel

## 它是什么

[coraspirin/ServerManagementPanel](https://github.com/coraspirin/ServerManagementPanel) 是 **coraspirin** 出的 Docker Linux 小主机**一体化管理面板**。把家庭 / 小团队常见的运维操作集中到一个 Web UI：

- 状态查看
- 容器启停
- 备份
- 端口转发

装一个面板，省得在 SSH + `docker ps` + `ufw` + `crontab` 之间来回切。

## 关键能力

| 能力 | 说明 |
|------|------|
| 状态总览 | CPU / 内存 / 磁盘 / 容器运行状态一览 |
| 容器启停 | 图形化启动 / 停止 / 重启 / 删除容器 |
| 备份 | 容器 / 关键目录的计划备份 |
| 端口转发 | 图形化配置 NAT / 反向代理 / 端口映射 |
| 单二进制部署 | 适合小型 Linux 服务器 / 树莓派 / NUC |

## 适合什么场景

- 家里 / 小团队跑了一台装 Docker 的 Linux 小主机（NAS / NUC / 树莓派），需要统一面板的运维人员。
- 不想上 Kubernetes / Portainer 这种重型方案、但又嫌命令行繁琐的个人 Homelab 玩家。
- 想给家庭成员 / 非技术同事一个「能点按钮管理服务」界面的极简派。

## 与相关概念的关系

- [Self-Hosted（自托管）](./term-self-hosted.md) — 是「家庭自托管 + Docker 编排」场景下的小型面板选择之一。

## 参考

- 项目链接：<https://github.com/coraspirin/ServerManagementPanel>

![preview](https://pbs.twimg.com/media/HSVvRoebIAAYGgW.jpg)
