---
type: "Tool"
title: "portop（终端端口侦探）"
description: "padovanl/portop：在终端里一眼看清每个端口背后是哪个进程、哪个 systemd 服务或 Docker 容器，并能一键查看详情、在浏览器打开或杀掉它。"
resource: "https://github.com/padovanl/portop"
tags: "[cli, port, devops, debugging, terminal-tui]"
timestamp: "2026-09-15T00:30:00Z"
---

# portop（终端端口侦探）

## 它是什么

[portop](https://github.com/padovanl/portop) 是一个把「**端口 → 进程 → systemd 服务 / Docker 容器**」链条一次性铺开的终端小工具：不需要在 `ss` / `lsof` / `docker ps` / `systemctl` 之间反复跳。

## 为什么用它

- 「**8888 端口被谁占了**」是开发 / 运维里最常被问的问题之一；portop 把这条链直接展示成一张表。
- 比 `lsof -i :8888` 多走一步：自动识别**它属于哪个 systemd unit 或哪个 Docker 容器**，免去再翻日志。
- 一键动作（详情 / 浏览器打开 / 杀进程）省去复制粘贴 PID。

## 关键能力

| 能力 | 说明 |
|------|------|
| 端口一览 | 终端里直接列出所有监听端口 |
| 进程归属 | 显示占用端口的 PID / 命令 |
| systemd 关联 | 自动识别端口属于哪个 systemd unit |
| Docker 关联 | 自动识别端口属于哪个容器 |
| 一键动作 | 查看详情 / 在浏览器打开 / 杀掉进程 |

## 适合谁

- 自托管 / DevOps / 后端开发，需要快速清理被占端口
- 想找 `lsof` / `netstat` 的更顺手替代品
- 给团队新成员配置统一的「端口排查 SOP」

## 媒体

视频演示：<https://video.twimg.com/tweet_video/HSLjtd0bIAAejVD.mp4>

## 项目链接

- 仓库：<https://github.com/padovanl/portop>