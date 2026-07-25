---
type: Tool
title: "sshbox"
description: "Go 单二进制 SSH 跳板工具，为每个会话启动受限 Alpine 容器并在断线后销毁。"
resource: "https://github.com/kknxzz/sshbox"
tags: [ssh, container, security]
timestamp: "2026-07-25T00:00:00Z"
---

# sshbox

Go 单二进制 SSH 跳板工具，为每个会话启动受限 Alpine 容器并在断线后销毁。

## 适用场景

- 需要每次连接启动独立 Alpine 容器，断线即删除的场景。

## 关键能力

| 能力 | 说明 |
|------|------|
| 会话隔离 | 每次连接启动独立 Alpine 容器，断线即删除。 |
| 资源边界 | 默认限制为 256 MB 内存与 0.5 CPU。 |
| 最小权限 | 不挂载宿主机目录且默认无网络。 |
| 部署前提 | 工具本身不验证身份，应通过 Tailscale、VPN 或等效网络边界保护端口。 |

## 链接与媒体

- [项目链接](https://github.com/kknxzz/sshbox)
- [原始链接](https://x.com/QingQ77/status/2081008566668870076)
- [视频](https://video.twimg.com/tweet_video/HOC7oteaMAAkXFg.mp4)

## 相关概念

暂无需要强关联的现有概念。
