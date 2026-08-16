---
type: Tool
title: "fob (Secure Enclave SSH)"
description: "把 Mac 当作物理钥匙扣：SSH 私钥锁进 Secure Enclave，从不导出，使用时必须 Touch ID 授权，并可绑定特定主机"
resource: "https://github.com/olivierzol/fob"
tags: [ssh, macos, secure-enclave, touch-id, security]
timestamp: 2026-08-16T16:00:00Z
---

# fob (Secure Enclave SSH)

## 它是什么
`olivierzol/fob` 是一个面向 macOS 的小工具，把 SSH 私钥"焊"在 Apple T2 / Apple Silicon 的 **Secure Enclave** 安全芯片里：密钥生成、存储、签名都在芯片内完成，私钥文件**永远无法导出**——任何想拿到 .pem / .key 的尝试都拿不到。日常登录时，每次签名都要 **Touch ID** 现场授权；还能把密钥**绑定到目标主机指纹**，避免「同一台 Mac 在另一台服务器上假装你是同一个身份」。

## 为什么用它 / 适合什么场景
- 笔记本 / Mac mini 被偷、被没收、被拷镜像：磁盘上根本不存在私钥文件，没有「私钥泄露」这一说。
- 多人共享开发机、家庭共用 Mac：每个人用自己的 Touch ID 解锁自己的密钥，互不可见。
- 多云 / 多账号 SSH：每把钥匙绑定特定 host，避免「错把生产钥匙贴到 staging 配置里」。
- 担心 `~/.ssh/` 备份到云盘、误传 Git 仓库：私钥根本不在文件系统里。

## 关键能力
| 能力 | 说明 |
|------|------|
| 私钥锁 Secure Enclave | 密钥在硬件安全芯片内生成，外部永远拿不到明文，无法 `cat` / `scp` 出去 |
| Touch ID 现场授权 | 每次 SSH 登录都要指纹确认，本地无感、远程体验类似硬件 key |
| 主机指纹绑定 | 私钥可锁定到目标公钥指纹，只对「说好的那台服务器」签字 |
| 视频演示 | 项目自带动手演示视频 |

## 媒体
- 视频：<https://video.twimg.com/tweet_video/HPuV4wza4AAVthS.mp4>

## 相关概念
- [该项目原始链接](https://github.com/olivierzol/fob)